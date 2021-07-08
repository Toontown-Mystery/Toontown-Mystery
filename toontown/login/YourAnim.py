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
        self.cogVariable = loader.loadModel('phase_11/models/lawbotHQ/LB_DA_Lobby.bam')
        self.cogVariable.reparentTo(render)
        base.oobe()

        self.Elevator2Prop = loader.loadModel('phase_5/models/props/birthday-cake-mod.bam')
        self.Elevator2Prop.setPos(-4, 0, 33.9)
        self.Elevator2Prop.setScale(0.7)
        self.Elevator2Prop.reparentTo(render)

        self.ElevatorProp = loader.loadModel('phase_5.5/models/estate/UWtable.bam')
        self.ElevatorProp.setPos(-4, 0, 32)
        self.ElevatorProp.setScale(0.6)
        self.ElevatorProp.reparentTo(render)
        
        self.toon = NPCToons.createLocalNPC(755)
        self.toon.pose('victory', 115)
        self.toon.setPos(-4, -3, 32)
        self.toon.setHpr(0, 0, 0)
        self.toon.setScale(1.3)
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
        
        camera.setPos(0, 20, 35)

        self.cogRoomSfx = base.loader.loadSfx('phase_3.5/audio/dial/go_to_your_room.ogg')
        self.cogWrongSfx = base.loader.loadSfx('phase_3.5/audio/dial/not_wrong.ogg')
        self.cogNothingSfx = base.loader.loadSfx('phase_3.5/audio/dial/nothing.ogg')
        self.cogWaSfx = base.loader.loadSfx('phase_3.5/audio/dial/wa.ogg')

        
        GoodTrack = Sequence()
        GoodTrack.start()