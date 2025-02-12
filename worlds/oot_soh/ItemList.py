from .Options import SoHOptions
from BaseClasses import ItemClassification
from enum import Enum

#TODO replace useful with progression on any item that is used in an access rule. See location access, logic.cpp

#The items which are used anywhere in the logic, or the AP items, alongside names. This way typos are less problematic
class Items(str, Enum):
    kokiri_sword = "Kokiri Sword"
    master_sword = "Master Sword"
    giants_knife = "Giant's Knife"
    biggoron_sword = "Biggoron Sword"
    deku_shield = "Deku Shield"
    hylian_shield = "Hylian Shield"
    mirror_shield = "Mirror Shield"
    goron_tunic = "Goron Tunic"
    zora_tunic = "Zora Tunic"
    iron_boots = "Iron Boots"
    hover_boots = "Hover Boots"
    boomerang = "Boomerang"
    lens_of_truth = "Lens of Truth"
    megaton_hammer = "Megaton Hammer"
    stone_of_agony = "Stone of Agony"
    dins_fire = "Din's Fire"
    farores_wind = "Farore's Wind"
    nayrus_love = "Nayru's Love"
    fire_arrows = "Fire Arrow"
    ice_arrows = "Ice Arrow"
    light_arrows = "Light Arrow"
    gerudo_membership_card = "Gerudo Membership Card"
    magic_bean = "Magic Bean"
    magic_bean_pack = "Magic Bean Pack"
    double_defense = "Double Defense"
    weird_egg = "Weird Egg"
    zeldas_letter = "Zelda's Letter"
    pocket_egg = "Pocket Egg"
    cojiro = "Cojiro"
    odd_mushroom = "Odd Mushroom"
    odd_potion = "Odd Potion"
    poachers_saw = "Poacher's Saw"
    broken_gorons_sword = "Broken Goron's Sword"
    prescription = "Prescription"
    eyeball_frog = "Eyeball Frog"
    worlds_finest_eyedrops = "World's Finest Eyedrops"
    claim_check = "Claim Check"
    gold_skulltula_token = "Gold Skulltula Token"
    progressive_stick_upgrade = "Progressive Stick Upgrade"
    progressive_nut_upgrade = "Progressive Nut Upgrade"
    progressive_bombs = "Progressive Bomb Bag"
    progressive_bow = "Progressive Bow"
    progressive_slingshot = "Progressive Slingshot"
    progressive_ocarina = "Progressive Ocarina"
    progressive_hookshot = "Progressive Hookshot"
    progressive_strength = "Strength Upgrade"
    progressive_wallet = "Progressive Wallet"
    progressive_scale = "Progressive Scale"
    progressive_magic_meter = "Progressive Magic Meter"
    progressive_bombchus = "Progressive Bombchus"
    progressive_goron_sword = "Progressive Goron Sword"
    empty_bottle = "Empty Bottle"
    bottle_with_milk = "Bottle with Milk"
    bottle_with_red_potion = "Bottle with Red Potion"
    bottle_with_green_potion = "Bottle with Green Potion"
    bottle_with_blue_potion = "Bottle with Blue Potion"
    bottle_with_fairy = "Bottle with Fairy"
    bottle_with_fish = "Bottle with Fish"
    bottle_with_blue_fire = "Bottle with Blue Fire"
    bottle_with_bugs = "Bottle with Bugs"
    bottle_with_poe = "Bottle with Poe"
    bottle_with_rutos_letter = "Bottle with Ruto's Letter"
    bottle_with_big_poe = "Bottle with Big Poe"
    zeldas_lullaby = "Zelda's Lullaby"
    eponas_song = "Epona's Song"
    sarias_song = "Saria's Song"
    suns_song = "Sun's Song"
    song_of_time = "Song of Time"
    song_of_storms = "Song of Storms"
    minuet_of_forest = "Minuet of Forest"
    bolero_of_fire = "Bolero of Fire"
    serenade_of_water = "Serenade of Water"
    nocturne_of_shadow = "Nocturne of Shadow"
    requiem_of_spirit = "Requiem of Spirit"
    prelude_of_light = "Prelude of Light"
    great_deku_tree_map = "Great Deku Tree Map"
    dodongos_cavern_map = "Dodongo's Cavern Map"
    jabujabus_belly_map = "Jabu-Jabu's Belly Map"
    forest_temple_map = "Forest Temple Map"
    fire_temple_map = "Fire Temple Map"
    water_temple_map = "Water Temple Map"
    spirit_temple_map = "Spirit Temple Map"
    shadow_temple_map = "Shadow Temple Map"
    bottom_of_the_well_map = "Bottom of the Well Map"
    ice_cavern_map = "Ice Cavern Map"
    great_deku_tree_compass = "Great Deku Tree Compass"
    dodongos_cavern_compass = "Dodongo's Cavern Compass"
    jabujabus_belly_compass = "Jabu-Jabu's Belly Compass"
    forest_temple_compass = "Forest Temple Compass"
    fire_temple_compass = "Fire Temple Compass"
    water_temple_compass = "Water Temple Compass"
    spirit_temple_compass = "Spirit Temple Compass"
    shadow_temple_compass = "Shadow Temple Compass"
    bottom_of_the_well_compass = "Bottom of the Well Compass"
    ice_cavern_compass = "Ice Cavern Compass"
    forest_temple_boss_key = "Forest Temple Boss Key"
    fire_temple_boss_key = "Fire Temple Boss Key"
    water_temple_boss_key = "Water Temple Boss Key"
    spirit_temple_boss_key = "Spirit Temple Boss Key"
    shadow_temple_boss_key = "Shadow Temple Boss Key"
    ganons_castle_boss_key = "Ganon's Castle Boss Key"
    forest_temple_small_key = "Forest Temple Small Key"
    fire_temple_small_key = "Fire Temple Small Key"
    water_temple_small_key = "Water Temple Small Key"
    spirit_temple_small_key = "Spirit Temple Small Key"
    shadow_temple_small_key = "Shadow Temple Small Key"
    bottom_of_the_well_small_key = "Bottom of the Well Small Key"
    training_ground_small_key = "Training Ground Small Key"
    gerudo_fortress_small_key = "Gerudo Fortress Small Key"
    ganons_castle_small_key = "Ganon's Castle Small Key"
    chest_game_small_key = "Chest Game Small Key"
    guard_house_key = "Guard House Key"
    market_bazaar_key = "Market Bazaar Key"
    market_potion_shop_key = "Market Potion Shop Key"
    mask_shop_key = "Mask Shop Key"
    market_shooting_gallery_key = "Market Shooting Gallery Key"
    bombchu_bowling_alley_key = "Bombchu Bowling Alley Key"
    treasure_chest_game_building_key = "Treasure Chest Game Building Key"
    bombchu_shop_key = "Bombchu Shop Key"
    richards_house_key = "Richard's House Key"
    alley_house_key = "Alley House Key"
    kakariko_bazaar_key = "Kakariko Bazaar Key"
    kakariko_potion_shop_key = "Kakariko Potion Shop Key"
    bosss_house_key = "Boss's House Key"
    grannys_potion_shop_key = "Granny's Potion Shop Key"
    skulltula_house_key = "Skulltula House Key"
    impas_house_key = "Impa's House Key"
    windmill_key = "Windmill Key"
    kakariko_shooting_gallery_key = "Kakariko Shooting Gallery Key"
    dampes_hut_key = "Dampe's Hut Key"
    talons_house_key = "Talon's House Key"
    stables_key = "Stables Key"
    back_tower_key = "Back Tower Key"
    hylia_laboratory_key = "Hylia Laboratory Key"
    fishing_hole_key = "Fishing Hole Key"
    forest_temple_key_ring = "Forest Temple Key Ring"
    fire_temple_key_ring = "Fire Temple Key Ring"
    water_temple_key_ring = "Water Temple Key Ring"
    spirit_temple_key_ring = "Spirit Temple Key Ring"
    shadow_temple_key_ring = "Shadow Temple Key Ring"
    bottom_of_the_well_key_ring = "Bottom of the Well Key Ring"
    training_ground_key_ring = "Training Ground Key Ring"
    gerudo_fortress_key_ring = "Gerudo Fortress Key Ring"
    ganons_castle_key_ring = "Ganon's Castle Key Ring"
    chest_game_key_ring = "Chest Game Key Ring"
    kokiri_emerald = "Kokiri Emerald"
    goron_ruby = "Goron Ruby"
    zora_sapphire = "Zora Sapphire"
    forest_medallion = "Forest Medallion"
    fire_medallion = "Fire Medallion"
    water_medallion = "Water Medallion"
    spirit_medallion = "Spirit Medallion"
    shadow_medallion = "Shadow Medallion"
    light_medallion = "Light Medallion"
    recovery_heart = "Recovery Heart"
    green_rupee = "Green Rupee"
    blue_rupee = "Blue Rupee"
    red_rupee = "Red Rupee"
    purple_rupee = "Purple Rupee"
    ice_trap = "Ice Trap"
    milk = "Milk"
    fish = "Fish"
    bombs_5 = "Bombs (5)"
    bombs_10 = "Bombs (10)"
    bombs_20 = "Bombs (20)"
    bombchus_5 = "Bombchus (5)"
    bombchus_10 = "Bombchus (10)"
    bombchus_20 = "Bombchus (20)"
    arrows_5 = "Arrows (5)"
    arrows_10 = "Arrows (10)"
    arrows_30 = "Arrows (30)"
    deku_nuts_5 = "Deku Nuts (5)"
    deku_nuts_10 = "Deku Nuts (10)"
    deku_seeds_30 = "Deku Seeds (30)"
    deku_stick_1 = "Deku Stick (1)"
    red_potion_refill = "Red Potion Refill"
    green_potion_refill = "Green Potion Refill"
    blue_potion_refill = "Blue Potion Refill"
    gohmas_soul = "Gohma's Soul"
    king_dodongos_soul = "King Dodongo's Soul"
    barinades_soul = "Barinade's Soul"
    phantom_ganons_soul = "Phantom Ganon's Soul"
    volvagias_soul = "Volvagia's Soul"
    morphas_soul = "Morpha's Soul"
    bongo_bongos_soul = "Bongo Bongo's Soul"
    twinrovas_soul = "Twinrova's Soul"
    ganons_soul = "Ganon's Soul"
    fishing_pole = "Fishing Pole"
    ocarina_a_button = "Ocarina A Button"
    ocarina_c_up_button = "Ocarina C Up Button"
    ocarina_c_down_button = "Ocarina C Down Button"
    ocarina_c_left_button = "Ocarina C Left Button"
    ocarina_c_right_button = "Ocarina C Right Button"
    bronze_scale = "Bronze Scale"
    bombchu_bag = "Bombchu Bag"
    infinite_quiver = "Infinite Quiver"
    infinite_bomb_bag = "Infinite Bomb Bag"
    infinite_bullet_bag = "Infinite Bullet Bag"
    infinite_stick_capacity = "Infinite Stick Capacity"
    infinite_nut_capacity = "Infinite Nut Capacity"
    infinite_magic_meter = "Infinite Magic Meter"
    infinite_bombchus = "Infinite Bombchus"
    infinite_wallet = "Infinite Wallet"
    skeleton_key = "Skeleton Key"
    deku_stick_bag = "Deku Stick Bag"
    deku_nut_bag = "Deku Nut Bag"
    triforce = "Triforce"
    recovery_heart = "Recovery Heart"
    bombs_5 = "Bombs (5)"
    bombs_10 = "Bombs (10)"
    arrows_5 = "Arrows (5)"
    arrows_10 = "Arrows (10)"
    blue_rupee = "Blue Rupee"
    red_rupee = "Red Rupee"
    purple_rupee = "Purple Rupee"
    huge_rupee = "Huge Rupee"
    greg_the_green_rupee = "Greg the Green Rupee"
    huge_rupee = "Huge Rupee"
    piece_of_heart = "Piece of Heart"
    heart_container = "Heart Container"
    piece_of_heart_winner = "Piece of Heart (WINNER)"
    green_rupee_loser = "Green Rupee (LOSER)"
    poachers_saw = "Poacher's Saw"

    #Not strictly AP items, but used in logic
    epona = "Epona"
    deku_nut = "Deku Nut"
    deku_stick = "Deku Stick"


