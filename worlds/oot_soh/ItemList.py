from .Options import SoHOptions
from BaseClasses import ItemClassification
from enum import Enum
from typing import Dict

#TODO replace useful with progression on any item that is used in an access rule. See location access, logic.cpp

#The items which are used anywhere in the logic, or the AP items, alongside names. This way typos are less problematic

major_items: Dict[str, tuple] = [
        ("Kokiri Sword", 1, ItemClassification.progression),
        ("Master Sword", 1, ItemClassification.progression),
        ("Giant's Knife", 1, ItemClassification.progression),
        ("Biggoron Sword", 1, ItemClassification.progression),
        ("Deku Shield", 1, ItemClassification.progression),
        ("Hylian Shield", 1, ItemClassification.progression),
        ("Mirror Shield", 1, ItemClassification.useful),
        ("Goron Tunic", 1, ItemClassification.progression),
        ("Zora Tunic", 1, ItemClassification.progression),
        ("Iron Boots", 1, ItemClassification.useful),
        ("Hover Boots", 1, ItemClassification.useful),
        ("Boomerang", 1, ItemClassification.progression),
        ("Lens of Truth", 1, ItemClassification.useful),
        ("Megaton Hammer", 1, ItemClassification.progression),
        ("Stone of Agony", 1, ItemClassification.progression),
        ("Din's Fire", 1, ItemClassification.progression),
        ("Farore's Wind", 1, ItemClassification.useful),
        ("Nayru's Love", 1, ItemClassification.progression),
        ("Fire Arrow", 1, ItemClassification.progression),
        ("Ice Arrow", 1, ItemClassification.progression),
        ("Light Arrow", 1, ItemClassification.progression),
        ("Gerudo Membership Card", 1, ItemClassification.useful),
        ("Magic Bean", 1, ItemClassification.useful),
        ("Magic Bean Pack", 1, ItemClassification.useful),
        ("Double Defense", 1, ItemClassification.useful),
]


trade_items: Dict[str, tuple] = [
        ("Weird Egg", 1, ItemClassification.useful),
        ("Zelda's Letter", 1, ItemClassification.useful),
        ("Pocket Egg", 1, ItemClassification.useful),
        ("Cojiro", 1, ItemClassification.useful),
        ("Odd Mushroom", 1, ItemClassification.useful),
        ("Odd Potion", 1, ItemClassification.useful),
        ("Poacher's Saw", 1, ItemClassification.useful),
        ("Broken Goron's Sword", 1, ItemClassification.useful),
        ("Prescription", 1, ItemClassification.useful),
        ("Eyeball Frog", 1, ItemClassification.useful),
        ("World's Finest Eyedrops", 1, ItemClassification.useful),
        ("Claim Check", 1, ItemClassification.useful),
]


progressive_item_data: Dict[str, tuple] = [
        ("Progressive Stick Upgrade", (lambda options: 2), ItemClassification.useful),
        ("Progressive Nut Upgrade", (lambda options: 2), ItemClassification.useful),
        ("Progressive Bomb Bag", (lambda options: 3), ItemClassification.progression),
        ("Progressive Bow", (lambda options: 3), ItemClassification.progression),
        ("Progressive Slingshot", (lambda options: 3), ItemClassification.progression),
        ("Progressive Ocarina", (lambda options: 1), ItemClassification.progression),
        ("Progressive Hookshot", (lambda options: 2), ItemClassification.progression),
        ("Strength Upgrade", (lambda options: 3), ItemClassification.progression),
        ("Progressive Wallet", (lambda options: 2), ItemClassification.useful),
        ("Progressive Scale", (lambda options: 2), ItemClassification.useful),
        ("Progressive Magic Meter", (lambda options: 2), ItemClassification.progression),
        ("Progressive Bombchus", (lambda options: 1), ItemClassification.progression),
        ("Progressive Goron Sword", (lambda options: 0), ItemClassification.progression),
]


skulltula_data: Dict[str, tuple] = [
        ("Gold Skulltula Token", 100, ItemClassification.useful),
]


