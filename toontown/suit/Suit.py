from direct.actor import Actor
from otp.avatar import Avatar
import SuitDNA
from toontown.toonbase import ToontownGlobals
from panda3d.core import *
from toontown.battle import SuitBattleGlobals
from direct.task.Task import Task
from toontown.battle import BattleProps
from toontown.toonbase import TTLocalizer
from libotp import *
from direct.showbase import AppRunnerGlobal
import string
import os
aSize = 6.06
bSize = 5.29
cSize = 4.14
SuitDialogArray = []
SkelSuitDialogArray = []
AllSuits = (('walk', 'walk'), ('run', 'walk'), ('neutral', 'neutral'))
AllSuitsMinigame = (('victory', 'victory'),
 ('flail', 'flailing'),
 ('tug-o-war', 'tug-o-war'),
 ('slip-backward', 'slip-backward'),
 ('slip-forward', 'slip-forward'))
AllSuitsTutorialBattle = (('lose', 'lose'), ('pie-small-react', 'pie-small'), ('squirt-small-react', 'squirt-small'))
AllSuitsBattle = (('drop-react', 'anvil-drop'),
 ('flatten', 'drop'),
 ('sidestep-left', 'sidestep-left'),
 ('sidestep-right', 'sidestep-right'),
 ('squirt-large-react', 'squirt-large'),
 ('landing', 'landing'),
 ('reach', 'walknreach'),
 ('rake-react', 'rake'),
 ('hypnotized', 'hypnotize'),
 ('lured', 'lured'),
 ('soak', 'soak'))
SuitsCEOBattle = (('sit', 'sit'),
 ('sit-eat-in', 'sit-eat-in'),
 ('sit-eat-loop', 'sit-eat-loop'),
 ('sit-eat-out', 'sit-eat-out'),
 ('sit-angry', 'sit-angry'),
 ('sit-hungry-left', 'leftsit-hungry'),
 ('sit-hungry-right', 'rightsit-hungry'),
 ('sit-lose', 'sit-lose'),
 ('tray-walk', 'tray-walk'),
 ('tray-neutral', 'tray-neutral'),
 ('sit-lose', 'sit-lose'))
f = (('throw-paper', 'throw-paper', 3.5), ('phone', 'phone', 3.5), ('shredder', 'shredder', 3.5))
p = (('pencil-sharpener', 'pencil-sharpener', 5),
 ('magic3', 'magic3', 5),
 ('hold-eraser', 'hold-eraser', 5),
 ('pen-squirt', 'pen-squirt', 5),
 ('finger-wag', 'finger-wag', 5),
 ('hold-pencil', 'hold-pencil', 5))
ym = (('magic1', 'magic1', 5),
 ('magic2', 'magic2', 5),
 ('magic3', 'magic3', 5),
 ('cigar-smoke', 'cigar-smoke', 8),
 ('smile', 'smile', 5))
mm = (('stomp', 'stomp', 5),
 ('effort', 'effort', 5),
 ('finger-wag', 'finger-wag', 5),
 ('quick-jump', 'jump', 6),
 ('magic2', 'magic2', 5),
 ('magic3', 'magic3', 5))
ds = (('magic1', 'magic1', 5),
 ('magic2', 'magic2', 5),
 ('throw-paper', 'throw-paper', 5),
 ('speak', 'speak', 5),
 ('throw-object', 'throw-object', 5),
 ('song-and-dance', 'song-and-dance', 8),
 ('glower', 'glower', 5),
 ('magic3', 'magic3', 5))
hh = (('quick-jump', 'jump', 6),
 ('effort', 'effort', 5),
 ('magic2', 'magic2', 5),
 ('stomp', 'stomp', 5),
 ('speak', 'speak', 5),
 ('finger-wag', 'finger-wag', 5),
 ('magic3', 'magic3', 5),
 ('throw-object', 'throw-object', 5),
 ('throw-paper', 'throw-paper', 5))
cr = (('pickpocket', 'pickpocket', 5), ('speak', 'speak', 5), ('magic1', 'magic1', 5), ('throw-paper', 'throw-paper', 5), ('glower', 'glower', 5))
tbc = (('magic2', 'magic2', 8),
 ('glower', 'glower', 5),
 ('magic1', 'magic1', 5),
 ('effort', 'effort', 6),
 ('magic3', 'magic3', 8),
 ('smile', 'smile', 5))
trb = (('magic1', 'magic1', 5), ('glower', 'glower', 5), ('magic2', 'magic2', 5), ('throw-object', 'throw-object', 5))
dot = (('magic1', 'magic1', 5), ('glower', 'glower', 5), ('effort', 'effort', 5), ('throw-paper', 'throw-paper', 3.5))
kb = (('effort', 'effort', 6),
 ('speak', 'speak', 5),
 ('magic2', 'magic2', 5))
cc = (('speak', 'speak', 5),
 ('glower', 'glower', 5),
 ('phone', 'phone', 3.5),
 ('magic2', 'magic2', 5),
 ('stomp', 'stomp', 5))
tm = (('speak', 'speak', 5),
 ('stomp', 'stomp', 5),
 ('pickpocket', 'pickpocket', 5),
 ('throw-paper', 'throw-paper', 5),
 ('phone', 'phone', 5))
nd = (('smile', 'smile', 5),
 ('magic1', 'magic1', 5),
 ('smile', 'smile', 5),
 ('effort', 'effort', 6),
 ('magic2', 'magic2', 5))
gh = (('speak', 'speak', 5), ('finger-wag', 'finger-wag', 5), ('effort', 'effort', 5), ('roll-o-dex', 'roll-o-dex', 5), ('magic2', 'magic2', 5), ('stomp', 'stomp', 5), ('throw-paper', 'throw-paper', 5))
ms = (('smile', 'smile', 5),
 ('throw-object', 'throw-object', 5),
 ('throw-paper', 'throw-paper', 5),
 ('pickpocket', 'pickpocket', 5),
 ('phone', 'phone', 5),
 ('finger-wag', 'fingerwag', 5))
tf = (('smile', 'smile', 5),
 ('magic1', 'magic1', 5),
 ('throw-paper', 'throw-paper', 5),
 ('throw-object', 'throw-object', 5),
 ('magic3', 'magic3', 5),
 ('phone', 'phone', 5))
m = (('speak', 'speak', 5),
 ('magic1', 'magic1', 5),
 ('smile', 'smile', 5),
 ('magic2', 'magic2', 5),
 ('throw-paper', 'throw-paper', 5),
 ('throw-object', 'throw-object', 5))
mh = (('magic1', 'magic1', 5),
 ('throw-paper', 'throw-paper', 5),
 ('effort', 'effort', 6),
 ('throw-object', 'throw-object', 5),
 ('glower', 'glower', 5),
 ('speak', 'speak', 5),
 ('pickpocket', 'pickpocket', 5),
 ('smile', 'smile', 5),
 ('phone', 'phone', 5),
 ('finger-wag', 'fingerwag', 5))
