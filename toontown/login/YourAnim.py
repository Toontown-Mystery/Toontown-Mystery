from direct.gui.DirectGui import OnscreenImage, DirectLabel, DirectButton, OnscreenText
import AvatarChooser
from panda3d.core import *
from direct.interval.IntervalGlobal import *
from libotp import *
from direct.task import Task
from direct.fsm import StateData
from direct.fsm import ClassicFSM, State
from direct.fsm import State
from direct.directnotify import DirectNotifyGlobal
from toontown.launcher import DownloadForceAcknowledge
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.ClockDelta import globalClockDelta
from direct.showbase import PythonUtil
from direct.task import Task
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from panda3d.toontown import DNAStorage
from toontown.toon import NPCToons
from toontown.suit import Suit
from toontown.suit import SuitDNA
from toontown.battle import BattleProps
class YourAnim():

    def __init__(self, leaveFunction):
        self.karenintro = base.loader.loadMusic('phase_9/audio/bgm/encntr_factory.ogg')
        self.karenbattle = base.loader.loadMusic('phase_7/audio/bgm/encntr_general_bg_indoor.ogg')
        self.karendefeat = base.loader.loadMusic('phase_9/audio/bgm/Victory_dance.ogg')
        
    def create(self):
        self.dnaStore = DNAStorage()
        loader.loadDNAFile(self.dnaStore, 'phase_8/dna/storage_BR.dna')
        loader.loadDNAFile(self.dnaStore, 'phase_8/dna/storage_BR_sz.dna')
        loader.loadDNAFile(self.dnaStore, 'phase_8/dna/storage_BR_town.dna')
        loader.loadDNAFile(self.dnaStore, 'phase_4/dna/storage.dna')
        loader.loadDNAFile(self.dnaStore, 'phase_5/dna/storage_town.dna')
        self.BR = loader.loadDNAFile(self.dnaStore, 'phase_8/dna/the_burrrgh_sz.dna')
        render.attachNewNode(self.BR)
        self.TTSky = loader.loadModel('phase_3.5/models/props/TT_sky.bam')
        self.TTSky.reparentTo(render)
        base.oobe()
        
        self.toon = NPCToons.createLocalNPC(555)
        self.toon.pose('throw', 30)
        self.toon.setPos(-5, -45, 6.3)
        self.toon.reparentTo(render)

        self.BombProp = loader.loadModel('phase_5/models/props/birthday-cake-mod.bam')
        self.BombProp.setPos(-5, -43, 7)
        self.BombProp.reparentTo(render)
        
        camera.setPos(3, -40, 7)
        
        self.nametagJ = None
        self.nametagS = None
        self.nametagJ = NametagGroup()
        self.nametagJ.setAvatar(self.toon)
        self.nametagJ.setFont(ToontownGlobals.getToonFont())
        self.nametagJ.setName('')
        self.nametagJ.manage(base.marginManager)
        self.nametagJ.getNametag3d().setBillboardOffset(4)
        nametagNode = self.nametagJ.getNametag3d().upcastToPandaNode()
        self.nametagS = self.toon.attachNewNode(nametagNode)
        self.nametagS.setPos(0, 0, 3.5)
        
        self.Karen = Suit.Suit()
        self.Karen.dna = SuitDNA.SuitDNA()
        self.Karen.dna.newSuit('ka')
        self.Karen.setDNA(self.Karen.dna)
        self.Karen.setPos(3, -45, 6.3)
        self.Karen.pose('glower', 30)
        self.Karen.reparentTo(render)
        self.Karen = self.Karen
        
        self.nametagJ2 = None
        self.nametagS2 = None
        self.nametagJ2 = NametagGroup()
        self.nametagJ2.setAvatar(self.Karen)
        self.nametagJ2.setFont(ToontownGlobals.getToonFont())
        self.nametagJ2.setName('')
        self.nametagJ2.manage(base.marginManager)
        self.nametagJ2.getNametag3d().setBillboardOffset(4)
        nametagNode2 = self.nametagJ2.getNametag3d().upcastToPandaNode()
        self.nametagS2 = self.Karen.attachNewNode(nametagNode2)
        self.nametagS2.setPos(0, 0, 8)

        
        GoodTrack = Sequence()
        GoodTrack.start()