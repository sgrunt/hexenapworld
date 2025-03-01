from typing import TYPE_CHECKING
from worlds.generic.Rules import set_rule

if TYPE_CHECKING:
    from . import HexenWorld

def set_hub1_rules(player, multiworld, pro):
    set_rule(multiworld.get_entrance("Hub -> Seven Portals - Winnowing Hall - Main", player), lambda state:
        state.has("Seven Portals", player, 1))
    set_rule(multiworld.get_entrance("Seven Portals - Winnowing Hall - Main -> Seven Portals - Winnowing Hall - Emerald Key", player), lambda state:
        state.has("Emerald Key", player, 1))
    set_rule(multiworld.get_entrance("Seven Portals - Winnowing Hall - Main -> Seven Portals - Seven Portals - Main", player), lambda state:
        state.has("Emerald Key", player, 1) and
        state.has("Silver Key", player, 1))
    set_rule(multiworld.get_entrance("Seven Portals - Seven Portals - Main -> Seven Portals - Seven Portals - Ice Stairs", player), lambda state:
        state.has("Seven Portals - Seven Portals - Ice Stairs", player, 1))
    set_rule(multiworld.get_entrance("Seven Portals - Seven Portals - Main -> Seven Portals - Seven Portals - Fire Stairs", player), lambda state:
        state.has("Seven Portals - Seven Portals - Fire Stairs", player, 1))
    set_rule(multiworld.get_entrance("Seven Portals - Seven Portals - Main -> Seven Portals - Seven Portals - Steel Stairs", player), lambda state:
        state.has("Seven Portals - Seven Portals - Steel Stairs", player, 1))
    set_rule(multiworld.get_entrance("Seven Portals - Seven Portals - Main -> Seven Portals - Seven Portals - Exit Area", player), lambda state:
        state.has("Seven Portals - Seven Portals - Exit Access (1/3)", player, 3))
    set_rule(multiworld.get_entrance("Seven Portals - Seven Portals - Main -> Seven Portals - Guardian of Ice - South", player), lambda state:
        state.has("Seven Portals - Seven Portals - West Access (1/3)", player, 2) and
        (state.has("Timon's Axe", player, 1) or
         state.has("Serpent Staff", player, 1) or
         state.has("Frost Shards", player, 1)))
    set_rule(multiworld.get_entrance("Seven Portals - Seven Portals - Main -> Seven Portals - Bright Crucible - Main", player), lambda state:
        state.has("Seven Portals - Bright Crucible Access (1/2)", player, 2))
    set_rule(multiworld.get_entrance("Seven Portals - Guardian of Ice - Main -> Seven Portals - Guardian of Ice - Fire Door", player), lambda state:
        state.has("Seven Portals - Guardian of Ice - Fire Door", player, 1))
    set_rule(multiworld.get_entrance("Seven Portals - Guardian of Ice - Main -> Seven Portals - Guardian of Ice - Steel Door", player), lambda state:
        state.has("Seven Portals - Guardian of Ice - Steel Door", player, 1))
    set_rule(multiworld.get_entrance("Seven Portals - Guardian of Ice - South -> Seven Portals - Guardian of Ice - Fire Key Access", player), lambda state:
        state.has("Flame Mask", player, 1))
    set_rule(multiworld.get_entrance("Seven Portals - Guardian of Fire - Main -> Seven Portals - Guardian of Fire - Fire Key", player), lambda state:
        state.has("Fire Key", player, 1))
    set_rule(multiworld.get_entrance("Seven Portals - Guardian of Steel - Main -> Seven Portals - Guardian of Steel - Steel Key", player), lambda state:
        state.has("Steel Key", player, 1) and
        (state.has("Timon's Axe", player, 1) or
         state.has("Serpent Staff", player, 1) or
         state.has("Frost Shards", player, 1)) and
        (state.has("Seven Portals - Seven Portals - West Access (1/3)", player, 2) or
         state.has("Seven Portals - Guardian of Ice - Steel Door", player, 1)))
    set_rule(multiworld.get_entrance("Seven Portals - Bright Crucible - Main -> Seven Portals - Bright Crucible - Heart", player), lambda state:
        state.has("Heart of D'Sparil", player, 1))

