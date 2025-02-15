from ToontownGlobals import *
import math
import TTLocalizer
BattleCamFaceOffFov = 30.0
BattleCamFaceOffPos = Point3(0, -10, 4)
BattleCamDefaultPos = Point3(0, -8.6, 16.5)
BattleCamDefaultHpr = Vec3(0, -61, 0)
BattleCamDefaultFov = 80.0
BattleCamMenuFov = 65.0
BattleCamJoinPos = Point3(0, -12, 13)
BattleCamJoinHpr = Vec3(0, -45, 0)
SkipMovie = 0
BaseHp = 145
Tracks = TTLocalizer.BattleGlobalTracks
NPCTracks = TTLocalizer.BattleGlobalNPCTracks
TrackColors = ((0 / 255.0, 148 / 255.0, 255 / 255.0),
 (255 / 255.0, 0 / 255.0, 0 / 255.0),
 (0 / 200.0, 255 / 255.0, 0 / 255.0),
 (255.0 / 255.0, 0.1 / 0.1, 0.1 / 0.1),
 (255.0 / 140.0, 145 / 35.0, 66 / 95.0),
 (15.0 / 25.0, 35.0 / 5.0, 9 / 7.0),
 (0.5 / 0.2, 0.5 / 0.3, 0.5 / 255.0))
HEAL_TRACK = 0
TRAP_TRACK = 1
LURE_TRACK = 2
SOUND_TRACK = 3
THROW_TRACK = 4
SQUIRT_TRACK = 5
DROP_TRACK = 6
NPC_RESTOCK_GAGS = 7
NPC_TOONS_HIT = 8
NPC_COGS_MISS = 9
MIN_TRACK_INDEX = 0
MAX_TRACK_INDEX = 6
MIN_LEVEL_INDEX = 0
MAX_LEVEL_INDEX = 6
MAX_UNPAID_LEVEL_INDEX = 4
LAST_REGULAR_GAG_LEVEL = 6
UBER_GAG_LEVEL_INDEX = 6
NUM_GAG_TRACKS = 7
AvLureRounds = (2,
 1,
 2,
 1,
 2,
 1,
 2)
PropTypeToTrackBonus = {AnimPropTypes.Hydrant: SQUIRT_TRACK,
 AnimPropTypes.Mailbox: THROW_TRACK,
 AnimPropTypes.Trashcan: HEAL_TRACK}
Levels = [[0,
  250,
  1000,
  3500,
  7500,
  12500,
  25000],
 [0,
  250,
  1000,
  3500,
  7500,
  12500,
  25000],
 [0,
  250,
  1000,
  3500,
  7500,
  12500,
  25000],
 [0,
  250,
  1000,
  3500,
  7500,
  12500,
  25000],
 [0,
  250,
  1000,
  3500,
  7500,
  12500,
  25000],
 [0,
  250,
  1000,
  3500,
  7500,
  12500,
  25000],
 [0,
  250,
  1000,
  3500,
  7500,
  12500,
  25000]]
regMaxSkill = 25000
UberSkill = 0
MaxSkill = UberSkill + regMaxSkill
UnpaidMaxSkills = [Levels[0][1] - 1,
 Levels[1][1] - 1,
 Levels[2][1] - 1,
 Levels[3][1] - 1,
 Levels[4][4] - 1,
 Levels[5][4] - 1,
 Levels[6][1] - 1]
ExperienceCap = 2500

def gagIsPaidOnly(track, level):
    return Levels[track][level] > UnpaidMaxSkills[track]


def gagIsVelvetRoped(track, level):
    if level > 0:
        if track in [4, 5]:
            if level > 3:
                return True
        else:
            return True
    return False


