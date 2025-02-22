from enum import Enum

class TrickTag(Enum):
    NOVICE = 0
    INTERMEDIATE = 1
    ADVANCED = 2
    EXPERT = 3
    EXTREME = 4
    EXPERIMENTAL = 5
    GLITCH = 6

logic_tricks = {
    "Pass Through Visible One-Way Collision": {
        'tag': TrickTag.NOVICE, 
        'description': "Allows climbing through the platform to reach Impa's House Back as adult with no items and going through the Kakariko Village Gate as child when coming from the Mountain Trail side."
    }, 
    "Hidden Grottos without Stone of Agony": {
        'tag': TrickTag.NOVICE, 
        'description': "Allows entering hidden grottos without the Stone of Agony."
    }, 
    "Fewer Tunic Requirements": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "Allows the following possible without Tunics:\n- Enter Water Temple. The area below the center pillar still requires Zora Tunic. Applies to MQ also.\n- Enter Fire Temple. Volvagia still requires Goron tunic. Applies to MQ also, and includes child access to first floor with dungeon shuffle."
    }, 
    "Hammer Rusted Switches Through Walls": {
        'tag': TrickTag.NOVICE, 
        'description': "Applies to:\n- Fire Temple Highest Goron Chest.\n- MQ Fire Temple Lizalfos Maze.\n- MQ Spirit Trial."
    }, 
    "Flaming Chests": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "The chests encircled in flames in Gerudo Training Ground and in Spirit Temple can be opened by running into the flames while Link is invincible after taking damage."}, 
    "Bombchu Beehives": {
        'tag': TrickTag.NOVICE, 
        'description': "Allows exploding beehives with bombchus."
    }, 
    "Break Mud Walls with Blue Fire": {
        'tag': TrickTag.NOVICE, 
        'description': "Use Blue Fire to break mud walls."
    }, 
    "Adult Kokiri Forest GS with Hover Boots": {
        'tag': TrickTag.NOVICE, 
        'description': "Can be obtained without Hookshot by using the Hover Boots off of one of the roots."
    }, 
    "Jump onto the Lost Woods Bridge as Adult with Nothing": {
        'tag': TrickTag.EXPERT, 'description': "With very precise movement it's possible for adult to jump onto the bridge without needing Longshot, Hover Boots, or Bean."}, 
    "Backflip over Mido as Adult": {
        'tag': TrickTag.NOVICE, 
        'description': "With a specific position and angle, you can backflip over Mido."
    }, 
    "Lost Woods Adult GS without Bean": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "You can collect the token with a precise Hookshot use, as long as you can kill the Skulltula somehow first. It can be killed using Longshot, Bow, Bombchus or Din's Fire."
    }, 
    "Hyrule Castle Storms Grotto GS with Just Boomerang": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "With precise throws, the Boomerang alone can kill the Skulltula and collect the token, without first needing to blow up the wall."
    }, 
    "Man on Roof without Hookshot": {
        'tag': TrickTag.NOVICE, 
        'description': "Can be reached by side-hopping off the watchtower as either age, or by jumping onto the potion shop's roof from the ledge as adult."
    }, 
    "Kakariko Tower GS with Jump Slash": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "Climb the tower as high as you can without touching the Gold Skulltula, then let go and jump slash immediately. By jump-slashing from as low on the ladder as possible to still hit the Skulltula, this trick can be done without taking fall damage."
    }, 
    "Windmill PoH as Adult with Nothing": {
        'tag': TrickTag.NOVICE, 
        'description': "Can jump up to the spinning platform from below as adult."
    }, 
    "Windmill PoH as Child with Precise Jump Slash": {
        'tag': TrickTag.EXTREME, 
        'description': "Can jump up to the spinning platform from below as child with a precise jumpslash timed with the platforms rotation."
    }, 
    "Kakariko Rooftop GS with Hover Boots": {
        'tag': TrickTag.ADVANCED, 
        'description': "Take the Hover Boots from the entrance to Impa's House over to the rooftop of Skulltula House. From there, a precise Hover Boots backwalk with backflip can be used to get onto a hill above the side of the village. And then from there you can Hover onto Impa's rooftop to kill the Skulltula and backflip into the token."
    }, 
    "Graveyard Freestanding PoH with Boomerang": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "Using a precise moving setup you can obtain the Piece of Heart by having the Boomerang interact with it along the return path."
    }, 
    "Second Dampe Race as Child": {
        'tag': TrickTag.NOVICE, 
        'description': "It is possible to complete the second dampe race as child in under a minute, but it is a strict time limit."
    }, 
    "Shadow Temple Entry with Fire Arrows": {
        'tag': TrickTag.EXPERT, 
        'description': "It is possible to light all of the torches to open the Shadow Temple entrance with just Fire Arrows, but you must be very quick, precise, and strategic with how you take your shots."
    }, 
    "Death Mountain Trail Soil GS without Destroying Boulder": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "Bugs will go into the soft soil even while the boulder is still blocking the entrance. Then, using a precise moving setup you can kill the Gold Skulltula and obtain the token by having the Boomerang interact with it along the return path."
    }, 
    "Death Mountain Trail Chest with Strength": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "Child Link can blow up the wall using a nearby bomb flower. You must backwalk with the flower and then quickly throw it toward the wall."
    }, 
    "Death Mountain Trail Lower Red Rock GS with Hookshot": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "After killing the Skulltula, the token can be fished out of the rock without needing to destroy it, by using the Hookshot in the correct way."
    }, 
    "Death Mountain Trail Lower Red Rock GS with Hover Boots": {
        'tag': TrickTag.ADVANCED, 
        'description': "After killing the Skulltula, the token can be collected without needing to destroy the rock by backflipping down onto it with the Hover Boots. First use the Hover Boots to stand on a nearby fence, and go for the Skulltula Token from there."
    }, 
    "Death Mountain Trail Lower Red Rock GS with Magic Bean": {
        'tag': TrickTag.EXPERT, 
        'description': "After killing the Skulltula, the token can be collected without needing to destroy the rock by jumping down onto it from the bean plant, midflight, with precise timing and positioning."
    }, 
    "Death Mountain Trail Lower Red Rock GS with Jump Slash": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "After killing the Skulltula, the token can be collected without needing to destroy the rock by jump slashing from a precise angle."
    }, 
    "Death Mountain Trail Climb with Hover Boots": {
        'tag': TrickTag.ADVANCED, 
        'description': "It is possible to use the Hover Boots to bypass needing to destroy the boulders blocking the path to the top of Death Mountain."
    }, 
    "Death Mountain Trail Upper Red Rock GS without Hammer": {
        'tag': TrickTag.NOVICE, 
        'description': "After killing the Skulltula, the token can be collected by backflipping into the rock at the correct angle."
    }, 
    "Goron City Spinning Pot PoH with Bombchu": {
        'tag': TrickTag.ADVANCED, 
        'description': "A Bombchu can be used to stop the spinning pot, but it can be quite finicky to get it to work."
    }, 
    "Goron City Spinning Pot PoH with Strength": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "Allows for stopping the Goron City Spinning Pot using a bomb flower alone, requiring strength in lieu of inventory explosives."
    }, 
    "Rolling Goron (Hot Rodder Goron) as Child with Strength": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "Use the bombflower on the stairs or near Medigoron. Timing is tight, especially without backwalking."
    }, 
    "Goron City Maze Left Chest with Hover Boots": {
        'tag': TrickTag.ADVANCED, 
        'description': "A precise backwalk starting from on top of the crate and ending with a precisely-timed backflip can reach this chest without needing either the Hammer or Silver Gauntlets."
    }, 
    "Goron City Grotto with Hookshot While Taking Damage": {
        'tag': TrickTag.ADVANCED, 
        'description': "It is possible to reach the Goron City Grotto by quickly using the Hookshot while in the midst of taking damage from the lava floor."
    }, 
    "Stop Link the Goron with Din's Fire": {
        'tag': TrickTag.NOVICE, 
        'description': "The timing is quite awkward."
    }, 
    "Crater's Bean PoH with Hover Boots": {
        'tag': TrickTag.NOVICE, 
        'description': "Hover from the base of the bridge near Goron City and walk up the very steep slope."
    }, 
    "Death Mountain Crater Jump to Bolero": {
        'tag': TrickTag.EXTREME, 
        'description': "As Adult, using a shield to drop a pot while you have the perfect speed and position, the pot can push you that little extra distance you need to jump across the gap in the bridge."
    }, 
    "Death Mountain Crater Upper to Lower with Hammer": {
        'tag': TrickTag.NOVICE, 
        'description': "With the Hammer, you can jump slash the rock twice in the same jump in order to destroy it before you fall into the lava."
    }, 
    "Death Mountain Crater Upper to Lower Boulder Skip": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "As adult, With careful positioning, you can jump to the ledge where the boulder is, then use repeated ledge grabs to shimmy to a climbable ledge. This trick supersedes \"Death Mountain Crater Upper to Lower with Hammer\"."
    }, 
    "Zora's River Lower Freestanding PoH as Adult with Nothing": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "Adult can reach this PoH with a precise jump, no Hover Boots required."
    }, 
    "Zora's River Upper Freestanding PoH as Adult with Nothing": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "Adult can reach this PoH with a precise jump, no Hover Boots required."
    }, 
    "Zora's Domain Entry with Hover Boots": {
        'tag': TrickTag.NOVICE, 
        'description': "Can hover behind the waterfall as adult."
    }, 
    "Zora's Domain Entry with Cucco": {
        'tag': TrickTag.NOVICE, 
        'description': "You can fly behind the waterfall with a Cucco as child."
    }, 
    "Skip King Zora as Adult with Nothing": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "With a precise jump as adult, it is possible to get on the fence next to King Zora from the front to access Zora's Fountain."
    }, 
    "Zora's Domain GS with No Additional Items": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "A precise jump slash can kill the Skulltula and recoil back onto the top of the frozen waterfall. To kill it, the logic normally guarantees one of Hookshot, Bow, or Magic."
    }, 
    "Zora's Fountain Great Fairy Without Explosives": {
        'tag': TrickTag.NOVICE, 
        'description': "It's possible to use silver gauntlets to pick up the silver rock and hammer to break the rock below it, allowing you to ledge grab the edge of the hole and get past the breakable wall (hammer can't break the wall itself)."
    }, 
    "Lake Hylia Lab Wall GS with Jump Slash": {
        'tag': TrickTag.NOVICE, 
        'description': "The jump slash to actually collect the token is somewhat precise."
    }, 
    "Lake Hylia Lab Dive without Gold Scale": {
        'tag': TrickTag.NOVICE, 
        'description': "Remove the Iron Boots in the midst of Hookshotting the underwater crate."
    }, 
    "Water Temple Entry without Iron Boots using Hookshot": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "When entering Water Temple using Gold Scale instead of Iron Boots, the Longshot is usually used to be able to hit the switch and open the gate. But, by standing in a particular spot, the switch can be hit with only the reach of the Hookshot."
    }, 
    "Gerudo Valley Crate PoH as Adult with Hover Boots": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "From the far side of Gerudo Valley, a precise Hover Boots movement and jump-slash recoil can allow adult to reach the ledge with the crate PoH without needing Longshot. You will take fall damage."
    }, 
    "Thieves' Hideout \"Kitchen\" with No Additional Items": {
        'tag': TrickTag.NOVICE, 
        'description': "Allows passing through the kitchen by avoiding being seen by the guards. The logic normally guarantees Bow or Hookshot to stun them from a distance, or Hover Boots to cross the room without needing to deal with the guards."
    }, 
    "Gerudo's Fortress Ledge Jumps": {
        'tag': TrickTag.NOVICE, 
        'description': "Adult can jump onto the top roof of the fortress without going through the interior of the hideout."
    }, 
    "Gerudo's Fortress Warriors with Difficult Weapons": {
        'tag': TrickTag.NOVICE, 
        'description': "Warriors can be defeated with slingshot or bombchus."
    }, 
    "Wasteland Crossing without Hover Boots or Longshot": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "You can beat the quicksand by backwalking across it in a specific way. Note that jumping to the carpet merchant as child typically requires a fairly precise jump slash."
    }, 
    "Lensless Wasteland": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "By memorizing the path, you can travel through the Wasteland without using the Lens of Truth to see the Poe. The equivalent trick for going in reverse through the Wasteland is \"Reverse Wasteland\"."
    }, 
    "Reverse Wasteland": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "By memorizing the path, you can travel through the Wasteland in reverse. Note that jumping to the carpet merchant as child typically requires a fairly precise jump slash. The equivalent trick for going forward through the Wasteland is \"Lensless Wasteland\". To cross the river of sand with no additional items, be sure to also enable \"Wasteland Crossing without Hover Boots or Longshot\". Unless all overworld entrances are randomized, child Link will not be expected to do anything at Gerudo's Fortress."
    }, 
    "Colossus Hill GS with Hookshot": {
        'tag': TrickTag.NOVICE, 
        'description': "Somewhat precise. If you kill enough Leevers you can get enough of a break to take some time to aim more carefully."
    }, 
    "Deku Tree Basement Vines GS with Jump Slash": {
        'tag': TrickTag.NOVICE, 
        'description': "Can be defeated by doing a precise jump slash."
    }, 
    "Deku Tree Basement without Slingshot": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "A precise jump can be used to skip needing to use the Slingshot to go around B1 of the Deku Tree. If used with the \"Closed Forest\" setting, a Slingshot will not be guaranteed to exist somewhere inside the Forest. This trick applies to both Vanilla and Master Quest."
    }, 
    "Deku Tree Basement Web to Gohma with Bow": {
        'tag': TrickTag.NOVICE, 
        'description': "All spider web walls in the Deku Tree basement can be burnt as adult with just a bow by shooting through torches. This trick only applies to the circular web leading to Gohma; the two vertical webs are always in logic. Backflip onto the chest near the torch at the bottom of the vine wall. With precise positioning you can shoot through the torch to the right edge of the circular web. This allows completion of adult Deku Tree with no fire source."
    }, 
    "Deku Tree Basement Backflip over Spiked Log": {
        'tag': TrickTag.NOVICE, 
        'description': "Allows backflipping over the spiked log in the Deku Tree basement in vanilla. Only relevant if \"Shuffle Swim\" is enabled."
    }, 
    "Deku Tree MQ Compass Room GS Boulders with Just Hammer": {
        'tag': TrickTag.NOVICE, 
        'description': "Climb to the top of the vines, then let go and jump slash immediately to destroy the boulders using the Hammer, without needing to spawn a Song of Time block."
    }, 
    "Deku Tree MQ Roll Under the Spiked Log": {
        'tag': TrickTag.NOVICE, 
        'description': "You can get past the spiked log by rolling to briefly shrink your hitbox. As adult, the timing is a bit more precise."
    }, 
    "Dodongo's Cavern Scarecrow GS with Armos Statue": {
        'tag': TrickTag.NOVICE, 
        'description': "You can jump off an Armos Statue to reach the alcove with the Gold Skulltula. It takes quite a long time to pull the statue the entire way. The jump to the alcove can be a bit picky when done as child."
    }, 
    "Dodongo's Cavern Vines GS from Below with Longshot": {
        'tag': TrickTag.NOVICE, 
        'description': "The vines upon which this Skulltula rests are one-sided collision. You can use the Longshot to get it from below, by shooting it through the vines, bypassing the need to lower the staircase."
    }, 
    "Dodongo's Cavern Staircase with Bow": {
        'tag': TrickTag.NOVICE, 
        'description': "The Bow can be used to knock down the stairs with two well-timed shots."
    }, 
    "Dodongo's Cavern Child Slingshot Skips": {
        'tag': TrickTag.EXPERT, 
        'description': "With precise platforming, child can cross the platforms while the flame circles are there. When enabling this trick, it's recommended that you also enable the Adult variant: \"Dodongo's Cavern Spike Trap Room Jump without Hover Boots\"."
    }, 
    "Dodongo's Cavern Two Scrub Room with Strength": {
        'tag': TrickTag.NOVICE, 
        'description': "With help from a conveniently-positioned block, Adult can quickly carry a bomb flower over to destroy the mud wall blocking the room with two Deku Scrubs."
    }, 
    "Dodongo's Cavern Spike Trap Room Jump without Hover Boots": {
        'tag': TrickTag.NOVICE, 
        'description': "The jump is adult Link only. Applies to both Vanilla and MQ."
    }, 
    "Dodongo's Cavern Smash the Boss Lobby Floor": {
        'tag': TrickTag.NOVICE, 
        'description': "The bombable floor before King Dodongo can be destroyed with Hammer if hit in the very center. This is only relevant with Shuffle Boss Entrances or if Dodongo's Cavern is MQ and either variant of \"Dodongo's Cavern MQ Light the Eyes with Strength\" is on."
    }, 
    "Dodongo's Cavern MQ Early Bomb Bag Area as Child": {
        'tag': TrickTag.ADVANCED, 
        'description': "With a precise jump slash from above, you can reach the Bomb Bag area as only child without needing a Slingshot. You will take fall damage."
    }, 
    "Dodongo's Cavern MQ Light the Eyes with Strength as Child": {
        'tag': TrickTag.EXPERT, 
        'description': "If you move very quickly, it is possible to use the bomb flower at the top of the room to light the eyes. To perform this trick as child is significantly more difficult than adult. The player is also expected to complete the DC back area without explosives, including getting past the Armos wall to the switch for the boss door."
    }, 
    "Dodongo's Cavern MQ Light the Eyes with Strength as Adult": {
        'tag': TrickTag.ADVANCED, 
        'description': "If you move very quickly, it is possible to use the bomb flower at the top of the room to light the eyes."
    }, 
    "Jabu Underwater Alcove as Adult with Jump Dive": {
        'tag': TrickTag.NOVICE, 
        'description': "Standing above the underwater tunnel leading to the scrub, jump down and swim through the tunnel. This allows adult to access the alcove with no Scale or Iron Boots. In vanilla Jabu, this alcove has a business scrub. In MQ Jabu, it has the compass chest and a door switch for the main floor."
    }, 
    "Jabu Near Boss Room with Hover Boots": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "A box for the blue switch can be carried over by backwalking with one while the elevator is at its peak. Alternatively, you can skip transporting a box by quickly rolling from the switch and opening the door before it closes. However, the timing for this is very tight."
    }, 
    "Jabu Near Boss Ceiling Switch/GS without Boomerang or Explosives": {
        'tag': TrickTag.NOVICE, 
        'description': "Vanilla Jabu: From near the entrance into the room, you can hit the switch that opens the door to the boss room using a precisely-aimed use of the Slingshot, Bow, or Longshot. As well, if you climb to the top of the vines you can stand on the right edge of the platform and shoot around the glass. From this distance, even the Hookshot can reach the switch. This trick is only relevant if \"Shuffle Boss Entrances\" is enabled. MQ Jabu: A Gold Skulltula Token can be collected with the Hookshot or Longshot using the same methods as hitting the switch in vanilla. This MQ trick is not currently relevant in logic."
    }, 
    "Jabu Near Boss Ceiling Switch with Explosives": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "You can hit the switch that opens the door to the boss room using a precisely-aimed Bombchu. Also, using the Hover Boots, adult can throw a Bomb at the switch. This trick is only relevant if \"Shuffle Boss Entrances\" is enabled."
    }, 
    "Jabu MQ without Lens of Truth": {
        'tag': TrickTag.NOVICE, 
        'description': "Removes the requirements for the Lens of Truth in Jabu MQ."
    }, 
    "Jabu MQ Compass Chest with Boomerang": {
        'tag': TrickTag.ADVANCED, 
        'description': "Boomerang can reach the cow switch to spawn the chest by targeting the cow, jumping off of the ledge where the chest spawns, and throwing the Boomerang in midair."
    }, 
    "Jabu MQ Song of Time Block GS with Boomerang": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "Allow the Boomerang to return to you through the Song of Time block to grab the token."
    }, 
    "Bottom of the Well without Lens of Truth": {
        'tag': TrickTag.NOVICE, 
        'description': "Removes the requirements for the Lens of Truth in Bottom of the Well."
    }, 
    "Child Dead Hand without Kokiri Sword": {
        'tag': TrickTag.NOVICE, 
        'description': "Requires 9 sticks or 5 jump slashes."
    }, 
    "Bottom of the Well Map Chest with Strength & Sticks": {
        'tag': TrickTag.NOVICE, 
        'description': "The chest in the basement can be reached with strength by doing a jump slash with a lit stick to access the bomb flowers."
    }, 
    "Bottom of the Well MQ Jump Over the Pits": {
        'tag': TrickTag.NOVICE, 
        'description': "While the pits in Bottom of the Well don\'t allow you to jump just by running straight at them, you can still get over them by side-hopping or backflipping across. With explosives, this allows you to access the central areas without Zelda's Lullaby. With Zelda's Lullaby, it allows you to access the west inner room without explosives."
    }, 
    "Bottom of the Well MQ Dead Hand Freestanding Key with Boomerang": {
        'tag': TrickTag.NOVICE, 
        'description': "Boomerang can fish the item out of the rubble without needing explosives to blow it up."
    }, 
    "Forest Temple First Room GS with Difficult-to-Use Weapons": {
        'tag': TrickTag.NOVICE, 
        'description': "Allows killing this Skulltula with Sword or Sticks by jump slashing it as you let go from the vines. You can avoid taking fall damage by recoiling onto the tree. Also allows killing it as Child with a Bomb throw. It's much more difficult to use a Bomb as child due to Child Link's shorter height."
    }, 
    "Forest Temple East Courtyard GS with Boomerang": {
        'tag': TrickTag.NOVICE, 
        'description': "Precise Boomerang throws can allow child to kill the Skulltula and collect the token."
    }, 
    "Forest Temple East Courtyard Vines with Hookshot": {
        'tag': TrickTag.NOVICE, 
        'description': "The vines in Forest Temple leading to where the well drain switch is in the standard form can be barely reached with just the Hookshot. Applies to MQ also."
    }, 
    "Forest Temple NE Outdoors Ledge with Hover Boots": {
        'tag': TrickTag.NOVICE, 
        'description': "With precise Hover Boots movement you can fall down to this ledge from upper balconies. If done precisely enough, it is not necessary to take fall damage. In MQ, this skips a Longshot requirement. In Vanilla, this can skip a Hookshot requirement in entrance randomizer."
    }, 
    "Forest Temple East Courtyard Door Frame with Hover Boots": {
        'tag': TrickTag.ADVANCED, 
        'description': "A precise Hover Boots movement from the upper balconies in this courtyard can be used to get on top of the door frame. Applies to both Vanilla and Master Quest. In Vanilla, from on top the door frame you can summon Pierre, allowing you to access the falling ceiling room early. In Master Quest, this allows you to obtain the GS on the door frame as adult without Hookshot or Song of Time."
    }, 
    "Forest Temple Outside Backdoor with Jump Slash": {
        'tag': TrickTag.ADVANCED, 
        'description': "A jump slash recoil can be used to reach the ledge in the block puzzle room that leads to the west courtyard. This skips a potential Hover Boots requirement in vanilla, and it can sometimes apply in MQ as well. This trick can be performed as both ages."
    }, 
    "Forest Temple Outside Hearts with Boomerang": {
        'tag': TrickTag.NOVICE, 
        'description': "A well aimed boomerang from the water's edge can reach the hearts from ground level. If unable to swim, you can back away from the water while the boomerang is returning so the hearts land on the ground."
    }, 
    "Swim Through Forest Temple MQ Well with Hookshot": {
        'tag': TrickTag.ADVANCED, 
        'description': "Shoot the vines in the well as low and as far to the right as possible, and then immediately swim under the ceiling to the right. This can only be required if Forest Temple is in its Master Quest form."
    }, 
    "Skip Forest Temple MQ Block Puzzle with Bombchu": {
        'tag': TrickTag.NOVICE, 
        'description': "Send the Bombchu straight up the center of the wall directly to the left upon entering the room."
    }, 
    "Forest Temple MQ Twisted Hallway Switch with Jump Slash": {
        'tag': TrickTag.NOVICE, 
        'description': "The switch to twist the hallway can be hit with a jump slash through the glass block. To get in front of the switch, either use the Hover Boots or hit the shortcut switch at the top of the room and jump from the glass blocks that spawn. Sticks can be used as child, but the Kokiri Sword is too short to reach through the glass."
    }, 
    "Forest Temple MQ Twisted Hallway Switch with Hookshot": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "There's a very small gap between the glass block and the wall. Through that gap you can hookshot the target on the ceiling."
    }, 
    "Forest Temple MQ Twisted Hallway Switch with Boomerang": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "The Boomerang can return to Link through walls, allowing child to hit the hallway switch. This can be used to allow adult to pass through later, or in conjuction with \"Forest Temple Outside Backdoor with Jump Slash\"."
    }, 
    "Fire Temple Boss Door without Hover Boots or Pillar": {
        'tag': TrickTag.NOVICE, 
        'description': "The Fire Temple Boss Door can be reached as adult with a precise jump. You must be touching the side wall of the room so that Link will grab the ledge from farther away than is normally possible."
    }, 
    "Fire Temple Song of Time Room GS without Song of Time": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "A precise jump can be used to reach this room."
    }, 
    "Fire Temple Climb without Strength": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "A precise jump can be used to skip pushing the block."
    }, 
    "Fire Temple East Tower without Scarecrow's Song": {
        'tag': TrickTag.EXPERT, 
        'description': "Also known as \"Pixelshot\". The Longshot can reach the target on the elevator itself, allowing you to skip needing to spawn the scarecrow."
    }, 
    "Fire Temple Flame Wall Maze Skip": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "If you move quickly you can sneak past the edge of a flame wall before it can rise up to block you. To do it without taking damage is more precise. Allows you to progress without needing either a Small Key or Hover Boots."
    }, 
    "Fire Temple MQ Chest Near Boss without Breaking Crate": {
        'tag': TrickTag.NOVICE, 
        'description': "The hitbox for the torch extends a bit outside of the crate. Shoot a flaming arrow at the side of the crate to light the torch without needing to get over there and break the crate."
    }, 
    "Fire Temple MQ Big Lava Room Blocked Door without Hookshot": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "There is a gap between the hitboxes of the flame wall in the big lava room. If you know where this gap is located, you can jump through it and skip needing to use the Hookshot. To do this without taking damage is more precise."
    }, 
    "Fire Temple MQ Boss Key Chest without Bow": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "It is possible to light both of the timed torches to unbar the door to the boss key chest's room with just Din's Fire if you move very quickly between the two torches. It is also possible to unbar the door with just Din's by abusing an oversight in the way the game counts how many torches have been lit."
    }, 
    "Fire Temple MQ Climb without Fire Source": {
        'tag': TrickTag.NOVICE, 
        'description': "You can use the Hover Boots to hover around to the climbable wall, skipping the need to use a fire source and spawn a Hookshot target."
    }, 
    "Fire Temple MQ Lizalfos Maze Side Room without Box": {
        'tag': TrickTag.NOVICE, 
        'description': "You can walk from the blue switch to the door and quickly open the door before the bars reclose. This skips needing to reach the upper sections of the maze to get a box to place on the switch."
    }, 
    "Fire Temple MQ Lower to Upper Lizalfos Maze with Hover Boots": {
        'tag': TrickTag.NOVICE, 
        'description': "Use the Hover Boots off of a crate to climb to the upper maze without needing to spawn and use the Hookshot targets."
    }, 
    "Fire Temple MQ Lower to Upper Lizalfos Maze with Precise Jump": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "A precise jump off of a crate can be used to climb to the upper maze without needing to spawn and use the Hookshot targets. This trick supersedes both \"Fire Temple MQ Lower to Upper Lizalfos Maze with Hover Boots\" and \"Fire Temple MQ Lizalfos Maze Side Room without Box\"."
    }, 
    "Fire Temple MQ Above Flame Wall Maze GS from Below with Longshot": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "The floor of the room that contains this Skulltula is only solid from above. From the maze below, the Longshot can be shot through the ceiling to obtain the token with two fewer small keys than normal."
    }, 
    "Fire Temple MQ Flame Wall Maze Skip": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "If you move quickly you can sneak past the edge of a flame wall before it can rise up to block you. To do it without taking damage is more precise. Allows you to reach the side room GS without needing Song of Time or Hover Boots. If either of \"Fire Temple MQ Lower to Upper Lizalfos Maze with Hover Boots\" or \"with Precise Jump\" are enabled, this also allows you to progress deeper into the dungeon without Hookshot."
    }, 
    "Water Temple Torch Longshot": {
        'tag': TrickTag.NOVICE, 
        'description': "Stand on the eastern side of the central pillar and longshot the torches on the bottom level. Swim through the corridor and float up to the top level. This allows access to this area and lower water levels without Iron Boots. The majority of the tricks that allow you to skip Iron Boots in the Water Temple are not going to be relevant unless this trick is first enabled."
    }, 
    "Water Temple Cracked Wall with Hover Boots": {
        'tag': TrickTag.NOVICE, 
        'description': "With a midair side-hop while wearing the Hover Boots, you can reach the cracked wall without needing to raise the water up to the middle level."
    }, 
    "Water Temple Cracked Wall with No Additional Items": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "A precise jump slash (among other methods) will get you to the cracked wall without needing the Hover Boots or to raise the water to the middle level. This trick supersedes \"Water Temple Cracked Wall with Hover Boots\"."
    }, 
    "Water Temple Boss Key Region with Hover Boots": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "With precise Hover Boots movement it is possible to reach the boss key chest's region without needing the Longshot. It is not necessary to take damage from the spikes. The Gold Skulltula Token in the following room can also be obtained with just the Hover Boots."
    }, 
    "Water Temple North Basement Ledge with Precise Jump": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "In the northern basement there's a ledge from where, in vanilla Water Temple, boulders roll out into the room. Normally to jump directly to this ledge logically requires the Hover Boots, but with precise jump, it can be done without them. This trick applies to both Vanilla and Master Quest."
    }, 
    "Water Temple Boss Key Jump Dive": {
        'tag': TrickTag.NOVICE, 
        'description': "Stand on the very edge of the raised corridor leading from the push block room to the rolling boulder corridor. Face the Gold Skulltula on the waterfall and jump over the boulder corridor floor into the pool of water, swimming right once underwater. This allows access to the boss key room without Iron boots."
    }, 
    "Water Temple Central Pillar GS with Farore's Wind": {
        'tag': TrickTag.NOVICE, 
        'description': "If you set Farore\'s Wind inside the central pillar and then return to that warp point after raising the water to the highest level, you can obtain this Skulltula Token with Hookshot or Boomerang."
    }, 
    "Water Temple Central Pillar GS with Iron Boots": {
        'tag': TrickTag.NOVICE, 
        'description': "After opening the middle water level door into the central pillar, the door will stay unbarred so long as you do not leave the room -- even if you were to raise the water up to the highest level. With the Iron Boots to go through the door after the water has been raised, you can obtain the Skulltula Token with the Hookshot."
    }, 
    "Water Temple Central Bow Target without Longshot or Hover Boots": {
        'tag': TrickTag.ADVANCED, 
        'description': "A very precise Bow shot can hit the eye switch from the floor above. Then, you can jump down into the hallway and make through it before the gate closes. It can also be done as child, using the Slingshot instead of the Bow."
    }, 
    "Water Temple Falling Platform Room GS with Hookshot": {
        'tag': TrickTag.NOVICE, 
        'description': "If you stand on the very edge of the platform, this Gold Skulltula can be obtained with only the Hookshot."
    }, 
    "Water Temple Falling Platform Room GS with Boomerang": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "If you stand on the very edge of the platform, this Gold Skulltula can be obtained with only the Boomerang."
    }, 
    "Water Temple River GS without Iron Boots": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "Standing on the exposed ground toward the end of the river, a precise Longshot use can obtain the token. The Longshot cannot normally reach far enough to kill the Skulltula, however. You'll first have to find some other way of killing it."
    }, 
    "Water Temple Dragon Statue Jump Dive": {
        'tag': TrickTag.NOVICE, 
        'description': "If you come into the dragon statue room from the serpent river, you can jump down from above and get into the tunnel without needing either Iron Boots or a Scale. This trick applies to both Vanilla and Master Quest. In Vanilla, you must shoot the switch from above with the Bow, and then quickly get through the tunnel before the gate closes."
    }, 
    "Water Temple Dragon Statue Switch from Above the Water as Adult": {
        'tag': TrickTag.NOVICE, 
        'description': "Normally you need both Hookshot and Iron Boots to hit the switch and swim through the tunnel to get to the chest. But by hitting the switch from dry land, using one of Bombchus, Hookshot, or Bow, it is possible to skip one or both of those requirements. After the gate has been opened, besides just using the Iron Boots, a well-timed dive with at least the Silver Scale could be used to swim through the tunnel. If coming from the serpent river, a jump dive can also be used to get into the tunnel."
    }, 
    "Water Temple Dragon Statue Switch from Above the Water as Child": {
        'tag': TrickTag.ADVANCED, 
        'description': "It is possible for child to hit the switch from dry land using one of Bombchus, Slingshot or Boomerang. Then, to get to the chest, child can dive through the tunnel using at least the Silver Scale. The timing and positioning of this dive needs to be perfect to actually make it under the gate, and it all needs to be done very quickly to be able to get through before the gate closes. Be sure to enable \"Water Temple Dragon Statue Switch from Above the Water as Adult\" for adult's variant of this trick."
    }, 
    "Water Temple MQ Central Pillar with Fire Arrows": {
        'tag': TrickTag.NOVICE, 
        'description': "Slanted torches have misleading hitboxes. Whenever you see a slanted torch jutting out of the wall, you can expect most or all of its hitbox is actually on the other side that wall. This can make slanted torches very finicky to light when using arrows. The torches in the central pillar of MQ Water Temple are a particularly egregious example. Logic normally expects Din's Fire and Song of Time."
    }, 
    "Water Temple MQ North Basement GS without Small Key": {
        'tag': TrickTag.NOVICE, 
        'description': "There is an invisible Hookshot target that can be used to get over the gate that blocks you from going to this Skulltula early, skipping a small key as well as needing Hovers or Scarecrow to reach the locked door."
    }, 
    "Shadow Temple Stationary Objects without Lens of Truth": {
        'tag': TrickTag.NOVICE, 
        'description': "Removes the requirements for the Lens of Truth in Shadow Temple for most areas in the dungeon except for crossing the moving platform in the huge pit room and for fighting Bongo Bongo."
    }, 
    "Shadow Temple Invisible Moving Platform without Lens of Truth": {
        'tag': TrickTag.NOVICE, 
        'description': "Removes the requirements for the Lens of Truth in Shadow Temple to cross the invisible moving platform in the huge pit room in either direction."
    }, 
    "Shadow Temple Bongo Bongo without Lens of Truth": {
        'tag': TrickTag.NOVICE, 
        'description': "Bongo Bongo can be defeated without the use of Lens of Truth, as the hands give a pretty good idea of where the eye is."
    }, 
    "Shadow Temple Stone Umbrella Skip": {
        'tag': TrickTag.EXPERT,
         'description': "A very precise Hover Boots movement from off of the lower chest can get you on top of the crushing spikes without needing to pull the block. Applies to both Vanilla and Master Quest."
    }, 
    "Shadow Temple Falling Spikes GS with Hover Boots": {
        'tag': TrickTag.EXPERT, 
        'description': "After killing the Skulltula, a very precise Hover Boots movement from off of the lower chest can get you on top of the crushing spikes without needing to pull the block. From there, another very precise Hover Boots movement can be used to obtain the token without needing the Hookshot. Applies to both Vanilla and Master Quest. For obtaining the chests in this room with just Hover Boots, be sure to enable \"Shadow Temple Stone Umbrella Skip\"."
    }, 
    "Shadow Temple Freestanding Key with Bombchu": {
        'tag': TrickTag.NOVICE, 
        'description': "Release the Bombchu with good timing so that it explodes near the bottom of the pot."
    }, 
    "Shadow Temple River Statue with Bombchu": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "By sending a Bombchu around the edge of the gorge, you can knock down the statue without needing a Bow. Applies in both vanilla and MQ Shadow."
    }, 
    "Shadow Temple Bongo Bongo without projectiles": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "Using precise sword slashes, Bongo Bongo can be defeated without using projectiles. This is only relevant in conjunction with Shadow Temple dungeon shortcuts or shuffled boss entrances."
    }, 
    "Shadow Temple MQ Stationary Objects without Lens of Truth": {
        'tag': TrickTag.NOVICE, 
        'description': "Removes the requirements for the Lens of Truth in Shadow Temple MQ for most areas in the dungeon. See \"Shadow Temple MQ Invisible Moving Platform without Lens of Truth\", \"Shadow Temple MQ Invisible Blades Silver Rupees without Lens of Truth\", \"Shadow Temple MQ 2nd Dead Hand without Lens of Truth\", and \"Shadow Temple Bongo Bongo without Lens of Truth\" for exceptions."
    }, 
    "Shadow Temple MQ Invisible Blades Silver Rupees without Lens of Truth": {
        'tag': TrickTag.NOVICE, 
        'description': "Removes the requirement for the Lens of Truth or Nayru's Love in Shadow Temple MQ for the Invisible Blades room silver rupee collection."
    }, 
    "Shadow Temple MQ Invisible Moving Platform without Lens of Truth": {
        'tag': TrickTag.NOVICE, 
        'description': "Removes the requirements for the Lens of Truth in Shadow Temple MQ to cross the invisible moving platform in the huge pit room in either direction."
    }, 
    "Shadow Temple MQ 2nd Dead Hand without Lens of Truth": {
        'tag': TrickTag.NOVICE, 
        'description': "Dead Hand spawns in a random spot within the room. Having Lens removes the hassle of having to comb the room looking for his spawn location."
    }, 
    "Shadow Temple MQ Truth Spinner Gap with Longshot": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "You can Longshot a torch and jump-slash recoil onto the tongue. It works best if you Longshot the right torch from the left side of the room."
    }, 
    "Shadow Temple MQ Invisible Blades without Song of Time": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "The Like Like can be used to boost you into the silver rupee or recovery hearts that normally require Song of Time. This cannot be performed on OHKO since the Like Like does not boost you high enough if you die."
    }, 
    "Shadow Temple MQ Lower Huge Pit without Fire Source": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "Normally a frozen eye switch spawns some platforms that you can use to climb down, but there's actually a small piece of ground that you can stand on that you can just jump down to."
    }, 
    "Shadow Temple MQ Windy Walkway Reverse without Hover Boots": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "It is possible to jump from the alcove in the windy hallway to the middle platform. There are two methods: wait out the fan opposite the door and hold forward, or jump to the right to be pushed by the fan there towards the platform ledge. Note that jumps of this distance are inconsistent, but still possible."
    }, 
    "Spirit Temple without Lens of Truth": {
        'tag': TrickTag.NOVICE, 'description': 
        "Removes the requirements for the Lens of Truth in Spirit Temple."
    }, 
    "Spirit Temple Child Side Bridge with Bombchu": {
        'tag': TrickTag.NOVICE, 
        'description': "A carefully-timed Bombchu can hit the switch."
    }, 
    "Spirit Temple Main Room GS with Boomerang": {
        'tag': TrickTag.NOVICE, 'description': 
        "Standing on the highest part of the arm of the statue, a precise Boomerang throw can kill and obtain this Gold Skulltula. You must throw the Boomerang slightly off to the side so that it curves into the Skulltula, as aiming directly at it will clank off of the wall in front."
    }, 
    "Spirit Temple Lower Adult Switch with Bombs": {
        'tag': TrickTag.ADVANCED, 
        'description': "A bomb can be used to hit the switch on the ceiling, but it must be thrown from a particular distance away and with precise timing."
    }, 
    "Spirit Temple Main Room Jump from Hands to Upper Ledges": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "A precise jump to obtain the following as adult without needing one of Hover Boots, or Hookshot (in vanilla) or Song of Time (in MQ): - Spirit Temple Statue Room Northeast Chest - Spirit Temple GS Lobby - Spirit Temple MQ Central Chamber Top Left Pot (Left) - Spirit Temple MQ Central Chamber Top Left Pot (Right)"
    }, 
    "Spirit Temple Map Chest with Bow": {
        'tag': TrickTag.NOVICE, 
        'description': "To get a line of sight from the upper torch to the map chest torches, you must pull an Armos statue all the way up the stairs."
    }, 
    "Spirit Temple Sun Block Room Chest with Bow": {
        'tag': TrickTag.ADVANCED, 
        'description': "Using the blocks in the room as platforms you can get lines of sight to all three torches. The timer on the torches is quite short so you must move quickly in order to light all three."
    }, 
    "Spirit Temple Shifting Wall with No Additional Items": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "Logic normally guarantees a way of dealing with both the Beamos and the Walltula before climbing the wall."
    }, 
    "Spirit Temple MQ without Lens of Truth": {
        'tag': TrickTag.NOVICE, 
        'description': "Removes the requirements for the Lens of Truth in Spirit Temple MQ."
    }, 
    "Spirit Temple MQ Sun Block Room as Child without Song of Time": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "While adult can easily jump directly to the switch that unbars the door to the sun block room, child Link cannot make the jump without spawning a Song of Time block to jump from. You can skip this by throwing the crate down onto the switch from above, which does unbar the door, however the crate immediately breaks, so you must move quickly to get through the door before it closes back up."
    }, 
    "Spirit Temple MQ Sun Block Room GS with Boomerang": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "Throw the Boomerang in such a way that it curves through the side of the glass block to hit the Gold Skulltula."
    }, 
    "Spirit Temple MQ Lower Adult without Fire Arrows": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "By standing in a precise position it is possible to light two of the torches with a single use of Din's Fire. This saves enough time to be able to light all three torches with only Din's."
    }, 
    "Spirit Temple MQ Frozen Eye Switch without Fire": {
        'tag': TrickTag.NOVICE, 
        'description': "You can melt the ice by shooting an arrow through a torch. The only way to find a line of sight for this shot is to first spawn a Song of Time block, and then stand on the very edge of it."
    }, 
    "Ice Cavern Block Room GS with Hover Boots": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "The Hover Boots can be used to get in front of the Skulltula to kill it with a jump slash. Then, the Hover Boots can again be used to obtain the Token, all without Hookshot or Boomerang."
    }, 
    "Ice Cavern MQ Red Ice GS without Song of Time": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "If you side-hop into the perfect position, you can briefly stand on the platform with the red ice just long enough to dump some blue fire."
    }, 
    "Ice Cavern MQ Scarecrow GS with No Additional Items": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "As adult a precise jump can be used to reach this alcove."
    }, 
    "Gerudo Training Ground without Lens of Truth": {
        'tag': TrickTag.NOVICE, 
        'description': "Removes the requirements for the Lens of Truth in Gerudo Training Ground."
    }, 
    "Gerudo Training Ground Left Side Silver Rupees without Hookshot": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "After collecting the rest of the silver rupees in the room, you can reach the final silver rupee on the ceiling by being pulled up into it after getting grabbed by the Wallmaster. Then, you must also reach the exit of the room without the use of the Hookshot. If you move quickly you can sneak past the edge of a flame wall before it can rise up to block you. To do so without taking damage is more precise."
    }, 
    "Reach Gerudo Training Ground Fake Wall Ledge with Hover Boots": {
        'tag': TrickTag.NOVICE, 
        'description': "A precise Hover Boots use from the top of the chest can allow you to grab the ledge without needing the usual requirements. In Master Quest, this always skips a Song of Time requirement. In Vanilla, this skips a Hookshot requirement, but is only relevant if \"Gerudo Training Ground Left Side Silver Rupees without Hookshot\" is enabled."
    }, 
    "Gerudo Training Ground MQ without Lens of Truth": {
        'tag': TrickTag.NOVICE, 
        'description': "Removes the requirements for the Lens of Truth in Gerudo Training Ground MQ."
    }, 
    "Gerudo Training Ground MQ Left Side Silver Rupees with Hookshot": {
        'tag': TrickTag.NOVICE, 
        'description': "The highest silver rupee can be obtained by hookshotting the target and then immediately jump slashing toward the rupee."
    }, 
    "Gerudo Training Ground MQ Left Side Silver Rupees without Hookshot": {
        'tag': TrickTag.INTERMEDIATE, 
        'description': "After collecting the rest of the silver rupees in the room, you can reach the final silver rupee on the ceiling by being pulled up into it after getting grabbed by the Wallmaster. The Wallmaster will not track you to directly underneath the rupee. You should take the last step to be under the rupee after the Wallmaster has begun its attempt to grab you. Also included with this trick is that fact that the switch that unbars the door to the final chest of GTG can be hit without a projectile, using a precise jump slash. This trick supersedes \"Gerudo Training Ground MQ Left Side Silver Rupees with Hookshot\"."
    }, 
    "Ganon's Castle without Lens of Truth": {
        'tag': TrickTag.NOVICE, 
        'description': "Removes the requirements for the Lens of Truth in Ganon's Castle."
    }, 
    "Spirit Trial without Hookshot": {
        'tag': TrickTag.NOVICE, 
        'description': "The highest rupee can be obtained as either age by performing a precise jump and a well-timed jumpslash off of an Armos."
    }, 
    "Ganon's Castle MQ without Lens of Truth": {
        'tag': TrickTag.NOVICE, 
        'description': "Removes the requirements for the Lens of Truth in Ganon's Castle MQ."
    }, 
    "Fire Trial MQ with Hookshot": {
        'tag': TrickTag.ADVANCED, 
        'description': "It's possible to hook the target at the end of fire trial with just Hookshot, but it requires precise aim and perfect positioning. The main difficulty comes from getting on the very corner of the obelisk without falling into the lava."
    }, 
    "Shadow Trial MQ Torch with Bow": {
        'tag': TrickTag.NOVICE, 
        'description': "You can light the torch in this room without a fire source by shooting an arrow through the lit torch at the beginning of the room. Because the room is so dark and the unlit torch is so far away, it can be difficult to aim the shot correctly."
    }, 
    "Light Trial MQ without Hookshot": {
        'tag': TrickTag.INTERMEDIATE, 
    'description': "If you move quickly you can sneak past the edge of a flame wall before it can rise up to block you. In this case to do it without taking damage is especially precise" 
    }
}

normalized_name_tricks = {trick.casefold(): info for (trick, info) in logic_tricks.items()}
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                