from .Items import *
from .Locations import *
from BaseClasses import CollectionState

class Logic:
    def has_item(name: str, state: CollectionState, player: int, count: int = 1):
        if name in state.prog_items[player].keys:
            return state.count(name, player) >= count
        return False

    def can_use_item(name: str, state: CollectionState, player: int, progressive_stage = 1):
        if not Logic.has_item(str, state, player, progressive_stage):
            return False
        match name:
            case _:
                return True #Assuming the item has no additional requirements beyond having the item. has_item should be used instead, however. 
    