MaxToonAcc = 95
StartingLevel = 0
CarryLimits = (((20,
   0,
   0,
   0,
   0,
   0,
   0),
  (20,
   15,
   0,
   0,
   0,
   0,
   0),
  (20,
   15,
   10,
   0,
   0,
   0,
   0),
  (20,
   15,
   10,
   7,
   0,
   0,
   0),
  (20,
   15,
   10,
   7,
   5,
   0,
   0),
  (20,
   15,
   10,
   7,
   5,
   2,
   0),
  (20,
   15,
   10,
   7,
   5,
   3,
   1)),
 ((20,
   0,
   0,
   0,
   0,
   0,
   0),
  (20,
   15,
   0,
   0,
   0,
   0,
   0),
  (20,
   15,
   10,
   0,
   0,
   0,
   0),
  (20,
   15,
   10,
   7,
   0,
   0,
   0),
  (20,
   15,
   10,
   7,
   5,
   0,
   0),
  (20,
   15,
   10,
   7,
   5,
   2,
   0),
  (20,
   15,
   10,
   7,
   5,
   2,
   1)),
 ((15,
   0,
   0,
   0,
   0,
   0,
   0),
  (15,
   10,
   0,
   0,
   0,
   0,
   0),
  (15,
   10,
   10,
   0,
   0,
   0,
   0),
  (15,
   10,
   10,
   5,
   0,
   0,
   0),
  (15,
   10,
   10,
   5,
   5,
   0,
   0),
  (15,
   10,
   10,
   5,
   5,
   2,
   0),
  (15,
   10,
   10,
   5,
   5,
   2,
   1)),
 ((10,
   0,
   0,
   0,
   0,
   0,
   0),
  (10,
   15,
   0,
   0,
   0,
   0,
   0),
  (15,
   10,
   7,
   0,
   0,
   0,
   0),
  (15,
   10,
   7,
   5,
   0,
   0,
   0),
  (15,
   10,
   7,
   5,
   3,
   0,
   0),
  (15,
   10,
   7,
   5,
   3,
   2,
   0),
  (15,
   10,
   7,
   5,
   3,
   2,
   1)),
 ((20,
   0,
   0,
   0,
   0,
   0,
   0),
  (20,
   15,
   0,
   0,
   0,
   0,
   0),
  (20,
   15,
   10,
   0,
   0,
   0,
   0),
  (20,
   15,
   10,
   7,
   0,
   0,
   0),
  (20,
   15,
   10,
   7,
   4,
   0,
   0),
  (20,
   15,
   10,
   7,
   4,
   2,
   0),
  (20,
   15,
   10,
   7,
   4,
   2,
   1)),
 ((20,
   0,
   0,
   0,
   0,
   0,
   0),
  (20,
   15,
   0,
   0,
   0,
   0,
   0),
  (20,
   15,
   10,
   0,
   0,
   0,
   0),
  (20,
   15,
   10,
   5,
   0,
   0,
   0),
  (20,
   15,
   10,
   7,
   4,
   0,
   0),
  (20,
   15,
   10,
   7,
   4,
   2,
   0),
  (20,
   15,
   10,
   7,
   4,
   2,
   1)),
 ((20,
   0,
   0,
   0,
   0,
   0,
   0),
  (20,
   15,
   0,
   0,
   0,
   0,
   0),
  (20,
   15,
   10,
   0,
   0,
   0,
   0),
  (20,
   15,
   10,
   5,
   0,
   0,
   0),
  (20,
   15,
   10,
   7,
   3,
   0,
   0),
  (20,
   15,
   10,
   7,
   4,
   2,
   0),
  (20,
   15,
   10,
   7,
   4,
   2,
   1)))
MaxProps = ((15, 40), (30, 60), (75, 80))
DLF_SKELECOG = 1
DLF_FOREMAN = 2
DLF_VP = 4
DLF_CFO = 8
DLF_SUPERVISOR = 16
DLF_VIRTUAL = 32
DLF_REVIVES = 64
pieNames = ['tart',
 'fruitpie-slice',
 'creampie-slice',
 'fruitpie',
 'creampie',
 'birthday-cake',
 'wedding-cake',
 'lawbook']
AvProps = (('feather',
  'bullhorn',
  'lipstick',
  'bamboocane',
  'pixiedust',
  'baton',
  'baton'),
 ('banana',
  'rake',
  'marbles',
  'quicksand',
  'trapdoor',
  'tnt',
  'traintrack'),
 ('1dollar',
  'smmagnet',
  '5dollar',
  'bigmagnet',
  '10dollar',
  'hypnogogs',
  'hypnogogs'),
 ('bikehorn',
  'whistle',
  'bugle',
  'aoogah',
  'elephant',
  'foghorn',
  'singing'),
 ('cupcake',
  'fruitpieslice',
  'creampieslice',
  'fruitpie',
  'creampie',
  'cake',
  'cake'),
 ('flower',
  'waterglass',
  'waterballoon',
  'bottle',
  'firehose',
  'stormcloud',
  'stormcloud'),
 ('flowerpot',
  'sandbag',
  'anvil',
  'weight',
  'safe',
  'piano',
  'piano'))
