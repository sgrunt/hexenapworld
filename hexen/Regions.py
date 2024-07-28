from typing import List
from BaseClasses import TypedDict

class ConnectionDict(TypedDict, total=False):
    target: str
    pro: bool

class RegionDict(TypedDict, total=False):
    name: str
    connects_to_hub: bool
    hub: int
    connections: List[ConnectionDict]


regions:List[RegionDict] = [
    # Seven Portals 
    {"name":"Seven Portals - Winnowing Hall - Main",
     "connects_to_hub":True,
     "hub":1,
     "connections":[
         {"target":"Seven Portals - Winnowing Hall - Emerald Key","pro":False},
         {"target":"Seven Portals - Seven Portals - Main","pro":False}]},
    {"name":"Seven Portals - Winnowing Hall - Emerald Key",
     "connects_to_hub":False,
     "hub":1,
     "connections":[
        {"target":"Seven Portals - Winnowing Hall - Main","pro":False}]},

    {"name":"Seven Portals - Seven Portals - Main",
     "connects_to_hub":False,
     "hub":1,
     "connections":[
        {"target":"Seven Portals - Winnowing Hall - Main","pro":False},
        {"target":"Seven Portals - Seven Portals - Ice Stairs","pro":False},
        {"target":"Seven Portals - Seven Portals - Fire Stairs","pro":False},
        {"target":"Seven Portals - Seven Portals - Steel Stairs","pro":False},
        {"target":"Seven Portals - Seven Portals - Exit Area","pro":False},
        {"target":"Seven Portals - Guardian of Ice - Main","pro":False},
        {"target":"Seven Portals - Guardian of Fire - Main","pro":False},
        {"target":"Seven Portals - Guardian of Steel - Main","pro":False},
        {"target":"Seven Portals - Guardian of Ice - South","pro":False},
        {"target":"Seven Portals - Bright Crucible - Main","pro":False}]},
    {"name":"Seven Portals - Seven Portals - Ice Stairs",
     "connects_to_hub":False,
     "hub":1,
     "connections":[{"target":"Seven Portals - Seven Portals - Main","pro":False}]},
    {"name":"Seven Portals - Seven Portals - Fire Stairs",
     "connects_to_hub":False,
     "hub":1,
     "connections":[{"target":"Seven Portals - Seven Portals - Main","pro":False}]},
    {"name":"Seven Portals - Seven Portals - Steel Stairs",
     "connects_to_hub":False,
     "hub":1,
     "connections":[{"target":"Seven Portals - Seven Portals - Main","pro":False}]},

    {"name":"Seven Portals - Seven Portals - Exit Area",
     "connects_to_hub":False,
     "hub":1,
     "connections":[{"target":"Seven Portals - Seven Portals - Main","pro":False}]},

    {"name":"Seven Portals - Guardian of Ice - Main",
     "connects_to_hub":False,
     "hub":1,
     "connections":[
        {"target":"Seven Portals - Seven Portals - Main","pro":False},
        {"target":"Seven Portals - Guardian of Ice - Fire Door","pro":False},
        {"target":"Seven Portals - Guardian of Ice - Steel Door","pro":False}]},
    {"name":"Seven Portals - Guardian of Ice - South",
     "connects_to_hub":False,
     "hub":1,
     "connections":[
        {"target":"Seven Portals - Guardian of Ice - Main","pro":False},
        {"target":"Seven Portals - Guardian of Ice - Fire Key Access","pro":False}]},
    {"name":"Seven Portals - Guardian of Ice - Fire Key Access",
     "connects_to_hub":False,
     "hub":1,
     "connections":[
        {"target":"Seven Portals - Guardian of Ice - South","pro":False}]},
    {"name":"Seven Portals - Guardian of Ice - Fire Door",
     "connects_to_hub":False,
     "hub":1,
     "connections":[
        {"target":"Seven Portals - Guardian of Ice - Main","pro":False},
        {"target":"Seven Portals - Guardian of Fire - Ice Area","pro":False}]},
    {"name":"Seven Portals - Guardian of Ice - Steel Door",
     "connects_to_hub":False,
     "hub":1,
     "connections":[
        {"target":"Seven Portals - Guardian of Ice - Main","pro":False},
        {"target":"Seven Portals - Guardian of Steel - Ice Area","pro":False}]},

    {"name":"Seven Portals - Guardian of Fire - Main",
     "connects_to_hub":False,
     "hub":1,
     "connections":[
        {"target":"Seven Portals - Seven Portals - Main","pro":False},
        {"target":"Seven Portals - Guardian of Fire - Fire Key","pro":False}]},
    {"name":"Seven Portals - Guardian of Fire - Fire Key",
     "connects_to_hub":False,
     "hub":1,
     "connections":[{"target":"Seven Portals - Guardian of Fire - Main","pro":False}]},
    {"name":"Seven Portals - Guardian of Fire - Ice Area",
     "connects_to_hub":False,
     "hub":1,
     "connections":[{"target":"Seven Portals - Guardian of Fire - Main","pro":False}]},

    {"name":"Seven Portals - Guardian of Steel - Main",
     "connects_to_hub":False,
     "hub":1,
     "connections":[
        {"target":"Seven Portals - Seven Portals - Main","pro":False},
        {"target":"Seven Portals - Guardian of Steel - Steel Key","pro":False}]},
    {"name":"Seven Portals - Guardian of Steel - Steel Key",
     "connects_to_hub":False,
     "hub":1,
     "connections":[{"target":"Seven Portals - Guardian of Steel - Main","pro":False}]},
    {"name":"Seven Portals - Guardian of Steel - Ice Area",
     "connects_to_hub":False,
     "hub":1,
     "connections":[{"target":"Seven Portals - Guardian of Steel - Main","pro":False}]},


    {"name":"Seven Portals - Bright Crucible - Main",
     "connects_to_hub":False,
     "hub":1,
     "connections":[
         {"target":"Seven Portals - Seven Portals - Main","pro":False},
         {"target":"Seven Portals - Bright Crucible - Heart","pro":False}]},

    {"name":"Seven Portals - Bright Crucible - Heart",
     "connects_to_hub":False,
     "hub":1,
     "connections":[{"target":"Seven Portals - Bright Crucible - Main","pro":False}]},

    # Shadow Wood
    {"name":"Shadow Wood - Shadow Wood - Main",
     "connects_to_hub":True,
     "hub":2,
     "connections":[
         {"target":"Shadow Wood - Darkmere - Main","pro":False},
         {"target":"Shadow Wood - Caves of Circe - Main","pro":False},
         {"target":"Shadow Wood - Wastelands - Main","pro":False},
         {"target":"Shadow Wood - Sacred Grove - Main","pro":False},
         {"target":"Shadow Wood - Hypostyle - Main","pro":False}]},

    {"name":"Shadow Wood - Darkmere - Main",
     "connects_to_hub":False,
     "hub":2,
     "connections":[
         {"target":"Shadow Wood - Shadow Wood - Main","pro":False},
         {"target":"Shadow Wood - Darkmere - Castle Key","pro":False},
         {"target":"Shadow Wood - Darkmere - Cave Key","pro":False}]},
    {"name":"Shadow Wood - Darkmere - Castle Key",
     "connects_to_hub":False,
     "hub":2,
     "connections":[
         {"target":"Shadow Wood - Darkmere - Main","pro":False},
         {"target":"Shadow Wood - Darkmere - Horn Key","pro":False}
         ]},
    {"name":"Shadow Wood - Darkmere - Cave Key",
     "connects_to_hub":False,
     "hub":2,
     "connections":[{"target":"Shadow Wood - Darkmere - Main","pro":False}]},
    {"name":"Shadow Wood - Darkmere - Horn Key",
     "connects_to_hub":False,
     "hub":2,
     "connections":[{"target":"Shadow Wood - Darkmere - Castle Key","pro":False}]},

    {"name":"Shadow Wood - Caves of Circe - Main",
     "connects_to_hub":False,
     "hub":2,
     "connections":[
         {"target":"Shadow Wood - Shadow Wood - Main","pro":False},
         {"target":"Shadow Wood - Caves of Circe - Swamp Key","pro":False},
         {"target":"Shadow Wood - Caves of Circe - Horn Key","pro":False}]},
    {"name":"Shadow Wood - Caves of Circe - Swamp Key",
     "connects_to_hub":False,
     "hub":2,
     "connections":[{"target":"Shadow Wood - Caves of Circe - Main","pro":False}]},
    {"name":"Shadow Wood - Caves of Circe - Horn Key",
     "connects_to_hub":False,
     "hub":2,
     "connections":[{"target":"Shadow Wood - Caves of Circe - Main","pro":False}]},

    {"name":"Shadow Wood - Wastelands - Main",
     "connects_to_hub":False,
     "hub":2,
     "connections":[
         {"target":"Shadow Wood - Shadow Wood - Main","pro":False},
         {"target":"Shadow Wood - Wastelands - Cave Key","pro":False},
         {"target":"Shadow Wood - Wastelands - Swamp Key","pro":False}]},
    {"name":"Shadow Wood - Wastelands - Cave Key",
     "connects_to_hub":False,
     "hub":2,
     "connections":[{"target":"Shadow Wood - Wastelands - Main","pro":False}]},
    {"name":"Shadow Wood - Wastelands - Swamp Key",
     "connects_to_hub":False,
     "hub":2,
     "connections":[{"target":"Shadow Wood - Wastelands - Main","pro":False}]},

    {"name":"Shadow Wood - Sacred Grove - Main",
     "connects_to_hub":False,
     "hub":2,
     "connections":[{"target":"Shadow Wood - Shadow Wood - Main","pro":False}]},

    {"name":"Shadow Wood - Hypostyle - Main",
     "connects_to_hub":False,
     "hub":2,
     "connections":[{"target":"Shadow Wood - Shadow Wood - Main","pro":False}]},

    # Heresiarch's Seminary
    {"name":"Heresiarch's Seminary - Heresiarch's Seminary - Main",
     "connects_to_hub":True,
     "hub":3,
     "connections":[
         {"target":"Heresiarch's Seminary - Orchard of Lamentations - Main","pro":False},
         {"target":"Heresiarch's Seminary - Silent Refectory - Main","pro":False},
         {"target":"Heresiarch's Seminary - Heresiarch's Seminary - Chapel Access","pro":False},
         {"target":"Heresiarch's Seminary - Heresiarch's Seminary - Exit Area","pro":False}]},
    {"name":"Heresiarch's Seminary - Heresiarch's Seminary - Chapel Access",
     "connects_to_hub":False,
     "hub":3,
     "connections":[
        {"target":"Heresiarch's Seminary - Heresiarch's Seminary - Main","pro":False},
        {"target":"Heresiarch's Seminary - Dragon Chapel - Main","pro":False},
        {"target":"Heresiarch's Seminary - Wolf Chapel - Main","pro":False},
        {"target":"Heresiarch's Seminary - Griffin Chapel - Main","pro":False}]},
    {"name":"Heresiarch's Seminary - Heresiarch's Seminary - Exit Area",
     "connects_to_hub":False,
     "hub":3,
     "connections":[
        {"target":"Heresiarch's Seminary - Heresiarch's Seminary - Main","pro":False},
        {"target":"Heresiarch's Seminary - Deathwind Chapel - Main","pro":False}]},
    {"name":"Heresiarch's Seminary - Orchard of Lamentations - Main",
     "connects_to_hub":False,
     "hub":3,
     "connections":[{"target":"Heresiarch's Seminary - Heresiarch's Seminary - Main","pro":False}]},
    {"name":"Heresiarch's Seminary - Silent Refectory - Main",
     "connects_to_hub":False,
     "hub":3,
     "connections":[{"target":"Heresiarch's Seminary - Heresiarch's Seminary - Main","pro":False}]},
    {"name":"Heresiarch's Seminary - Dragon Chapel - Main",
     "connects_to_hub":False,
     "hub":3,
     "connections":[
        {"target":"Heresiarch's Seminary - Heresiarch's Seminary - Chapel Access","pro":False},
        {"target":"Heresiarch's Seminary - Dragon Chapel - Wolf","pro":False},
        {"target":"Heresiarch's Seminary - Dragon Chapel - Griffin","pro":False},
        {"target":"Heresiarch's Seminary - Wolf Chapel - Main","pro":False},
        {"target":"Heresiarch's Seminary - Griffin Chapel - Main","pro":False}]},
    {"name":"Heresiarch's Seminary - Dragon Chapel - Wolf",
     "connects_to_hub":False,
     "hub":3,
     "connections":[{"target":"Heresiarch's Seminary - Dragon Chapel - Main","pro":False}]},
    {"name":"Heresiarch's Seminary - Dragon Chapel - Griffin",
     "connects_to_hub":False,
     "hub":3,
     "connections":[{"target":"Heresiarch's Seminary - Dragon Chapel - Main","pro":False}]},
    {"name":"Heresiarch's Seminary - Wolf Chapel - Main",
     "connects_to_hub":False,
     "hub":3,
     "connections":[
        {"target":"Heresiarch's Seminary - Heresiarch's Seminary - Chapel Access","pro":False},
        {"target":"Heresiarch's Seminary - Wolf Chapel - Dragon","pro":False},
        {"target":"Heresiarch's Seminary - Wolf Chapel - Griffin","pro":False},
        {"target":"Heresiarch's Seminary - Dragon Chapel - Main","pro":False},
        {"target":"Heresiarch's Seminary - Griffin Chapel - Main","pro":False}]},
    {"name":"Heresiarch's Seminary - Wolf Chapel - Dragon",
     "connects_to_hub":False,
     "hub":3,
     "connections":[
         {"target":"Heresiarch's Seminary - Wolf Chapel - Main","pro":False}]},
    {"name":"Heresiarch's Seminary - Wolf Chapel - Griffin",
     "connects_to_hub":False,
     "hub":3,
     "connections":[
         {"target":"Heresiarch's Seminary - Wolf Chapel - Main","pro":False}]},
    {"name":"Heresiarch's Seminary - Griffin Chapel - Main",
     "connects_to_hub":False,
     "hub":3,
     "connections":[
        {"target":"Heresiarch's Seminary - Heresiarch's Seminary - Chapel Access","pro":False},
        {"target":"Heresiarch's Seminary - Griffin Chapel - Dragon","pro":False},
        {"target":"Heresiarch's Seminary - Griffin Chapel - Wolf","pro":False},
        {"target":"Heresiarch's Seminary - Wolf Chapel - Main","pro":False},
        {"target":"Heresiarch's Seminary - Dragon Chapel - Main","pro":False}]},
    {"name":"Heresiarch's Seminary - Griffin Chapel - Dragon",
     "connects_to_hub":False,
     "hub":3,
     "connections":[{"target":"Heresiarch's Seminary - Griffin Chapel - Main","pro":False}]},
    {"name":"Heresiarch's Seminary - Griffin Chapel - Wolf",
     "connects_to_hub":False,
     "hub":3,
     "connections":[
         {"target":"Heresiarch's Seminary - Griffin Chapel - Main","pro":False}]},
    {"name":"Heresiarch's Seminary - Deathwind Chapel - Main",
     "connects_to_hub":False,
     "hub":3,
     "connections":[{"target":"Heresiarch's Seminary - Heresiarch's Seminary - Exit Area","pro":False}]},

    # Castle of Grief
    {"name":"Castle of Grief - Castle of Grief - Main",
     "connects_to_hub":True,
     "hub":4,
     "connections":[
        {"target":"Castle of Grief - Forsaken Outpost - Main","pro":False},
        {"target":"Castle of Grief - Castle of Grief - Gibbet Access","pro":False}]},
    {"name":"Castle of Grief - Castle of Grief - Gibbet Access",
     "connects_to_hub":False,
     "hub":4,
     "connections":[
        {"target":"Castle of Grief - Castle of Grief - Main","pro":False},
        {"target":"Castle of Grief - Gibbet - Main","pro":False}]},

    {"name":"Castle of Grief - Forsaken Outpost - Main",
     "connects_to_hub":False,
     "hub":4,
     "connections":[
        {"target":"Castle of Grief - Castle of Grief - Main","pro":False},
        {"target":"Castle of Grief - Forsaken Outpost - Rusted Key","pro":False}]},
    {"name":"Castle of Grief - Forsaken Outpost - Rusted Key",
     "connects_to_hub":False,
     "hub":4,
     "connections":[
        {"target":"Castle of Grief - Forsaken Outpost - Main","pro":False},
        {"target":"Castle of Grief - Desolate Garden - Main","pro":False}]},
    {"name":"Castle of Grief - Forsaken Outpost - From Effluvium",
     "connects_to_hub":False,
     "hub":4,
     "connections":[
        {"target":"Castle of Grief - Effluvium - Dungeons","pro":False},
        {"target":"Castle of Grief - Forsaken Outpost - Main","pro":False}]},

    {"name":"Castle of Grief - Gibbet - Main",
     "connects_to_hub":False,
     "hub":4,
     "connections":[
        {"target":"Castle of Grief - Castle of Grief - Gibbet Access","pro":False},
        {"target":"Castle of Grief - Gibbet - Library","pro":False},
        {"target":"Castle of Grief - Gibbet - Dungeon Key","pro":False},
        {"target":"Castle of Grief - Gibbet - Axe Key Cage","pro":False},
        {"target":"Castle of Grief - Gibbet - Axe Key","pro":False},
        {"target":"Castle of Grief - Effluvium - Main","pro":False}]},
    {"name":"Castle of Grief - Gibbet - Library",
     "connects_to_hub":False,
     "hub":4,
     "connections":[{"target":"Castle of Grief - Gibbet - Main","pro":False}]},
    {"name":"Castle of Grief - Gibbet - Dungeon Key",
     "connects_to_hub":False,
     "hub":4,
     "connections":[
         {"target":"Castle of Grief - Gibbet - Main","pro":False},
         {"target":"Castle of Grief - Dungeons - Main","pro":False}]},

    {"name":"Castle of Grief - Gibbet - Axe Key Cage",
     "connects_to_hub":False,
     "hub":4,
     "connections":[{"target":"Castle of Grief - Gibbet - Main","pro":False}]},
    {"name":"Castle of Grief - Gibbet - Axe Key",
     "connects_to_hub":False,
     "hub":4,
     "connections":[{"target":"Castle of Grief - Gibbet - Main","pro":False}]},

    {"name":"Castle of Grief - Effluvium - Main",
     "connects_to_hub":False,
     "hub":4,
     "connections":[{"target":"Castle of Grief - Gibbet - Main","pro":False}]},
    {"name":"Castle of Grief - Effluvium - Dungeons",
     "connects_to_hub":False,
     "hub":4,
     "connections":[
        {"target":"Castle of Grief - Dungeons - Main","pro":False},
        {"target":"Castle of Grief - Effluvium - Main","pro":False},
        {"target":"Castle of Grief - Forsaken Outpost - From Effluvium","pro":False}]},

    {"name":"Castle of Grief - Dungeons - Main",
     "connects_to_hub":False,
     "hub":4,
     "connections":[
         {"target":"Castle of Grief - Gibbet - Dungeon Key","pro":False},
         {"target":"Castle of Grief - Effluvium - Dungeons","pro":False}]},

    {"name":"Castle of Grief - Desolate Garden - Main",
     "connects_to_hub":False,
     "hub":4,
     "connections":[{"target":"Castle of Grief - Forsaken Outpost - Rusted Key","pro":False}]},

    # Necropolis
    {"name":"Necropolis - Necropolis - Main",
     "connects_to_hub":True,
     "hub":5,
     "connections":[
        {"target":"Necropolis - Vivarium - Main","pro":False},
        {"target":"Necropolis - Zedek's Tomb - Main","pro":False},
        {"target":"Necropolis - Menelkir's Tomb - Main","pro":False},
        {"target":"Necropolis - Traductus' Tomb - Main","pro":False},
        {"target":"Necropolis - Dark Crucible - Main","pro":False}]},

    {"name":"Necropolis - Vivarium - Main",
     "connects_to_hub":False,
     "hub":5,
     "connections":[{"target":"Necropolis - Necropolis - Main","pro":False}]},

    {"name":"Necropolis - Zedek's Tomb - Main",
     "connects_to_hub":False,
     "hub":5,
     "connections":[{"target":"Necropolis - Necropolis - Main","pro":False}]},

    {"name":"Necropolis - Menelkir's Tomb - Main",
     "connects_to_hub":False,
     "hub":5,
     "connections":[{"target":"Necropolis - Necropolis - Main","pro":False}]},

    {"name":"Necropolis - Traductus' Tomb - Main",
     "connects_to_hub":False,
     "hub":5,
     "connections":[{"target":"Necropolis - Necropolis - Main","pro":False}]},

    {"name":"Necropolis - Dark Crucible - Main",
     "connects_to_hub":False,
     "hub":5,
     "connections":[{"target":"Necropolis - Necropolis - Main","pro":False}]},
]
