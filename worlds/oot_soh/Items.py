from BaseClasses import CollectionState, MultiWorld, Item, ItemClassification
from .ItemList import *

all_id_by_name = {}

_next_id = 1
#Keys are ids for this
items_by_id = []

#Keys are names


names = []

#Can have duplicates for items with duplicates. Keys are not ids. For adding to Multiworld.itempool
items = []
#For returning filler items
filler_items = []

def add_item(name: str, classification: ItemClassification):
    global _next_id
    if name in names: #id for this exists
        id = all_id_by_name[name]
    else: #new item, new id
        id = _next_id
        _next_id = _next_id + 1
        items_by_id[id] = Item(name, classification, id)
        names += name
    items += items_by_id[id]
    return id


def create_items_for_settings():
    pass


def initialize_id_mapping(options):
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
                add_item(name, classif)
    for name, _, classification in filler_data:
        pass