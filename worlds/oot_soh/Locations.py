from BaseClasses import CollectionState, MultiWorld, Location, LocationProgressType, Region

class Locations:
    regions = [None]
    locations = [None]
    ids_by_name = {}

class SoHLocation(Location):
    game = "Ocarina of Time (SoH)"