def set_hub2_rules(player, multiworld, pro):
    set_rule(multiworld.get_entrance("Hub -> Shadow Wood - Shadow Wood - Main", player), lambda state:
        state.has("Shadow Wood", player, 1))
    set_rule(multiworld.get_entrance("Shadow Wood - Shadow Wood - Main -> Shadow Wood - Darkmere - Main", player), lambda state:
        (state.has("Timon's Axe", player, 1) or
         state.has("Serpent Staff", player, 1) or
         state.has("Frost Shards", player, 1)) and
        (state.has("Hammer of Retribution", player, 1) or
         state.has("Firestorm", player, 1) or
         state.has("Arc of Death", player, 1)))
    set_rule(multiworld.get_entrance("Shadow Wood - Shadow Wood - Main -> Shadow Wood - Caves of Circe - Main", player), lambda state:
        (state.has("Timon's Axe", player, 1) or
         state.has("Serpent Staff", player, 1) or
         state.has("Frost Shards", player, 1)) and
        (state.has("Hammer of Retribution", player, 1) or
         state.has("Firestorm", player, 1) or
         state.has("Arc of Death", player, 1)))
    set_rule(multiworld.get_entrance("Shadow Wood - Shadow Wood - Main -> Shadow Wood - Wastelands - Main", player), lambda state:
        (state.has("Timon's Axe", player, 1) or
         state.has("Serpent Staff", player, 1) or
         state.has("Frost Shards", player, 1)) and
        (state.has("Hammer of Retribution", player, 1) or
         state.has("Firestorm", player, 1) or
         state.has("Arc of Death", player, 1)))
    set_rule(multiworld.get_entrance("Shadow Wood - Shadow Wood - Main -> Shadow Wood - Sacred Grove - Main", player), lambda state:
        (state.has("Timon's Axe", player, 1) or
         state.has("Serpent Staff", player, 1) or
         state.has("Frost Shards", player, 1)) and
        (state.has("Hammer of Retribution", player, 1) or
         state.has("Firestorm", player, 1) or
         state.has("Arc of Death", player, 1)) and
        (state.has("Shadow Wood - Shadow Wood - Darkmere Horn Switch", player, 1) and
         state.has("Shadow Wood - Shadow Wood - Darkmere Cave Switch", player, 1) and
         state.has("Shadow Wood - Shadow Wood - Caves of Circe Horn Switch", player, 1) and
         state.has("Shadow Wood - Shadow Wood - Caves of Circe Swamp Switch", player, 1) and
         state.has("Shadow Wood - Shadow Wood - Wastelands Swamp Switch", player, 1) and
         state.has("Shadow Wood - Shadow Wood - Wastelands Cave Switch", player, 1)))
    set_rule(multiworld.get_entrance("Shadow Wood - Shadow Wood - Main -> Shadow Wood - Hypostyle - Main", player), lambda state:
        (state.has("Timon's Axe", player, 1) or
         state.has("Serpent Staff", player, 1) or
         state.has("Frost Shards", player, 1)) and
        (state.has("Hammer of Retribution", player, 1) or
         state.has("Firestorm", player, 1) or
         state.has("Arc of Death", player, 1)) and
        (state.has("Shadow Wood - Shadow Wood - Darkmere Horn Switch", player, 1) and
         state.has("Shadow Wood - Shadow Wood - Darkmere Cave Switch", player, 1) and
         state.has("Shadow Wood - Shadow Wood - Caves of Circe Horn Switch", player, 1) and
         state.has("Shadow Wood - Shadow Wood - Caves of Circe Swamp Switch", player, 1) and
         state.has("Shadow Wood - Shadow Wood - Wastelands Swamp Switch", player, 1) and
         state.has("Shadow Wood - Shadow Wood - Wastelands Cave Switch", player, 1)))
    set_rule(multiworld.get_entrance("Shadow Wood - Darkmere - Main -> Shadow Wood - Darkmere - Castle Key", player), lambda state:
        state.has("Castle Key", player, 1))
    set_rule(multiworld.get_entrance("Shadow Wood - Darkmere - Main -> Shadow Wood - Darkmere - Cave Key", player), lambda state:
        state.has("Cave Key", player, 1))
    set_rule(multiworld.get_entrance("Shadow Wood - Darkmere - Castle Key -> Shadow Wood - Darkmere - Horn Key", player), lambda state:
        state.has("Horn Key", player, 1))
    set_rule(multiworld.get_entrance("Shadow Wood - Caves of Circe - Main -> Shadow Wood - Caves of Circe - Swamp Key", player), lambda state:
        state.has("Swamp Key", player, 1))
    set_rule(multiworld.get_entrance("Shadow Wood - Caves of Circe - Main -> Shadow Wood - Caves of Circe - Horn Key", player), lambda state:
        state.has("Horn Key", player, 1))
    set_rule(multiworld.get_entrance("Shadow Wood - Wastelands - Main -> Shadow Wood - Wastelands - Cave Key", player), lambda state:
        state.has("Cave Key", player, 1))
    set_rule(multiworld.get_entrance("Shadow Wood - Wastelands - Main -> Shadow Wood - Wastelands - Swamp Key", player), lambda state:
        state.has("Swamp Key", player, 1))