major_items = [
    (Items.kokiri_sword, 1, ItemClassification.useful),
    (Items.master_sword, 1, ItemClassification.useful),
    (Items.giants_knife, 1, ItemClassification.useful),
    (Items.biggoron_sword, 1, ItemClassification.useful),
    (Items.deku_shield, 1, ItemClassification.useful),
    (Items.hylian_shield, 1, ItemClassification.useful),
    (Items.mirror_shield, 1, ItemClassification.useful),
    (Items.goron_tunic, 1, ItemClassification.useful),
    (Items.zora_tunic, 1, ItemClassification.useful),
    (Items.iron_boots, 1, ItemClassification.useful),
    (Items.hover_boots, 1, ItemClassification.useful),
    (Items.boomerang, 1, ItemClassification.useful),
    (Items.lens_of_truth, 1, ItemClassification.useful),
    (Items.megaton_hammer, 1, ItemClassification.useful),
    (Items.stone_of_agony, 1, ItemClassification.useful),
    (Items.dins_fire, 1, ItemClassification.useful),
    (Items.farores_wind, 1, ItemClassification.useful),
    (Items.nayrus_love, 1, ItemClassification.useful),
    (Items.fire_arrows, 1, ItemClassification.useful),
    (Items.ice_arrows, 1, ItemClassification.useful),
    (Items.light_arrows, 1, ItemClassification.useful),
    (Items.gerudo_membership_card, 1, ItemClassification.useful),
    (Items.magic_bean, 1, ItemClassification.useful),
    (Items.magic_bean_pack, 1, ItemClassification.useful),
    (Items.double_defense, 1, ItemClassification.useful)
]
trade_items = [
    (Items.weird_egg, 1, ItemClassification.useful),
    (Items.zeldas_letter, 1, ItemClassification.useful),
    (Items.pocket_egg, 1, ItemClassification.useful),
    (Items.cojiro, 1, ItemClassification.useful),
    (Items.odd_mushroom, 1, ItemClassification.useful),
    (Items.odd_potion, 1, ItemClassification.useful),
    (Items.poachers_saw, 1, ItemClassification.useful),
    (Items.broken_gorons_sword, 1, ItemClassification.useful),
    (Items.prescription, 1, ItemClassification.useful),
    (Items.eyeball_frog, 1, ItemClassification.useful),
    (Items.worlds_finest_eyedrops, 1, ItemClassification.useful),
    (Items.claim_check, 1, ItemClassification.useful)
]
skulltula_data = [
    (Items.gold_skulltula_token, 100, ItemClassification.useful)
]
progressive_item_data = [
    (Items.progressive_stick_upgrade, (lambda options: 2), ItemClassification.useful),
    (Items.progressive_nut_upgrade, (lambda options: 2), ItemClassification.useful),
    (Items.progressive_bombs, (lambda options: 3), ItemClassification.useful),
    (Items.progressive_bow, (lambda options: 3), ItemClassification.useful),
    (Items.progressive_slingshot, (lambda options: 3), ItemClassification.useful),
    (Items.progressive_ocarina, (lambda options: 1), ItemClassification.useful),
    (Items.progressive_hookshot, (lambda options: 2), ItemClassification.useful),
    (Items.progressive_strength, (lambda options: 3), ItemClassification.useful),
    (Items.progressive_wallet, (lambda options: 2), ItemClassification.useful),
    (Items.progressive_scale, (lambda options: 2), ItemClassification.useful),
    (Items.progressive_magic_meter, (lambda options: 2), ItemClassification.useful),
    (Items.progressive_bombchus, (lambda options: 1), ItemClassification.useful),
    (Items.progressive_goron_sword, (lambda options: 0), ItemClassification.useful)
]
bottles_data = [
    (Items.empty_bottle, 1, ItemClassification.useful),
    (Items.bottle_with_milk, 1, ItemClassification.useful),
    (Items.bottle_with_red_potion, 1, ItemClassification.useful),
    (Items.bottle_with_green_potion, 1, ItemClassification.useful),
    (Items.bottle_with_blue_potion, 1, ItemClassification.useful),
    (Items.bottle_with_fairy, 1, ItemClassification.useful),
    (Items.bottle_with_fish, 1, ItemClassification.useful),
    (Items.bottle_with_blue_fire, 1, ItemClassification.useful),
    (Items.bottle_with_bugs, 1, ItemClassification.useful),
    (Items.bottle_with_poe, 1, ItemClassification.useful),
    (Items.bottle_with_rutos_letter, 1, ItemClassification.useful),
    (Items.bottle_with_big_poe, 1, ItemClassification.useful)
]

