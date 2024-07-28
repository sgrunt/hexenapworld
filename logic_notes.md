# APHexen Level Tweaks and Unintuitive Behaviour

## General
There is plenty of behaviour that depends on certain monsters or certain quantities of monsters to trigger effects in Hexen; most of this will be noted and explained here.

Cross-level switches that display multiple lines of text will normally send their effect on the last line of text they display. Since most puzzle switches are adjacent to level teleporters, it is possible to leave the level before the resulting check is sent; should this happen you can re-enter the level and wait for a moment for it to take effect.

## Seven Portals
### General
The Guardian levels will be referred to in shorthand as Ice, Fire, and Steel throughout this section.

### Winnowing Hall
To allow for an adequate number of initial checks, world generation guarantees that the Emerald Key location is either the Emerald Key or access to Shadow Wood (assuming Shadow Wood is enabled); should the check be the Emerald Key, one of the two remaining checks in Winnowing Hall will be guaranteed to be either the Silver Key or access to Shadow Wood.

The Platinum Helm location is just up the stairs behind the Emerald Key door; at the top of the stairs jump up onto the ledge on the left and then again to the left from there to reach it.

### Seven Portals
Since there is normally no exit back to Winnowing Hall, a hub portal has been added to the starting room.

An adjustment has been made to the script of this level to allow the east Ice door trigger to fire multiple times but only act once. This is to allow for cases where the west Ice door opens early and players enter the west Ice portal without hitting the switch to open the east Ice door, which would lead to getting stuck behind the east Ice door.

It is similarly possible to arrive on the other side of most other doors before opening them. In the case of the east portals, a tweak has been made on Ice to open the doors in those cases (see below); in the case of the west Fire and Steel portals it is only possible to get there if the respective east portals are accessible from their respective levels, so one must merely re-enter the portal and exit the other level via its other exit.

The western Steel door opens when picking up the Steel Key location on Ice; the western Fire door opens when picking up the Fire Key location on Ice. Note that this implies that the western Fire door opening requires both access to the second part of Ice and the Flame Mask, but since this takes the player to the same area as the first portal this has no logical implications.

In vanilla Hexen, only two of the three initial puzzle switches are required to open the west door; in APHexen this behaviour is preserved by requiring only two of the three West Access checks.

Accessing the Ice portals requires killing all of the green Chaos Serpents within the respective Ice doors. The bridge to the exit spawns after killing all of the centaurs behind the exit doors.

### Guardian of Ice
In vanilla Hexen, hitting the initial switch just behind the Amulet of Warding is the trigger to open the Fire and Steel doors on Seven Portals, since this is normally required to leave Ice for the first time. In APHexen, the level script has been adjusted to fire the trigger upon entering Ice for the first time as players may be able to instead exit through the Fire or Steel portals instead if the respective checks have been made to open them.

### Guardian of Fire
It is possible to arrive here for the first time via either the west Fire portal on Seven Portals or via the portal behind the Fire door in Ice. The vanilla initial portal will still open normally, but the lava effect just past it will only trigger when approaching the portal for the first time.

### Guardian of Steel
It is possible to arrive in the Ice area without having the Steel Key; the puzzle to activate the Bright Crucible trigger can still be solved in this scenario.

### Bright Crucible
Since the exit portal cannot be accessed without solving the Heart of D'Sparil puzzle and it is possible to arrive here without having the Heart of D'Sparil, a hub portal has been added to the swamp (which is always accessible even if the player falls from the starting ledge).

## Shadow Wood
### Wastelands
Accessing the northern area with the Swamp Key door requires killing most (all but four) of the ettins on the map.

Accessing the Cave Key puzzle switch requires killing all of the Afrits in the area to spawn the bridge leading up to it.

### Sacred Grove
Additional ettins start spawning in Sacred Grove slightly more than 40 seconds after entering the level for the first time. In vanilla Hexen if the number of ettins exceeds 20 the exit closes and a large number of Chaos Serpents start spawning instead; this limit behaviour is disabled in APHexen as it permanently closes the exit portal and would leave the player in an unwinnable situation.

