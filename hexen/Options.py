from Options import PerGameCommonOptions, Choice, Toggle, DeathLink, DefaultOnToggle, StartInventoryPool
from dataclasses import dataclass


class Goal(Choice):
    """
    Choose the main goal.
    complete_all_hubs: Complete all selected hubs
    defeat_korax: Defeat Korax (complete Necropolis) 
    """
    display_name = "Goal"
    option_complete_all_hubs = 0
    option_defeat_korax = 1
    default = 0

class PlayerClass(Choice):
    """
    Choose your player class.
    fighter: Fighter.
    cleric: Cleric.
    mage: Mage.
    """
    display_name = "Player Class"
    option_fighter = 0
    option_cleric = 1
    option_mage = 2
    default = 1

class Difficulty(Choice):
    """
    Choose the difficulty option. Those match DOOM's difficulty options.

    baby (squire/altar boy/apprentice) - Fewer monsters and more items than medium. Damage taken is halved, and ammo pickups carry twice as much ammo. Any Quartz Flasks and Mystic Urns are automatically used when the player nears death.
    easy (knight/acolyte/enchanter) - Fewer monsters and more items than medium.
    medium (warrior/priest/sorcerer) - Completely balanced, this is the standard difficulty level.
    hard (berserker/cardinal/warlock) - More monsters and fewer items than medium.
    nightmare (titan/pope/archmage) - Same as hard, but monsters and their projectiles move much faster. Cheating is also disabled.
    """
    display_name = "Difficulty"
    option_baby = 0
    option_easy = 1
    option_medium = 2
    option_hard = 3
    option_nightmare = 4
    default = 2


class RandomMonsters(Choice):
    """
    Choose how monsters are randomized.
    vanilla: No randomization
    shuffle: Monsters are shuffled within the level
    random_balanced: Monsters are completely randomized, but balanced based on existing ratio in the level. (Small monsters vs medium vs big)
    random_chaotic: Monsters are completely randomized, but balanced based on existing ratio in the entire game.
    """
    display_name = "Random Monsters"
    option_vanilla = 0
    option_shuffle = 1
    option_random_balanced = 2
    option_random_chaotic = 3
    default = 1


class RandomPickups(Choice):
    """
    Choose how pickups are randomized.
    vanilla: No randomization
    shuffle: Pickups are shuffled within the level
    random_balanced: Pickups are completely randomized, but balanced based on existing ratio in the level. (Small pickups vs Big)
    """
    display_name = "Random Pickups"
    option_vanilla = 0
    option_shuffle = 1
    option_random_balanced = 2
    default = 1


class RandomMusic(Choice):
    """
    Level musics will be randomized.
    vanilla: No randomization
    shuffle_selected: Selected hubs' levels will be shuffled
    shuffle_game: All the music will be shuffled
    """
    display_name = "Random Music"
    option_vanilla = 0
    option_shuffle_selected = 1
    option_shuffle_game = 2
    default = 0


class Hub1(DefaultOnToggle):
    """Seven Portals
    If none of the hubs are chosen, Hub 1 will be chosen by default."""
    display_name = "Hub 1"


class Hub2(DefaultOnToggle):
    """Shadow Wood.
    If none of the hubs are chosen, Hub 1 will be chosen by default."""
    display_name = "Hub 2"


class Hub3(DefaultOnToggle):
    """Heresiarch's Seminary.
    If none of the hubs are chosen, Hub 1 will be chosen by default."""
    display_name = "Hub 3"


class Hub4(DefaultOnToggle):
    """Castle of Grief.
    If none of the hubs are chosen, Hub 1 will be chosen by default."""
    display_name = "Hub 4"


class Hub5(DefaultOnToggle):
    """Necropolis.
    If none of the hubs are chosen, Hub 1 will be chosen by default."""
    display_name = "Hub 5"


@dataclass
class HexenOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    goal: Goal
    player_class: PlayerClass
    difficulty: Difficulty
    random_monsters: RandomMonsters
    random_pickups: RandomPickups
    random_music: RandomMusic
    death_link: DeathLink
    hub1: Hub1
    hub2: Hub2
    hub3: Hub3
    hub4: Hub4
    hub5: Hub5