songs_data = [
    (Items.zeldas_lullaby, 1, ItemClassification.useful),
    (Items.eponas_song, 1, ItemClassification.useful),
    (Items.sarias_song, 1, ItemClassification.useful),
    (Items.suns_song, 1, ItemClassification.useful),
    (Items.song_of_time, 1, ItemClassification.useful),
    (Items.song_of_storms, 1, ItemClassification.useful),
    (Items.minuet_of_forest, 1, ItemClassification.useful),
    (Items.bolero_of_fire, 1, ItemClassification.useful),
    (Items.serenade_of_water, 1, ItemClassification.useful),
    (Items.nocturne_of_shadow, 1, ItemClassification.useful),
    (Items.requiem_of_spirit, 1, ItemClassification.useful),
    (Items.prelude_of_light, 1, ItemClassification.useful)
]

maps_compasses_data = [
    (Items.great_deku_tree_map, 1, ItemClassification.useful),
    (Items.dodongos_cavern_map, 1, ItemClassification.useful),
    (Items.jabujabus_belly_map, 1, ItemClassification.useful),
    (Items.forest_temple_map, 1, ItemClassification.useful),
    (Items.fire_temple_map, 1, ItemClassification.useful),
    (Items.water_temple_map, 1, ItemClassification.useful),
    (Items.spirit_temple_map, 1, ItemClassification.useful),
    (Items.shadow_temple_map, 1, ItemClassification.useful),
    (Items.bottom_of_the_well_map, 1, ItemClassification.useful),
    (Items.ice_cavern_map, 1, ItemClassification.useful),
    (Items.great_deku_tree_compass, 1, ItemClassification.useful),
    (Items.dodongos_cavern_compass, 1, ItemClassification.useful),
    (Items.jabujabus_belly_compass, 1, ItemClassification.useful),
    (Items.forest_temple_compass, 1, ItemClassification.useful),
    (Items.fire_temple_compass, 1, ItemClassification.useful),
    (Items.water_temple_compass, 1, ItemClassification.useful),
    (Items.spirit_temple_compass, 1, ItemClassification.useful),
    (Items.shadow_temple_compass, 1, ItemClassification.useful),
    (Items.bottom_of_the_well_compass, 1, ItemClassification.useful),
    (Items.ice_cavern_compass, 1, ItemClassification.useful)
]