AvPropsNew = (('inventory_feather',
  'inventory_megaphone',
  'inventory_lipstick',
  'inventory_bamboo_cane',
  'inventory_pixiedust',
  'inventory_juggling_cubes',
  'inventory_ladder'),
 ('inventory_bannana_peel',
  'inventory_rake',
  'inventory_marbles',
  'inventory_quicksand_icon',
  'inventory_trapdoor',
  'inventory_tnt',
  'inventory_traintracks'),
 ('inventory_1dollarbill',
  'inventory_small_magnet',
  'inventory_5dollarbill',
  'inventory_big_magnet',
  'inventory_10dollarbill',
  'inventory_hypno_goggles',
  'inventory_screen'),
 ('inventory_bikehorn',
  'inventory_whistle',
  'inventory_bugle',
  'inventory_aoogah',
  'inventory_elephant',
  'inventory_fog_horn',
  'inventory_opera_singer'),
 ('inventory_tart',
  'inventory_fruit_pie_slice',
  'inventory_cream_pie_slice',
  'inventory_fruitpie',
  'inventory_creampie',
  'inventory_cake',
  'inventory_wedding'),
 ('inventory_squirt_flower',
  'inventory_glass_of_water',
  'inventory_water_gun',
  'inventory_seltzer_bottle',
  'inventory_firehose',
  'inventory_storm_cloud',
  'inventory_storm_cloud'),
 ('inventory_flower_pot',
  'inventory_sandbag',
  'inventory_anvil',
  'inventory_weight',
  'inventory_safe_box',
  'inventory_piano',
  'inventory_piano'))
AvPropStrings = TTLocalizer.BattleGlobalAvPropStrings
AvPropStringsSingular = TTLocalizer.BattleGlobalAvPropStringsSingular
AvPropStringsPlural = TTLocalizer.BattleGlobalAvPropStringsPlural
AvPropAccuracy = ((95,
  95,
  95,
  95,
  95,
  95,
  95),
 (0,
  0,
  0,
  0,
  0,
  0,
  0),
 (95,
  95,
  95,
  95,
  95,
  95,
  95),
 (95,
  95,
  95,
  95,
  95,
  95,
  95),
 (95,
  95,
  95,
  95,
  95,
  95,
  95),
 (95,
  95,
  95,
  95,
  95,
  95,
  95),
 (95,
  95,
  95,
  95,
  95,
  95,
  95))
AvLureBonusAccuracy = (95,
 95,
 95,
 95,
 95,
 95,
 95)
AvTrackAccStrings = TTLocalizer.BattleGlobalAvTrackAccStrings
AvPropDamage = ((((75, 75), (Levels[0][0], Levels[0][1])),
  ((150, 150), (Levels[0][1], Levels[0][2])),
  ((125, 125), (Levels[0][2], Levels[0][3])),
  ((300, 300), (Levels[0][3], Levels[0][4])),
  ((175, 175), (Levels[0][4], Levels[0][5])),
  ((450, 450), (Levels[0][5], Levels[0][6])),
  ((750, 750), (Levels[0][6], MaxSkill))),
 (((50, 50), (Levels[1][0], Levels[1][1])),
  ((90, 90), (Levels[1][1], Levels[1][2])),
  ((150, 150), (Levels[1][2], Levels[1][3])),
  ((250, 250), (Levels[1][3], Levels[1][4])),
  ((450, 450), (Levels[1][4], Levels[1][5])),
  ((650, 650), (Levels[1][5], Levels[1][6])),
  ((1000, 1000), (Levels[1][6], MaxSkill))),
 (((0, 0), (0, 0)),
  ((0, 0), (0, 0)),
  ((0, 0), (0, 0)),
  ((0, 0), (0, 0)),
  ((0, 0), (0, 0)),
  ((0, 0), (0, 0)),
  ((0, 0), (0, 0))),
 (((5, 5), (Levels[3][0], Levels[3][1])),
  ((20, 20), (Levels[3][1], Levels[3][2])),
  ((40, 40), (Levels[3][2], Levels[3][3])),
  ((70, 70), (Levels[3][3], Levels[3][4])),
  ((100, 100), (Levels[3][4], Levels[3][5])),
  ((150, 150), (Levels[3][5], Levels[3][6])),
  ((300, 300), (Levels[3][6], MaxSkill))),
 (((10, 10), (Levels[4][0], Levels[4][1])),
  ((20, 20), (Levels[4][1], Levels[4][2])),
  ((30, 30), (Levels[4][2], Levels[4][3])),
  ((50, 50), (Levels[4][3], Levels[4][4])),
  ((75, 75), (Levels[4][4], Levels[4][5])),
  ((125, 125), (Levels[4][5], Levels[4][6])),
  ((200, 200), (Levels[4][6], MaxSkill))),
(((10, 10), (Levels[5][0], Levels[5][1])),
  ((20, 20), (Levels[5][1], Levels[5][2])),
  ((30, 30), (Levels[5][2], Levels[5][3])),
  ((50, 50), (Levels[5][3], Levels[5][4])),
  ((75, 75), (Levels[5][4], Levels[5][5])),
  ((125, 125), (Levels[5][5], Levels[5][6])),
  ((200, 200), (Levels[5][6], MaxSkill))),
(((20, 20), (Levels[6][0], Levels[6][1])),
  ((35, 35), (Levels[6][1], Levels[6][2])),
  ((60, 60), (Levels[6][2], Levels[6][3])),
  ((100, 100), (Levels[6][3], Levels[6][4])),
  ((150, 150), (Levels[6][4], Levels[6][5])),
  ((200, 200), (Levels[6][5], Levels[6][6])),
  ((400, 400), (Levels[6][6], MaxSkill))))