bottles_data: Dict[str, tuple] = [
        ("Empty Bottle", 1, ItemClassification.progression),
        ("Bottle with Milk", 1, ItemClassification.useful),
        ("Bottle with Red Potion", 1, ItemClassification.useful),
        ("Bottle with Green Potion", 1, ItemClassification.useful),
        ("Bottle with Blue Potion", 1, ItemClassification.useful),
        ("Bottle with Fairy", 1, ItemClassification.useful),
        ("Bottle with Fish", 1, ItemClassification.useful),
        ("Bottle with Blue Fire", 1, ItemClassification.useful),
        ("Bottle with Bugs", 1, ItemClassification.useful),
        ("Bottle with Poe", 1, ItemClassification.useful),
        ("Bottle with Ruto's Letter", 1, ItemClassification.useful),
        ("Bottle with Big Poe", 1, ItemClassification.useful),
]


songs_data: Dict[str, tuple] = [
        ("Zelda's Lullaby", 1, ItemClassification.useful),
        ("Epona's Song", 1, ItemClassification.useful),
        ("Saria's Song", 1, ItemClassification.useful),
        ("Sun's Song", 1, ItemClassification.useful),
        ("Song of Time", 1, ItemClassification.useful),
        ("Song of Storms", 1, ItemClassification.useful),
        ("Minuet of Forest", 1, ItemClassification.useful),
        ("Bolero of Fire", 1, ItemClassification.useful),
        ("Serenade of Water", 1, ItemClassification.useful),
        ("Nocturne of Shadow", 1, ItemClassification.useful),
        ("Requiem of Spirit", 1, ItemClassification.useful),
        ("Prelude of Light", 1, ItemClassification.useful),
]


maps_compasses_data: Dict[str, tuple] = [
        ("Great Deku Tree Map", 1, ItemClassification.useful),
        ("Dodongo's Cavern Map", 1, ItemClassification.useful),
        ("Jabu-Jabu's Belly Map", 1, ItemClassification.useful),
        ("Forest Temple Map", 1, ItemClassification.useful),
        ("Fire Temple Map", 1, ItemClassification.useful),
        ("Water Temple Map", 1, ItemClassification.useful),
        ("Spirit Temple Map", 1, ItemClassification.useful),
        ("Shadow Temple Map", 1, ItemClassification.useful),
        ("Bottom of the Well Map", 1, ItemClassification.useful),
        ("Ice Cavern Map", 1, ItemClassification.useful),
        ("Great Deku Tree Compass", 1, ItemClassification.useful),
        ("Dodongo's Cavern Compass", 1, ItemClassification.useful),
        ("Jabu-Jabu's Belly Compass", 1, ItemClassification.useful),
        ("Forest Temple Compass", 1, ItemClassification.useful),
        ("Fire Temple Compass", 1, ItemClassification.useful),
        ("Water Temple Compass", 1, ItemClassification.useful),
        ("Spirit Temple Compass", 1, ItemClassification.useful),
        ("Shadow Temple Compass", 1, ItemClassification.useful),
        ("Bottom of the Well Compass", 1, ItemClassification.useful),
        ("Ice Cavern Compass", 1, ItemClassification.useful),
]