keys_data = [
    (Items.forest_temple_boss_key, 1, ItemClassification.useful),
    (Items.fire_temple_boss_key, 1, ItemClassification.useful),
    (Items.water_temple_boss_key, 1, ItemClassification.useful),
    (Items.spirit_temple_boss_key, 1, ItemClassification.useful),
    (Items.shadow_temple_boss_key, 1, ItemClassification.useful),
    (Items.ganons_castle_boss_key, 1, ItemClassification.useful),
    (Items.forest_temple_small_key, 1, ItemClassification.useful),
    (Items.fire_temple_small_key, 1, ItemClassification.useful),
    (Items.water_temple_small_key, 1, ItemClassification.useful),
    (Items.spirit_temple_small_key, 1, ItemClassification.useful),
    (Items.shadow_temple_small_key, 1, ItemClassification.useful),
    (Items.bottom_of_the_well_small_key, 1, ItemClassification.useful),
    (Items.training_ground_small_key, 1, ItemClassification.useful),
    (Items.gerudo_fortress_small_key, 1, ItemClassification.useful),
    (Items.ganons_castle_small_key, 1, ItemClassification.useful),
    (Items.chest_game_small_key, 1, ItemClassification.useful),
    (Items.guard_house_key, 1, ItemClassification.useful),
    (Items.market_bazaar_key, 1, ItemClassification.useful),
    (Items.market_potion_shop_key, 1, ItemClassification.useful),
    (Items.mask_shop_key, 1, ItemClassification.useful),
    (Items.market_shooting_gallery_key, 1, ItemClassification.useful),
    (Items.bombchu_bowling_alley_key, 1, ItemClassification.useful),
    (Items.treasure_chest_game_building_key, 1, ItemClassification.useful),
    (Items.bombchu_shop_key, 1, ItemClassification.useful),
    (Items.richards_house_key, 1, ItemClassification.useful),
    (Items.alley_house_key, 1, ItemClassification.useful),
    (Items.kakariko_bazaar_key, 1, ItemClassification.useful),
    (Items.kakariko_potion_shop_key, 1, ItemClassification.useful),
    (Items.bosss_house_key, 1, ItemClassification.useful),
    (Items.grannys_potion_shop_key, 1, ItemClassification.useful),
    (Items.skulltula_house_key, 1, ItemClassification.useful),
    (Items.impas_house_key, 1, ItemClassification.useful),
    (Items.windmill_key, 1, ItemClassification.useful),
    (Items.kakariko_shooting_gallery_key, 1, ItemClassification.useful),
    (Items.dampes_hut_key, 1, ItemClassification.useful),
    (Items.talons_house_key, 1, ItemClassification.useful),
    (Items.stables_key, 1, ItemClassification.useful),
    (Items.back_tower_key, 1, ItemClassification.useful),
    (Items.hylia_laboratory_key, 1, ItemClassification.useful),
    (Items.fishing_hole_key, 1, ItemClassification.useful)
]

