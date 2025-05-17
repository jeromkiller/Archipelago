from typing import List, Dict, Any

from worlds.AutoWorld import World, WebWorld
from .Locations import Locations, SoHLocation
from .LocationList import loc_id_by_name
from .Items import Items, SoHItem
from .ItemList import all_items_data, non_filler_data, filler_data
from .Options import SoHOptions, soh_option_groups
from .noOptions import noSoHOptions
from BaseClasses import Tutorial, Item, ItemClassification, Region

class SoHWebWorld(WebWorld):
    theme = "grass"
    #option_groups = soh_option_groups
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
    
    options_dataclass = noSoHOptions
    options: noSoHOptions
    game: str = "Ocarina of Time (SoH)"
    web: SoHWebWorld = SoHWebWorld()

    # Sets the starting region to "Root" instead of menu
    origin_region_name = "Root"
    required_client_version = (0, 5, 1)
    #Items.initialize_item_id_mapping(options)
    item_name_to_id = Items.all_id_by_name

    location_name_to_id = loc_id_by_name

    def create_item(self, name: str) -> SoHItem:
        item_entry = [item for item in all_items_data if item[0] == name][0]
        name, num, classification = item_entry
        if callable(classification):
            classification = classification(noSoHOptions)

        id = Items.all_id_by_name[name]
        return SoHItem(name, classification, id, self.player)
    
    def create_items(self) -> None:
        item_pool: List[SoHItem] = list()

        # add non filler data
        for name, num, classification in non_filler_data:
            if callable(num):
                num = num(True)

            if(num < 1):
                continue    # idk if this can happen
            item_group = (self.create_item(name) for _ in range(num))
            item_pool.extend(item_group)

        while len(LocationList.locations) != len(item_pool):
            # just fill with recovery hearts for now
            # It would be better to randomize these
            name = "Recovery Heart"
            item_pool.append(SoHItem(name, ItemClassification.filler, Items.all_id_by_name[name], self.player))

        self.multiworld.itempool += item_pool

    def create_regions(self):
        menu_region = Region("Root", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)

        game_region = Region("The Game", self.player, self.multiworld)
        
        game_region.add_locations({
            name: id for name, id in LocationList.loc_id_by_name.items()
        }, SoHLocation)
        self.multiworld.regions.append(game_region)

        self.multiworld.get_region("Root", self.player).add_exits(["The Game"])

    def fill_slot_data(self) -> Dict[str, Any]:
        return {
            "Settings": "Todo"
        }        

