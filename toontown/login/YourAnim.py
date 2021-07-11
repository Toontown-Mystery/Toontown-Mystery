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
        self.mixsong = base.loader.loadMusic('phase_3.5/audio/bgm/MeowMix.ogg')
        
    def create(self):
        self.cogVariable = loader.loadModel('phase_10/models/cogHQ/MidVault.bam')
        self.cogVariable.reparentTo(render)
        
        self.Angel = Suit.Suit()
        self.Angel.dna = SuitDNA.SuitDNA()
        self.Angel.dna.newSuit('ls')
        self.Angel.setDNA(self.Angel.dna)
        self.Angel.setPos(120, 15, 71)
        self.Angel.setHpr(180, 0, 0)
        self.Angel.loop('neutral')
        self.Angel.reparentTo(render)
        self.Angel = self.Angel
        
        self.nametagJ = None
        self.nametagS = None
        self.nametagJ = NametagGroup()
        self.nametagJ.setAvatar(self.Angel)
        self.nametagJ.setFont(ToontownGlobals.getToonFont())
        self.nametagJ.setName('')
        self.nametagJ.manage(base.marginManager)
        self.nametagJ.getNametag3d().setBillboardOffset(4)
        nametagNode = self.nametagJ.getNametag3d().upcastToPandaNode()
        self.nametagS = self.Angel.attachNewNode(nametagNode)
        self.nametagS.setPos(0, 0, 9.5)

        self.Amanda = Suit.Suit()
        self.Amanda.dna = SuitDNA.SuitDNA()
        self.Amanda.dna.newSuit('mh')
        self.Amanda.setDNA(self.Amanda.dna)
        self.Amanda.setPos(120, -30, 71)
        self.Amanda.setHpr(0, 0, 0)
        self.Amanda.loop('neutral')
        self.Amanda.reparentTo(render)
        self.Amanda = self.Amanda
        
        self.nametagJ2 = None
        self.nametagS2 = None
        self.nametagJ2 = NametagGroup()
        self.nametagJ2.setAvatar(self.Amanda)
        self.nametagJ2.setFont(ToontownGlobals.getToonFont())
        self.nametagJ2.setName('')
        self.nametagJ2.manage(base.marginManager)
        self.nametagJ2.getNametag3d().setBillboardOffset(4)
        nametagNode2 = self.nametagJ2.getNametag3d().upcastToPandaNode()
        self.nametagS2 = self.Amanda.attachNewNode(nametagNode2)
        self.nametagS2.setPos(0, 0, 9.5)

        self.Mimi = Suit.Suit()
        self.Mimi.dna = SuitDNA.SuitDNA()
        self.Mimi.dna.newSuit('rb')
        self.Mimi.setDNA(self.Mimi.dna)
        self.Mimi.setPos(50, -35, 71)
        self.Mimi.setHpr(0, 0, 0)
        self.Mimi.loop('neutral')
        self.Mimi.reparentTo(render)
        self.Mimi = self.Mimi
        
        self.nametagJ3 = None
        self.nametagS3 = None
        self.nametagJ3 = NametagGroup()
        self.nametagJ3.setAvatar(self.Mimi)
        self.nametagJ3.setFont(ToontownGlobals.getToonFont())
        self.nametagJ3.setName('')
        self.nametagJ3.manage(base.marginManager)
        self.nametagJ3.getNametag3d().setBillboardOffset(4)
        nametagNode3 = self.nametagJ3.getNametag3d().upcastToPandaNode()
        self.nametagS3 = self.Mimi.attachNewNode(nametagNode3)
        self.nametagS3.setPos(0, 0, 9.5)

        self.ElevatorProp = loader.loadModel('phase_9/models/cogHQ/cogHQ_elevator.bam')
        self.ElevatorProp.setPos(65, -10, 71)
        self.ElevatorProp.setHpr(90, 0, 0)
        self.ElevatorProp.setScale(2.5)
        self.ElevatorProp.reparentTo(render)
        
        camera.setPos(60, -10, 75)
        camera.setHpr(90, 10, 0)

        self.cogGruntSpeech = base.loader.loadSfx('phase_3.5/audio/dial/COG_VO_grunt.ogg')
        self.cogMurmurSpeech = base.loader.loadSfx('phase_3.5/audio/dial/COG_VO_murmur.ogg')
        self.cogQuestionSpeech = base.loader.loadSfx('phase_3.5/audio/dial/COG_VO_question.ogg')
        self.cogStatementSpeech = base.loader.loadSfx('phase_3.5/audio/dial/COG_VO_statement.ogg')
        self.mimiExclaimSpeech = base.loader.loadSfx('phase_5/audio/sfx/Skel_COG_VO_grunt.ogg')
        self.mimiGruntSpeech = base.loader.loadSfx('phase_5/audio/sfx/Skel_COG_VO_grunt.ogg')
        self.mimiMurmurSpeech = base.loader.loadSfx('phase_5/audio/sfx/Skel_COG_VO_murmur.ogg')
        self.mimiQuestionSpeech = base.loader.loadSfx('phase_5/audio/sfx/Skel_COG_VO_question.ogg')
        self.mimiStatementSpeech = base.loader.loadSfx('phase_5/audio/sfx/Skel_COG_VO_statement.ogg')
        self.amandaGruntSpeech = base.loader.loadSfx('phase_9/audio/sfx/Boss_COG_VO_grunt.ogg')
        self.amandaMurmurSpeech = base.loader.loadSfx('phase_9/audio/sfx/Boss_COG_VO_murmur.ogg')
        self.amandaQuestionSpeech = base.loader.loadSfx('phase_9/audio/sfx/Boss_COG_VO_question.ogg')
        self.amandaStatementSpeech = base.loader.loadSfx('phase_9/audio/sfx/Boss_COG_VO_statement.ogg')

        
        GoodTrack = Sequence(Func(base.transitions.irisOut, 2), Wait(5), Func(base.transitions.irisIn, 2),
        LerpPosHprInterval(camera, duration=10, pos=Point3(160, -10, 75), hpr=(90, 10, 0), blendType='easeInOut'),
        Wait(3),
        LerpPosHprInterval(camera, duration=2, pos=Point3(120, -15, 78), hpr=(180, 10, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "We ready for the revamped security?", CFSpeech | CFTimeout), SoundInterval(self.amandaQuestionSpeech),
        Wait(3),
        Func(self.nametagJ2.clearChat),
        LerpPosHprInterval(camera, duration=2, pos=Point3(120, -2, 78), hpr=(0, 10, 0), blendType='easeInOut'),
        Func(self.nametagJ.setChat, "Yes.", CFSpeech | CFTimeout), SoundInterval(self.cogStatementSpeech),
        Wait(2),
        Func(self.nametagJ.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(120, -15, 76), hpr=(180, 10, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "Perfect!", CFSpeech | CFTimeout), SoundInterval(self.amandaGruntSpeech),
        Wait(2),
        Func(self.nametagJ2.clearChat),
        LerpPosHprInterval(camera, duration=1, pos=Point3(120, -15, 74), hpr=(180, 15, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "Now our plan won't go crazy like last time, right?", CFSpeech | CFTimeout), SoundInterval(self.amandaQuestionSpeech),
        Wait(3),
        Func(self.nametagJ2.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(120, -2, 78), hpr=(0, 10, 0), blendType='easeInOut'),
        Func(self.nametagJ.setChat, "Nope.", CFSpeech | CFTimeout), SoundInterval(self.cogGruntSpeech),
        Wait(2),
        Func(self.nametagJ.clearChat),
        LerpPosHprInterval(camera, duration=2, pos=Point3(120, 3, 78), hpr=(0, 5, 0), blendType='easeInOut'),
        Func(self.nametagJ.setChat, "We completely got everything covered.", CFSpeech | CFTimeout), SoundInterval(self.cogMurmurSpeech),
        Wait(3.5),
        Func(self.nametagJ.clearChat),
        LerpPosHprInterval(camera, duration=1, pos=Point3(120, -17, 77), hpr=(180, 15, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "That's what I like to hear!", CFSpeech | CFTimeout), SoundInterval(self.amandaGruntSpeech),
        Wait(2.5),
        Func(self.nametagJ2.clearChat),
        LerpPosHprInterval(camera, duration=2, pos=Point3(160, -10, 75), hpr=(90, 10, 0), blendType='easeInOut'),
        LerpPosHprInterval(camera, duration=5, pos=Point3(65, -10, 75), hpr=(90, 10, 0), blendType='easeInOut'),
        LerpPosHprInterval(camera, duration=2, pos=Point3(50, 6, 75), hpr=(180, 10, 0), blendType='easeInOut'),
        Wait(0.5),
        Func(self.Mimi.loop, 'walk'), Func(self.Mimi.loop, 'walk'),
        LerpPosInterval(self.Mimi, duration=4, pos=Point3(50, -10, 71), blendType='noBlend'),
        Func(self.Mimi.loop, 'walk'), Func(self.Mimi.loop, 'walk'),
        LerpPosHprInterval(self.Mimi, duration=2.5, pos=Point3(50, -10, 71), hpr=(270, 0, 0), blendType='noBlend'),
        Func(self.Mimi.loop, 'neutral'), Func(self.Mimi.loop, 'neutral'),
        LerpPosHprInterval(camera, duration=2, pos=Point3(62, -10, 77), hpr=(90, 8, 0), blendType='easeInOut'),
        Func(self.nametagJ3.setChat, "So. Are the things ready yet? Is everything secured?", CFSpeech | CFTimeout), SoundInterval(self.mimiQuestionSpeech),
        Wait(2.5),
        Func(self.nametagJ3.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(120, -17, 78), hpr=(180, 5, 0), blendType='easeInOut'),
        Func(self.Amanda.loop, 'walk'), Func(self.Amanda.loop, 'walk'),
        LerpPosHprInterval(self.Amanda, duration=2.5, pos=Point3(120, -30, 71), hpr=(90, 0, 0), blendType='noBlend'),
        Func(self.Amanda.loop, 'neutral'), Func(self.Amanda.loop, 'neutral'),
        Func(self.nametagJ2.setChat, "Yep! Sure is!", CFSpeech | CFTimeout), SoundInterval(self.amandaGruntSpeech),
        Wait(2.5),
        Func(self.nametagJ2.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(62, -10, 77), hpr=(90, 8, 0), blendType='easeInOut'),
        Func(self.nametagJ3.setChat, "Good.", CFSpeech | CFTimeout), SoundInterval(self.mimiGruntSpeech),
        Wait(2.5),
        Func(self.nametagJ3.clearChat),
        LerpPosHprInterval(camera, duration=1, pos=Point3(64, -10, 77), hpr=(90, 15, 0), blendType='easeInOut'),
        Func(self.nametagJ3.setChat, "Let's now show these Toons what we're made of...", CFSpeech | CFTimeout), SoundInterval(self.mimiMurmurSpeech),
        Wait(3),
        Func(base.transitions.irisOut, 2))
        GoodTrack.start()