key_rings_data = [
    (Items.forest_temple_key_ring, 1, ItemClassification.useful),
    (Items.fire_temple_key_ring, 1, ItemClassification.useful),
    (Items.water_temple_key_ring, 1, ItemClassification.useful),
    (Items.spirit_temple_key_ring, 1, ItemClassification.useful),
    (Items.shadow_temple_key_ring, 1, ItemClassification.useful),
    (Items.bottom_of_the_well_key_ring, 1, ItemClassification.useful),
    (Items.training_ground_key_ring, 1, ItemClassification.useful),
    (Items.gerudo_fortress_key_ring, 1, ItemClassification.useful),
    (Items.ganons_castle_key_ring, 1, ItemClassification.useful),
    (Items.chest_game_key_ring, 1, ItemClassification.useful)
]

dungeon_reward_data = [
    (Items.kokiri_emerald, 1, (lambda options: ItemClassification.useful)),
    (Items.goron_ruby, 1, (lambda options: ItemClassification.useful)),
    (Items.zora_sapphire, 1, (lambda options: ItemClassification.useful)),
    (Items.forest_medallion, 1, ItemClassification.useful),
    (Items.fire_medallion, 1, ItemClassification.useful),
    (Items.water_medallion, 1, ItemClassification.useful),
    (Items.spirit_medallion, 1, (lambda options: ItemClassification.useful)),
    (Items.shadow_medallion, 1, (lambda options: ItemClassification.useful)),
    (Items.light_medallion, 1, (lambda options: ItemClassification.useful))
]