keys_data: Dict[str, tuple] = [
        ("Forest Temple Boss Key", 1, ItemClassification.useful),
        ("Fire Temple Boss Key", 1, ItemClassification.useful),
        ("Water Temple Boss Key", 1, ItemClassification.useful),
        ("Spirit Temple Boss Key", 1, ItemClassification.useful),
        ("Shadow Temple Boss Key", 1, ItemClassification.useful),
        ("Ganon's Castle Boss Key", 1, ItemClassification.useful),
        ("Forest Temple Small Key", 1, ItemClassification.useful),
        ("Fire Temple Small Key", 1, ItemClassification.useful),
        ("Water Temple Small Key", 1, ItemClassification.useful),
        ("Spirit Temple Small Key", 1, ItemClassification.useful),
        ("Shadow Temple Small Key", 1, ItemClassification.useful),
        ("Bottom of the Well Small Key", 1, ItemClassification.useful),
        ("Training Ground Small Key", 1, ItemClassification.useful),
        ("Gerudo Fortress Small Key", 1, ItemClassification.useful),
        ("Ganon's Castle Small Key", 1, ItemClassification.useful),
        ("Chest Game Small Key", 1, ItemClassification.useful),
        ("Guard House Key", 1, ItemClassification.useful),
        ("Market Bazaar Key", 1, ItemClassification.useful),
        ("Market Potion Shop Key", 1, ItemClassification.useful),
        ("Mask Shop Key", 1, ItemClassification.useful),
        ("Market Shooting Gallery Key", 1, ItemClassification.useful),
        ("Bombchu Bowling Alley Key", 1, ItemClassification.useful),
        ("Treasure Chest Game Building Key", 1, ItemClassification.useful),
        ("Bombchu Shop Key", 1, ItemClassification.useful),
        ("Richard's House Key", 1, ItemClassification.useful),
        ("Alley House Key", 1, ItemClassification.useful),
        ("Kakariko Bazaar Key", 1, ItemClassification.useful),
        ("Kakariko Potion Shop Key", 1, ItemClassification.useful),
        ("Boss's House Key", 1, ItemClassification.useful),
        ("Granny's Potion Shop Key", 1, ItemClassification.useful),
        ("Skulltula House Key", 1, ItemClassification.useful),
        ("Impa's House Key", 1, ItemClassification.useful),
        ("Windmill Key", 1, ItemClassification.useful),
        ("Kakariko Shooting Gallery Key", 1, ItemClassification.useful),
        ("Dampe's Hut Key", 1, ItemClassification.useful),
        ("Talon's House Key", 1, ItemClassification.useful),
        ("Stables Key", 1, ItemClassification.useful),
        ("Back Tower Key", 1, ItemClassification.useful),
        ("Hylia Laboratory Key", 1, ItemClassification.useful),
        ("Fishing Hole Key", 1, ItemClassification.useful),
]


key_rings_data: Dict[str, tuple] = [
        ("Forest Temple Key Ring", 1, ItemClassification.useful),
        ("Fire Temple Key Ring", 1, ItemClassification.useful),
        ("Water Temple Key Ring", 1, ItemClassification.useful),
        ("Spirit Temple Key Ring", 1, ItemClassification.useful),
        ("Shadow Temple Key Ring", 1, ItemClassification.useful),
        ("Bottom of the Well Key Ring", 1, ItemClassification.useful),
        ("Training Ground Key Ring", 1, ItemClassification.useful),
        ("Gerudo Fortress Key Ring", 1, ItemClassification.useful),
        ("Ganon's Castle Key Ring", 1, ItemClassification.useful),
        ("Chest Game Key Ring", 1, ItemClassification.useful),
]


dungeon_reward_data: Dict[str, tuple] = [
        ("Kokiri Emerald", 1, (lambda options: ItemClassification.progression)),
        ("Goron Ruby", 1, (lambda options: ItemClassification.progression)),
        ("Zora Sapphire", 1, (lambda options: ItemClassification.progression)),
        ("Forest Medallion", 1, ItemClassification.progression),
        ("Fire Medallion", 1, ItemClassification.progression),
        ("Water Medallion", 1, ItemClassification.progression),
        ("Spirit Medallion", 1, (lambda options: ItemClassification.progression)),
        ("Shadow Medallion", 1, (lambda options: ItemClassification.progression)),
        ("Light Medallion", 1, (lambda options: ItemClassification.progression)),
]


boss_soul_data: Dict[str, tuple] = [
        ("Gohma's Soul", 1, ItemClassification.progression),
        ("King Dodongo's Soul", 1, ItemClassification.progression),
        ("Barinade's Soul", 1, ItemClassification.progression),
        ("Phantom Ganon's Soul", 1, ItemClassification.progression),
        ("Volvagia's Soul", 1, ItemClassification.progression),
        ("Morpha's Soul", 1, ItemClassification.progression),
        ("Bongo Bongo's Soul", 1, ItemClassification.progression),
        ("Twinrova's Soul", 1, ItemClassification.progression),
        ("Ganon's Soul", 1, ItemClassification.progression),
]


