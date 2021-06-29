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
        self.coolintro = base.loader.loadMusic('phase_4/audio/bgm/building_shop.ogg')
        
    def create(self):
        self.cogVariable = loader.loadModel('phase_9/models/cogHQ/BossRoomHQ.bam')
        self.cogVariable.reparentTo(render)
        base.oobe()

        self.Elevator2Prop = loader.loadModel('phase_5/models/cogdominium/tt_m_ara_csa_elevator.bam')
        self.Elevator2Prop.setPos(0, 75, 16)
        self.Elevator2Prop.setHpr(0, 0, 0)
        self.Elevator2Prop.setScale(3.5)
        self.Elevator2Prop.reparentTo(render)
        
        self.toon = NPCToons.createLocalNPC(753)
        self.toon.pose('angry', 30)
        self.toon.setPos(-4, -30, 0)
        self.toon.setHpr(270, 0, 0)
        self.toon.reparentTo(render)
        
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
        self.nametagS.setPos(0, 0, 4.5)
        
        self.toon2 = NPCToons.createLocalNPC(754)
        self.toon2.pose('cringe', 30)
        self.toon2.setPos(4, -30, 0)
        self.toon2.setHpr(180, 0, 0)
        self.toon2.reparentTo(render)
        
        self.nametagJ2 = None
        self.nametagS2 = None
        self.nametagJ2 = NametagGroup()
        self.nametagJ2.setAvatar(self.toon2)
        self.nametagJ2.setFont(ToontownGlobals.getToonFont())
        self.nametagJ2.setName('')
        self.nametagJ2.manage(base.marginManager)
        self.nametagJ2.getNametag3d().setBillboardOffset(4)
        nametagNode2 = self.nametagJ2.getNametag3d().upcastToPandaNode()
        self.nametagS2 = self.toon2.attachNewNode(nametagNode2)
        self.nametagS2.setPos(0, 0, 3.8)
        
        camera.setPos(0, 20, 35)

        self.cogRoomSfx = base.loader.loadSfx('phase_3.5/audio/dial/go_to_your_room.ogg')
        self.cogWrongSfx = base.loader.loadSfx('phase_3.5/audio/dial/not_wrong.ogg')
        self.cogNothingSfx = base.loader.loadSfx('phase_3.5/audio/dial/nothing.ogg')
        self.cogWaSfx = base.loader.loadSfx('phase_3.5/audio/dial/wa.ogg')

        
        GoodTrack = Sequence()
        GoodTrack.start()