filler_data = [
    (Items.recovery_heart, -1, ItemClassification.filler),
    (Items.green_rupee, -1, ItemClassification.filler),
    #(Items.greg_the_green_rupee, -1, ItemClassification.filler),
    (Items.blue_rupee, -1, ItemClassification.filler),
    (Items.red_rupee, -1, ItemClassification.filler),
    (Items.purple_rupee, -1, ItemClassification.filler),
    #(Items.huge_rupee, -1, ItemClassification.filler),
    #(Items.piece_of_heart, -1, ItemClassification.filler),
    #(Items.heart_container, -1, ItemClassification.filler),
    (Items.ice_trap, -1, ItemClassification.filler),
    (Items.milk, -1, ItemClassification.filler),
    (Items.fish, -1, ItemClassification.filler),
    (Items.bombs_5, -1, ItemClassification.filler),
    (Items.bombs_10, -1, ItemClassification.filler),
    (Items.bombs_20, -1, ItemClassification.filler),
    (Items.bombchus_5, -1, ItemClassification.filler),
    (Items.bombchus_10, -1, ItemClassification.filler),
    (Items.bombchus_20, -1, ItemClassification.filler),
    (Items.arrows_5, -1, ItemClassification.filler),
    (Items.arrows_10, -1, ItemClassification.filler),
    (Items.arrows_30, -1, ItemClassification.filler),
    (Items.deku_nuts_5, -1, ItemClassification.filler),
    (Items.deku_nuts_10, -1, ItemClassification.filler),
    (Items.deku_seeds_30, -1, ItemClassification.filler),
    (Items.deku_stick_1, -1, ItemClassification.filler),
    (Items.red_potion_refill, -1, ItemClassification.filler),
    (Items.green_potion_refill, -1, ItemClassification.filler),
    (Items.blue_potion_refill, -1, ItemClassification.filler)
]

