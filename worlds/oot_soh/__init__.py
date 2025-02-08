from worlds.AutoWorld import World, WebWorld
from .Locations import Locations
from .Items import Items

class SoHWebWorld(WebWorld):
    a

class SoHWorld(World):
    game: str = "Ocarina of Time (SoH)"
    web: SoHWebWorld
    required_client_version = (0, 5, 1)
    Items.initialize_item_id_mapping()
    item_name_to_id = Items.all_id_by_name
    location_name_to_id
