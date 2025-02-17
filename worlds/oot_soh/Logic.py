#from .Items import *
#from .Locations import *
from .Options import SoHOptions
from BaseClasses import CollectionState
from typing import List
from .ItemList import Items

from .LogicDataStructures import EnemyDistance, Enemies, WaterLevel

class Logic:
    state: CollectionState
    player: int
    options: SoHOptions
    def can_be_adult(self):
        pass

    def can_be_child(self):
        return True #TODO some settings allow starting as adult to build a logical seed, figure those out

    def can_attack(self, child, adult):
        return self.can_damage(child, adult) or self.can_use(Items.boomerang, child, adult) or self.can_use(Items.progressive_hookshot, child, adult)

    def can_damage(self, child, adult):
        return self.can_use(Items.progressive_slingshot, child, adult) or self.can_jumpslash() or self.has_explosives() or \
        self.can_use(Items.dins_fire, child, adult) or self.can_use(Items.progressive_bow, child, adult)

    def can_jumpslash(self, child, adult):
        return self.can_jumpslash_except_hammer(child, adult) or self.can_use(Items.megaton_hammer, child, adult)
    
    def can_jumpslash_except_hammer(self, child, adult):
        return self.can_use(Items.deku_stick, child, adult) or self.can_use(Items.kokiri_sword, child, adult) or \
            self.can_use(Items.master_sword, child, adult) or self.can_use(Items.biggoron_sword, child, adult)

    def can_reflect_nuts(self, child, adult):
        return self.can_use(Items.deku_shield, child, adult) or (adult and self.has_item(Items.hylian_shield))

    def can_cut_shrubs(self, child, adult):
        return self.can_use(Items.kokiri_sword, child, adult) or self.can_use(Items.boomerang, child, adult) or \
        self.can_use(Items.master_sword, child, adult) or self.can_use(Items.megaton, child, adult) or \
        self.can_use(Items.biggoron, child, adult) or self.has_explosives()
    
    def can_stun_deku(self, child, adult):
        return self.can_attack(child, adult) or self.can_use(Items.deku_nut, child, adult) or self.can_reflect_nuts(child, adult) 

    def can_leave_forest(self, child, adult):
        return ClosedForestOn or adult or DekuTreeClear or ShuffleInteriorEntrances or ShuffleOverworldEntrances
    
    def call_gossip_fairy_except_suns(self, child, adult):
        return self.can_use(Items.zeldas_lullaby, child, adult) or self.can_use(Items.eponas_song, child, adult) or self.can_use(Items.song_of_time, child, adult)

    def call_gossip_fairy(self, child, adult):
        return self.call_gossip_fairy_except_suns(child, adult) or self.can_use(Items.suns_song, child, adult)

    def effective_health(self):
        multiplier = 10
        if DamageMultiplierOn:
            multiplier = DamageMultiplier
        if self.has_item(Items.double_defense):
            if (self.hearts() << 3) % (1 << multiplier) > 0:
                return ((self.hearts() << 3) >> multiplier) + 1
            return (self.hearts() << 3) >> multiplier
        else:
            if (self.hearts() << 2) % (1 << multiplier) > 0:
                return ((self.hearts() << 2) >> multiplier) + 1
            return (self.hearts() << 2) >> multiplier
        
    def hearts(self):
        return HealthCapacity / 16

    def can_take_damage(self, child, adult):
        return self.can_use(Items.bottle_with_fairy) or self.effective_health() > 1 or self.can_use(Items.nayrus_love)

    def can_open_bomb_grotto(self, child, adult):
        return self.blast_or_smash(child, adult) and (self.has_item(Items.stone_of_agony, child, adult) or GrottosWithoutAgony)
    
    def can_open_storms_grotto(self, child, adult):
        return self.can_use(Items.song_of_storms, child, adult) and (self.has_item(Items.stone_of_agony, child, adult) or GrottosWithoutAgony)
    
    def can_get_night_gs(self, child, adult):
        return self.can_use(Items.suns_song, child, adult) or not SkullsSunsSong

    def can_break_upper_beehives(self, child, adult):
        return self.hookshot_or_boomerang(child, adult) or (BombchuBeehives and self.can_use(Items.progressive_bombchus, child, adult))
    
    def can_break_lower_beehives(self, child, adult):
        return self.can_break_upper_beehives(child, adult) or self.can_use(Items.progressive_bombs, child, adult)

    def has_fire_source(self, child, adult):
        return self.can_use(Items.dins_fire, child, adult) or self.can_use(Items.fire_arrows, child, adult)
    
    def has_fire_source_with_torch(self, child, adult):
        return self.has_fire_source(child, adult) or self.can_use(Items.deku_stick, child, adult)

    def can_standing_shield(self, child, adult):
        pass

    def can_spawn_soil_skull(self, child, adult):
        return child and self.can_use(Items.bottle_with_bugs, child, False)

    def blue_fire(self, child, adult):
        return self.can_use(Items.bottle_with_blue_fire, child, adult) or (BlueFireArrows and self.can_use(Items.ice_arrows, child, adult))

    def can_break_mud_walls(self, child, adult):
        return self.has_explosives() or self.can_use(Items.megaton_hammer, child, adult) or (BlueFireMudWallsTrick and self.blue_fire())

    def has_explosives(self):
        return self.can_use(Items.progressive_bombs) or self.can_use(Items.progressive_bombchus)

    #TODO BombchusEnabled, BonchuRefill need options setup
    #Logic.cpp 1006
    def bombchu_enabled(self):
        pass

    #Logic.cpp 1011
    def bombchu_refill(self):
        pass

    def can_detonate_bomb_flowers(self, child, adult):
        return self.can_use(Items.progressive_bow, child, adult) or self.has_explosives() or self.can_use(Items.dins_fire, child, adult)

    def can_detonate_upright_bomb_flower(self, child, adult):
        return self.can_detonate_bomb_flowers(child, adult) or self.has_item(Items.progressive_strength)

    def blast_or_smash(self, child, adult):
        return self.has_explosives() or self.can_use(Items.megaton_hammer, child, adult)
    
    def hookshot_or_boomerang(self, child, adult):
        return self.can_use(Items.boomerang, child, adult) or self.can_use(Items.progressive_hookshot, child, adult)

    def can_get_deku_baba_sticks(self, child, adult):
        return self.can_use(Items.kokiri_sword, child, adult) or self.can_use(Items.master_sword, child, adult) or \
            self.can_use(Items.biggoron_sword, child, adult) or self.can_use(Items.boomerang, child, adult)
    
    def can_get_deku_baba_nuts(self, child, adult):
        return self.can_jumpslash() or self.can_use(Items.progressive_slingshot, child, adult) or self.can_use(Items.progressive_bow, child, adult) \
        or self.has_explosives() or self.can_use(Items.dins_fire, child, adult)
    
    def can_hit_eye_targets(self, child, adult):
        return self.can_use(Items.progressive_bow, child, adult) or self.can_use(Items.progressive_slingshot, child, adult)

    #TODO improve this to consider whether the bottle can be emptied
    def has_bottle(self):
        return self.state.has_any([Items.empty_bottle, Items.bottle_with_milk, Items.bottle_with_red_potion, Items.bottle_with_green_potion,
                                  Items.bottle_with_blue_potion, Items.bottle_with_fairy, Items.bottle_with_fish, Items.bottle_with_blue_fire, 
                                  Items.bottle_with_bugs, Items.bottle_with_poe, Items.bottle_with_rutos_letter, Items.bottle_with_big_poe], self.player)

    def ocarina_button_count(self):
        return self.state.count_from_list([Items.ocarina_a_button, Items.ocarina_c_down_button, Items.ocarina_c_left_button, Items.ocarina_c_right_button, 
                                           Items.ocarina_c_up_button], self.player)

    def scarecrows_song(self):
        return self.ocarina_button_count() >= 2

    def mq_water_level(self, level: WaterLevel):
        match level:
            case WaterLevel.low:
                return (CanWaterTempleHigh and CanWaterTempleLowFromHigh) or (CanWaterTempleLowFromMid and CanWaterTempleLowFromHigh)
            case WaterLevel.low_or_mid:
                return (CanWaterTempleHigh and CanWaterTempleLowFromHigh) or (CanWaterTempleLowFromHigh and CanWaterTEmpleMiddle) or (CanWaterTempleLowFromMid and CanWaterTempleLowFromHigh)
            case WaterLevel.mid:
                return CanWaterTempleLowFromHigh and CanWaterTempleMiddle
            case WaterLevel.high:
                return ReachedWaterHighEmblem
            case WaterLevel.high_or_mid:
                return ReachedWaterHighEmblem or (CanWaterTempleLowFromHigh and CanWaterTempleMiddle)
            
    def can_hit_switch(self, child, adult, distance: EnemyDistance, inWater: bool):
        hit = False
        if distance <= EnemyDistance.SHORT_JUMPSLASH:
            hit = self.can_use(Items.kokiri_sword, child, adult) or self.can_use(Items.megaton_hammer, child, adult)
        if distance <= EnemyDistance.MASTER_SWORD_JUMPSLASH:
            hit = hit or self.can_use(Items.master_sword, child, adult)
        if distance <= EnemyDistance.LONG_JUMPSLASH:
            hit = hit or self.can_use(Items.biggoron_sword, child, adult) or self.can_use(Items.deku_stick, child, adult)
        if distance <= EnemyDistance.BOMB_THROW:
            hit = hit or (not inWater and self.can_use(Items.progressive_bombs, child, adult))
        if distance <= EnemyDistance.BOOMERANG:
            hit = hit or self.can_use(Items.boomerang, child, adult)
        if distance <= EnemyDistance.HOOKSHOT:
            hit = hit or self.can_use(Items.progressive_hookshot, child, adult)
        if distance <= EnemyDistance.LONGSHOT:
            hit = hit or self.can_use(Items.progressive_hookshot, child, adult, 2)
        if distance <= EnemyDistance.FAR:
            hit = hit or self.can_use(Items.progressive_slingshot, child, adult) or self.can_use(Items.progressive_bow, child, adult)

    def can_break_pots(self):
        return True

    def dungeon_count(self):
        count = 0
        if DekuTreeClear:
            count = count + 1
        if DodongosCavernClear:
            count = count + 1
        if JabuJabusBellyClear:
            count = count + 1
        if ForestTempleClear:
            count = count + 1
        if FireTempleClear:
            count = count + 1
        if WaterTempleClear:
            count = count + 1
        if SpiritTempleClear:
            count = count + 1
        if ShadowTempleClear:
            count = count + 1
        return count

    def stone_count(self):
        count = 0
        if self.has_item(Items.kokiri_emerald):
            count = count + 1
        if self.has_item(Items.goron_ruby):
            count = count + 1
        if self.has_item(Items.zora_sapphire):
            count = count + 1
        return count
    
    def medallion_count(self):
        count = 0
        if self.has_item(Items.forest_medallion):
            count = count + 1
        if self.has_item(Items.fire_medallion):
            count = count + 1
        if self.has_item(Items.water_medallion):
            count = count + 1
        if self.has_item(Items.spirit_medallion):
            count = count + 1
        if self.has_item(Items.shadow_medallion):
            count = count + 1
        if self.has_item(Items.light_medallion):
            count = count + 1
        return count
    
    def fire_timer(self, child, adult):
        if self.can_use(Items.goron_tunic, child, adult):
            return 255
        if FewerTunicRequirements:
            return self.hearts() * 8
        return 0
    
    def water_timer(self, child, adult):
        if self.can_use(Items.zora_tunic, child, adult):
            return 255
        if FewerTunicRequirements:
            return self.hearts() * 8
        return 0

    def has_item(self, name: Items, count: int = 1):
        if "Bottle" in name.value: #Can empty or fill bottles
            return self.has_bottle()
        if "Soul" in name.value:
            return self.has_boss_soul(self, name)
        if name in self.state.prog_items[self.player].keys:
            return self.state.count(name, self.player) >= count
        return False

    #can_child and can_adult correlate to whether the particular case can be done in that state. 
    #For instance, a child-only check should have can_child true, can_adult false
    def can_use(self, name: Items, can_child: bool = True, can_adult: bool = True, progressive_stage = 1):
        if not self.has_item(name, self.state, self, progressive_stage):
            return False        
        #Patterns found in multiple rules
        def has_item(name: Items, progressive_stage: int = 1):
            return self.has_item(name, progressive_stage)
        def can_use(name: Items, progressive_stage: int = 1):
            return self.can_use(name, can_child, can_adult, progressive_stage)
        def adult():
            return can_adult and self.can_be_child()
        def child():
            return can_child and self.can_be_adult()
        def ammo_drops():
            return True #TODO ship hasn't set up this setting
        def has_bottle():
            return self.has_bottle()
        def can_play_song(buttons: List[str]):
            return self.has_item(Items.progressive_ocarina) and (not ButtonShuffle or self.state.has_all(buttons, self.player))

        
        #TODO some of these are pascalcase variables, replace them with references to options once options are implemented
        magic = lambda: can_use(Items.progressive_magic_meter)
        magic_arrow = lambda: magic() and can_use(Items.progressive_bow)
        def can_use_strength():
            match(progressive_stage):
                case 1:
                    return True
                case 2:
                    return adult()
                case 3:
                    return adult()
        match name:
            case Items.progressive_magic_meter:
                return ammo_drops() or (has_bottle() and BuyingMagicPotionInLogic)
            case Items.dins_fire: 
                return magic()
            case Items.farores_wind: 
                return magic()
            case Items.nayrus_love: 
                return magic()
            case Items.lens_of_truth: 
                return magic()
            case Items.fire_arrows: 
                return magic_arrow()
            case Items.ice_arrows: 
                return magic_arrow()
            case Items.light_arrows: 
                return magic_arrow()
            case Items.progressive_bow: 
                return adult() and (ammo_drops() or BuyingArrowsInLogic) 
            case Items.megaton_hammer: 
                return adult()
            case Items.iron_boots: 
                return adult()
            case Items.hover_boots: 
                return adult()
            case Items.progressive_hookshot: 
                return adult()
            case Items.goron_tunic: 
                return adult()
            case Items.zora_tunic: 
                return adult()
            case Items.mirror_shield: 
                return adult()
            case Items.master_sword: 
                return adult()
            case Items.biggoron_sword: 
                return adult()
            case Items.pocket_egg: 
                return adult()
            case Items.cojiro: 
                return adult()
            case Items.odd_mushroom: 
                return adult()
            case Items.odd_potion: 
                return adult()
            case Items.poachers__saw: 
                return adult()
            case Items.broken_gorons_sword: 
                return adult()
            case Items.prescription: 
                return adult()
            case Items.eyeball_frog: 
                return adult()
            case Items.worlds_finest_eyedrops: 
                return adult()
            case Items.claim_check: 
                return adult()
            case Items.progressive_strength: 
                return can_use_strength()
            case Items.progressive_slingshot: 
                return child()
            case Items.boomerang:
                return child()
            case Items.kokiri_sword:
                return child()
            case Items.deku_nut:
                return (NutPot or NutCrate or DekuBabaNuts) and ammo_drops() and (not NutBag or has_item(Items.progressive_nut_upgrade))
            case Items.deku_stick:
                return child() and (StickPot or DekuBabaSticks) and (not StickBag or has_item(Items.progressive_stick_upgrade))
            case Items.progressive_bombchus:
                return self.bombchu_refill() and self.bombchus_enabled()
            case Items.weird_egg:
                return child()
            case Items.bottle_with_rutos_letter:
                return child()
            case Items.magic_bean:
                return child()
            case Items.zeldas_lullaby:
                return can_play_song([Items.ocarina_c_left_button, Items.ocarina_c_right_button, Items.ocarina_c_up_button])
            case Items.eponas_song:
                return can_play_song([Items.ocarina_c_left_button, Items.ocarina_c_right_button, Items.ocarina_c_up_button])
            case Items.prelude_of_light:
                return can_play_song([Items.ocarina_c_left_button, Items.ocarina_c_right_button, Items.ocarina_c_up_button])
            case Items.sarias_song:
                return can_play_song([Items.ocarina_c_left_button, Items.ocarina_c_right_button, Items.ocarina_c_down_button])
            case Items.suns_song:
                return can_play_song([Items.ocarina_c_right_button, Items.ocarina_c_up_button, Items.ocarina_c_down_button])
            case Items.song_of_time:
                return can_play_song([Items.ocarina_a_button, Items.ocarina_c_right_button, Items.ocarina_c_down_button])
            case Items.bolero_of_fire:
                return can_play_song([Items.ocarina_a_button, Items.ocarina_c_right_button, Items.ocarina_c_down_button])
            case Items.requiem_of_spirit:
                return can_play_song([Items.ocarina_a_button, Items.ocarina_c_right_button, Items.ocarina_c_down_button])
            case Items.song_of_storms:
                return can_play_song([Items.ocarina_a_button, Items.ocarina_c_up_button, Items.ocarina_c_down_button])
            case Items.minuet_of_forest:
                return can_play_song([Items.ocarina_a_button, Items.ocarina_c_left_button, Items.ocarina_c_right_button, Items.ocarina_c_up_button])
            case Items.serenade_of_water:
                return can_play_song([Items.ocarina_a_button, Items.ocarina_c_left_button, Items.ocarina_c_right_button, Items.ocarina_c_down_button])
            case Items.fishing_pole:
                return has_item(Items.child_wallet)
            case Items.epona: 
                return adult() and can_use(Items.eponas_song)
            case Items.bottle_with_bugs:
                return BugShrub or WanderingBugs or BugRock or BugAccessInLogic
            case Items.bottle_with_fish:
                return LoneFish or FishGroup or FishAccessInLogic
            case Items.bottle_with_blue_fire:
                return BlueFireAccess or BlueFireAccessInLogic
            case Items.bottle_with_fairy:
                return FairyPot or GossipStoneFairy or BeanPlantFairy or ButterflyFairy or FreeFairies or FairyPond or FairyAccessInLogic
            case _:
                return True
    
    def has_projectile_either_age(self):
        return self.has_child_projectile() or self.has_adult_projectile()
    
    def has_child_projectile(self):
        return self.has_explosives() or \
            self.can_use(Items.progressive_slingshot) or self.can_use(Items.boomerang)

    def has_adult_projectile(self):
        return self.has_explosives() or \
            self.can_use(Items.progressive_hookshot) or self.can_use(Items.progressive_bow)
    
    def has_projectiles_all_ages(self):
        return self.has_explosives() or \
            (self.has_child_projectile() and self.has_adult_projectile())


    def has_boss_soul(self, name: str):
        if not ShuffleBossSouls:
            return True
        if name == Items.ganons_soul:
            if ShuffleGanonBossSoul: #In ship it's a set of three options: no shuffle, shuffle boss souls, shuffle boss + ganon souls 
                return self.state.has(Items.ganons_soul, self.player)
            else:
                return True
        return False

    def can_open_overworld_door(self, keyName: str):
        if not LockOverworldDoors:
            return True
        if self.state.has(Items.skeleton_key, self.player):
            return True
        return self.state.has(keyName, self.player)

    #TODO ship is gonna be reworking this section
    def get_glitch_difficulty(glitchName: str):
        pass

    def can_equip_swap_either(name: str, self):
        if not self.has_item(name):
            return False
        return self.can_do_glitch_either("Equip Swap (Din's)") or self.can_do_glitch_either("Equip Swap")
    
    def can_equip_swap_child(self, name: str):
        if not self.has_item(name):
            return False
        return self.can_do_glitch_child("Equip Swap (Din's)") or self.can_do_glitch_child("Equip Swap")
    
    def can_equip_swap_either(self, name: str):
        if not self.has_item(name):
            return False
        return self.can_do_glitch_adult("Equip Swap (Din's)") or self.can_do_glitch_adult("Equip Swap")
    
    def can_do_glitch_either(self, glitch: str):
        def has(name: str):
            return self.has_item(name)
        match glitch: 
            case "Equip Swap (Din's)":
                if not False: #TODO swap to not GlitchEquipSwapDins when ship does
                    return False
                if self.can_be_adult():
                    return has(Items.dins_fire)
                if self.can_be_child():
                    return has(Items.progressive_stick_upgrade) or has(Items.dins_fire)
            case "Equip Swap":
                if not False: #TODO swap to not GlitchEquipSwap when ship does
                    return False
                if self.can_be_adult():
                    return has(Items.dins_fire) or has("Nayru's Love") or has("Farore's Wind")
                if self.can_be_child():
                    return has("Deku Sticks") or has(Items.progressive_slingshot) or has(Items.boomerang) or self.has_bottle() or has("Nayru's Love") or \
                    has(Items.progressive_ocarina) or has("Lens of Truth") or has("Magic Bean") or has("Nuts") or has(Items.dins_fire) or has("Farore's Wind")
            case _:
                return False
            
    def can_do_glitch_child(self, glitch: str):
        def has(name: str):
            return self.has_item(name)
        match glitch: 
            case "Equip Swap (Din's)":
                if not False: #TODO swap to not GlitchEquipSwapDins when ship does
                    return False
                if self.can_be_child():
                    return has(Items.progressive_stick_upgrade) or has(Items.dins_fire)
                return False
            case "Equip Swap":
                if not False: #TODO swap to not GlitchEquipSwap when ship does
                    return False
                if self.can_be_child():
                    return has("Deku Sticks") or has(Items.progressive_slingshot) or has(Items.boomerang) or self.has_bottle() or has("Nayru's Love") or \
                    has(Items.progressive_ocarina) or has("Lens of Truth") or has("Magic Bean") or has("Nuts") or has(Items.dins_fire) or has("Farore's Wind")
                return False
            case _:
                return False
    
    def can_do_glitch_adult(self, glitch: str):
        def has(name: str):
            return self.has_item(name)
        match glitch: 
            case "Equip Swap (Din's)":
                if not False: #TODO swap to not GlitchEquipSwapDins when ship does
                    return False
                if self.can_be_adult():
                    return has(Items.dins_fire)
                return False
            case "Equip Swap":
                if not False: #TODO swap to not GlitchEquipSwap when ship does
                    return False
                if self.can_be_adult():
                    return has(Items.dins_fire) or has("Nayru's Love") or has("Farore's Wind")
                return False
            case _:
                return False

    #Child and adult refer to accessibility at those ages
    def can_kill_enemy(self, enemy: str, child: bool, adult: bool, distance: EnemyDistance = EnemyDistance.CLOSE, onWallOrFloor: bool = True, quantity: int = 1, timer: bool = False, inWater: bool = False):
        def can_use(name: str, amount = 1):
            return self.can_use(name, child, adult, amount)
        killed = False
        match enemy:
            case Enemies.gold_skulltula:
                if distance == EnemyDistance.CLOSE:
                    killed = can_use(Items.megaton_hammer)
                if distance <= EnemyDistance.SHORT_JUMPSLASH:
                    killed = killed or can_use(Items.kokiri_sword)
                if distance <= EnemyDistance.MASTER_SWORD_JUMPSLASH:
                    killed = killed or can_use(Items.master_sword)
                if distance <= EnemyDistance.LONG_JUMPSLASH:
                    killed = killed or can_use(Items.biggoron_sword) or can_use(Items.deku_stick)
                if distance <= EnemyDistance.BOMB_THROW:
                    killed = killed or can_use(Items.progressive_bombs)
                if distance <= EnemyDistance.HOOKSHOT:
                    killed = killed or can_use(Items.progressive_hookshot)
                if distance <= EnemyDistance.LONGSHOT:
                    killed = killed or can_use(Items.progressive_hookshot, 2) or (onWallOrFloor and can_use(Items.progressive_bombchus))
                if distance <= EnemyDistance.FAR:
                    killed = killed or can_use(Items.progressive_slingshot) or can_use(Items.progressive_bow)
                return killed
            case Enemies.gohma_larva:
                return self.can_attack()
            case Enemies.mad_scrub:
                return self.can_attack()
            case Enemies.deku_baba:
                return self.can_attack()
            case Enemies.big_skulltula:
                if distance == EnemyDistance.CLOSE:
                    killed = can_use(Items.megaton_hammer)
                if distance <= EnemyDistance.SHORT_JUMPSLASH:
                    killed = killed or can_use(Items.kokiri_sword)
                if distance <= EnemyDistance.MASTER_SWORD_JUMPSLASH:
                    killed = killed or can_use(Items.master_sword)
                if distance <= EnemyDistance.LONG_JUMPSLASH:
                    killed = killed or can_use(Items.biggoron_sword) or can_use(Items.deku_stick)
                if distance <= EnemyDistance.BOMB_THROW:
                    killed = killed or can_use(Items.progressive_bombs)
                if distance <= EnemyDistance.HOOKSHOT:
                    killed = killed or can_use(Items.progressive_hookshot)
                if distance <= EnemyDistance.LONGSHOT:
                    killed = killed or can_use(Items.progressive_hookshot, 2) or (onWallOrFloor and can_use(Items.progressive_bombchus))
                if distance <= EnemyDistance.FAR:
                    killed = killed or can_use(Items.progressive_slingshot) or can_use(Items.progressive_bow)
                return killed
            case Enemies.dodongo:
                return can_use(Items.kokiri_sword) or can_use(Items.master_sword) or can_use(Items.biggoron_sword) or (quantity <= 5 and can_use(Items.deku_stick)) \
                or self.has_explosives() or can_use(Items.progressive_slingshot) or can_use(Items.progressive_bow)
            case Enemies.lizalfos:
                return self.can_jumpslash() or self.has_explosives() or can_use(Items.progressive_slingshot) or can_use(Items.progressive_bow)
            case Enemies.keese:
                if distance <= EnemyDistance.SHORT_JUMPSLASH:
                    killed = can_use(Items.megaton_hammer) or can_use(Items.kokiri_sword)
                if distance <= EnemyDistance.MASTER_SWORD_JUMPSLASH:
                    killed = killed or can_use(Items.master_sword)
                if distance <= EnemyDistance.LONG_JUMPSLASH:
                    killed = killed or can_use(Items.biggoron_sword) or can_use(Items.deku_stick)
                if distance <= EnemyDistance.BOMB_THROW:
                    killed = killed or (not inWater and can_use(Items.progressive_bombs))
                if distance <= EnemyDistance.BOOMERANG:
                    killed = killed or can_use(Items.boomerang)
                if distance <= EnemyDistance.HOOKSHOT:
                    killed = killed or can_use(Items.progressive_hookshot) or (onWallOrFloor and can_use(Items.progressive_bombchus))
                if distance <= EnemyDistance.LONGSHOT:
                    killed = killed or can_use(Items.progressive_hookshot, 2)
                if distance <= EnemyDistance.FAR:
                    killed = killed or can_use(Items.progressive_slingshot) or can_use(Items.progressive_bow)
                return killed
            case Enemies.fire_keese:
                if distance <= EnemyDistance.SHORT_JUMPSLASH:
                    killed = can_use(Items.megaton_hammer) or can_use(Items.kokiri_sword)
                if distance <= EnemyDistance.MASTER_SWORD_JUMPSLASH:
                    killed = killed or can_use(Items.master_sword)
                if distance <= EnemyDistance.LONG_JUMPSLASH:
                    killed = killed or can_use(Items.biggoron_sword) or can_use(Items.deku_stick)
                if distance <= EnemyDistance.BOMB_THROW:
                    killed = killed or (not inWater and can_use(Items.progressive_bombs))
                if distance <= EnemyDistance.BOOMERANG:
                    killed = killed or can_use(Items.boomerang)
                if distance <= EnemyDistance.HOOKSHOT:
                    killed = killed or can_use(Items.progressive_hookshot) or (onWallOrFloor and can_use(Items.progressive_bombchus))
                if distance <= EnemyDistance.LONGSHOT:
                    killed = killed or can_use(Items.progressive_hookshot, 2)
                if distance <= EnemyDistance.FAR:
                    killed = killed or can_use(Items.progressive_slingshot) or can_use(Items.progressive_bow)
                return killed
            case Enemies.blue_bubble:
                return self.blast_or_smash() or can_use(Items.progressive_bow) or ((self.can_jumpslash_except_hammer() \
                or can_use(Items.progressive_slingshot)) and (can_use(Items.deku_nut) or self.hookshot_or_boomerang(child, adult) or self.can_standing_shield()))
            case Enemies.dead_hand:
                return can_use(Items.kokiri_sword) or can_use(Items.master_sword) or can_use(Items.biggoron_sword) or (can_use(Items.deku_stick) and BotwChildDeadHand)
            case Enemies.withered_deku_baba:
                return can_use(Items.kokiri_sword) or can_use(Items.master_sword) or can_use(Items.biggoron_sword) or can_use(Items.boomerang)
            case Enemies.like_like:
                return self.can_damage()
            case Enemies.floormaster:
                return self.can_damage()
            case Enemies.stalfos:
                if distance <= EnemyDistance.SHORT_JUMPSLASH:
                    killed = can_use(Items.megaton_hammer) or can_use(Items.kokiri_sword)
                if distance <= EnemyDistance.MASTER_SWORD_JUMPSLASH:
                    killed = killed or can_use(Items.master_sword)
                if distance <= EnemyDistance.LONG_JUMPSLASH:
                    killed = killed or can_use(Items.biggoron_sword) or can_use(Items.deku_stick)
                if distance <= EnemyDistance.BOMB_THROW:
                    killed = killed or (quantity <= 2 and not timer and not inWater and (can_use(Items.deku_nut) or self.hookshot_or_boomerang(child, adult)) and can_use(Items.progressive_bombs))
                if distance <= EnemyDistance.BOOMERANG:
                    killed = killed or can_use(Items.boomerang)
                if distance <= EnemyDistance.HOOKSHOT:
                    killed = killed or can_use(Items.progressive_hookshot) or (onWallOrFloor and can_use(Items.progressive_bombchus))
                if distance <= EnemyDistance.LONGSHOT:
                    killed = killed or can_use(Items.progressive_hookshot, 2)
                if distance <= EnemyDistance.FAR:
                    killed = killed or can_use(Items.progressive_slingshot) or can_use(Items.progressive_bow)
                return killed
            case Enemies.iron_knuckle:
                return can_use(Items.kokiri_sword) or can_use(Items.master_sword) or can_use(Items.biggoron_sword) or can_use(Items.megaton_hammer) or self.has_explosives()
            case Enemies.flare_dancer:
                return can_use(Items.megaton_hammer) or can_use(Items.progressive_hookshot) or (self.has_explosives() and \
                (self.can_jumpslash_except_hammer() or can_use(Items.progressive_bow) or can_use(Items.progressive_slingshot) or can_use(Items.boomerang)))
            case Enemies.wolfos:
                return self.can_jumpslash() or can_use(Items.progressive_bow) or can_use(Items.progressive_slingshot) or can_use(Items.progressive_bombchus) or \
                can_use(Items.dins_fire) or (can_use(Items.progressive_bombs) and (can_use(Items.deku_nut) or can_use(Items.progressive_hookshot) or can_use(Items.boomerang)))
            case Enemies.white_wolfos:
                return self.can_jumpslash() or can_use(Items.progressive_bow) or can_use(Items.progressive_slingshot) or can_use(Items.progressive_bombchus) or \
                can_use(Items.dins_fire) or (can_use(Items.progressive_bombs) and (can_use(Items.deku_nut) or can_use(Items.progressive_hookshot) or can_use(Items.boomerang)))
            case Enemies.wallmaster:
                return self.can_jumpslash() or can_use(Items.progressive_bow) or can_use(Items.progressive_slingshot) or can_use(Items.progressive_bombchus) or \
                can_use(Items.dins_fire) or (can_use(Items.progressive_bombs) and (can_use(Items.deku_nut) or can_use(Items.progressive_hookshot) or can_use(Items.boomerang)))
            case Enemies.gerudo_warrior:
                return self.can_jumpslash() or can_use(Items.progressive_bow) or (GFWarriorWithDifficultWeapon and (can_use(Items.progressive_slingshot) or can_use(Items.progressive_bombchus)))
            case Enemies.gibdo:
                return self.can_jumpslash() or can_use(Items.dins_fire)
            case Enemies.redead:
                return self.can_jumpslash() or can_use(Items.dins_fire)
            case Enemies.meg: #TODO the fourth poe in forest temple
                return can_use(Items.progressive_bow) or can_use(Items.progressive_hookshot) or self.has_explosives()
            case Enemies.armos:
                return self.blast_or_smash() or can_use(Items.master_sword) or can_use(Items.biggoron_sword) or can_use(Items.deku_stick) or can_use(Items.progressive_bow) \
                or ((can_use(Items.deku_nut) or can_use(Items.progressive_hookshot) or can_use(Items.boomerang)) and (can_use(Items.kokiri_sword)) or can_use(Items.progressive_slingshot))
            case Enemies.green_bubble:
                return self.can_jumpslash() or can_use(Items.progressive_bow) or can_use(Items.progressive_slingshot) or self.has_explosives()
            case Enemies.dinolfos:
                return self.can_jumpslash() or can_use(Items.progressive_bow) or can_use(Items.progressive_slingshot) or (not Timer and can_use(Items.progressive_bombchus))
            case Enemies.torch_slug:
                return self.can_jumpslash() or self.has_explosives() or can_use(Items.progressive_bow)
            case Enemies.freezard:
                return can_use(Items.master_sword) or can_use(Items.biggoron_sword) or can_use(Items.megaton_hammer) or can_use(Items.deku_stick) \
                or self.has_explosives() or can_use(Items.progressive_hookshot) or can_use(Items.dins_fire) or can_use(Items.fire_arrows)
            case Enemies.shell_blade:
                return can_use(Items.kokiri_sword) or can_use(Items.master_sword) or can_use(Items.biggoron_sword) or can_use(Items.megaton_hammer) or \
                can_use(Items.deku_stick) or self.has_explosives() or can_use(Items.progressive_hookshot) or can_use(Items.progressive_bow) or \
                can_use(Items.dins_fire) 
            case Enemies.spike:
                return can_use(Items.master_sword) or can_use(Items.biggoron_sword) or can_use(Items.megaton_hammer) or can_use(Items.deku_stick) \
                or self.has_explosives() or can_use(Items.progressive_hookshot) or can_use(Items.dins_fire) or can_use(Items.progressive_bow)
            case Enemies.stinger:
                if distance <= EnemyDistance.SHORT_JUMPSLASH:
                    killed = can_use(Items.megaton_hammer) or can_use(Items.kokiri_sword)
                if distance <= EnemyDistance.MASTER_SWORD_JUMPSLASH:
                    killed = killed or can_use(Items.master_sword)
                if distance <= EnemyDistance.LONG_JUMPSLASH:
                    killed = killed or can_use(Items.biggoron_sword) or can_use(Items.deku_stick)
                if distance <= EnemyDistance.BOMB_THROW:
                    killed = killed or (not inWater and can_use(Items.progressive_bombs))
                if distance <= EnemyDistance.HOOKSHOT:
                    killed = killed or can_use(Items.progressive_hookshot) or (onWallOrFloor and can_use(Items.progressive_bombchus))
                if distance <= EnemyDistance.LONG_JUMPSLASH:
                    killed = killed or can_use(Items.progressive_hookshot, 2)
                if distance <= EnemyDistance.FAR:
                    killed = killed or can_use(Items.progressive_slingshot) or can_use(Items.progressive_bow)
                return killed
            case Enemies.big_octo:
                return can_use(Items.kokiri_sword) or can_use(Items.deku_stick) or can_use(Items.master_sword)
            case Enemies.ganondorf:
                return self.has_boss_soul(Items.ganons_soul) and can_use(Items.light_arrows) and (can_use(Items.kokiri_sword) \
                or can_use(Items.master_sword) or can_use(Items.biggoron_sword))
            case Enemies.ganon:
                return self.has_boss_soul(Items.ganons_soul) and can_use(Items.master_sword)
            case Enemies.dark_link:
                return self.can_jumpslash() and can_use(Items.progressive_bow)
            case Enemies.anubis:
                return self.has_fire_source()
            case Enemies.beamos:
                return self.has_explosives()
            case Enemies.purple_leever:
                return can_use(Items.master_sword) or can_use(Items.biggoron_sword)
            case Enemies.tentacle:
                return can_use(Items.boomerang)
            case Enemies.bari:
                return self.hookshot_or_boomerang(child, adult) or can_use(Items.progressive_bow) or self.has_explosives() \
                    or can_use(Items.megaton_hammer) or can_use(Items.deku_stick) or can_use(Items.dins_fire) or (self.can_take_damage() \
                    and (can_use(Items.kokiri_sword) or can_use(Items.master_sword) or can_use(Items.biggoron_sword)))
            case Enemies.shabom:
                return can_use(Items.boomerang) or can_use(Items.deku_nut) or self.can_jumpslash() or can_use(Items.dins_fire) or can_use(Items.ice_arrows)
            case Enemies.octorok:
                return self.can_reflect_nuts() or self.hookshot_or_boomerang(child, adult) or \
                can_use(Items.progressive_bow) or can_use(Items.progressive_slingshot) or can_use(Items.progressive_bombs) or \
                (onWallOrFloor and can_use(Items.progressive_bombchus))
            case _:
                return False
    
    def can_pass_enemy(self, enemy: str, distance: EnemyDistance = EnemyDistance.CLOSE, onWallOrFloor: bool = True, child: bool = True, adult: bool = True):
        if self.can_kill_enemy(enemy, child, adult, distance, onWallOrFloor):
            return True
        def can_use(name: str, amount = 1):
            return self.can_use(name, child, adult, amount)
        match enemy:
            case Enemies.gold_skulltula: 
                return True
            case Enemies.gohma_larva: 
                return True
            case Enemies.lizalfos: 
                return True
            case Enemies.dodongo: 
                return True
            case Enemies.mad_scrub: 
                return True
            case Enemies.keese: 
                return True
            case Enemies.fire_keese: 
                return True
            case Enemies.blue_bubble: 
                return True
            case Enemies.dead_hand: 
                return True
            case Enemies.deku_baba: 
                return True
            case Enemies.withered_deku_baba: 
                return True
            case Enemies.stalfos: 
                return True
            case Enemies.flare_dancer: 
                return True
            case Enemies.wolfos: 
                return True
            case Enemies.white_wolfos: 
                return True
            case Enemies.floormaster: 
                return True
            case Enemies.meg: 
                return True
            case Enemies.armos: 
                return True
            case Enemies.freezard: 
                return True
            case Enemies.spike: 
                return True
            case Enemies.dark_link: 
                return True
            case Enemies.anubis: 
                return True
            case Enemies.wallmaster: 
                return True
            case Enemies.purple_leever: 
                return True
            case Enemies.octorok: 
                return True
            case Enemies.big_skulltula:
                return can_use(Items.deku_nut) or can_use(Items.boomerang)
            case Enemies.like_like:
                return can_use(Items.progressive_hookshot) or can_use(Items.boomerang)
            case Enemies.gibdo:
                return can_use(Items.progressive_hookshot) or can_use(Items.suns_song)
            case Enemies.redead: 
                return can_use(Items.progressive_hookshot) or can_use(Items.suns_song)
            case Enemies.iron_knuckle:
                return False
            case Enemies.big_octo:
                return False
            case Enemies.green_bubble:
                return self.can_take_damage() or can_use(Items.deku_nut) or can_use(Items.boomerang) or can_use(Items.progressive_hookshot)
            case _:
                return False

    def can_avoid_enemy(self, enemy: str, child: bool, adult: bool, grounded: bool = False, quantity: int = 1):
        if self.can_kill_enemy(enemy, child, adult, EnemyDistance.CLOSE, True, quantity):
            return True
        def can_use(name: str, stage: int):
            return self.can_use(name, child, adult, stage)
        match enemy:
            case Enemies.gold_skulltula: 
                return True
            case Enemies.gohma_larva: 
                return True
            case Enemies.lizalfos: 
                return True
            case Enemies.dodongo: 
                return True
            case Enemies.big_skulltula:
                return True
            case Enemies.dead_hand: 
                return True
            case Enemies.deku_baba: 
                return True
            case Enemies.withered_deku_baba: 
                return True
            case Enemies.like_like:
                return True
            case Enemies.stalfos: 
                return True
            case Enemies.iron_knuckle:
                return True
            case Enemies.flare_dancer: 
                return True
            case Enemies.wolfos: 
                return True
            case Enemies.white_wolfos: 
                return True
            case Enemies.floormaster: 
                return True
            case Enemies.redead:
                return True
            case Enemies.meg: 
                return True
            case Enemies.armos: 
                return True
            case Enemies.green_bubble:
                return True
            case Enemies.freezard: 
                return True
            case Enemies.shell_blade:
                return True
            case Enemies.spike: 
                return True
            case Enemies.big_octo:
                return True
            case Enemies.gibdo:
                return True
            case Enemies.dark_link: 
                return True
            case Enemies.wallmaster: 
                return True
            case Enemies.anubis: 
                return True
            case Enemies.purple_leever: 
                return True
            case Enemies.beamos:
                return not grounded or can_use(Items.deku_nut) or (quantity == 1 and (can_use(Items.progressive_bow) or can_use(Items.progressive_slingshot)))
            case Enemies.mad_scrub:
                return not grounded or can_use(Items.deku_nut)
            case Enemies.keese:
                return can_use(Items.deku_nut)
            case Enemies.fire_keese:
                return can_use(Items.deku_nut)
            case Enemies.blue_bubble:
                return not grounded or can_use(Items.deku_nut) or self.hookshot_or_boomerang(child, adult) or self.can_standing_shield()


    def can_get_enemy_drop(self, enemy: str, child: bool, adult: bool, distance: EnemyDistance = EnemyDistance.CLOSE, aboveLink: bool = False):
        if not self.can_kill_enemy(enemy, child, adult, distance):
            return False
        if distance <= EnemyDistance.MASTER_SWORD_JUMPSLASH:
            return True
        def can_use(name: str, stage: int):
            return self.can_use(name, child, adult, stage)
        drop: bool = False
        match enemy:
            case Enemies.gold_skulltula:
                if distance <= EnemyDistance.BOOMERANG:
                    drop = drop or can_use(Items.boomerang)
                if distance <= EnemyDistance.HOOKSHOT:
                    drop = drop or can_use(Items.progressive_hookshot)
                if distance <= EnemyDistance.LONGSHOT:
                    drop = drop or can_use(Items.progressive_hookshot, 2)
                return drop
            case Enemies.keese:
                return True
            case Enemies.fire_keese:
                return True
            case _:
                return aboveLink or (distance <= EnemyDistance.BOOMERANG and can_use(Items.boomerang))