boss_soul_data = [
    (Items.gohmas_soul, 1, ItemClassification.progression),
    (Items.king_dodongos_soul, 1, ItemClassification.progression),
    (Items.barinades_soul, 1, ItemClassification.progression),
    (Items.phantom_ganons_soul, 1, ItemClassification.progression),
    (Items.volvagias_soul, 1, ItemClassification.progression),
    (Items.morphas_soul, 1, ItemClassification.progression),
    (Items.bongo_bongos_soul, 1, ItemClassification.progression),
    (Items.twinrovas_soul, 1, ItemClassification.progression),
    (Items.ganons_soul, 1, ItemClassification.progression)
]

other_setting_item_data = [
    (Items.fishing_pole, 1, ItemClassification.useful),
    (Items.ocarina_a_button, 1, ItemClassification.useful),
    (Items.ocarina_c_up_button, 1, ItemClassification.useful),
    (Items.ocarina_c_down_button, 1, ItemClassification.useful),
    (Items.ocarina_c_left_button, 1, ItemClassification.useful),
    (Items.ocarina_c_right_button, 1, ItemClassification.useful),
    (Items.bronze_scale, 1, ItemClassification.useful),
    (Items.bombchu_bag, 1, ItemClassification.useful),
    (Items.infinite_quiver, 1, ItemClassification.useful),
    (Items.infinite_bomb_bag, 1, ItemClassification.useful),
    (Items.infinite_bullet_bag, 1, ItemClassification.useful),
    (Items.infinite_stick_capacity, 1, ItemClassification.useful),
    (Items.infinite_nut_capacity, 1, ItemClassification.useful),
    (Items.infinite_magic_meter, 1, ItemClassification.useful),
    (Items.infinite_bombchus, 1, ItemClassification.useful),
    (Items.infinite_wallet, 1, ItemClassification.useful),
    (Items.skeleton_key, 1, ItemClassification.useful),
    (Items.deku_stick_bag, 1, ItemClassification.useful),
    (Items.deku_nut_bag, 1, ItemClassification.useful),
    (Items.triforce, 1, ItemClassification.useful) 
]

non_useful_item_data = [
    (Items.recovery_heart, 6, ItemClassification.filler),
    (Items.bombs_5, 2, ItemClassification.filler),
    (Items.bombs_10, 2, ItemClassification.filler),
    (Items.arrows_5, 2, ItemClassification.filler),
    (Items.arrows_10, 3, ItemClassification.filler),
    (Items.blue_rupee, 13, ItemClassification.filler),
    (Items.red_rupee, 5, ItemClassification.filler),
    (Items.purple_rupee, 7, ItemClassification.filler),
    (Items.huge_rupee, 3, ItemClassification.filler)
]

special_item_data = [
    (Items.greg_the_green_rupee, 1, ItemClassification.useful),
    (Items.huge_rupee, 1, ItemClassification.useful),
    (Items.piece_of_heart, 35, ItemClassification.useful),
    (Items.heart_container, 8, ItemClassification.useful),
    (Items.piece_of_heart_winner, 1, ItemClassification.useful),
    (Items.green_rupee_loser, 1, ItemClassification.filler)
]

non_filler_data = major_items + trade_items + progressive_item_data + skulltula_data + bottles_data + songs_data \
+ maps_compasses_data + keys_data + key_rings_data + dungeon_reward_data + boss_soul_data + other_setting_item_data + special_item_data + non_useful_item_data
all_items_data = non_filler_data + filler_data