ATK_SINGLE_TARGET = 0
ATK_GROUP_TARGET = 1
AvPropTargetCat = ((ATK_SINGLE_TARGET,
  ATK_GROUP_TARGET,
  ATK_SINGLE_TARGET,
  ATK_GROUP_TARGET,
  ATK_SINGLE_TARGET,
  ATK_GROUP_TARGET,
  ATK_GROUP_TARGET),
 (ATK_SINGLE_TARGET,
  ATK_SINGLE_TARGET,
  ATK_SINGLE_TARGET,
  ATK_SINGLE_TARGET,
  ATK_SINGLE_TARGET,
  ATK_SINGLE_TARGET,
  ATK_SINGLE_TARGET),
 (ATK_GROUP_TARGET,
  ATK_GROUP_TARGET,
  ATK_GROUP_TARGET,
  ATK_GROUP_TARGET,
  ATK_GROUP_TARGET,
  ATK_GROUP_TARGET,
  ATK_GROUP_TARGET),
 (ATK_SINGLE_TARGET,
  ATK_SINGLE_TARGET,
  ATK_SINGLE_TARGET,
  ATK_SINGLE_TARGET,
  ATK_SINGLE_TARGET,
  ATK_SINGLE_TARGET,
  ATK_SINGLE_TARGET))
AvPropTarget = (0,
 3,
 0,
 2,
 3,
 3,
 3)

def getAvPropDamage(attackTrack, attackLevel, exp, organicBonus = False, propBonus = False, propAndOrganicBonusStack = False):
    minD = AvPropDamage[attackTrack][attackLevel][0][0]
    maxD = AvPropDamage[attackTrack][attackLevel][0][1]
    minE = AvPropDamage[attackTrack][attackLevel][1][0]
    maxE = AvPropDamage[attackTrack][attackLevel][1][1]
    expVal = min(exp, maxE)
    expPerHp = float(maxE - minE + 1) / float(maxD - minD + 1)
    damage = math.floor((expVal - minE) / expPerHp) + minD
    if damage <= 0:
        damage = minD
    if propAndOrganicBonusStack:
        originalDamage = damage
        if organicBonus:
            damage += getDamageBonus(originalDamage)
        if propBonus:
            damage += getDamageBonus(originalDamage)
    elif organicBonus or propBonus:
        damage += getDamageBonus(damage)
    return damage


def getDamageBonus(normal):
    bonus = int(normal * 0.5)
    if bonus < 1 and normal > 0:
        bonus = 1
    return bonus


def isGroup(track, level):
    return AvPropTargetCat[AvPropTarget[track]][level]


def getCreditMultiplier(floorIndex):
    return 1 + floorIndex * 2.5


def getFactoryCreditMultiplier(factoryId):
    return 7.0


def getFactoryMeritMultiplier(factoryId):
    return 12.0


def getMintCreditMultiplier(mintId):
    return {CashbotMintIntA: 5.5,
     CashbotMintIntB: 7.5,
     CashbotMintIntC: 9.5}.get(mintId, 1.0)


def getStageCreditMultiplier(floor):
    return getCreditMultiplier(floor)


def getCountryClubCreditMultiplier(countryClubId):
    return {BossbotCountryClubIntA: 8.0,
     BossbotCountryClubIntB: 10.0,
     BossbotCountryClubIntC: 12.0}.get(countryClubId, 1.0)


def getBossBattleCreditMultiplier(battleNumber):
    return 1.5 + battleNumber


def getInvasionMultiplier():
    return 4.0


def getMoreXpHolidayMultiplier():
    return 4.0


def encodeUber(trackList):
    bitField = 0
    for trackIndex in xrange(len(trackList)):
        if trackList[trackIndex] > 0:
            bitField += pow(2, trackIndex)

    return bitField


def decodeUber(flagMask):
    if flagMask == 0:
        return []
    maxPower = 16
    workNumber = flagMask
    workPower = maxPower
    trackList = []
    while workPower >= 0:
        if workNumber >= pow(2, workPower):
            workNumber -= pow(2, workPower)
            trackList.insert(0, 1)
        else:
            trackList.insert(0, 0)
        workPower -= 1

    endList = len(trackList)
    foundOne = 0
    while not foundOne:
        if trackList[endList - 1] == 0:
            trackList.pop(endList - 1)
            endList -= 1
        else:
            foundOne = 1

    return trackList


def getUberFlag(flagMask, index):
    decode = decodeUber(flagMask)
    if index >= len(decode):
        return 0
    else:
        return decode[index]


def getUberFlagSafe(flagMask, index):
    if flagMask == 'unknown' or flagMask < 0:
        return -1
    else:
        return getUberFlag(flagMask, index)