other_setting_item_data: Dict[str, tuple] = [
        ("Fishing Pole", 1, ItemClassification.useful),
        ("Ocarina A Button", 1, ItemClassification.useful),
        ("Ocarina C Up Button", 1, ItemClassification.useful),
        ("Ocarina C Down Button", 1, ItemClassification.useful),
        ("Ocarina C Left Button", 1, ItemClassification.useful),
        ("Ocarina C Right Button", 1, ItemClassification.useful),
        ("Bronze Scale", 1, ItemClassification.useful),
        ("Bombchu Bag", 1, ItemClassification.useful),
        ("Infinite Quiver", 1, ItemClassification.useful),
        ("Infinite Bomb Bag", 1, ItemClassification.useful),
        ("Infinite Bullet Bag", 1, ItemClassification.useful),
        ("Infinite Stick Capacity", 1, ItemClassification.useful),
        ("Infinite Nut Capacity", 1, ItemClassification.useful),
        ("Infinite Magic Meter", 1, ItemClassification.useful),
        ("Infinite Bombchus", 1, ItemClassification.useful),
        ("Infinite Wallet", 1, ItemClassification.useful),
        ("Skeleton Key", 1, ItemClassification.useful),
        ("Deku Stick Bag", 1, ItemClassification.useful),
        ("Deku Nut Bag", 1, ItemClassification.useful),
        ("Triforce", 1, ItemClassification.useful),
]


special_item_data: Dict[str, tuple] = [
        ("Greg the Green Rupee", 1, ItemClassification.useful),
        ("Huge Rupee", 1, ItemClassification.useful),
        ("Piece of Heart", 35, ItemClassification.useful),
        ("Heart Container", 8, ItemClassification.useful),
        ("Piece of Heart (WINNER)", 1, ItemClassification.useful),
        ("Green Rupee (LOSER)", 1, ItemClassification.filler),
]


non_useful_item_data: Dict[str, tuple] = [
        ("Recovery Heart", 6, ItemClassification.filler),
        ("Bombs (5)", 2, ItemClassification.filler),
        ("Bombs (10)", 2, ItemClassification.filler),
        ("Arrows (5)", 2, ItemClassification.filler),
        ("Arrows (10)", 3, ItemClassification.filler),
        ("Blue Rupee", 13, ItemClassification.filler),
        ("Red Rupee", 5, ItemClassification.filler),
        ("Purple Rupee", 7, ItemClassification.filler),
        ("Huge Rupee", 3, ItemClassification.filler),
]


filler_data: Dict[str, tuple] = [
        ("Recovery Heart", -1, ItemClassification.filler),
        ("Green Rupee", -1, ItemClassification.filler),
        ("Blue Rupee", -1, ItemClassification.filler),
        ("Red Rupee", -1, ItemClassification.filler),
        ("Purple Rupee", -1, ItemClassification.filler),
        ("Ice Trap", -1, ItemClassification.filler),
        ("Milk", -1, ItemClassification.filler),
        ("Fish", -1, ItemClassification.filler),
        ("Bombs (5)", -1, ItemClassification.filler),
        ("Bombs (10)", -1, ItemClassification.filler),
        ("Bombs (20)", -1, ItemClassification.filler),
        ("Bombchus (5)", -1, ItemClassification.filler),
        ("Bombchus (10)", -1, ItemClassification.filler),
        ("Bombchus (20)", -1, ItemClassification.filler),
        ("Arrows (5)", -1, ItemClassification.filler),
        ("Arrows (10)", -1, ItemClassification.filler),
        ("Arrows (30)", -1, ItemClassification.filler),
        ("Deku Nuts (5)", -1, ItemClassification.filler),
        ("Deku Nuts (10)", -1, ItemClassification.filler),
        ("Deku Seeds (30)", -1, ItemClassification.filler),
        ("Deku Stick (1)", -1, ItemClassification.filler),
        ("Red Potion Refill", -1, ItemClassification.filler),
        ("Green Potion Refill", -1, ItemClassification.filler),
        ("Blue Potion Refill", -1, ItemClassification.filler),
]

non_filler_data = major_items + trade_items + progressive_item_data + skulltula_data + bottles_data + songs_data \
+ maps_compasses_data + keys_data + key_rings_data + dungeon_reward_data + boss_soul_data + other_setting_item_data + special_item_data + non_useful_item_data
all_items_data = non_filler_data + filler_data