ka = (('magic2', 'magic2', 5), ('glower', 'glower', 5), ('magic1', 'magic1', 5), ('effort', 'effort', 6), ('speak', 'speak', 5))
bbs = (('magic2', 'magic2', 5), ('magic1', 'magic1', 5), ('throw-object', 'throw-object', 5), ('effort', 'effort', 6))
fd = (('magic1', 'magic1', 5), ('throw-paper', 'throw-paper', 5), ('effort', 'effort', 6), ('magic2', 'magic2', 5))
sc = (('throw-paper', 'throw-paper', 3.5), ('watercooler', 'watercooler', 5), ('pickpocket', 'pickpocket', 5))
pp = (('throw-paper', 'throw-paper', 5), ('throw-object', 'throw-object', 5), ('effort', 'effort', 5), ('finger-wag', 'finger-wag', 5))
tw = (('speak', 'speak', 5),
 ('glower', 'glower', 5),
 ('smile', 'smile', 5),
 ('magic2', 'magic2', 5),
 ('finger-wag', 'fingerwag', 5))
bc = (('phone', 'phone', 5), ('roll-o-dex', 'roll-o-dex', 5))
nc = (('phone', 'phone', 5), ('finger-wag', 'fingerwag', 5), ('glower', 'glower', 5), ('magic1', 'magic1', 5), ('throw-object', 'throw-object', 5),  ('throw-paper', 'throw-paper', 5))
mb = (('pickpocket', 'pickpocket', 5), ('magic3', 'magic3', 5), ('speak', 'speak', 5), ('magic1', 'magic1', 5), ('throw-object', 'throw-object', 5), ('golf-club-swing', 'golf-club-swing', 5))
ls = (('roll-o-dex', 'roll-o-dex', 5), ('speak', 'speak', 5), ('effort', 'effort', 5), ('throw-paper', 'throw-paper', 5), ('throw-object', 'throw-object', 5), ('magic2', 'magic2', 5), ('hold-pencil', 'hold-pencil', 5))
rb = (('pickpocket', 'pickpocket', 5), ('finger-wag', 'fingerwag', 5), ('speak', 'speak', 5), ('magic3', 'magic3', 5), ('magic2', 'magic2', 5), ('glower', 'glower', 5), ('pen-squirt', 'fountain-pen', 7), ('magic1', 'magic1', 5), ('rubber-stamp', 'rubber-stamp', 5))
gm = (('magic1', 'magic1', 5), ('throw-paper', 'throw-paper', 5))
ad = (('throw-object', 'throw-object', 5), ('throw-paper', 'throw-paper', 5), ('pickpocket', 'pickpocket', 5))
dm = (('magic3', 'magic3', 5), ('pickpocket', 'pickpocket', 5), ('throw-paper', 'throw-paper', 5), ('roll-o-dex', 'roll-o-dex', 5), ('hold-pencil', 'hold-pencil', 5), ('finger-wag', 'finger-wag', 5))
bf = (('pickpocket', 'pickpocket', 5),
 ('rubber-stamp', 'rubber-stamp', 5),
 ('shredder', 'shredder', 3.5),
 ('watercooler', 'watercooler', 5))
b = (('effort', 'effort', 5),
 ('throw-paper', 'throw-paper', 5),
 ('magic1', 'magic1', 5),
 ('throw-object', 'throw-object', 5),
 ('finger-wag', 'finger-wag', 5))
dt = (('rubber-stamp', 'rubber-stamp', 5),
 ('throw-paper', 'throw-paper', 5),
 ('throw-object', 'throw-object', 5),
 ('speak', 'speak', 5),
 ('magic2', 'magic2', 5),
 ('roll-o-dex', 'roll-o-dex', 5))
ac = (('finger-wag', 'finger-wag', 5),
 ('throw-paper', 'throw-paper', 3.5),
 ('magic2', 'magic2', 5),
 ('magic1', 'magic1', 5),
 ('phone', 'phone', 3.5),
 ('throw-paper', 'throw-paper', 3.5))
bs = (('magic1', 'magic1', 5), ('magic2', 'magic2', 5), ('throw-paper', 'throw-paper', 5), ('finger-wag', 'finger-wag', 5))
sd = (('magic2', 'magic2', 5),
 ('speak', 'speak', 5),
 ('phone', 'phone', 5),
 ('magic3', 'magic3', 5),
 ('golf-club-swing', 'golf-club-swing', 5),
 ('throw-paper', 'throw-paper', 5))
le = (('speak', 'speak', 5),
 ('phone', 'phone', 5),
 ('magic3', 'magic3', 5),
 ('magic2', 'magic2', 5),
 ('pickpocket', 'pickpocket', 5),
 ('magic1', 'magic1', 5),
 ('effort', 'effort', 6))
bw = (('magic1', 'magic1', 5),
 ('magic2', 'magic2', 5),
 ('phone', 'phone', 5),
 ('throw-object', 'throw-object', 5),
 ('throw-paper', 'throw-paper', 5),
 ('magic3', 'magic3', 5),
 ('effort', 'effort', 6),
 ('smile', 'smile', 5),
 ('throw-paper', 'throw-paper', 5))
brv = (('finger-wag', 'finger-wag', 5), ('stomp', 'stomp', 5), ('quick-jump', 'jump', 6), ('magic1', 'magic1', 5))
sb = (('pickpocket', 'pickpocket', 5), ('magic3', 'magic3', 5), ('throw-paper', 'throw-paper', 5), ('throw-object', 'throw-object', 5))
cm = (('magic1', 'magic1', 5), ('throw-object', 'throw-object', 5), ('phone', 'phone', 5), ('throw-paper', 'throw-paper', 5), ('finger-wag', 'fingerwag', 5))
if not base.config.GetBool('want-new-cogs', 0):
    ModelDict = {'a': ('/models/char/suitA-', 4),
     'b': ('/models/char/suitB-', 4),
     'c': ('/models/char/suitC-', 3.5)}
    TutorialModelDict = {'a': ('/models/char/suitA-', 4),
     'b': ('/models/char/suitB-', 4),
     'c': ('/models/char/suitC-', 3.5)}
else:
    ModelDict = {'a': ('/models/char/tt_a_ene_cga_', 4),
     'b': ('/models/char/tt_a_ene_cgb_', 4),
     'c': ('/models/char/tt_a_ene_cgc_', 3.5)}
    TutorialModelDict = {'a': ('/models/char/tt_a_ene_cga_', 4),
     'b': ('/models/char/tt_a_ene_cgb_', 4),
     'c': ('/models/char/tt_a_ene_cgc_', 3.5)}
HeadModelDict = {'a': ('/models/char/suitA-', 4),
 'b': ('/models/char/suitB-', 4),
 'c': ('/models/char/suitC-', 3.5)}

def loadTutorialSuit():
    loader.loadModel('phase_3.5/models/char/suitC-mod').node()
    loadDialog(1)


def loadSuits(level):
    loadSuitModelsAndAnims(level, flag=1)
    loadDialog(level)


def unloadSuits(level):
    loadSuitModelsAndAnims(level, flag=0)
    unloadDialog(level)


def loadSuitModelsAndAnims(level, flag = 0):
    for key in ModelDict.keys():
        model, phase = ModelDict[key]
        if base.config.GetBool('want-new-cogs', 0):
            headModel, headPhase = HeadModelDict[key]
        else:
            headModel, headPhase = ModelDict[key]
        if flag:
            if base.config.GetBool('want-new-cogs', 0):
                filepath = 'phase_3.5' + model + 'zero'
                if cogExists(model + 'zero.bam'):
                    loader.loadModel(filepath).node()
            else:
                loader.loadModel('phase_3.5' + model + 'mod').node()
            loader.loadModel('phase_' + str(headPhase) + headModel + 'heads').node()
        else:
            if base.config.GetBool('want-new-cogs', 0):
                filepath = 'phase_3.5' + model + 'zero'
                if cogExists(model + 'zero.bam'):
                    loader.unloadModel(filepath)
            else:
                loader.unloadModel('phase_3.5' + model + 'mod')
            loader.unloadModel('phase_' + str(headPhase) + headModel + 'heads')