def set_hub3_rules(player, multiworld, pro):
    set_rule(multiworld.get_entrance("Hub -> Heresiarch's Seminary - Heresiarch's Seminary - Main", player), lambda state:
        state.has("Heresiarch's Seminary", player, 1) and
        (state.has("Timon's Axe", player, 1) or
         state.has("Serpent Staff", player, 1) or
         state.has("Frost Shards", player, 1)) and
        (state.has("Hammer of Retribution", player, 1) or
         state.has("Firestorm", player, 1) or
         state.has("Arc of Death", player, 1)))
    set_rule(multiworld.get_entrance("Heresiarch's Seminary - Heresiarch's Seminary - Main -> Heresiarch's Seminary - Heresiarch's Seminary - Chapel Access", player), lambda state:
        (state.has("Ruby Planet", player, 1) and
         state.has("Emerald Planet 1", player, 1) and
         state.has("Emerald Planet 2", player, 1) and
         state.has("Sapphire Planet 1", player, 1) and
         state.has("Sapphire Planet 2", player, 1)))
    set_rule(multiworld.get_entrance("Heresiarch's Seminary - Heresiarch's Seminary - Main -> Heresiarch's Seminary - Heresiarch's Seminary - Exit Area", player), lambda state:
        (state.has("Heresiarch's Seminary - Heresiarch's Seminary - Dragon Chapel Dragon Switch", player, 1) and
         state.has("Heresiarch's Seminary - Heresiarch's Seminary - Dragon Chapel Wolf Switch", player, 1) and
         state.has("Heresiarch's Seminary - Heresiarch's Seminary - Dragon Chapel Griffin Switch", player, 1) and
         state.has("Heresiarch's Seminary - Heresiarch's Seminary - Griffin Chapel Griffin Switch", player, 1) and
         state.has("Heresiarch's Seminary - Heresiarch's Seminary - Griffin Chapel Dragon Switch", player, 1) and
         state.has("Heresiarch's Seminary - Heresiarch's Seminary - Griffin Chapel Wolf Trigger", player, 1) and
         state.has("Heresiarch's Seminary - Heresiarch's Seminary - Wolf Chapel Wolf Switch", player, 1) and
         state.has("Heresiarch's Seminary - Heresiarch's Seminary - Wolf Chapel Dragon Switch", player, 1) and
         state.has("Heresiarch's Seminary - Heresiarch's Seminary - Wolf Chapel Griffin Trigger", player, 1)))
    set_rule(multiworld.get_entrance("Heresiarch's Seminary - Dragon Chapel - Main -> Heresiarch's Seminary - Dragon Chapel - Wolf", player), lambda state:
        state.has("Heresiarch's Seminary - Heresiarch's Seminary - Wolf Chapel Wolf Switch", player, 1))
    set_rule(multiworld.get_entrance("Heresiarch's Seminary - Dragon Chapel - Main -> Heresiarch's Seminary - Dragon Chapel - Griffin", player), lambda state:
        state.has("Heresiarch's Seminary - Heresiarch's Seminary - Griffin Chapel Griffin Switch", player, 1))
    set_rule(multiworld.get_entrance("Heresiarch's Seminary - Wolf Chapel - Main -> Heresiarch's Seminary - Wolf Chapel - Dragon", player), lambda state:
        state.has("Heresiarch's Seminary - Heresiarch's Seminary - Dragon Chapel Dragon Switch", player, 1))
    set_rule(multiworld.get_entrance("Heresiarch's Seminary - Wolf Chapel - Main -> Heresiarch's Seminary - Wolf Chapel - Griffin", player), lambda state:
        state.has("Heresiarch's Seminary - Heresiarch's Seminary - Griffin Chapel Griffin Switch", player, 1))
    set_rule(multiworld.get_entrance("Heresiarch's Seminary - Griffin Chapel - Main -> Heresiarch's Seminary - Griffin Chapel - Dragon", player), lambda state:
        state.has("Heresiarch's Seminary - Heresiarch's Seminary - Dragon Chapel Dragon Switch", player, 1))
    set_rule(multiworld.get_entrance("Heresiarch's Seminary - Griffin Chapel - Main -> Heresiarch's Seminary - Griffin Chapel - Wolf", player), lambda state:
        state.has("Heresiarch's Seminary - Heresiarch's Seminary - Wolf Chapel Wolf Switch", player, 1))

