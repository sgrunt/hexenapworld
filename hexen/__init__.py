import functools
import logging
from typing import Any, Dict, List, Set

from BaseClasses import Entrance, CollectionState, Item, Location, MultiWorld, Region, Tutorial
from worlds.AutoWorld import WebWorld, World
from . import Items, Locations, Maps, Regions, Rules
from .Options import HexenOptions

logger = logging.getLogger("Hexen")

HEXEN_TYPE_LEVEL_COMPLETE = -2


class HexenLocation(Location):
    game: str = "Hexen"


class HexenItem(Item):
    game: str = "Hexen"


class HexenWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Hexen randomizer connected to an Archipelago Multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["Daivuk"]
    )]
    theme = "dirt"


class HexenWorld(World):
    """
    Hexen is a dark fantasy first-person shooter video game released in October 1995. It was developed by Raven Software.
    """
    options_dataclass = HexenOptions
    options: HexenOptions
    game = "Hexen"
    web = HexenWeb()
    required_client_version = (0, 3, 9)

    item_name_to_id = {data["name"]: item_id for item_id, data in Items.item_table.items()}
    item_name_groups = Items.item_name_groups

    location_name_to_id = {data["name"]: loc_id for loc_id, data in Locations.location_table.items()}
    location_name_groups = Locations.location_name_groups

    starting_level_for_hub: List[str] = [
        "Seven Portals",
        "Shadow Wood",
        "Heresiarch's Seminary",
        "Castle of Grief",
        "Necropolis"
    ]

    boss_level_for_hub: List[str] = [
        "Necropolis",
    ]

    weapon2_by_class: List[str] = [
        "Timon's Axe",
        "Serpent Staff",
        "Frost Shards"
    ]

    weapon3_by_class: List[str] = [
        "Hammer of Retribution",
        "Firestorm",
        "Arc of Death"
    ]

    weapon4_pieces_by_class: List[List[str]] = [
        [
            "Quietus Blade",
            "Quietus Cross",
            "Quietus Hilt"
        ],
        [
            "Wraithverge Arc",
            "Wraithverge Cross",
            "Wraithverge Shaft"
        ],
        [
            "Bloodscourge Skull",
            "Bloodscourge Stub",
            "Bloodscourge Stick"
        ]
    ]

    # Item ratio. This is an overall count, scaled down by number of hubs.
    items_ratio: Dict[str, float] = {
        "Porkalator": 14,
        "Mystic Urn": 14,
        "Krater of Might": 14,
        "Amulet of Warding": 9,
        "Platinum Helm": 8,
        "Icon of the Defender": 8,
        "Falcon Shield": 8,
        "Mesh Armor": 7,
        "Dragonskin Bracers": 7,
        "Torch": 5,
        "Banishment Device": 5,
        "Chaos Device": 4,
        "Boots of Speed": 4,
        "Dark Servant": 2
    }

    def __init__(self, multiworld: MultiWorld, player: int):
        self.included_hubs = [1, 1, 1, 0, 0]
        self.location_count = 0

        super().__init__(multiworld, player)

    def get_hub_count(self):
        return functools.reduce(lambda count, hub: count + hub, self.included_hubs)

    def generate_early(self):
        # Cache which hubs are included
        self.included_hubs[0] = self.options.hub1.value
        self.included_hubs[1] = self.options.hub2.value
        self.included_hubs[2] = self.options.hub3.value
        self.included_hubs[3] = self.options.hub4.value
        self.included_hubs[4] = self.options.hub5.value

        # If no hubs selected, select Episode 1
        if self.get_hub_count() == 0:
            self.included_hubs[0] = 1

        # Force enable Necropolis if the goal is to defeat Korax
        if self.options.goal.value:
            self.included_hubs[4] = 1

    def create_regions(self):
        # Main regions
        menu_region = Region("Menu", self.player, self.multiworld)
        hub_region = Region("Hub", self.player, self.multiworld)
        self.multiworld.regions += [menu_region, hub_region]
        menu_region.add_exits(["Hub"])

        # Create regions and locations
        main_regions = []
        connections = []
        for region_dict in Regions.regions:
            if not self.included_hubs[region_dict["hub"] - 1]:
                continue

            region_name = region_dict["name"]
            if region_dict["connects_to_hub"]:
                main_regions.append(region_name)

            region = Region(region_name, self.player, self.multiworld)
            region.add_locations({
                loc["name"]: loc_id
                for loc_id, loc in Locations.location_table.items()
                if loc["region"] == region_name
            }, HexenLocation)

            self.multiworld.regions.append(region)

            for connection_dict in region_dict["connections"]:
                # Check if it's a pro-only connection
                if connection_dict["pro"]:
                    continue
                connections.append((region, connection_dict["target"]))
        
        # Connect main regions to Hub
        hub_region.add_exits(main_regions)

        # Do the other connections between regions (They are not all both ways)
        for connection in connections:
            source = connection[0]
            target = self.multiworld.get_region(connection[1], self.player)

            entrance = Entrance(self.player, f"{source.name} -> {target.name}", source)
            source.exits.append(entrance)
            entrance.connect(target)

        # Sum locations for items creation
        self.location_count = len(self.multiworld.get_locations(self.player))

    def completion_rule(self, state: CollectionState):
        goal_levels = Maps.map_names 
        if self.options.goal.value:
            goal_levels = self.boss_level_for_hub

        for map_name in goal_levels:
            if map_name + " - Exit" not in self.location_name_to_id:
                continue
            
            # Exit location names are in form: The Docks (E1M1) - Exit
            loc = Locations.location_table[self.location_name_to_id[map_name + " - Exit"]]
            if not self.included_hubs[loc["hub"] - 1]:
                continue

            # Map complete item names are in form: The Docks (E1M1) - Complete
            if not state.has(map_name + " - Complete", self.player, 1):
                return False
            
        return True

    def set_rules(self):
        Rules.set_rules(self, self.included_hubs, False)
        self.multiworld.completion_condition[self.player] = lambda state: self.completion_rule(state)

        # Forbid progression items to locations that can be missed and can't be picked up. (e.g. One-time timed
        # platform) Unless the user allows for it.
        for death_logic_location in Locations.death_logic_locations:
            self.options.exclude_locations.value.add(death_logic_location)
    
    def create_item(self, name: str) -> HexenItem:
        item_id: int = self.item_name_to_id[name]
        return HexenItem(name, Items.item_table[item_id]["classification"], item_id, self.player)

    def create_items(self):
        itempool: List[HexenItem] = []
        starting_level: str = ""
        emerald_key_item: str = ""
        winnowing_hall_additional_item: str = ""
        start_with_weapon2: bool = False
        start_with_weapon3: bool = False
        start_with_weapon4: bool = False

        # Grab starting level
        for i in range(len(self.included_hubs)):
            if self.included_hubs[i]:
                if (i > 1): # Start with weapons 2/3 if starting hub isn't Seven Portals or Shadow Wood
                    start_with_weapon2 = True
                    start_with_weapon3 = True
                if (i == 4): # Start with weapon 4 if starting hub is Necropolis (Necropolis only)
                    start_with_weapon4 = True
                starting_level = self.starting_level_for_hub[i]
                break

        # Starting item lock: if starting in Seven Portals, require that the Emerald Key check be either
        # the Emerald Key or Shadow Wood (if unlocked).
        if (starting_level == "Seven Portals"):
            if self.included_hubs[1]: # Shadow Wood is unlocked
                emerald_key_item = self.multiworld.random.choices(['Emerald Key', 'Shadow Wood'], weights=[6, 2])[0]
            else:
                emerald_key_item = 'Emerald Key'
        
            self.multiworld.get_location('Seven Portals - Winnowing Hall - Emerald Key', self.player).place_locked_item(self.create_item(emerald_key_item))
            self.location_count -= 1

            # If the Emerald Key item is the Emerald Key, guarantee that one of the two remaining Winnowing
            # Hall items is either the Silver Key or Shadow Wood (if unlocked).
            if (emerald_key_item == 'Emerald Key'):
                if self.included_hubs[1]: # Shadow Wood is unlocked
                    winnowing_hall_additional_item = self.multiworld.random.choices(['Silver Key', 'Shadow Wood'], weights=[4, 2])[0]
                else:
                    winnowing_hall_additional_item = 'Silver Key'

                winnowing_hall_additional_loc = self.multiworld.random.choice([
                    'Seven Portals - Winnowing Hall - Silver Key',
                    'Seven Portals - Winnowing Hall - Platinum Helm'
                ])
                self.multiworld.get_location(winnowing_hall_additional_loc, self.player).place_locked_item(self.create_item(winnowing_hall_additional_item))
                self.location_count -= 1

        # Items
        for item_id, item in Items.item_table.items():
            if item["doom_type"] == HEXEN_TYPE_LEVEL_COMPLETE:
                continue # We'll fill it manually later

            if item["hub"] != -1 and not self.included_hubs[item["hub"] - 1]:
                continue

            count = item["count"] if (item["name"] != starting_level and item["name"] != emerald_key_item and item["name"] != winnowing_hall_additional_item) else item["count"] - 1
            if not start_with_weapon2 and item["name"] == self.weapon2_by_class[self.options.player_class.value]:
                count = count + 1
            if not start_with_weapon3 and item["name"] == self.weapon3_by_class[self.options.player_class.value]:
                count = count + 1
            if not start_with_weapon4 and item["name"] in self.weapon4_pieces_by_class[self.options.player_class.value]:
                count = count + 1
            itempool += [self.create_item(item["name"]) for _ in range(count)]

        # Place end level items in locked locations
        for map_name in Maps.map_names:
            loc_name = map_name + " - Exit"
            item_name = map_name + " - Complete"

            if loc_name not in self.location_name_to_id:
                continue

            if item_name not in self.item_name_to_id:
                continue

            loc = Locations.location_table[self.location_name_to_id[loc_name]]
            if not self.included_hubs[loc["hub"] - 1]:
                continue

            self.multiworld.get_location(loc_name, self.player).place_locked_item(self.create_item(item_name))
            self.location_count -= 1

        # Give starting level right away
        self.multiworld.push_precollected(self.create_item(starting_level))

        # And any starting weapons
        if start_with_weapon2:
            self.multiworld.push_precollected(self.create_item(self.weapon2_by_class[self.options.player_class.value]))
        if start_with_weapon3:
            self.multiworld.push_precollected(self.create_item(self.weapon3_by_class[self.options.player_class.value]))
        if start_with_weapon4:
            self.multiworld.push_precollected(self.create_item(self.weapon4_pieces_by_class[self.options.player_class.value][0]))
            self.multiworld.push_precollected(self.create_item(self.weapon4_pieces_by_class[self.options.player_class.value][1]))
            self.multiworld.push_precollected(self.create_item(self.weapon4_pieces_by_class[self.options.player_class.value][2]))
        
        # Fill the rest starting with powerups, then fillers
        self.create_ratioed_items("Amulet of Warding", itempool)
        self.create_ratioed_items("Falcon Shield", itempool)
        self.create_ratioed_items("Mesh Armor", itempool)
        self.create_ratioed_items("Platinum Helm", itempool)
        self.create_ratioed_items("Dragonskin Bracers", itempool)
        self.create_ratioed_items("Mystic Urn", itempool)
        self.create_ratioed_items("Banishment Device", itempool)
        self.create_ratioed_items("Boots of Speed", itempool)
        self.create_ratioed_items("Chaos Device", itempool)
        self.create_ratioed_items("Dark Servant", itempool)
        self.create_ratioed_items("Icon of the Defender", itempool)
        self.create_ratioed_items("Krater of Might", itempool)
        self.create_ratioed_items("Porkalator", itempool)
        self.create_ratioed_items("Torch", itempool)

        while len(itempool) < self.location_count:
            itempool.append(self.create_item(self.get_filler_item_name()))

        # add itempool to multiworld
        self.multiworld.itempool += itempool

    def get_filler_item_name(self):
        return self.multiworld.random.choice([
            "Blue Mana",
            "Green Mana",
            "Combined Mana",
            "Quartz Flask",
            "Disc of Repulsion",
            "Flechette"
        ])

    def create_ratioed_items(self, item_name: str, itempool: List[HexenItem]):
        remaining_loc = self.location_count - len(itempool)
        if remaining_loc <= 0:
            return

        hub_count = self.get_hub_count()
        count = min(remaining_loc, max(1, self.items_ratio[item_name] * hub_count // 5))
        if count == 0:
            logger.warning("Warning, no " + item_name + " will be placed.")
            return

        for i in range(count):
            itempool.append(self.create_item(item_name))

    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data = self.options.as_dict("goal", "player_class", "difficulty", "random_monsters", "random_pickups", "random_music")

        # Make sure we send proper hub settings
        slot_data["hub1"] = self.included_hubs[0]
        slot_data["hub2"] = self.included_hubs[1]
        slot_data["hub3"] = self.included_hubs[2]
        slot_data["hub4"] = self.included_hubs[3]
        slot_data["hub5"] = self.included_hubs[4]

        return slot_data