def cogExists(filePrefix):
    searchPath = DSearchPath()
    if AppRunnerGlobal.appRunner:
        searchPath.appendDirectory(Filename.expandFrom('$TT_3_5_ROOT/phase_3.5'))
    else:
        basePath = os.path.expandvars('$TTMODELS') or './ttmodels'
        searchPath.appendDirectory(Filename.fromOsSpecific(basePath + '/built/phase_3.5'))
    filePrefix = filePrefix.strip('/')
    pfile = Filename(filePrefix)
    found = vfs.resolveFilename(pfile, searchPath)
    if not found:
        return False
    return True


def loadSuitAnims(suit, flag = 1):
    if suit in SuitDNA.suitHeadTypes:
        try:
            animList = eval(suit)
        except NameError:
            animList = ()

    else:
        print 'Invalid suit name: ', suit
        return -1
    for anim in animList:
        phase = 'phase_' + str(anim[2])
        filePrefix = ModelDict[bodyType][0]
        animName = filePrefix + anim[1]
        if flag:
            loader.loadModel(animName).node()
        else:
            loader.unloadModel(animName)


def loadDialog(level):
    global SuitDialogArray
    if len(SuitDialogArray) > 0:
        return
    else:
        loadPath = 'phase_3.5/audio/dial/'
        SuitDialogFiles = ['COG_VO_grunt',
         'COG_VO_murmur',
         'COG_VO_statement',
         'COG_VO_question',
         'COG_VO_exclaim']
        for file in SuitDialogFiles:
            SuitDialogArray.append(base.loadSfx(loadPath + file + '.ogg'))

        SuitDialogArray.append(SuitDialogArray[2])
        SuitDialogArray.append(SuitDialogArray[2])


def loadSkelDialog():
    global SkelSuitDialogArray
    if len(SkelSuitDialogArray) > 0:
        return
    else:
        grunt = loader.loadSfx('phase_5/audio/sfx/Skel_COG_VO_grunt.ogg')
        murmur = loader.loadSfx('phase_5/audio/sfx/Skel_COG_VO_murmur.ogg')
        statement = loader.loadSfx('phase_5/audio/sfx/Skel_COG_VO_statement.ogg')
        question = loader.loadSfx('phase_5/audio/sfx/Skel_COG_VO_question.ogg')
        exclaim = loader.loadSfx('phase_5/audio/sfx/Skel_COG_VO_exclaim.ogg')
        SkelSuitDialogArray = [grunt,
         murmur,
         statement,
         question,
         exclaim,
         statement]


def unloadDialog(level):
    global SuitDialogArray
    SuitDialogArray = []


def unloadSkelDialog():
    global SkelSuitDialogArray
    SkelSuitDialogArray = []


def attachSuitHead(node, suitName):
    suitIndex = SuitDNA.suitHeadTypes.index(suitName)
    suitDNA = SuitDNA.SuitDNA()
    suitDNA.newSuit(suitName)
    suit = Suit()
    suit.setDNA(suitDNA)
    headParts = suit.getHeadParts()
    head = node.attachNewNode('head')
    for part in headParts:
        copyPart = part.copyTo(head)
        copyPart.setDepthTest(1)
        copyPart.setDepthWrite(1)

    suit.delete()
    suit = None
    p1 = Point3()
    p2 = Point3()
    head.calcTightBounds(p1, p2)
    d = p2 - p1
    biggest = max(d[0], d[2])
    column = suitIndex % SuitDNA.suitsPerDept
    s = (0.2 + column / 100.0) / biggest
    pos = -0.14 + (SuitDNA.suitsPerDept - column - 1) / 135.0
    head.setPosHprScale(0, 0, pos, 180, 0, 0, s, s, s)
    return head


