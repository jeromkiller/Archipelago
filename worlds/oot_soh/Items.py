from BaseClasses import CollectionState, MultiWorld, Item, ItemClassification
from .ItemList import *
from .Options import *

class SoHItem(Item):
    game = "Ocarina of Time (SoH)"

class Items:
    _next_id = 1

    all_id_by_name = {item[0]: id for id, item in enumerate(all_items_data)}
    #Keys are ids for this
    items_by_id = []
    names_by_id = []
    #Keys are names


    names = []

    #Can have duplicates for items with duplicates. Keys are not ids. For adding to Multiworld.itempool
    items = []
    #For returning filler items
    filler_items = []

    def add_item(name: str, classification: ItemClassification):
        if name in Items.names: #id for this exists
            id = Items.all_id_by_name[name]
        else: #new item, new id
            id = Items._next_id
            Items._next_id = Items._next_id + 1
            Items.items_by_id[id] = Item(name, classification, id)
            Items.names_by_id[id] = name
            Items.names += name
        Items.items += Items.items_by_id[id]
        return id

    def add_filler(name: str):
        if name not in Items.names:
            id = Items._next_id
            Items._next_id = Items._next_id + 1
            item = Item(name, ItemClassification.filler, id)
            Items.items_by_id[id] = item
            Items.names_by_id[id] = name
            Items.filler_items += item

    def create_items_for_settings(self, settings: SoHOptions):
        pass


    def initialize_item_id_mapping(options):
        #Probably should handle in groups. Perhaps another file to organize things?
        #That file should hold many lists of items
        for name, quantity, classification in non_filler_data:
            amount = -1
            classif = classification
            if type(quantity) is int:
                amount = quantity
            else: #quantity is a lambda
                amount = quantity(options)
            if type(classification) is ItemClassification:
                classif = classification
            else:
                classif = classification(options)
            if amount > 0:
                for i in range(amount):
                    Items.add_item(name, classif)
        for name, _, _ in filler_data:
            Items.add_filler(name)