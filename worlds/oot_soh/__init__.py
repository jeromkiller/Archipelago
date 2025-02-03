from worlds.AutoWorld import World, WebWorld
from .Locations import *
from .Items import *

class SoHWebWorld(WebWorld):
    a

class SoHWorld(World):
    game: str = "Ocarina of Time (SoH)"
    web: SoHWebWorld
    required_client_version = (0, 5, 1)
    item_name_to_id
    location_name_to_id