### Hypostyle
Dying in one of the four puzzle rooms is not a softlock - even in vanilla Hexen it is possible to use the closed door from the outside to reopen it so that the puzzle can be solved.

Entering the north puzzle room too quickly can sometimes lock one of the centaurs that need to be killed to advance the room out. If this happens, you will need to respawn to get out of the room to kill it to advance the room.

## Heresiarch's Seminary
### Heresiarch's Seminary
Opening the main doors requires killing all but two of the initial wave of centaurs.

Opening the exit from the room with the Icon of the Defender location requires killing all but three of the Chaos Serpents in the room.

## Castle of Grief
### Forsaken Outpost
It is possible to first enter this level via the Effluvium portal. If the initial area accessible from Castle of Grief has not been completed yet, you will be unable to access it from the Effluvium portal area and will need to exit through the Effluvium portal, through which you can eventually return to Castle of Grief and take the portal from there back to the main area of the level.

Some items that spawn on the shelves in the Rusted Key area are not large enough to be easily obtainable - they can still be picked up by running into the shelves with sufficient speed.

### Gibbet
Vanilla Hexen contains a scripting error in the final area where exactly three Chaos Serpents need to be left alive to open up the side rooms with Dark Bishops. The script has been adjusted in APHexen to require three or fewer Chaos Serpents to be alive.

Accessing the Heresiarch requires killing all of the Afrits, at least one of the Chaos Serpents, and all of the Dark Bishops in the final area in that order.

### Dungeons
Opening the cell bars requires killing all but three of the Chaos Serpents on the level.

Accessing the easternmost portion of the level via the cells requires killing all but nine of the ettins on the level.

### Effluvium
An adjustment has been made to the script of this level to fix a potential softlock. In the area accessed from Dungeons, it is possible to hit the switch to raise the sludge level and then die or otherwise respawn out of it, locking away a check and the second switch needed to open doors elsewhere on the level. The door leading into this area can now be opened from the outside if this occurs, resetting the room to its initial state.

Note that in many cases you will enter Effluvium for the first time through the Dungeons portal; completing the initial Dungeons area places you in the starting area accessible from Gibbet where you then proceed as normal.

### Desolate Garden
An adjustment has been made to the script of this level to fix a potential softlock. The only way to deactivate the sludge trap was to hit the switch on the far end of the room; if this is not done normally the room cannot be re-entered should the player die and respawn. The trap now deactivates and lowers the sludge level on its own should it rise all the way to the ceiling, allowing access to the checks in the room again.

## Necropolis
### Necropolis
The script to close the Vivarium door has been disabled; Vivarium is thus always accessible.

Reivers come in four waves in this level - killing all but four Reivers in a wave will start the next wave.

### Zedek's Tomb
Should you be killed by the combination lock trap, the ceiling will eventually raise back up far enough to allow access again, at which point you can generate and enter a new combination to disarm the trap and allow access to Zedek.

### Traductus' Tomb
An adjustment has been made to the script of this level to fix a potential softlock. Approaching the switches at the north end of the level causes the elevator leading into that area to rise back up and lock, and it is normally required to defeat Traductus to reactivate the elevator (causing it to permanently move on its own). The elevator will now start moving on its own shortly after approaching the switches for the first time.

### Dark Crucible
Several adjustments have been made to this level to prevent softlocks and ensure all checks are accessible:
 - A hub portal has been added at the start to allow for exiting the level before defeating Korax.
 - The first door now opens permanently.
 - In vanilla Hexen, stunlocking Korax (usually via Cleric flechette or Wraithverge spam) can kill Korax before Korax can teleport to the second area. The door between the two areas can now be opened by using it to prevent this from being a softlock. Note that this can be done even if Korax teleports away normally; Korax is invulnerable and dormant in this scenario and continuing the fight requires defeating the waves of ettins and centaurs as normal.
 - Since there are checks behind the ettin and centaur doors and killing Korax early would normally leave those doors closed, they can also be opened manually.
 - Since the enemy doors in the second area are normally only opened randomly by Korax and there are checks behind those doors, they can now also be opened manually.


