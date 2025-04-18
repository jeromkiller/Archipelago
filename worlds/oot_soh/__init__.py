from worlds.AutoWorld import World, WebWorld
from .Locations import Locations
from .Items import Items
from .Options import SoHOptions, soh_option_groups
from BaseClasses import Tutorial

class SoHWebWorld(WebWorld):
    theme = "grass"
    option_groups = soh_option_groups
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Ocarina of Time (SoH) randomizer connected to an Archipelago Multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["mattman107"]
    )]
    rich_text_options_doc = True
    bug_report_page = "https://github.com/HarbourMasters/Shipwright/issues"    

class SoHWorld(World):
    """
    Ship of Harkinian is an unofficial PC port of the classic N64 game The Legend of Zelda: Ocarina of Time.
    Created by the [HarborMasters64](https://github.com/HarbourMasters) team, it allows players to experience thier favorite old game with the option of 
    modern amenities such as native Windows/Mac/Linux builds, mod support, customizable UI elements, and more!
    """
    
    options_dataclass = SoHOptions
    options: SoHOptions
    game: str = "Ocarina of Time (SoH)"
    web: SoHWebWorld = SoHWebWorld()

    # Sets the starting region to "Root" instead of menu
    origin_region_name = "Root"
    required_client_version = (0, 5, 1)
    Items.initialize_item_id_mapping()
    item_name_to_id = Items.all_id_by_name
    #location_name_to_id
