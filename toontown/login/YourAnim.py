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
        self.mixsong = base.loader.loadMusic('phase_14/audio/bgm/LarryMix.ogg')
        
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

        self.CarProp = loader.loadModel('phase_6/models/karting/Kart1_Final.bam')
        self.CarProp.setPos(60, 10, 10)
        self.CarProp.setHpr(180, 45, 0)
        self.CarProp.setScale(2.2)
        self.CarProp.setColor(0, 0, 1, 1)
        self.CarProp.reparentTo(render)
        
        self.toon = NPCToons.createLocalNPC(755)
        self.toon.loop('neutral')
        self.toon.setPos(60, 0, 4)
        self.toon.setHpr(90, 0, 0)
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
        self.toon2.setPos(60, -3, 4)
        self.toon2.setHpr(90, 0, 0)
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

        self.toon3 = NPCToons.createLocalNPC(784)
        self.toon3.loop('neutral')
        self.toon3.setPos(60, -6, 4)
        self.toon3.setHpr(90, 0, 0)
        self.toon3.reparentTo(render)
        
        self.nametagJ3 = None
        self.nametagS3 = None
        self.nametagJ3 = NametagGroup()
        self.nametagJ3.setAvatar(self.toon3)
        self.nametagJ3.setFont(ToontownGlobals.getToonFont())
        self.nametagJ3.setName('')
        self.nametagJ3.manage(base.marginManager)
        self.nametagJ3.getNametag3d().setBillboardOffset(4)
        nametagNode3 = self.nametagJ3.getNametag3d().upcastToPandaNode()
        self.nametagS3 = self.toon3.attachNewNode(nametagNode3)
        self.nametagS3.setPos(0, 0, 9.5)

        self.toon4 = NPCToons.createLocalNPC(784)
        self.toon4.loop('neutral')
        self.toon4.setPos(64, -11, 4)
        self.toon4.setHpr(90, 0, 0)
        self.toon4.reparentTo(render)
        
        self.nametagJ4 = None
        self.nametagS4 = None
        self.nametagJ4 = NametagGroup()
        self.nametagJ4.setAvatar(self.toon4)
        self.nametagJ4.setFont(ToontownGlobals.getToonFont())
        self.nametagJ4.setName('')
        self.nametagJ4.manage(base.marginManager)
        self.nametagJ4.getNametag3d().setBillboardOffset(4)
        nametagNode4 = self.nametagJ4.getNametag3d().upcastToPandaNode()
        self.nametagS4 = self.toon4.attachNewNode(nametagNode4)
        self.nametagS4.setPos(0, 0, 9.5)

        self.toon5 = NPCToons.createLocalNPC(784)
        self.toon5.loop('neutral')
        self.toon5.setPos(62, -15, 4)
        self.toon5.setHpr(120, 0, 0)
        self.toon5.reparentTo(render)
        
        self.nametagJ5 = None
        self.nametagS5 = None
        self.nametagJ5 = NametagGroup()
        self.nametagJ5.setAvatar(self.toon5)
        self.nametagJ5.setFont(ToontownGlobals.getToonFont())
        self.nametagJ5.setName('')
        self.nametagJ5.manage(base.marginManager)
        self.nametagJ5.getNametag3d().setBillboardOffset(4)
        nametagNode5 = self.nametagJ5.getNametag3d().upcastToPandaNode()
        self.nametagS5 = self.toon5.attachNewNode(nametagNode5)
        self.nametagS5.setPos(0, 0, 9.5)

        self.toon6 = NPCToons.createLocalNPC(784)
        self.toon6.loop('neutral')
        self.toon6.setPos(58, -17, 4)
        self.toon6.setHpr(35, 0, 0)
        self.toon6.reparentTo(render)
        
        self.nametagJ6 = None
        self.nametagS6 = None
        self.nametagJ6 = NametagGroup()
        self.nametagJ6.setAvatar(self.toon6)
        self.nametagJ6.setFont(ToontownGlobals.getToonFont())
        self.nametagJ6.setName('')
        self.nametagJ6.manage(base.marginManager)
        self.nametagJ6.getNametag3d().setBillboardOffset(4)
        nametagNode6 = self.nametagJ6.getNametag3d().upcastToPandaNode()
        self.nametagS6 = self.toon6.attachNewNode(nametagNode6)
        self.nametagS6.setPos(0, 0, 9.5)
    
        self.toon7 = NPCToons.createLocalNPC(784)
        self.toon7.loop('neutral')
        self.toon7.setPos(60, -20, 8)
        self.toon7.setHpr(0, 0, 0)
        self.toon7.reparentTo(render)
        
        self.nametagJ7 = None
        self.nametagS7 = None
        self.nametagJ7 = NametagGroup()
        self.nametagJ7.setAvatar(self.toon7)
        self.nametagJ7.setFont(ToontownGlobals.getToonFont())
        self.nametagJ7.setName('')
        self.nametagJ7.manage(base.marginManager)
        self.nametagJ7.getNametag3d().setBillboardOffset(4)
        nametagNode7 = self.nametagJ7.getNametag3d().upcastToPandaNode()
        self.nametagS7 = self.toon7.attachNewNode(nametagNode7)
        self.nametagS7.setPos(0, 0, 9.5)

        self.toon8 = NPCToons.createLocalNPC(784)
        self.toon8.loop('neutral')
        self.toon8.setPos(49, -26, 8)
        self.toon8.setHpr(0, 0, 0)
        self.toon8.reparentTo(render)
        
        self.nametagJ8 = None
        self.nametagS8 = None
        self.nametagJ8 = NametagGroup()
        self.nametagJ8.setAvatar(self.toon8)
        self.nametagJ8.setFont(ToontownGlobals.getToonFont())
        self.nametagJ8.setName('')
        self.nametagJ8.manage(base.marginManager)
        self.nametagJ8.getNametag3d().setBillboardOffset(4)
        nametagNode8 = self.nametagJ8.getNametag3d().upcastToPandaNode()
        self.nametagS8 = self.toon8.attachNewNode(nametagNode8)
        self.nametagS8.setPos(0, 0, 4.5)

        self.toon9 = NPCToons.createLocalNPC(784)
        self.toon9.loop('neutral')
        self.toon9.setPos(62, 2, 4)
        self.toon9.setHpr(45, 0, 0)
        self.toon9.reparentTo(render)
        
        self.nametagJ9 = None
        self.nametagS9 = None
        self.nametagJ9 = NametagGroup()
        self.nametagJ9.setAvatar(self.toon9)
        self.nametagJ9.setFont(ToontownGlobals.getToonFont())
        self.nametagJ9.setName('')
        self.nametagJ9.manage(base.marginManager)
        self.nametagJ9.getNametag3d().setBillboardOffset(4)
        nametagNode9 = self.nametagJ9.getNametag3d().upcastToPandaNode()
        self.nametagS9 = self.toon9.attachNewNode(nametagNode9)
        self.nametagS9.setPos(0, 0, 9.5)

        self.toon10 = NPCToons.createLocalNPC(784)
        self.toon10.loop('neutral')
        self.toon10.setPos(70, 0, 45)
        self.toon10.setHpr(90, 0, 0)
        self.toon10.reparentTo(render)
        
        self.nametagJ10 = None
        self.nametagS10 = None
        self.nametagJ10 = NametagGroup()
        self.nametagJ10.setAvatar(self.toon10)
        self.nametagJ10.setFont(ToontownGlobals.getToonFont())
        self.nametagJ10.setName('')
        self.nametagJ10.manage(base.marginManager)
        self.nametagJ10.getNametag3d().setBillboardOffset(4)
        nametagNode10 = self.nametagJ10.getNametag3d().upcastToPandaNode()
        self.nametagS10 = self.toon10.attachNewNode(nametagNode10)
        self.nametagS10.setPos(0, 0, 9.5)

        self.toon11 = NPCToons.createLocalNPC(784)
        self.toon11.loop('neutral')
        self.toon11.setPos(70, 10, 10)
        self.toon11.setHpr(90, 0, 0)
        self.toon11.reparentTo(render)
        
        self.nametagJ11 = None
        self.nametagS11 = None
        self.nametagJ11 = NametagGroup()
        self.nametagJ11.setAvatar(self.toon11)
        self.nametagJ11.setFont(ToontownGlobals.getToonFont())
        self.nametagJ11.setName('')
        self.nametagJ11.manage(base.marginManager)
        self.nametagJ11.getNametag3d().setBillboardOffset(4)
        nametagNode11 = self.nametagJ11.getNametag3d().upcastToPandaNode()
        self.nametagS11 = self.toon11.attachNewNode(nametagNode11)
        self.nametagS11.setPos(0, 0, 9.5)

        self.toon12 = NPCToons.createLocalNPC(784)
        self.toon12.loop('neutral')
        self.toon12.setPos(70, 5, 10)
        self.toon12.setHpr(180, -90, 0)
        self.toon12.reparentTo(render)
        
        self.nametagJ12 = None
        self.nametagS12 = None
        self.nametagJ12 = NametagGroup()
        self.nametagJ12.setAvatar(self.toon12)
        self.nametagJ12.setFont(ToontownGlobals.getToonFont())
        self.nametagJ12.setName('')
        self.nametagJ12.manage(base.marginManager)
        self.nametagJ12.getNametag3d().setBillboardOffset(4)
        nametagNode12 = self.nametagJ12.getNametag3d().upcastToPandaNode()
        self.nametagS12 = self.toon12.attachNewNode(nametagNode12)
        self.nametagS12.setPos(0, 0, 9.5)

        self.toon13 = NPCToons.createLocalNPC(784)
        self.toon13.loop('sit')
        self.toon13.setPos(60, 10, 10)
        self.toon13.setHpr(180, 45, 0)
        self.toon13.reparentTo(render)
        
        self.nametagJ13 = None
        self.nametagS13 = None
        self.nametagJ13 = NametagGroup()
        self.nametagJ13.setAvatar(self.toon13)
        self.nametagJ13.setFont(ToontownGlobals.getToonFont())
        self.nametagJ13.setName('')
        self.nametagJ13.manage(base.marginManager)
        self.nametagJ13.getNametag3d().setBillboardOffset(4)
        nametagNode13 = self.nametagJ13.getNametag3d().upcastToPandaNode()
        self.nametagS13 = self.toon13.attachNewNode(nametagNode13)
        self.nametagS13.setPos(0, 0, 9.5)

        self.toon14 = NPCToons.createLocalNPC(784)
        self.toon14.loop('neutral')
        self.toon14.setPos(50, 10, 4)
        self.toon14.setHpr(270, 0, 0)
        self.toon14.reparentTo(render)
        
        self.nametagJ14 = None
        self.nametagS14 = None
        self.nametagJ14 = NametagGroup()
        self.nametagJ14.setAvatar(self.toon14)
        self.nametagJ14.setFont(ToontownGlobals.getToonFont())
        self.nametagJ14.setName('')
        self.nametagJ14.manage(base.marginManager)
        self.nametagJ14.getNametag3d().setBillboardOffset(4)
        nametagNode14 = self.nametagJ14.getNametag3d().upcastToPandaNode()
        self.nametagS14 = self.toon14.attachNewNode(nametagNode14)
        self.nametagS14.setPos(0, 0, 9.5)

        self.toon15 = NPCToons.createLocalNPC(555)
        self.toon15.loop('victory')
        self.toon15.setPos(45, 10, 4)
        self.toon15.setHpr(270, 0, 0)
        self.toon15.reparentTo(render)
        
        self.nametagJ15 = None
        self.nametagS15 = None
        self.nametagJ15 = NametagGroup()
        self.nametagJ15.setAvatar(self.toon15)
        self.nametagJ15.setFont(ToontownGlobals.getToonFont())
        self.nametagJ15.setName('')
        self.nametagJ15.manage(base.marginManager)
        self.nametagJ15.getNametag3d().setBillboardOffset(4)
        nametagNode15 = self.nametagJ15.getNametag3d().upcastToPandaNode()
        self.nametagS15 = self.toon15.attachNewNode(nametagNode15)
        self.nametagS15.setPos(0, 0, 9.5)

        self.toon16 = NPCToons.createLocalNPC(1116)
        self.toon16.loop('think')
        self.toon16.setPos(45, 44, 4)
        self.toon16.setHpr(270, 0, 0)
        self.toon16.reparentTo(render)
        
        self.nametagJ16 = None
        self.nametagS16 = None
        self.nametagJ16 = NametagGroup()
        self.nametagJ16.setAvatar(self.toon15)
        self.nametagJ16.setFont(ToontownGlobals.getToonFont())
        self.nametagJ16.setName('')
        self.nametagJ16.manage(base.marginManager)
        self.nametagJ16.getNametag3d().setBillboardOffset(4)
        nametagNode16 = self.nametagJ16.getNametag3d().upcastToPandaNode()
        self.nametagS16 = self.toon16.attachNewNode(nametagNode16)
        self.nametagS16.setPos(0, 0, 9.5)

        self.toon17 = NPCToons.createLocalNPC(777)
        self.toon17.pose('angry', 30)
        self.toon17.setPos(58, 8, 3.5)
        self.toon17.setHpr(90, 0, 0)
        self.toon17.setScale(1.9)
        self.toon17.reparentTo(render)
        
        self.nametagJ17 = None
        self.nametagS17 = None
        self.nametagJ17 = NametagGroup()
        self.nametagJ17.setAvatar(self.toon17)
        self.nametagJ17.setFont(ToontownGlobals.getToonFont())
        self.nametagJ17.setName('')
        self.nametagJ17.manage(base.marginManager)
        self.nametagJ17.getNametag3d().setBillboardOffset(4)
        nametagNode17 = self.nametagJ2.getNametag3d().upcastToPandaNode()
        self.nametagS17 = self.toon17.attachNewNode(nametagNode17)
        self.nametagS17.setPos(0, 0, 8)
        
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