class Suit(Avatar.Avatar):
    healthColors = (Vec4(0, 0.7, 0.9, 1),
	 Vec4(0, 0.6, 0.65, 1),
	 Vec4(0.5, 1, 0.6, 1),
	 Vec4(0, 1, 0, 1),
     Vec4(0.0, 0.0, 1.0, 1),
	 Vec4(0.5, 0.0, 1.0, 1),
	 Vec4(0.7, 0.0, 0.9, 1),
     Vec4(0.95, 0.95, 1, 1),
     Vec4(1, 0, 0, 1),
	 Vec4(0, 0, 0, 1),
     Vec4(0.3, 0.3, 0.3, 1),
     ToontownGlobals.CogImmuneColor)
    healthGlowColors = (Vec4(0, 0.7, 0.9, 1),
	 Vec4(0, 0.6, 0.65, 1),
	 Vec4(0.5, 1, 0.6, 1),
	 Vec4(0, 1, 0, 1),
     Vec4(0.25, 0.25, 1.0, 0.5),
	 Vec4(0.5, 0.0, 1.0, 1),
	 Vec4(0.7, 0.0, 0.9, 1),
     Vec4(0.95, 0.95, 1, 1),
     Vec4(1, 0, 0, 1),
	 Vec4(0, 0, 0, 1),
     Vec4(0.3, 0.3, 0.3, 1),
     ToontownGlobals.CogImmuneGlowColor)
    medallionColors = {'c': Vec4(0.863, 0.776, 0.769, 1.0),
     's': Vec4(0.843, 0.745, 0.745, 1.0),
     'l': Vec4(0.749, 0.776, 0.824, 1.0),
     'm': Vec4(0.749, 0.769, 0.749, 1.0)}

    def __init__(self):
        try:
            self.Suit_initialized
            return
        except:
            self.Suit_initialized = 1

        Avatar.Avatar.__init__(self)
        self.isVault = False
        self.isHat = False
        self.isHud = False
        self.setFont(ToontownGlobals.getSuitFont())
        self.setPlayerType(NametagGroup.CCSuit)
        self.setPickable(1)
        self.leftHand = None
        self.rightHand = None
        self.shadowJoint = None
        self.nametagJoint = None
        self.headParts = []
        self.healthBar = None
        self.healthCondition = 0
        self.isDisguised = 0
        self.isWaiter = 0
        self.isRental = 0
        self.isImmune = 0
        return

    def delete(self):
        try:
            self.Suit_deleted
        except:
            self.Suit_deleted = 1
            if self.leftHand:
                self.leftHand.removeNode()
                self.leftHand = None
            if self.rightHand:
                self.rightHand.removeNode()
                self.rightHand = None
            if self.shadowJoint:
                self.shadowJoint.removeNode()
                self.shadowJoint = None
            if self.nametagJoint:
                self.nametagJoint.removeNode()
                self.nametagJoint = None
            for part in self.headParts:
                part.removeNode()

            self.headParts = []
            self.removeHealthBar()
            Avatar.Avatar.delete(self)

        return

    def setHeight(self, height):
        Avatar.Avatar.setHeight(self, height)
        self.nametag3d.setPos(0, 0, height + 1.0)

    def getRadius(self):
        return 2

    def setDNAString(self, dnaString):
        self.dna = SuitDNA.SuitDNA()
        self.dna.makeFromNetString(dnaString)
        self.setDNA(self.dna)

    def setDNA(self, dna):
        if self.style:
            pass
        else:
            self.style = dna
            self.generateSuit()
            self.initializeDropShadow()
            self.initializeNametag3d()
            self.setBlend(frameBlend=True)

    def generateSuit(self):
        dna = self.style
        self.headParts = []
        self.headColor = None
        self.headTexture = None
        self.loseActor = None
        self.isSkeleton = 0
        self.isVirtual = 0
        self.isImmune = 0
        self.setBlend(frameBlend=True)
        if dna.name == 'f':
            self.scale = 4.0 / cSize
            self.handColor = VBase4(1.0, 0, 0, 1.0)
            self.generateBody()
            self.generateHead('gladhander')
            self.setHeight(4.88)
        elif dna.name == 'p':
            self.scale = 3.35 / bSize
            self.handColor = SuitDNA.corpPolyColor
            self.generateBody()
            self.generateHead('pencilpusher')
            self.setHeight(5.0)
        elif dna.name == 'ym':
            self.scale = 4.125 / aSize
            self.handColor = VBase4(1.0, 1.0, 0, 1.0)
            self.generateBody()
            self.generateHead('backstabber')
            self.setHeight(5.28)
        elif dna.name == 'mm':
            self.scale = 4.5 / bSize
            self.handColor = VBase4(1.0, 0, 0.2, 0.5)
            self.generateBody()
            self.headTexture = 'cat.jpg'
            self.generateHead('movershaker')
            self.setHeight(5.25)
        elif dna.name == 'ds':
            self.scale = 4.5 / aSize
            self.handColor = VBase4(0.8, 0.7, 0.7, 1.0)
            self.generateBody()
            self.generateHead('headhunter')
            self.generateHudStuff()
            self.setHeight(6.08)
        elif dna.name == 'hh':
            self.scale = 6.5 / bSize
            self.handColor = VBase4(0, 1.0, 0, 1.0)
            self.generateBody()
            self.headTexture = 'spin-doctor.jpg'
            self.generateHead('telemarketer')
            self.setHeight(7.45)
        elif dna.name == 'cr':
            self.scale = 6.75 / aSize
            self.handColor = VBase4(1.0, 0, 0, 1.0)
            self.generateBody()
            self.headTexture = 'halloween_mingler.jpg'
            self.generateHead('twoface')
            self.setHeight(8.23)
        elif dna.name == 'tbc':
            self.scale = 7.0 / aSize
            self.handColor = VBase4(0.95, 0.95, 1.0, 1.0)
            self.generateBody()
            self.generateHead('bigcheese')
            self.setHeight(9.34)
        elif dna.name == 'trb':
            self.scale = 6.05 / aSize
            self.handColor = VBase4(0, 0, 1.0, 1.0)
            self.generateBody()
            self.headTexture = 'rain.jpg'
            self.generateHead('numbercruncher')
            self.setHeight(7.53)
        elif dna.name == 'dot':
            self.scale = 6.75 / cSize
            self.handColor = VBase4(0, 1.0, 0, 1.0)
            self.headColor = VBase4(0.0, 1.0, 0.0, 1.0)
            self.generateBody()
            self.generateHead('Icosphere', 'phase_3.5/models/char/tomato.bam')
            self.setHeight(9.23)
        elif dna.name == 'kb':
            self.scale = 8.5 / aSize
            self.handColor = SuitDNA.corpPolyColor
            self.setPickable(0)
            self.generateBody()
            self.generateHead('yesman')
            self.makeSkeleton()
            self.setHeight(9.5)
            self.setTransparency(1)
            self.setColor(0, 0.5, 1, 1)
        elif dna.name == 'bf':
            self.scale = 4.0 / cSize
            self.handColor = SuitDNA.legalPolyColor
            self.generateBody()
            self.headTexture = 'bottom-feeder.jpg'
            self.generateHead('flunky')
            self.setHeight(4.81)
        elif dna.name == 'b':
            self.scale = 4.375 / bSize
            self.handColor = VBase4(0.95, 0.95, 1.0, 1.0)
            self.generateBody()
            self.headTexture = 'halloween_blood-sucker.jpg'
            self.generateHead('movershaker')
            self.setHeight(6.17)
        elif dna.name == 'dt':
            self.scale = 4.25 / aSize
            self.handColor = VBase4(1.0, 0.2, 0.4, 0.3)
            self.generateBody()
            self.headTexture = 'double-talker.jpg'
            self.generateHead('yesman')
            self.setHeight(5.63)
        elif dna.name == 'ac':
            self.scale = 1.25 / cSize
            self.handColor = SuitDNA.legalPolyColor
            self.generateBody()
            self.generateHead('micromanager')
            self.setHeight(1.89)
        elif dna.name == 'bs':
            self.scale = 4.5 / bSize
            self.handColor = VBase4(0, 1.0, 0.2, 1.0)
            self.generateBody()
            self.generateHead('beancounter')
            self.setHeight(6.71)
        elif dna.name == 'sd':
            self.scale = 5.65 / aSize
            self.handColor = VBase4(1.0, 0, 1.0, 1.0)
            self.generateBody()
            self.headTexture = 'software_simian.jpg'
            self.generateHead('numbercruncher')
            self.setHeight(7.9)
        elif dna.name == 'le':
            self.scale = 7.125 / aSize
            self.handColor = VBase4(0, 0, 0, 0)
            self.generateBody()
            self.headTexture = 'sun.jpg'
            self.generateHead('yesman')
            self.setHeight(8.27)
        elif dna.name == 'bw':
            self.scale = 7.0 / aSize
            self.handColor = SuitDNA.legalPolyColor
            self.generateBody()
            self.headTexture = 'diamond.jpg'
            self.generateHead('yesman')
            self.setHeight(8.69)
        elif dna.name == 'brv':
            self.scale = 5.75 / bSize
            self.handColor = VBase4(0, 0, 1.0, 1.0)
            self.generateBody()
            self.headTexture = 'bravester.jpg'
            self.generateHead('movershaker')
            self.setHeight(6.93)
        elif dna.name == 'sb':
            self.scale = 6.35 / bSize
            self.handColor = VBase4(1.0, 1.0, 1.0, 1.0)
            self.headColor = VBase4(0.0, 0.0, 0.0, 1.0)
            self.generateBody()
            self.generateHead('safe', 'phase_5/models/props/safe.bam')
            self.setHeight(8.13)
        elif dna.name == 'cm':
            self.scale = 7.5 / aSize
            self.handColor = SuitDNA.legalPolyColor
            self.setPickable(0)
            self.generateBody()
            self.generateHead('yesman')
            self.makeSkeleton()
            self.setTransparency(1)
            self.setColor(0, 1, 1, 1)
            self.setHeight(8.5)
        elif dna.name == 'sc':
            self.scale = 3.6 / cSize
            self.handColor = VBase4(1.0, 1.0, 0, 1.0)
            self.generateBody()
            self.headTexture = 'conartist.jpg'
            self.generateHead('coldcaller')
            self.setHeight(4.77)
        elif dna.name == 'pp':
            self.scale = 3.55 / bSize
            self.handColor = VBase4(1.0, 0.6, 0.5, 1.0)
            self.generateBody()
            self.generateHead('loanshark')
            self.setHeight(5.26)
        elif dna.name == 'tw':
            self.scale = 4.5 / aSize
            self.handColor = VBase4(0, 1.0, 0, 1.0)
            self.generateBody()
            self.headTexture = 'janet_lady.jpg'
            self.generateHead('yesman')
            self.setHeight(5.41)
        elif dna.name == 'bc':
            self.scale = 4.4 / bSize
            self.handColor = VBase4(1, 0.6, 0, 1.0)
            self.generateBody()
            self.generateHead('movershaker')
            self.setHeight(5.95)
        elif dna.name == 'nc':
            self.scale = 5.25 / aSize
            self.handColor = VBase4(1.0, 0, 0, 1.0)
            self.generateBody()
            self.generateHead('numbercruncher')
            self.setHeight(7.22)
        elif dna.name == 'mb':
            self.scale = 5.3 / aSize
            self.handColor = VBase4(0, 1.0, 0, 1.0)
            self.generateBody()
            self.headTexture = 'law-keeper.jpg'
            self.generateHead('twoface')
            self.setHeight(6.97)
        elif dna.name == 'ls':
            self.scale = 6.5 / bSize
            self.handColor = VBase4(0.95, 0.95, 1.0, 1.0)
            self.generateBody()
            self.headTexture = 'wizard-shaker.jpg'
            self.generateHead('movershaker')
            self.setHeight(8.58)
        elif dna.name == 'rb':
            self.scale = 7.0 / aSize
            self.handColor = VBase4(1.0, 0, 0, 1.0)
            self.generateBody()
            self.headTexture = 'careman.jpg'
            self.generateHead('yesman')
            self.setHeight(8.95)
        elif dna.name == 'gm':
            self.scale = 5.5 / aSize
            self.handColor = VBase4(0, 0, 1.0, 1.0)
            self.generateBody()
            self.headTexture = 'guilt.jpg'
            self.generateHead('Cone', 'phase_4/models/char/customCog.bam')
            self.setHeight(7.2)
        elif dna.name == 'ad':
            self.scale = 5.89 / bSize
            self.handColor = VBase4(0, 1.0, 0, 1.0)
            self.generateBody()
            self.headTexture = 'alfred.jpg'
            self.generateHead('Cylinder', 'phase_4/models/char/alfred.bam')
            self.setHeight(7.29)
        elif dna.name == 'dm':
            self.scale = 6.5 / bSize
            self.handColor = SuitDNA.moneyPolyColor
            self.setPickable(0)
            self.generateBody()
            self.generateHead('movershaker')
            self.makeSkeleton()
            self.setHeight(7.5)
            self.setTransparency(1)
            self.setColor(0, 1, 0.5, 1)
        elif dna.name == 'cc':
            self.scale = 3.5 / cSize
            self.handColor = VBase4(0.5, 0.4, 0.3, 0.1)
            self.headColor = VBase4(0.25, 0.35, 1.0, 1.0)
            self.generateBody()
            self.generateHead('coldcaller')
            self.setHeight(4.63)
        elif dna.name == 'tm':
            self.scale = 3.75 / bSize
            self.handColor = VBase4(0, 1.0, 0, 1.0)
            self.generateBody()
            self.generateHead('telemarketer')
            self.setHeight(5.24)
        elif dna.name == 'nd':
            self.scale = 4.35 / aSize
            self.handColor = VBase4(0.55, 0.65, 1.0, 1.0)
            self.generateBody()
            self.headTexture = 'mingler.jpg'
            self.generateHead('twoface')
            self.setHeight(5.98)
        elif dna.name == 'gh':
            self.scale = 4.75 / bSize
            self.handColor = VBase4(0.4, 0.1, 0, 0.3)
            self.generateBody()
            self.headTexture = 'installation-wizard.jpg'
            self.generateHead('movershaker')
            self.setHeight(6.4)
        elif dna.name == 'ms':
            self.scale = 4.75 / aSize
            self.handColor = VBase4(0, 0, 0, 0)
            self.generateBody()
            self.headTexture = 'halloween_name-dropper.jpg'
            self.generateHead('numbercruncher')
            self.setHeight(6.7)
        elif dna.name == 'tf':
            self.scale = 5.25 / aSize
            self.handColor = VBase4(0, 0.1, 0, 0.1)
            self.generateBody()
            self.headTexture = 'middleman.jpg'
            self.generateHead('twoface')
            self.setHeight(6.95)
        elif dna.name == 'm':
            self.scale = 5.75 / aSize
            self.handColor = VBase4(1.0, 1.0, 0, 1.0)
            self.generateBody()
            self.headTexture = 'blood-sucker.jpg'
            self.generateHead('yesman')
            self.setHeight(7.61)
        elif dna.name == 'mh':
            self.scale = 7.0 / aSize
            self.handColor = VBase4(1.0, 0.3, 0.2, 0.6)
            self.generateBody()
            self.generateHead('yesman')
            self.generateVaultStuff()
            self.setHeight(8.95)
        elif dna.name == 'ka':
            self.scale = 5.75 / aSize
            self.handColor = VBase4(0.5, 0, 1.0, 1.0)
            self.generateBody()
            self.headTexture = 'karen.jpg'
            self.generateHead('twoface')
            self.generateHatStuff()
            self.setHeight(7.61)
        elif dna.name == 'bbs':
            self.scale = 7.37 / aSize
            self.handColor = VBase4(1.0, 1.0, 1.0, 1.0)
            self.headColor = VBase4(0, 0, 0, 0)
            self.generateBody()
            self.headTexture = 'stardeath.jpg'
            self.generateHead('Sphere', 'phase_4/models/char/star.bam')
            self.setHeight(9.03)
        elif dna.name == 'fd':
            self.scale = 8.0 / aSize
            self.handColor = SuitDNA.salesPolyColor
            self.setPickable(0)
            self.generateBody()
            self.generateHead('yesman')
            self.makeSkeleton()
            self.setHeight(9)
            self.setTransparency(1)
            self.setColor(0, 0, 0, 1)
        self.setName(SuitBattleGlobals.SuitAttributes[dna.name]['name'])
        self.getGeomNode().setScale(self.scale)
        self.generateHealthBar()
        if self.isSkeleton:
            pass
        else:
            self.generateCorporateMedallion()
        return

    def generateBody(self):
        animDict = self.generateAnimDict()
        filePrefix, bodyPhase = ModelDict[self.style.body]
        if base.config.GetBool('want-new-cogs', 0):
            if cogExists(filePrefix + 'zero.bam'):
                self.loadModel('phase_3.5' + filePrefix + 'zero')
            else:
                self.loadModel('phase_3.5' + filePrefix + 'mod')
        else:
            self.loadModel('phase_3.5' + filePrefix + 'mod')
        self.loadAnims(animDict)
        self.setSuitClothes()
		
    def generateSkelSuit(self):
        dna = self.style
        self.headParts = []
        self.headColor = None
        self.headTexture = None
        self.loseActor = None
        self.isSkeleton = 1

        if dna.name in SuitGlobals.suitProperties:
            self.scale = SuitGlobals.suitProperties[dna.name][SuitGlobals.SCALE_INDEX]
               
            print 'b4 skelbody'
            self.generateSkelBody()
            print 'after skelbody'

            self.setHeight(SuitGlobals.suitProperties[dna.name][SuitGlobals.HEIGHT_INDEX])

        self.setName(SuitBattleGlobals.SuitAttributes[dna.name]['name'])
        self.getGeomNode().setScale(self.scale)
        print 'b4 geomnode'
        self.generateHealthBar()
        print 'genHealth'
        self.generateCorporateMedallion()
        print 'genCorp'
        self.generateCorporateTie()
        print 'genTie'
        self.setBlend(frameBlend=True)
        
    def generateSkelBody(self):
        global Preloaded
        animDict = self.generateAnimDict()
        filePrefix, bodyPhase = ModelDict[self.style.body]
        filepath = 'phase_5/models/char/cog' + string.upper(self.style.body) + '_robot-zero'
        self.loadModel(Preloaded[filepath], copy = True)
        self.loadAnims(animDict)
        parts = self.findAllMatches('**/pPlane*')
        for partNum in xrange(0, parts.getNumPaths()):
            bb = parts.getPath(partNum)
            bb.setTwoSided(1)
        self.setBlend(frameBlend=True)

    def generateAnimDict(self):
        animDict = {}
        filePrefix, bodyPhase = ModelDict[self.style.body]
        for anim in AllSuits:
            animDict[anim[0]] = 'phase_' + str(bodyPhase) + filePrefix + anim[1]

        for anim in AllSuitsMinigame:
            animDict[anim[0]] = 'phase_4' + filePrefix + anim[1]

        for anim in AllSuitsTutorialBattle:
            filePrefix, bodyPhase = TutorialModelDict[self.style.body]
            animDict[anim[0]] = 'phase_' + str(bodyPhase) + filePrefix + anim[1]

        for anim in AllSuitsBattle:
            animDict[anim[0]] = 'phase_5' + filePrefix + anim[1]

        if not base.config.GetBool('want-new-cogs', 0):
            if self.style.body == 'a':
                animDict['neutral'] = 'phase_4/models/char/suitA-neutral'
                for anim in SuitsCEOBattle:
                    animDict[anim[0]] = 'phase_12/models/char/suitA-' + anim[1]

            elif self.style.body == 'b':
                animDict['neutral'] = 'phase_4/models/char/suitB-neutral'
                for anim in SuitsCEOBattle:
                    animDict[anim[0]] = 'phase_12/models/char/suitB-' + anim[1]

            elif self.style.body == 'c':
                animDict['neutral'] = 'phase_3.5/models/char/suitC-neutral'
                for anim in SuitsCEOBattle:
                    animDict[anim[0]] = 'phase_12/models/char/suitC-' + anim[1]

        try:
            animList = eval(self.style.name)
        except NameError:
            animList = ()

        for anim in animList:
            phase = 'phase_' + str(anim[2])
            animDict[anim[0]] = phase + filePrefix + anim[1]

        return animDict

    def initializeBodyCollisions(self, collIdStr):
        Avatar.Avatar.initializeBodyCollisions(self, collIdStr)
        if not self.ghostMode:
            self.collNode.setCollideMask(self.collNode.getIntoCollideMask() | ToontownGlobals.PieBitmask)

    def setSuitClothes(self, modelRoot = None):
        if not modelRoot:
            modelRoot = self
        dept = self.style.dept
        phase = 3.5

        def __doItTheOldWay__():
            torsoTex = loader.loadTexture('phase_%s/maps/%s_blazer.jpg' % (phase, dept))
            torsoTex.setMinfilter(Texture.FTLinearMipmapLinear)
            torsoTex.setMagfilter(Texture.FTLinear)
            legTex = loader.loadTexture('phase_%s/maps/%s_leg.jpg' % (phase, dept))
            legTex.setMinfilter(Texture.FTLinearMipmapLinear)
            legTex.setMagfilter(Texture.FTLinear)
            armTex = loader.loadTexture('phase_%s/maps/%s_sleeve.jpg' % (phase, dept))
            armTex.setMinfilter(Texture.FTLinearMipmapLinear)
            armTex.setMagfilter(Texture.FTLinear)
            modelRoot.find('**/torso').setTexture(torsoTex, 1)
            modelRoot.find('**/arms').setTexture(armTex, 1)
            modelRoot.find('**/legs').setTexture(legTex, 1)
            modelRoot.find('**/hands').setColor(self.handColor)
            self.leftHand = self.find('**/joint_Lhold')
            self.rightHand = self.find('**/joint_Rhold')
            self.shadowJoint = self.find('**/joint_shadow')
            self.nametagJoint = self.find('**/joint_nameTag')

        if base.config.GetBool('want-new-cogs', 0):
            if dept == 'c':
                texType = 'bossbot'
            elif dept == 'm':
                texType = 'cashbot'
            elif dept == 'l':
                texType = 'lawbot'
            elif dept == 's':
                texType = 'sellbot'
            if self.find('**/body').isEmpty():
                __doItTheOldWay__()
            else:
                filepath = 'phase_3.5/maps/tt_t_ene_' + texType + '.jpg'
                if cogExists('/maps/tt_t_ene_' + texType + '.jpg'):
                    bodyTex = loader.loadTexture(filepath)
                    self.find('**/body').setTexture(bodyTex, 1)
                self.leftHand = self.find('**/def_joint_left_hold')
                self.rightHand = self.find('**/def_joint_right_hold')
                self.shadowJoint = self.find('**/def_shadow')
                self.nametagJoint = self.find('**/def_nameTag')
        else:
            __doItTheOldWay__()

    def makeWaiter(self, modelRoot = None):
        if not modelRoot:
            modelRoot = self
        self.isWaiter = 1
        torsoTex = loader.loadTexture('phase_3.5/maps/waiter_m_blazer.jpg')
        torsoTex.setMinfilter(Texture.FTLinearMipmapLinear)
        torsoTex.setMagfilter(Texture.FTLinear)
        legTex = loader.loadTexture('phase_3.5/maps/waiter_m_leg.jpg')
        legTex.setMinfilter(Texture.FTLinearMipmapLinear)
        legTex.setMagfilter(Texture.FTLinear)
        armTex = loader.loadTexture('phase_3.5/maps/waiter_m_sleeve.jpg')
        armTex.setMinfilter(Texture.FTLinearMipmapLinear)
        armTex.setMagfilter(Texture.FTLinear)
        modelRoot.find('**/torso').setTexture(torsoTex, 1)
        modelRoot.find('**/arms').setTexture(armTex, 1)
        modelRoot.find('**/legs').setTexture(legTex, 1)
		
    def makeVirtual(self, modelRoot = None):
        if not modelRoot:
            modelRoot = self
        self.isVirtual = 3
        actorNode = self.find('**/__Actor_modelRoot')
        actorCollection = actorNode.findAllMatches('*')
        parts = ()
        for thingIndex in range(0, actorCollection.getNumPaths()):
            thing = actorCollection[thingIndex]
            if thing.getName() not in ('joint_attachMeter', 'joint_nameTag', 'def_nameTag'):
                thing.setColorScale(0.2, 0.3, 1.0, 1.0)
                thing.setAttrib(ColorBlendAttrib.make(ColorBlendAttrib.MAdd))
                thing.setDepthWrite(False)
                thing.setBin('fixed', 1)
        self.find('**/joint_shadow').hide()
        self.isVirtuallyVirtual = True

    def makeRentalSuit(self, suitType, modelRoot = None):
        if not modelRoot:
            modelRoot = self.getGeomNode()
        if suitType == 's':
            torsoTex = loader.loadTexture('phase_3.5/maps/tt_t_ene_sellbotRental_blazer.jpg')
            legTex = loader.loadTexture('phase_3.5/maps/tt_t_ene_sellbotRental_leg.jpg')
            armTex = loader.loadTexture('phase_3.5/maps/tt_t_ene_sellbotRental_sleeve.jpg')
            handTex = loader.loadTexture('phase_3.5/maps/tt_t_ene_sellbotRental_hand.jpg')
        else:
            self.notify.warning('No rental suit for cog type %s' % suitType)
            return
        self.isRental = 1
        modelRoot.find('**/torso').setTexture(torsoTex, 1)
        modelRoot.find('**/arms').setTexture(armTex, 1)
        modelRoot.find('**/legs').setTexture(legTex, 1)
        modelRoot.find('**/hands').setTexture(handTex, 1)

    def generateHead(self, headType, modelOverride = None):
        if base.config.GetBool('want-new-cogs', 0):
            filePrefix, phase = HeadModelDict[self.style.body]
        else:
            filePrefix, phase = ModelDict[self.style.body]
        if modelOverride:
            headModel = loader.loadModel(modelOverride)
        else:
            headModel = loader.loadModel('phase_' + str(phase) + filePrefix + 'heads')
        headReferences = headModel.findAllMatches('**/' + headType)
        for i in range(0, headReferences.getNumPaths()):
            if self.style.body == 'a' or self.style.body == 'b':
                headPart = self.instance(headReferences.getPath(i), 'modelRoot', 'to_head')
            else:
                headPart = self.instance(headReferences.getPath(i), 'modelRoot', 'joint_head')
            if self.headTexture:
                headTex = loader.loadTexture('phase_' + str(phase) + '/maps/' + self.headTexture)
                headTex.setMinfilter(Texture.FTLinearMipmapLinear)
                headTex.setMagfilter(Texture.FTLinear)
                headPart.setTexture(headTex, 1)
            if self.headColor:
                headPart.setColor(self.headColor)
            if headType == 'Cone':
                headPart.setH(180)
                headPart.setY(0)
                headPart.setZ(0.7)
                headPart.setScale(0.87)
            elif headType == 'safe':
                headPart.setH(180)
                headPart.setX(0)
                headPart.setY(0)
                headPart.setZ(0)
                headPart.setScale(0.57)
            elif headType == 'Cylinder':
                headPart.setH(3.8)
                headPart.setX(0)
                headPart.setY(0)
                headPart.setZ(0.7)
                headPart.setScale(0.87)
            elif headType == 'Icosphere':
                headPart.setH(180)
                headPart.setX(0)
                headPart.setY(0)
                headPart.setZ(0.7)
                headPart.setScale(1.57)
            elif headType == 'Sphere':
                headPart.setH(180)
                headPart.setX(0)
                headPart.setY(0)
                headPart.setZ(0.2)
                headPart.setScale(0.87)
                headPart.setBillboardPointEye()
            self.headParts.append(headPart)

        headModel.removeNode()

    def generateCorporateTie(self, modelPath = None):
        if not modelPath:
            modelPath = self
        dept = self.style.dept
        tie = modelPath.find('**/tie')
        if tie.isEmpty():
            self.notify.warning('skelecog has no tie model!!!')
            return
        if dept == 'c':
            tieTex = loader.loadTexture('phase_5/maps/cog_robot_tie_boss.jpg')
        elif dept == 's':
            tieTex = loader.loadTexture('phase_5/maps/cog_robot_tie_sales.jpg')
        elif dept == 'l':
            tieTex = loader.loadTexture('phase_5/maps/cog_robot_tie_legal.jpg')
        elif dept == 'm':
            tieTex = loader.loadTexture('phase_5/maps/cog_robot_tie_money.jpg')
        tieTex.setMinfilter(Texture.FTLinearMipmapLinear)
        tieTex.setMagfilter(Texture.FTLinear)
        tie.setTexture(tieTex, 1)

    def generateCorporateMedallion(self):
        icons = loader.loadModel('phase_3/models/gui/cog_icons')
        dept = self.style.dept
        if base.config.GetBool('want-new-cogs', 0):
            chestNull = self.find('**/def_joint_attachMeter')
            if chestNull.isEmpty():
                chestNull = self.find('**/joint_attachMeter')
        else:
            chestNull = self.find('**/joint_attachMeter')
        if dept == 'c':
            self.corpMedallion = icons.find('**/CorpIcon').copyTo(chestNull)
        elif dept == 's':
            self.corpMedallion = icons.find('**/SalesIcon').copyTo(chestNull)
        elif dept == 'l':
            self.corpMedallion = icons.find('**/LegalIcon').copyTo(chestNull)
        elif dept == 'm':
            self.corpMedallion = icons.find('**/MoneyIcon').copyTo(chestNull)
        self.corpMedallion.setPosHprScale(0.02, 0.05, 0.04, 180.0, 0.0, 0.0, 0.51, 0.51, 0.51)
        self.corpMedallion.setColor(self.medallionColors[dept])
        icons.removeNode()

    def generateHealthBar(self):
        self.removeHealthBar()
        model = loader.loadModel('phase_3.5/models/gui/matching_game_gui')
        button = model.find('**/minnieCircle')
        button.setScale(3.0)
        button.setH(180.0)
        button.setColor(self.healthColors[0])
        if base.config.GetBool('want-new-cogs', 0):
            chestNull = self.find('**/def_joint_attachMeter')
            if chestNull.isEmpty():
                chestNull = self.find('**/joint_attachMeter')
        else:
            chestNull = self.find('**/joint_attachMeter')
        button.reparentTo(chestNull)
        if self.isImmune == 1:
            button.setColor(self.healthColors[5])
        self.healthBar = button
        glow = BattleProps.globalPropPool.getProp('glow')
        glow.reparentTo(self.healthBar)
        glow.setScale(0.28)
        glow.setPos(-0.005, 0.01, 0.015)
        glow.setColor(self.healthGlowColors[0])
        if self.isImmune == 1:
            glow.setColor(self.healthGlowColors[5])
        button.flattenLight()
        self.healthBarGlow = glow
        self.healthBar.hide()
        self.healthCondition = 0

    def resetHealthBarForSkele(self):
        self.healthBar.setPos(0.0, 0.1, 0.0)

    def updateHealthBar(self, hp, forceUpdate = 0):
        if hp > self.currHP:
            hp = self.currHP
        self.currHP -= hp
        health = float(self.currHP) / float(self.maxHP)
        if self.isImmune != 1:
            if health > 0.95:
                condition = 0
            elif health > 0.9:
                condition = 1
            elif health > 0.8:
                condition = 2
            elif health > 0.7:
                condition = 3
            elif health > 0.6:
                condition = 4
            elif health > 0.5:
                condition = 5
            elif health > 0.3:
                condition = 6
            elif health > 0.15:
                condition = 7
            elif health > 0.10:
                condition = 8
            elif health > 0.5:
                condition = 9
            elif health > 0.0:
                condition = 10
            else:
                condition = 11
        elif self.isImmune == 1:
            condition = 6
        if self.healthCondition != condition or forceUpdate:
            if condition == 10:
                blinkTask = Task.loop(Task(self.__blinkRed), Task.pause(0.75), Task(self.__blinkGray), Task.pause(0.1))
                taskMgr.add(blinkTask, self.uniqueName('blink-task'))
            elif condition == 11:
                if self.healthCondition == 10:
                    taskMgr.remove(self.uniqueName('blink-task'))
                blinkTask = Task.loop(Task(self.__blinkRed), Task.pause(0.25), Task(self.__blinkGray), Task.pause(0.1))
                taskMgr.add(blinkTask, self.uniqueName('blink-task'))
            else:
                if not self.isImmune:
                    self.healthBar.setColor(self.healthColors[condition], 1)
                    self.healthBarGlow.setColor(self.healthGlowColors[condition], 1)
                else:
                    self.healthBar.setColor(self.healthColors[10], 1)
                    self.healthBarGlow.setColor(self.healthGlowColors[10], 1)
            self.healthCondition = condition

    def __blinkRed(self, task):
        self.healthBar.setColor(self.healthColors[9], 1)
        self.healthBarGlow.setColor(self.healthGlowColors[9], 1)
        if self.healthCondition == 11:
            self.healthBar.setScale(1.17)
        return Task.done

    def __blinkGray(self, task):
        if not self.healthBar:
            return
        self.healthBar.setColor(self.healthColors[10], 1)
        self.healthBarGlow.setColor(self.healthGlowColors[10], 1)
        if self.healthCondition == 11:
            self.healthBar.setScale(1.0)
        return Task.done

    def removeHealthBar(self):
        if self.healthBar:
            self.healthBar.removeNode()
            self.healthBar = None
        if self.healthCondition == 10 or self.healthCondition == 11:
            taskMgr.remove(self.uniqueName('blink-task'))
        self.healthCondition = 0
        return

    def getLoseActor(self):
        if base.config.GetBool('want-new-cogs', 0):
            if self.find('**/body'):
                return self
        if self.loseActor == None:
            if not self.isSkeleton:
                filePrefix, phase = TutorialModelDict[self.style.body]
                loseModel = 'phase_' + str(phase) + filePrefix + 'lose-mod'
                loseAnim = 'phase_' + str(phase) + filePrefix + 'lose'
                self.loseActor = Actor.Actor(loseModel, {'lose': loseAnim})
                loseNeck = self.loseActor.find('**/joint_head')
                for part in self.headParts:
                    part.instanceTo(loseNeck)

                if self.isWaiter:
                    self.makeWaiter(self.loseActor)
                else:
                    self.setSuitClothes(self.loseActor)
            else:
                loseModel = 'phase_5/models/char/cog' + string.upper(self.style.body) + '_robot-lose-mod'
                filePrefix, phase = TutorialModelDict[self.style.body]
                loseAnim = 'phase_' + str(phase) + filePrefix + 'lose'
                self.loseActor = Actor.Actor(loseModel, {'lose': loseAnim})
                self.generateCorporateTie(self.loseActor)
        if self.isVirtual:
            actorNode = self.loseActor.find('**/__Actor_modelRoot')
            actorCollection = actorNode.findAllMatches('*')
            parts = ()
            for thingIndex in range(0, actorCollection.getNumPaths()):
                thing = actorCollection[thingIndex]
                if thing.getName() not in ('joint_attachMeter', 'joint_nameTag', 'def_nameTag'):
                    thing.setColorScale(0.2, 0.3, 1.0, 1.0)
                    thing.setAttrib(ColorBlendAttrib.make(ColorBlendAttrib.MAdd))
                    thing.setDepthWrite(False)
                    thing.setBin('fixed', 1)
            self.loseActor.find('**/joint_shadow').hide()
        self.loseActor.setBlend(frameBlend=True)
        self.loseActor.setScale(self.scale)
        self.loseActor.setPos(self.getPos())
        self.loseActor.setHpr(self.getHpr())
        shadowJoint = self.loseActor.find('**/joint_shadow')
        dropShadow = loader.loadModel('phase_3/models/props/drop_shadow')
        dropShadow.setScale(0.45)
        dropShadow.setColor(0.0, 0.0, 0.0, 0.5)
        dropShadow.reparentTo(shadowJoint)
        self.loseActor.setBlend(frameBlend=True)
        return self.loseActor

    def cleanupLoseActor(self):
        self.notify.debug('cleanupLoseActor()')
        if self.loseActor != None:
            self.notify.debug('cleanupLoseActor() - got one')
            self.loseActor.cleanup()
        self.loseActor = None
        return

    def makeIntoImmune(self):
        self.isImmune = 1
        self.healthBar.setColor(self.healthColors[5])
        self.healthBarGlow.setColor(self.healthGlowColors[5])

    def removeImmune(self):
        self.isImmune = 0
        self.healthBar.setColor(self.healthColors[0])
        self.healthBarGlow.setColor(self.healthGlowColors[0])

    def makeSkeleton(self):
        model = 'phase_5/models/char/cog' + string.upper(self.style.body) + '_robot-zero'
        anims = self.generateAnimDict()
        anim = self.getCurrentAnim()
        dept = self.style.dept
        self.removePart('modelRoot')
        self.loadModel(model)
        self.loadAnims(anims)
        self.getGeomNode().setScale(self.scale * 1.0173)
        self.generateHealthBar()
        self.generateCorporateMedallion()
        self.generateCorporateTie()
        self.setHeight(self.height)
        parts = self.findAllMatches('**/pPlane*')
        for partNum in xrange(0, parts.getNumPaths()):
            bb = parts.getPath(partNum)
            bb.setTwoSided(1)

    
        self.setName(TTLocalizer.Skeleton)
        nameInfo = TTLocalizer.SuitBaseNameWithLevel % {'name': self._name,
         'dept': self.getStyleDept(),
         'level': self.getActualLevel()}
        self.setDisplayName(nameInfo)
        self.leftHand = self.find('**/joint_Lhold')
        self.rightHand = self.find('**/joint_Rhold')
        self.nametagNull = self.find('**/joint_nameTag')
        self.loop(anim)
        self.isSkeleton = 1
        self.setBlend(frameBlend=True)

    def getHeadParts(self):
        return self.headParts

    def getRightHand(self):
        return self.rightHand

    def getLeftHand(self):
        return self.leftHand

    def getShadowJoint(self):
        return self.shadowJoint

    def getNametagJoints(self):
        return []

    def getDialogueArray(self):
        if self.isSkeleton:
            loadSkelDialog()
            return SkelSuitDialogArray
        else:
            return SuitDialogArray

    def getStyleDept(self):
        if hasattr(self, 'dna') and self.dna:
            return SuitDNA.getDeptFullname(self.dna.dept)
            
    def getActualLevel(self):
        if hasattr(self, 'dna'):
            return SuitBattleGlobals.getActualFromRelativeLevel(self.getStyleName(), self.level) + 1
        else:
            self.notify.warning('called getActualLevel with no DNA, returning 1 for level')
            return 1
            
    def getStyleName(self):
        if hasattr(self, 'dna') and self.dna:
            return self.dna.name
        else:
            self.notify.error('called getStyleName() before dna was set!')
            return 'unknown'
			
    def generateVaultStuff(self):
        self.Vault = loader.loadModel('phase_4/models/accessories/tt_m_chr_avt_acc_msk_narrowGlasses')
        self.Vault.reparentTo(self.find('**/joint_head'))
        self.Vault.setScale(0.4, 0.4, 0.4)
        self.Vault.setPosHpr(0, 0, 0.70, 180, -20, 0)
        self.Vault.setZ(0.7)
        self.isVault = True
		
    def generateHatStuff(self):
        self.Vault = loader.loadModel('phase_4/models/accessories/tt_m_chr_avt_acc_hat_ribbon')
        self.Vault.reparentTo(self.find('**/joint_head'))
        self.Vault.setScale(0.4, 0.4, 0.4)
        self.Vault.setPosHpr(0, 0, 0.70, 180, -20, 0)
        self.Vault.setZ(1.4)
        self.isHat = True
		
    def generateHudStuff(self):
        self.Vault = loader.loadModel('phase_4/models/accessories/tt_m_chr_avt_acc_hat_crown')
        self.Vault.reparentTo(self.find('**/joint_head'))
        self.Vault.setScale(0.5, 0.5, 0.5)
        self.Vault.setPosHpr(0, 0, 0.70, 180, -20, 0)
        self.Vault.setZ(0.5)
        self.isHud = True