def set_hub4_rules(player, multiworld, pro):
    set_rule(multiworld.get_entrance("Hub -> Castle of Grief - Castle of Grief - Main", player), lambda state:
        state.has("Castle of Grief", player, 1) and
        (state.has("Timon's Axe", player, 1) or
         state.has("Serpent Staff", player, 1) or
         state.has("Frost Shards", player, 1)) and
        (state.has("Hammer of Retribution", player, 1) or
         state.has("Firestorm", player, 1) or
         state.has("Arc of Death", player, 1)))
    set_rule(multiworld.get_entrance("Castle of Grief - Castle of Grief - Main -> Castle of Grief - Castle of Grief - Gibbet Access", player), lambda state:
        state.has("Clock Gear 1", player, 1) and
        state.has("Clock Gear 2", player, 1) and
        state.has("Clock Gear 3", player, 1) and
        state.has("Clock Gear 4", player, 1))
    set_rule(multiworld.get_entrance("Castle of Grief - Forsaken Outpost - Main -> Castle of Grief - Forsaken Outpost - Rusted Key", player), lambda state:
        state.has("Rusted Key", player, 1))
    set_rule(multiworld.get_entrance("Castle of Grief - Forsaken Outpost - Rusted Key -> Castle of Grief - Desolate Garden - Main", player), lambda state:
        state.has("Castle of Grief - Forsaken Outpost - Desolate Garden Access 1", player, 1) and
        state.has("Castle of Grief - Forsaken Outpost - Desolate Garden Access 2", player, 1))
    set_rule(multiworld.get_entrance("Castle of Grief - Gibbet - Main -> Castle of Grief - Gibbet - Library", player), lambda state:
        state.has("Daemon Codex", player, 1) and
        state.has("Liber Oscura", player, 1))
    set_rule(multiworld.get_entrance("Castle of Grief - Gibbet - Main -> Castle of Grief - Gibbet - Dungeon Key", player), lambda state:
        state.has("Dungeon Key", player, 1))
    set_rule(multiworld.get_entrance("Castle of Grief - Gibbet - Main -> Castle of Grief - Gibbet - Axe Key Cage", player), lambda state:
        state.has("Castle of Grief - Gibbet - Axe Key Access", player, 1))
    set_rule(multiworld.get_entrance("Castle of Grief - Gibbet - Main -> Castle of Grief - Gibbet - Axe Key", player), lambda state:
        state.has("Axe Key", player, 1))
    set_rule(multiworld.get_entrance("Castle of Grief - Gibbet - Main -> Castle of Grief - Effluvium - Main", player), lambda state:
        state.has("Yorick's Skull", player, 1))

def set_hub5_rules(player, multiworld, pro):
    set_rule(multiworld.get_entrance("Hub -> Necropolis - Necropolis - Main", player), lambda state:
        state.has("Necropolis", player, 1) and
        (state.has("Timon's Axe", player, 1) or
         state.has("Serpent Staff", player, 1) or
         state.has("Frost Shards", player, 1)) and
        (state.has("Hammer of Retribution", player, 1) or
         state.has("Firestorm", player, 1) or
         state.has("Arc of Death", player, 1)) and
        (state.has("Quietus Blade", player, 1) or
         state.has("Wraithverge Arc", player, 1) or
         state.has("Bloodscourge Skull", player, 1)) and
        (state.has("Quietus Cross", player, 1) or
         state.has("Wraithverge Cross", player, 1) or
         state.has("Bloodscourge Stub", player, 1)) and
        (state.has("Quietus Hilt", player, 1) or
         state.has("Wraithverge Shaft", player, 1) or
         state.has("Bloodscourge Stick", player, 1)))
    set_rule(multiworld.get_entrance("Necropolis - Necropolis - Main -> Necropolis - Dark Crucible - Main", player), lambda state:
        state.has("Glaive Seal", player, 1) and
            state.has("Holy Relic", player, 1) and
            state.has("Sigil of the Magus", player, 1))


def set_rules(hexen_world: "HexenWorld", included_hubs, pro):
    player = hexen_world.player
    multiworld = hexen_world.multiworld

    if included_hubs[0]:
        set_hub1_rules(player, multiworld, pro)
    if included_hubs[1]:
        set_hub2_rules(player, multiworld, pro)
    if included_hubs[2]:
        set_hub3_rules(player, multiworld, pro)
    if included_hubs[3]:
        set_hub4_rules(player, multiworld, pro)
    if included_hubs[4]:
        set_hub5_rules(player, multiworld, pro)
