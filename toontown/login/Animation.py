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
class Animation():

    def __init__(self, leaveFunction):
        self.mixsong = base.loader.loadMusic('phase_14/audio/bgm/estate_interior.ogg')
        self.sonicintrosong = base.loader.loadMusic('phase_14/audio/bgm/CFO_win.ogg')
        self.HQsong = base.loader.loadMusic('phase_9/audio/bgm/CogHQ_Stage_bg.ogg')

    def create(self):
        self.houseVariable = loader.loadModel('phase_5.5/models/estate/tt_m_ara_int_estateHouseB.bam')
        self.houseVariable.reparentTo(render)
        
        self.placeVariable = loader.loadModel('phase_7/models/modules/suit_interior.bam')

        self.HQVariable = loader.loadModel('phase_9/models/cogHQ/SellbotHQExterior.bam')
        
        self.TTSky = loader.loadModel('phase_9/models/cogHQ/cog_sky.bam')
        self.TTSky.reparentTo(render)

        self.TableProp = loader.loadModel('phase_5.5/models/estate/TABLE_Bedroom_Desat.bam')
        self.TableProp.setPos(-15, 15, 0)
        self.TableProp.setScale(2.2)
        self.TableProp.reparentTo(render)

        self.TableProp2 = loader.loadModel('phase_5.5/models/estate/CarmelAppleFireplace.bam')
        self.TableProp2.setPos(-15, 15, 2.5)
        self.TableProp2.setScale(0.5)
        self.TableProp2.reparentTo(render)

        self.TableProp3 = loader.loadModel('phase_5.5/models/estate/deskChair.bam')
        self.TableProp3.setPos(-15, 10.5, 0)
        self.TableProp3.setHpr(180, 0, 0)
        self.TableProp3.setScale(0.9)
        self.TableProp3.reparentTo(render)

        self.TableProp4 = loader.loadModel('phase_5.5/models/estate/deskChair.bam')
        self.TableProp4.setPos(0, -15, 0)
        self.TableProp4.setHpr(90, 0, 0)
        self.TableProp4.setScale(0.9)
        self.TableProp4.reparentTo(render)

        self.TableProp5 = loader.loadModel('phase_5/models/cogdominium/cogdominiumElevator.bam')
        self.TableProp5.setPos(0, -5, -20)
        self.TableProp5.setHpr(0, 0, 0)
        self.TableProp5.setScale(1)
        self.TableProp5.reparentTo(render)

        self.TableProp6 = loader.loadModel('phase_5/models/cogdominium/cogdominiumElevator.bam')
        self.TableProp6.setPos(0, -55, -20)
        self.TableProp6.setHpr(180, 0, 0)
        self.TableProp6.setScale(1)
        self.TableProp6.reparentTo(render)

        self.TableProp7 = loader.loadModel('phase_5/models/props/weight-mod.bam')
        self.TableProp7.setPos(-5, -15, 35)
        self.TableProp7.setHpr(180, 0, 0)
        self.TableProp7.setScale(1)
        self.TableProp7.reparentTo(render)
        
        self.toon = NPCToons.createLocalNPC(555)
        self.toon.loop('sit')
        self.toon.setPos(-15, 11.7, 0.5)
        self.toon.setHpr(0, 0, 0)
        self.toon.setHat(14, 0, 0)
        self.toon.setBackpack(7, 0, 0)
        self.toon.setShoes(2, 9, 0)
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

        self.toon2 = NPCToons.createLocalNPC(1116)
        self.toon2.loop('sit')
        self.toon2.setPos(1.2, -15, 0.5)
        self.toon2.setHpr(270, 0, 0)
        self.toon2.setHat(5, 0, 0)
        self.toon2.setBackpack(23, 0, 0)
        self.toon2.setGlasses(3, 0, 0)
        self.toon2.setShoes(2, 5, 0)
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
        self.nametagS2.setPos(0, 0, 3.5)

        self.toon3 = NPCToons.createLocalNPC(788)
        self.toon3.loop('bored')
        self.toon3.setPos(1.2, -15, -5)
        self.toon3.setHpr(180, 0, 0)
        self.toon3.setHat(3, 0, 0)
        self.toon3.setBackpack(7, 0, 0)
        self.toon3.setGlasses(13, 0, 0)
        self.toon3.setShoes(2, 9, 0)
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
        self.nametagS3.setPos(0, 0, 3.5)

        self.Rose = Suit.Suit()
        self.Rose.dna = SuitDNA.SuitDNA()
        self.Rose.dna.newSuit('le')
        self.Rose.setDNA(self.Rose.dna)
        self.Rose.setPos(-10, -15, -14)
        self.Rose.setHpr(90, 0, 0)
        self.Rose.loop('neutral')
        self.Rose.reparentTo(render)
        self.Rose = self.Rose
        
        self.nametagJ4 = None
        self.nametagS4 = None
        self.nametagJ4 = NametagGroup()
        self.nametagJ4.setAvatar(self.Rose)
        self.nametagJ4.setFont(ToontownGlobals.getToonFont())
        self.nametagJ4.setName('')
        self.nametagJ4.manage(base.marginManager)
        self.nametagJ4.getNametag3d().setBillboardOffset(4)
        nametagNode4 = self.nametagJ4.getNametag3d().upcastToPandaNode()
        self.nametagS4 = self.Rose.attachNewNode(nametagNode4)
        self.nametagS4.setPos(0, 0, 9.5)
        
        camera.setPos(0, -25, 5)
        camera.setHpr(0, 0, 0)

        self.cogGruntSpeech = base.loader.loadSfx('phase_14/audio/sfx/COG_VO_grunt.ogg')
        self.cogMurmurSpeech = base.loader.loadSfx('phase_14/audio/sfx/COG_VO_murmur.ogg')
        self.cogStatementSpeech = base.loader.loadSfx('phase_14/audio/sfx/COG_VO_statement.ogg')
        self.cogQuestionSpeech = base.loader.loadSfx('phase_14/audio/sfx/COG_VO_question.ogg')
        self.cogEmotionalSpeech = base.loader.loadSfx('phase_14/audio/sfx/COG_indifferent.ogg')
        self.catQuestionSpeech = base.loader.loadSfx('phase_3.5/audio/dial/AV_cat_question.ogg')
        self.catMedSpeech = base.loader.loadSfx('phase_3.5/audio/dial/AV_cat_med.ogg')
        self.catExclaimSpeech = base.loader.loadSfx('phase_3.5/audio/dial/AV_cat_exclaim.ogg')
        self.catStatementSpeech = base.loader.loadSfx('phase_3.5/audio/dial/AV_cat_statement.ogg')
        self.catEmotionalSpeech = base.loader.loadSfx('phase_3.5/audio/dial/AV_cat_indifferent.ogg')
        self.catEmotionalSpamSpeech = base.loader.loadSfx('phase_3.5/audio/dial/AV_cat_indifferent_spam.ogg')
        self.catHowlSpeech = base.loader.loadSfx('phase_3.5/audio/dial/AV_cat_howl.ogg')
        self.catLongSpeech = base.loader.loadSfx('phase_3.5/audio/dial/AV_cat_long.ogg')
        self.catShortSpeech = base.loader.loadSfx('phase_3.5/audio/dial/AV_cat_short.ogg')
        self.dogExclaimSpeech = base.loader.loadSfx('phase_3.5/audio/dial/AV_dog_exclaim.ogg')
        self.dogQuestionSpeech = base.loader.loadSfx('phase_3.5/audio/dial/AV_dog_question.ogg')
        self.dogMedSpeech = base.loader.loadSfx('phase_3.5/audio/dial/AV_dog_med.ogg')
        self.dogStatementSpeech = base.loader.loadSfx('phase_3.5/audio/dial/AV_dog_statement.ogg')
        self.dogEmotionalSpeech = base.loader.loadSfx('phase_3.5/audio/dial/AV_dog_indifferent.ogg')
        self.dogHowlSpeech = base.loader.loadSfx('phase_3.5/audio/dial/AV_dog_howl.ogg')
        self.dogLongSpeech = base.loader.loadSfx('phase_3.5/audio/dial/AV_dog_long.ogg')
        self.dogShortSpeech = base.loader.loadSfx('phase_3.5/audio/dial/AV_dog_short.ogg')
        self.tonCrashSfx = base.loader.loadSfx('phase_5/audio/sfx/AA_drop_bigweight_miss.ogg')
        self.alarmAlertSfx = base.loader.loadSfx('phase_14/audio/sfx/AA_sound_aoogah.ogg')

        
        GoodTrack = Sequence(Wait(3), Func(base.transitions.irisIn, 1), Func(self.mixsong.play),
        Func(self.toon.blinkEyes),
        LerpPosHprInterval(camera, duration=3, pos=Point3(-13, -25, 5), hpr=(0, 0, 0), blendType='easeInOut'),
        Wait(1),
        LerpPosHprInterval(camera, duration=3, pos=Point3(-7, 23, 5), hpr=(135, 10, 0), blendType='easeInOut'),
        Wait(2),
        LerpPosHprInterval(camera, duration=1.5, pos=Point3(-8, 16, 4), hpr=(125, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ.setChat, "What am I going to eat?", CFSpeech | CFTimeout), SoundInterval(self.catQuestionSpeech),
        Wait(3),
        Func(self.nametagJ.setChat, "I'm hungry. :P", CFSpeech | CFTimeout), SoundInterval(self.catMedSpeech),
        Wait(2),
        Func(self.nametagJ.clearChat),
        Func(self.toon2.sadEyes),
        Func(self.toon2.blinkEyes),
        LerpPosHprInterval(camera, duration=0, pos=Point3(6, -13, 4), hpr=(110, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "When will this blasphemy end...?", CFSpeech | CFTimeout), SoundInterval(self.catEmotionalSpeech), Wait(0.4), SoundInterval(self.catQuestionSpeech),
        Wait(2),
        Parallel(LerpPosHprInterval(camera, duration=1.5, pos=Point3(6, -13.6, 4), hpr=(100, 0, 0), blendType='easeInOut')),
        Func(self.nametagJ2.setChat, "Redsonic is attacking me worse than ever now...", CFSpeech | CFTimeout), SoundInterval(self.catEmotionalSpeech),
        Wait(2.5),
        Func(self.nametagJ2.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(-6, -15, 4), hpr=(270, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "I don't understand...", CFSpeech | CFTimeout), SoundInterval(self.catEmotionalSpeech),
        Wait(2.5),
        Func(self.nametagJ2.setChat, "Why can't he leave me alone...?", CFSpeech | CFTimeout), SoundInterval(self.catEmotionalSpeech), Wait(0.4), SoundInterval(self.catQuestionSpeech),
        Wait(2.5),
        Func(self.nametagJ2.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(-8, 16, 4), hpr=(125, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ.setChat, "Hm?", CFSpeech | CFTimeout), SoundInterval(self.catQuestionSpeech),
        Wait(1.5),
        Parallel(LerpPosHprInterval(camera, duration=1, pos=Point3(-8, 16, 4), hpr=(125, 0, 0), blendType='easeInOut')),
        Func(self.toon.loop, 'jump'), Func(self.toon.loop, 'jump'),
        LerpPosHprInterval(self.toon, duration=1.5, pos=Point3(-12, 11.7, 0.5), hpr=(270, 0, 0), blendType='noBlend'),
        Func(self.toon.loop, 'walk'), Func(self.toon.loop, 'walk'),
        Parallel(LerpPosHprInterval(camera, duration=1, pos=Point3(-2, 20, 4), hpr=(175, 0, 0), blendType='easeInOut')),
        LerpPosHprInterval(self.toon, duration=2, pos=Point3(-3, 11.7, 0.5), hpr=(270, 0, 0), blendType='noBlend'), 
        LerpPosHprInterval(self.toon, duration=1, pos=Point3(-3, 11.7, 0.5), hpr=(180, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.toon, duration=4, pos=Point3(-3, -11.7, 0.5), hpr=(180, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.toon, duration=2, pos=Point3(-3, -11.7, 0.5), hpr=(235, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(camera, duration=0, pos=Point3(1.5, -15, 3.5), hpr=(45, 0, 0), blendType='easeInOut'),
        Func(self.toon.loop, 'neutral'), Func(self.toon.loop, 'neutral'),
        Func(self.nametagJ.setChat, "Hey, I heard you crying.", CFSpeech | CFTimeout), SoundInterval(self.catMedSpeech), SoundInterval(self.catHowlSpeech),
        Wait(1.5),
        Func(self.nametagJ.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(8, -11, 4), hpr=(110, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "Nice...", CFSpeech | CFTimeout), SoundInterval(self.catEmotionalSpeech),
        Wait(2),
        Func(self.nametagJ2.clearChat),
        Parallel(LerpPosHprInterval(camera, duration=1.5, pos=Point3(6, -13.6, 4), hpr=(100, 0, 0), blendType='easeInOut')),
        Func(self.nametagJ2.setChat, "I don't care... </3", CFSpeech | CFTimeout), SoundInterval(self.catEmotionalSpeech),
        Wait(2.5),
        Func(self.nametagJ2.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(1.5, -15, 3.5), hpr=(45, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ.setChat, "Wha, what's wrong?", CFSpeech | CFTimeout), SoundInterval(self.catShortSpeech), SoundInterval(self.catQuestionSpeech),
        Wait(2),
        Func(self.nametagJ.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(6, -13.6, 4), hpr=(100, 0, 0), blendType='easeInOut'),
        Wait(1.5),
        Func(self.toon2.sadEyes),
        Func(self.toon2.closeEyes),
        Wait(1),
        Func(self.nametagJ2.setChat, "Sniff...", CFSpeech | CFTimeout), SoundInterval(self.catEmotionalSpeech),
        Wait(2.5),
        Func(self.nametagJ2.setChat, "I just...", CFSpeech | CFTimeout), SoundInterval(self.catEmotionalSpeech),
        Wait(2),
        Func(self.nametagJ2.clearChat),
        Func(self.toon2.sadEyes),
        Func(self.toon2.blinkEyes),
        Wait(1),
        Func(self.nametagJ2.setChat, "I wish RedSonic would leave me alone...", CFSpeech | CFTimeout), SoundInterval(self.catLongSpeech), SoundInterval(self.catMedSpeech), SoundInterval(self.catEmotionalSpeech),
        Wait(2),
        Func(self.nametagJ2.clearChat),
        Func(self.toon.sadEyes),
        Func(self.toon.blinkEyes),
        LerpPosHprInterval(camera, duration=0, pos=Point3(1.5, -15, 3.5), hpr=(45, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ.setChat, "Aw... :(", CFSpeech | CFTimeout), SoundInterval(self.catShortSpeech), SoundInterval(self.catEmotionalSpeech),
        Wait(2),
        Func(self.nametagJ.clearChat),
        Func(self.toon.loop, 'walk'), Func(self.toon.loop, 'walk'),
        Parallel(LerpPosHprInterval(self.toon, duration=1.5, pos=Point3(0, -13.5, 0.5), hpr=(235, 0, 0), blendType='noBlend')),
        LerpPosHprInterval(camera, duration=1, pos=Point3(8, -12, 3.5), hpr=(100, 0, 0), blendType='easeInOut'),
        LerpPosHprInterval(self.toon, duration=1.5, pos=Point3(0, -13.5, 0.5), hpr=(180, 0, 0), blendType='noBlend'),
        Func(self.toon.pose, 'throw', 30), Func(self.toon.pose, 'throw', 30),
        Func(self.nametagJ.setChat, "I'm right here... let it all out...", CFSpeech | CFTimeout), SoundInterval(self.catShortSpeech), SoundInterval(self.catEmotionalSpeech), SoundInterval(self.catEmotionalSpeech),
        Wait(2),
        Func(self.nametagJ.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(6, -13.6, 4), hpr=(100, 0, 0), blendType='easeInOut'),
        Wait(1.5),
        Func(self.toon2.sadEyes),
        Func(self.toon2.closeEyes),
        Func(self.nametagJ2.setChat, "</3 </3 </3 </3 </3 </3 T_T T_T T_T T_T T_T T_T :( :( :( :( :(", CFSpeech | CFTimeout), SoundInterval(self.catEmotionalSpamSpeech),
        Wait(2),
        Func(self.nametagJ2.clearChat),
        LerpPosHprInterval(self.toon2, duration=0, pos=Point3(0, -14, 0.5), hpr=(0, 0, 0), blendType='noBlend'),
        Func(self.toon2.sadEyes),
        Func(self.toon2.blinkEyes),
        LerpPosHprInterval(camera, duration=1, pos=Point3(9, -14, 4), hpr=(100, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "I... Thank you...", CFSpeech | CFTimeout), SoundInterval(self.catEmotionalSpeech),
        Wait(2),
        Func(self.nametagJ2.clearChat),
        LerpPosHprInterval(camera, duration=1, pos=Point3(8, -13.6, 4), hpr=(100, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ.setChat, "Mhm..", CFSpeech | CFTimeout), SoundInterval(self.catShortSpeech),
        Wait(1.5),
        Func(self.nametagJ.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(5, -13.1, 3.8), hpr=(100, 0, 0), blendType='easeInOut'),
        Wait(1.5),
        Func(self.toon.showSmileMuzzle),
        Func(self.toon.normalEyes),
        Func(self.toon.closeEyes),
        Func(self.nametagJ.setChat, "<3", CFSpeech | CFTimeout), SoundInterval(self.catShortSpeech),
        Wait(2),
        Func(self.nametagJ.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(4, -13.6, 4), hpr=(100, 0, 0), blendType='easeInOut'),
        Wait(1.5),
        Func(self.toon2.showSmileMuzzle),
        Func(self.toon2.normalEyes),
        Func(self.toon2.closeEyes),
        Func(self.nametagJ2.setChat, "<3", CFSpeech | CFTimeout), SoundInterval(self.catShortSpeech),
        Wait(2),
        Func(self.nametagJ2.clearChat),
        Func(self.toon.hideSmileMuzzle),
        Func(self.toon.openEyes),
        Func(self.toon.normalEyes),
        Func(self.toon2.hideSmileMuzzle),
        Func(self.toon2.openEyes),
        Func(self.toon2.normalEyes),
        LerpPosHprInterval(camera, duration=0, pos=Point3(5, -13.1, 4), hpr=(100, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ.setChat, "So, are you gonna stop him now?", CFSpeech | CFTimeout), SoundInterval(self.catQuestionSpeech),
        Wait(2),
        Func(self.nametagJ.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(6, -13.6, 4), hpr=(100, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "Mhm, and I'm ready.", CFSpeech | CFTimeout), SoundInterval(self.catLongSpeech),
        Wait(2),
        Func(self.nametagJ2.clearChat),
        Func(self.toon.loop, 'neutral'), Func(self.toon.loop, 'neutral'),
        LerpPosHprInterval(camera, duration=0.8, pos=Point3(10, -13.6, 4), hpr=(100, 0, 0), blendType='easeInOut'),
        Func(self.toon2.loop, 'jump'), Func(self.toon2.loop, 'jump'),
        LerpPosHprInterval(self.toon2, duration=1.5, pos=Point3(0, -16, 0.5), hpr=(180, 0, 0), blendType='noBlend'),
        Func(self.toon2.loop, 'walk'), Func(self.toon2.loop, 'walk'),
        LerpPosHprInterval(self.toon2, duration=2, pos=Point3(0, -23, 0.5), hpr=(180, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.toon2, duration=0.5, pos=Point3(0, -23, 0.5), hpr=(90, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.toon2, duration=1.5, pos=Point3(-12, -23, 0.5), hpr=(90, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.toon2, duration=1, pos=Point3(-12, -23, 0.5), hpr=(180, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(camera, duration=1.2, pos=Point3(0, -18, 3.5), hpr=(0, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ.setChat, ":(", CFSpeech | CFTimeout), SoundInterval(self.catShortSpeech),
        Wait(2),
        Func(self.nametagJ.clearChat),
        LerpPosHprInterval(camera, duration=1, pos=Point3(-12, -17, 3), hpr=(180, 10, 0), blendType='easeInOut'),
        LerpPosHprInterval(self.toon2, duration=0.5, pos=Point3(-12, -23, 0.5), hpr=(180, 0, 0), blendType='noBlend'),
        Func(self.toon2.loop, 'neutral'), Func(self.toon2.loop, 'neutral'),
        Wait(1),
        Func(self.toon2.loop, 'walk'), Func(self.toon2.loop, 'walk'),
        LerpPosHprInterval(self.toon2, duration=1, pos=Point3(-12, -23, 0.5), hpr=(0, 0, 0), blendType='noBlend'),
        Func(self.toon2.loop, 'neutral'), Func(self.toon2.loop, 'neutral'),
        Func(self.nametagJ2.setChat, "?", CFSpeech | CFTimeout), SoundInterval(self.catQuestionSpeech),
        Wait(2),
        Func(self.nametagJ2.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(0, -18, 3.5), hpr=(0, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ.setChat, "You didn't kiss me. T_T", CFSpeech | CFTimeout), SoundInterval(self.catLongSpeech),
        Wait(2),
        Func(self.nametagJ.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(-12, -17, 3), hpr=(180, 10, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "Ahh, no me sowwy.", CFSpeech | CFTimeout), SoundInterval(self.catMedSpeech),
        Wait(2),
        Func(self.nametagJ2.clearChat),
        Func(self.toon.loop, 'walk'), Func(self.toon.loop, 'walk'),
        Parallel(LerpPosHprInterval(camera, duration=1, pos=Point3(10, -13.6, 4), hpr=(90, 0, 0), blendType='easeInOut')),
        LerpPosHprInterval(self.toon, duration=1, pos=Point3(0, -13.5, 0.5), hpr=(90, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.toon, duration=2, pos=Point3(-12, -13.5, 0.5), hpr=(90, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.toon, duration=1, pos=Point3(-12, -13.5, 0.5), hpr=(180, 0, 0), blendType='noBlend'),
        Parallel(LerpPosHprInterval(camera, duration=1.5, pos=Point3(10, -18.6, 4), hpr=(90, 0, 0), blendType='easeInOut')),
        LerpPosHprInterval(self.toon, duration=3, pos=Point3(-12, -20, 0.5), hpr=(180, 0, 0), blendType='noBlend'),
        Func(self.toon.loop, 'neutral'), Func(self.toon.loop, 'neutral'),
        LerpPosHprInterval(camera, duration=1.5, pos=Point3(-6, -20.6, 4), hpr=(90, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ.setChat, "*Kisses*", CFSpeech | CFTimeout), SoundInterval(self.catShortSpeech),
        Wait(2),
        Func(self.nametagJ.clearChat),
        Func(self.nametagJ2.setChat, "*Kisses back*", CFSpeech | CFTimeout), SoundInterval(self.catShortSpeech),
        Wait(2),
        Func(self.nametagJ2.clearChat),
        Func(base.transitions.irisOut, 0),
        LerpPosHprInterval(self.TableProp, duration=0, pos=Point3(-12, -20, -12), hpr=(0, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.TableProp2, duration=0, pos=Point3(-12, -20, -12), hpr=(0, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.TableProp3, duration=0, pos=Point3(-12, -20, -12), hpr=(0, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.TableProp4, duration=0, pos=Point3(-12, -20, -12), hpr=(0, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.toon, duration=0, pos=Point3(-12, -20, -12), hpr=(0, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.toon2, duration=0, pos=Point3(-12, -20, -12), hpr=(180, 0, 0), blendType='noBlend'), 
        Wait(3),
        Func(self.sonicintrosong.play),
        Func(base.transitions.irisIn, 1.5),
        Func(self.changeModels),
        LerpPosHprInterval(camera, duration=0, pos=Point3(0, -20, 4), hpr=(180, 0, 0), blendType='easeInOut'),
        LerpPosHprInterval(camera, duration=3.5, pos=Point3(0, -8, 4), hpr=(180, 0, 0), blendType='easeInOut'),
        LerpPosHprInterval(self.toon3, duration=0, pos=Point3(0, -15, 0.5), hpr=(180, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.TableProp5, duration=0, pos=Point3(0, 29, 0), hpr=(0, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.TableProp6, duration=0, pos=Point3(0, -29, 0), hpr=(180, 0, 0), blendType='noBlend'),
        Wait(2),
        Sequence(LerpPosHprInterval(camera, duration=1.5, pos=Point3(0, -19, 4), hpr=(0, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ3.setChat, "Ugh, I can't take this.", CFSpeech | CFTimeout), SoundInterval(self.dogMedSpeech), SoundInterval(self.dogShortSpeech),
        Wait(2),
        Func(self.nametagJ3.setChat, "Knowing that Master Stink Cat is around, I can't execute my plan.", CFSpeech | CFTimeout), SoundInterval(self.dogLongSpeech), SoundInterval(self.dogLongSpeech),
        Wait(2),
        Func(self.nametagJ3.clearChat),
        LerpPosHprInterval(camera, duration=0.3, pos=Point3(0, -25, 4), hpr=(0, 0, 0), blendType='easeInOut'),
        LerpPosHprInterval(self.TableProp7, duration=0.25, pos=Point3(-10, -15, 0), hpr=(180, 0, 0), blendType='noBlend'),
        SoundInterval(self.tonCrashSfx),
        Func(self.toon3.pose, 'cringe', 30), Func(self.toon3.pose, 'cringe', 30),
        LerpPosHprInterval(self.toon3, duration=0, pos=Point3(0, -15, 0.5), hpr=(90, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(camera, duration=0, pos=Point3(0, -21, 4), hpr=(0, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ3.setChat, "Wot?", CFSpeech | CFTimeout), SoundInterval(self.dogQuestionSpeech),
        Wait(2),
        Func(self.nametagJ3.clearChat),
        LerpPosHprInterval(camera, duration=1, pos=Point3(-10, -21, 4), hpr=(0, 0, 0), blendType='easeInOut'),
        Wait(2),
        LerpPosHprInterval(camera, duration=1, pos=Point3(-10, -24, 4), hpr=(0, 0, 0), blendType='easeInOut'),
        LerpPosHprInterval(camera, duration=1, pos=Point3(-10, -24, 7), hpr=(0, 0, 0), blendType='easeInOut'),
        LerpPosHprInterval(self.Rose, duration=2, pos=Point3(-10, -15, 4.5), hpr=(270, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(camera, duration=1, pos=Point3(12, -15, 4), hpr=(90, 15, 0), blendType='easeInOut'),
        Func(self.nametagJ4.setChat, "What's up, Redsonic?", CFSpeech | CFTimeout), SoundInterval(self.cogQuestionSpeech),
        Wait(2.5),
        Func(self.nametagJ4.clearChat),
        Sequence(LerpPosHprInterval(camera, duration=0.5, pos=Point3(-1, -15, 4), hpr=(270, 0, 0), blendType='easeInOut'),
        Func(self.toon3.showSurpriseMuzzle),
        Func(self.toon3.surpriseEyes),
        Func(self.toon3.blinkEyes),
        Func(self.toon3.pose, 'conked', 30), Func(self.toon3.pose, 'conked', 30),
        Parallel(SoundInterval(self.alarmAlertSfx)),
        Func(self.nametagJ3.setChat, "Hollywood???!", CFSpeech | CFTimeout), SoundInterval(self.dogExclaimSpeech), SoundInterval(self.dogQuestionSpeech),
        Wait(2.5),
        Func(self.nametagJ3.clearChat),
        LerpPosHprInterval(camera, duration=1, pos=Point3(-7, -15, 3), hpr=(280, 0, 0), blendType='easeInOut'),
        Func(self.toon3.hideSurpriseMuzzle),
        Func(self.toon3.showAngryMuzzle),
        Func(self.toon3.angryEyes),
        Func(self.toon3.blinkEyes),
        Func(self.toon3.pose, 'angry', 30), Func(self.toon3.pose, 'angry', 30),
        Func(self.nametagJ3.setChat, "How did you get here!?", CFSpeech | CFTimeout), SoundInterval(self.dogExclaimSpeech), SoundInterval(self.dogQuestionSpeech),
        Wait(2.5),
        Func(self.nametagJ3.clearChat),
        LerpPosHprInterval(camera, duration=1, pos=Point3(12, -15, 4), hpr=(90, 15, 0), blendType='easeInOut'),
        Func(self.nametagJ4.setChat, "It's simple.", CFSpeech | CFTimeout), SoundInterval(self.cogStatementSpeech),
        Wait(2.5),
        Func(self.nametagJ4.setChat, "We have a secret lab of Toons.", CFSpeech | CFTimeout), SoundInterval(self.cogMurmurSpeech), SoundInterval(self.cogStatementSpeech),
        Wait(3),
        LerpPosHprInterval(camera, duration=0.8, pos=Point3(5, -14, 11), hpr=(100, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ4.setChat, "And in every one of those labs, we receive data.", CFSpeech | CFTimeout), SoundInterval(self.cogStatementSpeech), SoundInterval(self.cogGruntSpeech),
        Wait(3),
        LerpPosHprInterval(camera, duration=0.8, pos=Point3(4, -10, 11), hpr=(110, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ4.setChat, "Does that make any sense now?", CFSpeech | CFTimeout), SoundInterval(self.cogQuestionSpeech),
        Wait(3),
        Func(self.nametagJ4.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(-7, -15, 3), hpr=(280, 0, 0), blendType='easeInOut'),
        Func(self.toon3.pose, 'bored', 50), Func(self.toon3.pose, 'bored', 50),
        Func(self.nametagJ3.setChat, "No, and I don't care.", CFSpeech | CFTimeout), SoundInterval(self.dogLongSpeech),
        Wait(2.5),
        Func(self.nametagJ3.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(6, -10, 12), hpr=(110, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ4.setChat, "Aw, such a shame...", CFSpeech | CFTimeout), SoundInterval(self.cogEmotionalSpeech),
        Wait(3),
        Func(self.nametagJ4.setChat, "However, I'd like to share a little quote with you that I got from someone.", CFSpeech | CFTimeout), SoundInterval(self.cogStatementSpeech),
        Wait(3),
        Func(self.nametagJ4.clearChat),
        LerpPosHprInterval(self.Rose, duration=2, pos=Point3(-10, -15, -20), hpr=(-270, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.Rose, duration=2, pos=Point3(-8, -15, -20), hpr=(270, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(camera, duration=2, pos=Point3(-4, -29, 3), hpr=(0, 13, 0), blendType='easeInOut'),
        LerpPosHprInterval(self.Rose, duration=1, pos=Point3(-8, -15, 0), hpr=(270, 0, 0), blendType='noBlend'),
        Func(self.nametagJ4.setChat, "When did a good sir like you become so aggressive around the mighty Mr. Hollywood??", CFSpeech | CFTimeout), SoundInterval(self.cogQuestionSpeech), SoundInterval(self.cogQuestionSpeech),
        Wait(3),
        Func(self.nametagJ4.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(-5, -15, 4), hpr=(270, 0, 0), blendType='easeInOut'),
        Func(self.toon3.loop, 'neutral'), Func(self.toon3.loop, 'neutral'),
        Func(self.nametagJ3.setChat, "I didn't, thank you very much.", CFSpeech | CFTimeout), SoundInterval(self.dogLongSpeech),
        Wait(2.5),
        Func(self.nametagJ3.clearChat),
        LerpPosHprInterval(camera, duration=2, pos=Point3(8, -15, 8), hpr=(90, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ4.setChat, "Such a shame, I thought you would have.", CFSpeech | CFTimeout), SoundInterval(self.cogMurmurSpeech),
        Wait(3),
        LerpPosHprInterval(camera, duration=0.6, pos=Point3(6, -15, 9), hpr=(90, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ4.setChat, "That's it. Since you saw no potental, I'm banning all gags.", CFSpeech | CFTimeout), SoundInterval(self.cogStatementSpeech),
        Wait(3),
        Func(self.nametagJ4.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(-5, -15, 4), hpr=(270, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ3.setChat, "Ugh... Banned all gags, really?", CFSpeech | CFTimeout), SoundInterval(self.dogEmotionalSpeech), SoundInterval(self.dogQuestionSpeech),
        Wait(2.5),
        Func(self.nametagJ3.clearChat),
        Func(self.toon3.pose, 'angry', 30), Func(self.toon3.pose, 'angry', 30),
        LerpPosHprInterval(camera, duration=0, pos=Point3(0, -28, 3), hpr=(0, 11, 0), blendType='easeInOut'),
        Func(self.nametagJ3.setChat, "Whatever, I'm out of here.", CFSpeech | CFTimeout), SoundInterval(self.dogShortSpeech), SoundInterval(self.dogShortSpeech), SoundInterval(self.dogMedSpeech), SoundInterval(self.dogLongSpeech),
        Wait(2.5),
        Func(self.nametagJ3.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(0, -28, 3), hpr=(0, 11, 0), blendType='easeInOut'),
        Func(self.nametagJ3.setChat, "I'm gonna go fight Master Cool Cat.", CFSpeech | CFTimeout), SoundInterval(self.dogLongSpeech), SoundInterval(self.dogLongSpeech),
        Wait(2.5),
        Func(self.nametagJ3.clearChat),
        LerpPosHprInterval(camera, duration=0.6, pos=Point3(20, -12, 5), hpr=(90, 0, 0), blendType='easeInOut'),
        Func(self.toon3.loop, 'walk'), Func(self.toon3.loop, 'walk'),
        LerpPosHprInterval(self.toon3, duration=3, pos=Point3(0, -15, 0.5), hpr=(0, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.toon3, duration=3, pos=Point3(0, -5, 0.5), hpr=(0, 0, 0), blendType='noBlend'),
        Func(self.Rose.loop, 'walk'), Func(self.Rose.loop, 'walk'),
        Parallel(LerpPosHprInterval(self.toon3, duration=3, pos=Point3(0, 5, 0.5), hpr=(0, 0, 0), blendType='noBlend'),
        Sequence(LerpPosHprInterval(self.Rose, duration=3, pos=Point3(0, -15, 0), hpr=(270, 0, 0), blendType='noBlend'),
        Parallel(LerpPosHprInterval(self.toon3, duration=3, pos=Point3(0, 15, 0.5), hpr=(0, 0, 0), blendType='noBlend'),
        Sequence(LerpPosHprInterval(self.Rose, duration=3, pos=Point3(0, -15, 0), hpr=(0, 0, 0), blendType='noBlend'),
        Func(self.Rose.loop, 'neutral'), Func(self.Rose.loop, 'neutral'),
        Func(self.toon3.loop, 'neutral'), Func(self.toon3.loop, 'neutral'),
        Wait(2),
        LerpPosHprInterval(camera, duration=1, pos=Point3(0, -12, 6), hpr=(180, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ4.setChat, "You're doomed, Toon!", CFSpeech | CFTimeout), SoundInterval(self.cogStatementSpeech), SoundInterval(self.cogGruntSpeech),
        Wait(3),
        LerpPosHprInterval(camera, duration=1, pos=Point3(0, -9, 6), hpr=(180, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ4.setChat, "You will not mess with the Mr. Hollywood!", CFSpeech | CFTimeout), SoundInterval(self.cogMurmurSpeech), SoundInterval(self.cogGruntSpeech),
        Wait(2.5),
        Func(self.nametagJ4.clearChat),
        Func(base.transitions.irisOut, 0),
        Func(self.sonicintrosong.stop),
        LerpPosHprInterval(self.toon3, duration=0, pos=Point3(0, 15, -10.5), hpr=(0, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.Rose, duration=0, pos=Point3(0, -15, -20), hpr=(0, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.TableProp4, duration=0, pos=Point3(-10, -15, -40), hpr=(180, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.TableProp5, duration=0, pos=Point3(-10, -15, -40), hpr=(180, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.TableProp7, duration=0, pos=Point3(-10, -15, -40), hpr=(180, 0, 0), blendType='noBlend'),
        Wait(3),
        Func(self.HQsong.play),
        Parallel(Func(base.transitions.irisIn, 1.5),
        Sequence(LerpPosHprInterval(camera, duration=7, pos=Point3(0, -9, 6), hpr=(90, 0, 0), blendType='easeInOut'),
        Func(self.CogHQModels))))))))))

        GoodTrack.start()
        
    def changeModels(self):
        self.houseVariable.removeNode()
        self.placeVariable.reparentTo(render)

    def CogHQModels(self):
        self.placeVariable.removeNode()
        self.HQVariable.reparentTo(render)