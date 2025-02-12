from enum import Enum
from functools import total_ordering

#An estimate of how far the enemy is from Link in the given location
@total_ordering
class EnemyDistance(Enum):
    CLOSE = 1
    SHORT_JUMPSLASH = 2
    MASTER_SWORD_JUMPSLASH = 3
    LONG_JUMPSLASH = 4
    BOMB_THROW = 5
    BOOMERANG = 6
    HOOKSHOT = 7
    LONGSHOT = 8
    FAR = 9

    def __lt__(self, other):
        if self.__class is other.__class:
            return self.value < other.value
        return NotImplemented
    
#The enemies which are used in logic rules
class Enemies(str, Enum):
    gold_skulltula = "Gold Skulltula"
    gohma_larva = "Gohma Larva"
    mad_scrub = "Mad Scrub"
    deku_baba = "Deku Baba"
    withered_deku_baba = "Withered Deku Baba"
    big_skulltula = "Big Skulltula"
    dodongo = "Dodongo"
    lizalfos = "Lizalfos"
    keese = "Keese"
    fire_keese = "Fire Keese"
    blue_bubble = "Blue Bubble"
    dead_hand = "Dead Hand"
    like_like = "Like-Like"
    floormaster = "Floormaster"
    wallmaster = "Wallmaster"
    stalfos = "Stalfos"
    iron_knuckle = "Iron Knuckle"
    flare_dancer = "Flare Dancer"
    wolfos = "Wolfos"
    white_wolfos = "White Wolfos"
    gerudo_warrior = "Gerudo Warrior"
    gibdo = "Gibdo"
    redead = "Redead"
    meg = "Meg"
    armos = "Armos"
    green_bubble = "Green Bubble"
    dinolfos = "Dinolfos"
    torch_slug = "Torch Slug"
    freezard = "Freezard"
    shell_blade = "Shell Blade"
    spike = "Spike"
    stinger = "Stinger"
    big_octo = "Big Octo"
    ganondorf = "Ganondorf"
    ganon = "Ganon"
    dark_link = "Dark Link"
    anubis = "Anubis"
    purple_leever = "Purple Leever"
    octorok = "Octorok"
    beamos = "Beamos"
    tentacle = "Tentacle"
    bari = "Bari"
    shabom = "Shabom"