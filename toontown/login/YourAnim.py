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
        self.dnaStore = DNAStorage()
        loader.loadDNAFile(self.dnaStore, 'phase_4/dna/storage_TT.dna')
        loader.loadDNAFile(self.dnaStore, 'phase_4/dna/storage_TT_sz.dna')
        loader.loadDNAFile(self.dnaStore, 'phase_4/dna/storage.dna')
        loader.loadDNAFile(self.dnaStore, 'phase_5/dna/storage_town.dna')
        self.BR = loader.loadDNAFile(self.dnaStore, 'phase_4/dna/toontown_central_sz.dna')
        render.attachNewNode(self.BR)
        self.TTSky = loader.loadModel('phase_3.5/models/props/TT_sky.bam')
        self.TTSky.reparentTo(render)
        base.oobe()
        
        self.toon = NPCToons.createLocalNPC(555)
        self.toon.loop('neutral')
        self.toon.setPos(0, 0, 7)
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
        self.nametagS.setPos(0, 0, 3.5)

        self.toon2 = NPCToons.createLocalNPC(784)
        self.toon2.loop('neutral')
        self.toon2.setPos(0, 0, 7)
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

        
        GoodTrack = Sequence()
        GoodTrack.start()