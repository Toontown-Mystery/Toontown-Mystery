from direct.gui.DirectGui import *
from panda3d.core import *
from direct.interval.IntervalGlobal import *
from libotp import *
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from panda3d.toontown import DNAStorage
from toontown.toon import NPCToons
from toontown.suit import Suit
from toontown.suit import SuitDNA
from toontown.battle import BattleProps
from direct.distributed.DistributedObject import DistributedObject
class AnimationRedSonic(DistributedObject):

    def __init__(self, leaveFunction):
        self.mixsong = base.loader.loadMusic('phase_14/audio/bgm/estate_interior.ogg')
        self.sonicintrosong = base.loader.loadMusic('phase_14/audio/bgm/CFO_win.ogg')
        self.HQsong = base.loader.loadMusic('phase_9/audio/bgm/CogHQ_Stage_bg.ogg')
        self.battlesong = base.loader.loadMusic('phase_14/audio/bgm/SBHQ_prepare_objective.ogg')
        self.sonicpreparesong = base.loader.loadMusic('phase_14/audio/bgm/Boss_Prepare.ogg')
        self.factorysong = base.loader.loadMusic('phase_14/audio/bgm/Factory_Music.ogg')
        self.mintsong = base.loader.loadMusic('phase_14/audio/bgm/CHQ_MINT_bg.ogg')

    def create(self):
        base.playMusic(self.mintsong, looping=1, volume=1)

        base.playMusic(self.factorysong, looping=1, volume=2)

        base.playMusic(self.sonicpreparesong, looping=1, volume=1)
        
        base.playMusic(self.battlesong, looping=1, volume=1)

        base.playMusic(self.HQsong, looping=1, volume=1)

        base.playMusic(self.mixsong, looping=1, volume=1)

        self.houseVariable = loader.loadModel('phase_5.5/models/estate/tt_m_ara_int_estateHouseB.bam')
        self.houseVariable.reparentTo(render)
        
        self.placeVariable = loader.loadModel('phase_7/models/modules/suit_interior.bam')

        self.HQVariable = loader.loadModel('phase_9/models/cogHQ/SellbotHQExterior.bam')

        self.sonicplaceVariable = loader.loadModel('phase_7/models/modules/suit_interior.bam')

        self.factoryVariable = loader.loadModel('phase_9/models/cogHQ/SelbotLegFactory.bam')

        self.otherVariable = loader.loadModel('phase_10/models/cashbotHQ/ZONE03a.bam')

        self.mintVariable = loader.loadModel('phase_10/models/cashbotHQ/ZONE08a.bam')

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

        self.TableProp8 = loader.loadModel('phase_4/models/minigames/toonblitz_game_elevator.bam')
        self.TableProp8.setPos(64, 0, -20)
        self.TableProp8.setHpr(90, 0, 0)
        self.TableProp8.setScale(1)
        self.TableProp8.reparentTo(render)

        self.TableProp9 = loader.loadModel('phase_4/models/minigames/toonblitz_game_elevator.bam')
        self.TableProp9.setPos(64, 0, -20)
        self.TableProp9.setHpr(90, 0, 0)
        self.TableProp9.setScale(1)
        self.TableProp9.reparentTo(render)

        self.CarProp = loader.loadModel('phase_5/models/cogdominium/tt_m_ara_csa_memo.bam')
        self.CarProp.setPos(60, 0, -15)
        self.CarProp.setHpr(90, 0, 0)
        self.CarProp.reparentTo(render)

        self.CarPropTexture = loader.loadTexture('phase_14/maps/map.jpg')
        self.CarProp.setTexture(self.CarPropTexture, 1)

        self.map = loader.loadModel('phase_5/models/cogdominium/tt_m_ara_csa_memo.bam')
        self.map.setScale(1.5)

        self.mapTexture = loader.loadTexture('phase_14/maps/map.jpg')
        self.map.setTexture(self.mapTexture, 1)

        self.book = loader.loadModel('phase_3.5/models/props/book-mod.bam')
        self.book.setScale(0.7)

        self.button = loader.loadModel('phase_3.5/models/props/button.bam')
        self.button.setScale(1)

        self.gun = loader.loadModel('phase_4/models/props/water-gun.bam')
        self.gun.setScale(1)

        self.gun2 = loader.loadModel('phase_4/models/props/cog-gun.bam')
        self.gun2.setScale(1)
        
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

        self.suit = Suit.Suit()
        self.suit.dna = SuitDNA.SuitDNA()
        self.suit.dna.newSuit('m')
        self.suit.setDNA(self.suit.dna)
        self.suit.setPos(20, 106, -20)
        self.suit.setHpr(180, 0, 0)
        self.suit.loop('neutral')
        self.suit.reparentTo(render)
        self.suit = self.suit
        
        self.nametagJ5 = None
        self.nametagS5 = None
        self.nametagJ5 = NametagGroup()
        self.nametagJ5.setAvatar(self.suit)
        self.nametagJ5.setFont(ToontownGlobals.getToonFont())
        self.nametagJ5.setName('')
        self.nametagJ5.manage(base.marginManager)
        self.nametagJ5.getNametag3d().setBillboardOffset(4)
        nametagNode5 = self.nametagJ5.getNametag3d().upcastToPandaNode()
        self.nametagS5 = self.suit.attachNewNode(nametagNode5)
        self.nametagS5.setPos(0, 0, 7.5)

        self.suit2 = Suit.Suit()
        self.suit2.dna = SuitDNA.SuitDNA()
        self.suit2.dna.newSuit('ls')
        self.suit2.setDNA(self.suit2.dna)
        self.suit2.setPos(30, 6, -20)
        self.suit2.setHpr(270, 0, 0)
        self.suit2.loop('speak')
        self.suit2.reparentTo(render)
        self.suit2 = self.suit2
        
        self.nametagJ6 = None
        self.nametagS6 = None
        self.nametagJ6 = NametagGroup()
        self.nametagJ6.setAvatar(self.suit2)
        self.nametagJ6.setFont(ToontownGlobals.getToonFont())
        self.nametagJ6.setName('')
        self.nametagJ6.manage(base.marginManager)
        self.nametagJ6.getNametag3d().setBillboardOffset(4)
        nametagNode6 = self.nametagJ6.getNametag3d().upcastToPandaNode()
        self.nametagS6 = self.suit2.attachNewNode(nametagNode6)
        self.nametagS6.setPos(0, 0, 7.5)

        self.suit3 = Suit.Suit()
        self.suit3.dna = SuitDNA.SuitDNA()
        self.suit3.dna.newSuit('rb')
        self.suit3.setDNA(self.suit3.dna)
        self.suit3.setPos(40, 6, -20)
        self.suit3.setHpr(90, 0, 0)
        self.suit3.loop('neutral')
        self.suit3.reparentTo(render)
        self.suit3 = self.suit3
        
        self.nametagJ7 = None
        self.nametagS7 = None
        self.nametagJ7 = NametagGroup()
        self.nametagJ7.setAvatar(self.suit3)
        self.nametagJ7.setFont(ToontownGlobals.getToonFont())
        self.nametagJ7.setName('')
        self.nametagJ7.manage(base.marginManager)
        self.nametagJ7.getNametag3d().setBillboardOffset(4)
        nametagNode7 = self.nametagJ7.getNametag3d().upcastToPandaNode()
        self.nametagS7 = self.suit3.attachNewNode(nametagNode7)
        self.nametagS7.setPos(0, 0, 8.5)
        
        camera.setPos(0, -25, 5)
        camera.setHpr(0, 0, 0)

        self.cogGruntSpeech = base.loader.loadSfx('phase_14/audio/sfx/COG_VO_grunt.ogg')
        self.cogMurmurSpeech = base.loader.loadSfx('phase_14/audio/sfx/COG_VO_murmur.ogg')
        self.cogStatementSpeech = base.loader.loadSfx('phase_14/audio/sfx/COG_VO_statement.ogg')
        self.cogQuestionSpeech = base.loader.loadSfx('phase_14/audio/sfx/COG_VO_question.ogg')
        self.angelGruntSpeech = base.loader.loadSfx('phase_14/audio/sfx/Angel_COG_VO_grunt.ogg')
        self.angelMurmurSpeech = base.loader.loadSfx('phase_14/audio/sfx/Angel_COG_VO_murmur.ogg')
        self.angelStatementSpeech = base.loader.loadSfx('phase_14/audio/sfx/Angel_COG_VO_statement.ogg')
        self.angelQuestionSpeech = base.loader.loadSfx('phase_14/audio/sfx/Angel_COG_VO_question.ogg')
        self.mimiGruntSpeech = base.loader.loadSfx('phase_14/audio/sfx/Mimi_COG_VO_grunt.ogg')
        self.mimiMurmurSpeech = base.loader.loadSfx('phase_14/audio/sfx/Mimi_COG_VO_murmur.ogg')
        self.mimiStatementSpeech = base.loader.loadSfx('phase_14/audio/sfx/Mimi_COG_VO_statement.ogg')
        self.mimiQuestionSpeech = base.loader.loadSfx('phase_14/audio/sfx/Mimi_COG_VO_question.ogg')
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
        self.HoldUpSfx = base.loader.loadSfx('phase_14/audio/sfx/record_scratch.ogg')
        self.ExplosionSfx = base.loader.loadSfx('phase_3.5/audio/sfx/ENC_cogfall_apart.ogg')

        self.accept('2', self.goToSceneTwo)
        self.accept('3', self.goToSceneThree)
        self.accept('4', self.goToSceneFour)
        self.accept('5', self.goToSceneFive)
        self.accept('6', self.goToSceneSix)
        self.accept('7', self.goToSceneSeven)

        self.enterTrack = Sequence(Wait(3), Func(base.transitions.irisIn, 1), Func(self.mixsong.play), Func(self.sceneOne))
        self.enterTrack.start()
        
    def sceneOne(self):
        self.GoodTrack = Sequence(
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
        LerpPosHprInterval(self.toon3, duration=0, pos=Point3(0, -15, 0.5), hpr=(180, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.TableProp5, duration=0, pos=Point3(0, 29, 0), hpr=(0, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.TableProp6, duration=0, pos=Point3(0, -29, 0), hpr=(180, 0, 0), blendType='noBlend'),
        Wait(3),
        Func(self.sonicintrosong.play),
        Func(base.transitions.irisIn, 1.5),
        Func(self.sceneTwo))
        self.GoodTrack.start()
        
    def sceneTwo(self):
        self.sceneTwoTrack = Sequence(		
        Func(self.changeModels),
        LerpPosHprInterval(camera, duration=0, pos=Point3(0, -20, 4), hpr=(180, 0, 0), blendType='easeInOut'),
        LerpPosHprInterval(camera, duration=3.5, pos=Point3(0, -8, 4), hpr=(180, 0, 0), blendType='easeInOut'),
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
        Func(self.nametagJ3.setChat, "Sunlight Elvis???!", CFSpeech | CFTimeout), SoundInterval(self.dogExclaimSpeech), SoundInterval(self.dogQuestionSpeech),
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
        LerpPosHprInterval(camera, duration=0.8, pos=Point3(3, -14, 11), hpr=(100, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ4.setChat, "And in every one of those labs, we receive data.", CFSpeech | CFTimeout), SoundInterval(self.cogStatementSpeech), SoundInterval(self.cogGruntSpeech),
        Wait(3),
        LerpPosHprInterval(camera, duration=0.8, pos=Point3(0, -10, 12), hpr=(110, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ4.setChat, "Does that make any sense now?", CFSpeech | CFTimeout), SoundInterval(self.cogQuestionSpeech),
        Wait(3),
        Func(self.nametagJ4.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(-7, -15, 3), hpr=(280, 0, 0), blendType='easeInOut'),
        Func(self.toon3.pose, 'bored', 50), Func(self.toon3.pose, 'bored', 50),
        Func(self.nametagJ3.setChat, "No, and I don't care.", CFSpeech | CFTimeout), SoundInterval(self.dogLongSpeech),
        Wait(2.5),
        Func(self.nametagJ3.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(4, -10, 12), hpr=(110, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ4.setChat, "Aw, such a shame...", CFSpeech | CFTimeout), SoundInterval(self.cogEmotionalSpeech),
        Wait(3),
        Func(self.nametagJ4.setChat, "However, I'd like to share a little quote with you that I got from someone.", CFSpeech | CFTimeout), SoundInterval(self.cogStatementSpeech),
        Wait(3),
        Func(self.nametagJ4.clearChat),
        LerpPosHprInterval(self.Rose, duration=2, pos=Point3(-10, -15, -20), hpr=(-270, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.Rose, duration=2, pos=Point3(-8, -15, -20), hpr=(270, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(camera, duration=2, pos=Point3(-4, -29, 3), hpr=(0, 13, 0), blendType='easeInOut'),
        LerpPosHprInterval(self.Rose, duration=3, pos=Point3(-8, -15, 0), hpr=(270, 0, 0), blendType='noBlend'),
        Func(self.nametagJ4.setChat, "What made a good sir like you want to judge the almighty Sunlight Elvis?", CFSpeech | CFTimeout), SoundInterval(self.cogQuestionSpeech), SoundInterval(self.cogQuestionSpeech),
        Wait(3),
        Func(self.nametagJ4.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(-5, -15, 4), hpr=(270, 0, 0), blendType='easeInOut'),
        Func(self.toon3.loop, 'neutral'), Func(self.toon3.loop, 'neutral'),
        Func(self.nametagJ3.setChat, "I didn't, thank you very much.", CFSpeech | CFTimeout), SoundInterval(self.dogLongSpeech),
        Wait(2.5),
        Func(self.nametagJ3.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(4, -15, 8), hpr=(90, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ4.setChat, "Such a shame, I thought you would have.", CFSpeech | CFTimeout), SoundInterval(self.cogMurmurSpeech),
        Wait(3),
        LerpPosHprInterval(camera, duration=0.6, pos=Point3(2, -15, 9), hpr=(90, 0, 0), blendType='easeInOut'),
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
        LerpPosHprInterval(camera, duration=0, pos=Point3(0, -28, 3), hpr=(0, 11, 0), blendType='easeInOut'),
        Func(self.nametagJ3.setChat, "I'm gonna go fight Master Cool Cat.", CFSpeech | CFTimeout), SoundInterval(self.dogLongSpeech), SoundInterval(self.dogLongSpeech),
        Wait(2.5),
        Func(self.nametagJ3.clearChat),
        LerpPosHprInterval(camera, duration=0.6, pos=Point3(20, -12, 5), hpr=(90, 0, 0), blendType='easeInOut'),
        Func(self.toon3.loop, 'walk'), Func(self.toon3.loop, 'walk'),
        LerpPosHprInterval(self.toon3, duration=3, pos=Point3(0, -15, 0.5), hpr=(0, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.toon3, duration=3, pos=Point3(0, -5, 0.5), hpr=(0, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.toon3, duration=3, pos=Point3(0, 5, 0.5), hpr=(0, 0, 0), blendType='noBlend'),
        Func(self.Rose.loop, 'walk'), Func(self.Rose.loop, 'walk'),
        LerpPosHprInterval(self.Rose, duration=3, pos=Point3(0, -15, 0), hpr=(270, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.toon3, duration=0, pos=Point3(0, 15, 0.5), hpr=(0, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.Rose, duration=3, pos=Point3(0, -15, 0), hpr=(0, 0, 0), blendType='noBlend'),
        Func(self.Rose.loop, 'neutral'), Func(self.Rose.loop, 'neutral'),
        Func(self.toon3.loop, 'neutral'), Func(self.toon3.loop, 'neutral'),
        Wait(2),
        LerpPosHprInterval(camera, duration=1, pos=Point3(0, -2, 7), hpr=(180, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ4.setChat, "You're doomed, Toon!", CFSpeech | CFTimeout), SoundInterval(self.cogStatementSpeech), SoundInterval(self.cogGruntSpeech),
        Wait(3),
        LerpPosHprInterval(camera, duration=1, pos=Point3(0, -5, 8), hpr=(180, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ4.setChat, "You will not mess with the Sunlight Elvis!", CFSpeech | CFTimeout), SoundInterval(self.cogMurmurSpeech), SoundInterval(self.cogGruntSpeech),
        Wait(2.5),
        Func(self.nametagJ4.clearChat),
        Func(base.transitions.irisOut, 0),
        Func(self.sonicintrosong.stop)),
        LerpPosHprInterval(self.toon3, duration=0, pos=Point3(0, 15, -10.5), hpr=(0, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.CarProp, duration=0, pos=Point3(-55, -135, -50), hpr=(180, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.Rose, duration=0, pos=Point3(0, -15, -20), hpr=(0, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.TableProp5, duration=0, pos=Point3(-10, -15, -40), hpr=(180, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.TableProp6, duration=0, pos=Point3(-10, -15, -40), hpr=(180, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.TableProp7, duration=0, pos=Point3(-10, -15, -40), hpr=(180, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.toon2, duration=0, pos=Point3(-8, -55, -12), hpr=(270, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(camera, duration=0, pos=Point3(40, -145, 8), hpr=(180, 0, 0), blendType='easeInOut'),
        Wait(3),
        Func(self.HQsong.play),
        Func(base.transitions.irisIn, 1.5)),
        Func(self.sceneThree))
        self.sceneTwoTrack.start()
      
    def sceneThree(self):
        self.sceneThreeTrack = Sequence(
        Func(self.CogHQModels),
        Func(base.transitions.irisIn, 1.5),
        LerpPosHprInterval(camera, duration=7, pos=Point3(50, -105, 4), hpr=(90, 0, 0), blendType='easeInOut'),
        Wait(2),
        LerpPosHprInterval(camera, duration=5, pos=Point3(-20, -105, 4), hpr=(90, 0, 0), blendType='easeInOut'),
        Wait(2),
        Func(self.toon2.loop, 'jump'), Func(self.toon2.loop, 'jump'),
        LerpPosHprInterval(self.toon2, duration=0, pos=Point3(-60, -105, 0.5), hpr=(270, 0, 0), blendType='noBlend'),
        Wait(1.5),
        Func(self.toon2.loop, 'neutral'), Func(self.toon2.loop, 'neutral'),
        Wait(2),
        LerpPosHprInterval(camera, duration=0, pos=Point3(-52, -105, 4), hpr=(90, 0, 0), blendType='easeInOut'),
        Func(self.toon2.pose, 'think', 30), Func(self.toon2.pose, 'think', 30),
        Func(self.nametagJ2.setChat, "Ok. I'm here, so now what?", CFSpeech | CFTimeout), SoundInterval(self.catLongSpeech), SoundInterval(self.catQuestionSpeech),
        Wait(2.5),
        Parallel(LerpPosHprInterval(self.book, duration=0, pos=Point3(-0.5, 0, 0), hpr=(0, 0, 0)), Func(self.book.reparentTo, self.toon2.rightHand), Func(self.book.show), Func(self.toon2.pose, 'book', 60)),
        LerpPosHprInterval(camera, duration=0, pos=Point3(-50, -105, 4), hpr=(100, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "According to this map, there should be secret treasure here.", CFSpeech | CFTimeout), SoundInterval(self.catLongSpeech),
        Wait(2.5),
        LerpPosHprInterval(camera, duration=0, pos=Point3(-50, -95, 4), hpr=(120, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "Only problem is though, I can't seem to locate it.", CFSpeech | CFTimeout), SoundInterval(self.catLongSpeech),
        Wait(2.5),
        Func(self.nametagJ2.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(-50, -135, 4), hpr=(90, 0, 0), blendType='easeInOut'),
        LerpPosHprInterval(self.CarProp, duration=0, pos=Point3(-60, -135, 4), hpr=(90, 0, 0), blendType='noBlend'),
        Wait(2.5),
        LerpPosHprInterval(camera, duration=0, pos=Point3(-52, -105, 4), hpr=(90, 0, 0), blendType='easeInOut'),
        LerpPosHprInterval(self.toon2, duration=0, pos=Point3(-60, -105, 0.5), hpr=(180, 0, 0), blendType='noBlend'),
        Func(self.toon2.loop, 'neutral'), Func(self.toon2.loop, 'neutral'),
        Func(self.nametagJ2.setChat, "Oh, there it is.", CFSpeech | CFTimeout), SoundInterval(self.catMedSpeech),
        Wait(2.5),
        Func(self.nametagJ2.clearChat),
        LerpPosHprInterval(camera, duration=2, pos=Point3(-48, -135, 4), hpr=(90, 0, 0), blendType='easeInOut'),
        Func(self.toon2.loop, 'run'), Func(self.toon2.loop, 'run'),
        LerpPosHprInterval(self.toon2, duration=3, pos=Point3(-60, -135, 0.5), hpr=(180, 0, 0), blendType='noBlend'),
        Func(self.toon2.loop, 'walk'), Func(self.toon2.loop, 'walk'),
        LerpPosHprInterval(self.toon2, duration=2, pos=Point3(-60, -135, 0.5), hpr=(90, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.toon2, duration=3, pos=Point3(-53, -135, 0.5), hpr=(90, 0, 0), blendType='noBlend'),
        Func(self.toon2.loop, 'neutral'), Func(self.toon2.loop, 'neutral'),
        LerpPosHprInterval(camera, duration=2, pos=Point3(-53, -125, 4), hpr=(180, 0, 0), blendType='easeInOut'),
        LerpPosHprInterval(self.book, duration=0, pos=Point3(-0.5, 0, 0), hpr=(0, 0, 0)), Func(self.book.reparentTo, self.toon2.rightHand), Func(self.book.show), Func(self.toon2.pose, 'book', 60),
        Func(self.nametagJ2.setChat, "Hm. What does this say?", CFSpeech | CFTimeout), SoundInterval(self.catShortSpeech), SoundInterval(self.catQuestionSpeech),
        Wait(2.5),
        Func(self.nametagJ2.setChat, "According to the map, it looks like a pathway to freedom.", CFSpeech | CFTimeout), SoundInterval(self.catLongSpeech),
        Wait(2.5),
        LerpPosHprInterval(camera, duration=0, pos=Point3(-57, -120, 4), hpr=(185, 0, 0), blendType='easeInOut'),
        LerpPosHprInterval(camera, duration=0.2, pos=Point3(-61, -124, 4), hpr=(195, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "Whoever enters this land shall perish.", CFSpeech | CFTimeout), SoundInterval(self.catLongSpeech), Wait(2.5),
        LerpPosHprInterval(camera, duration=0.2, pos=Point3(-67, -128, 4), hpr=(210, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "However, you may accept this offer of path, if you just do 1 task.", CFSpeech | CFTimeout), SoundInterval(self.catLongSpeech), Wait(2.5), Func(self.nametagJ2.clearChat),
        Func(self.HQsong.stop),
        LerpPosHprInterval(camera, duration=0.8, pos=Point3(-75, -105, 4), hpr=(235, 0, 0), blendType='easeInOut'),
        SoundInterval(self.HoldUpSfx),
        LerpPosHprInterval(camera, duration=0, pos=Point3(-57, -125, 4), hpr=(185, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "Wait what...", CFSpeech | CFTimeout), SoundInterval(self.catEmotionalSpeech),
        Wait(3),
        Func(self.nametagJ2.setChat, "It's right here though, I can just grab it.", CFSpeech | CFTimeout), SoundInterval(self.catLongSpeech),
        Wait(2.5),
        Func(self.nametagJ2.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(-60.8714, -129.531, 4), hpr=(185, 0, 0), blendType='easeInOut'),
        Func(self.toon2.loop, 'walk'), Func(self.toon2.loop, 'walk'),
        LerpPosHprInterval(self.toon2, duration=1, pos=Point3(-58.8, -135, 0.5), hpr=(90, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(camera, duration=0, pos=Point3(-60.8714, -129.531, 4), hpr=(185, 0, 0), blendType='easeInOut'),
        LerpPosHprInterval(self.book, duration=0, pos=Point3(3, 0, 0), hpr=(3, 0, 0)), Func(self.book.reparentTo, self.toon2.rightHand), Func(self.book.show), Func(self.toon2.pose, 'jump', 20),
        LerpPosHprInterval(self.book, duration=0, pos=Point3(0, 0, 0), hpr=(0, 0, 0)), Func(self.book.reparentTo, self.toon2.rightHand), Func(self.book.hide), Func(self.toon2.pose, 'jump', 20),
        Wait(2),
        LerpPosHprInterval(self.CarProp, duration=0, pos=Point3(-60, -135, -50), hpr=(90, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.map, duration=0, pos=Point3(0, 0, 0), hpr=(3, 0, 0)), Func(self.map.reparentTo, self.toon2.rightHand), Func(self.map.show), Func(self.toon2.pose, 'jump', 20),
        LerpPosHprInterval(self.CarProp, duration=0, pos=Point3(-60.8714, -134.531, -50), hpr=(180, 0, 0), blendType='noBlend'),
        Wait(2),
        Func(self.battlesong.play),
        Func(self.toon2.pose, 'book', 40), Func(self.toon2.pose, 'book', 40),
        LerpPosHprInterval(self.toon2, duration=0, pos=Point3(-60, -135, 0.5), hpr=(90, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(camera, duration=0, pos=Point3(-60.8714, -129.531, 4), hpr=(185, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "Too easy, lol.", CFSpeech | CFTimeout), SoundInterval(self.catMedSpeech),
        Wait(2.5),
        Func(self.nametagJ2.setChat, "Time to go to the next area.", CFSpeech | CFTimeout), SoundInterval(self.catMedSpeech),
        Wait(2.5),
        Func(self.nametagJ2.clearChat),
        Func(base.transitions.irisOut, 0),
        Func(self.battlesong.stop),
        LerpPosHprInterval(self.TableProp, duration=0, pos=Point3(-12, -20, -12), hpr=(0, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.TableProp2, duration=0, pos=Point3(-12, -20, -12), hpr=(0, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.TableProp3, duration=0, pos=Point3(-12, -20, -12), hpr=(0, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.TableProp4, duration=0, pos=Point3(-12, -20, -12), hpr=(0, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.toon, duration=0, pos=Point3(-12, -20, -12), hpr=(0, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.map, duration=0, pos=Point3(0, 0, 0), hpr=(3, 0, 0)), Func(self.map.reparentTo, self.toon2.rightHand), Func(self.map.hide), Func(self.toon2.pose, 'shrug', 20),
        LerpPosHprInterval(self.toon2, duration=0, pos=Point3(-12, -20, -12), hpr=(180, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.toon3, duration=0, pos=Point3(0, -15, 0.5), hpr=(180, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.TableProp5, duration=0, pos=Point3(0, 29, 0), hpr=(0, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.TableProp6, duration=0, pos=Point3(0, -29, 0), hpr=(180, 0, 0), blendType='noBlend'),
        Func(self.toon3.pose, 'bored', 50), Func(self.toon3.pose, 'bored', 50),
        Func(self.toon3.hideAngryMuzzle),
        Func(self.toon3.showSmileMuzzle),
        Func(self.toon3.angryEyes),
        Func(self.toon3.blinkEyes),
        Wait(3),
        Func(self.sonicpreparesong.play),
        Func(base.transitions.irisIn, 1.5),
        Func(self.sceneFour))
        self.sceneThreeTrack.start()
        
    def sceneFour(self):
        self.sceneFourTrack = Sequence(
        Func(self.changeModels2),
        LerpPosHprInterval(camera, duration=0, pos=Point3(0, -19, 4), hpr=(0, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ3.setChat, "Ha. I distracted the Sunlight dude.", CFSpeech | CFTimeout), SoundInterval(self.dogMedSpeech), Wait(0.5), SoundInterval(self.dogMedSpeech),
        Wait(2),
        LerpPosHprInterval(camera, duration=0, pos=Point3(3, -22, 4), hpr=(20, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ3.setChat, "Does he not realize my true colors?", CFSpeech | CFTimeout), SoundInterval(self.dogQuestionSpeech),
        Wait(3),
        Func(self.nametagJ3.setChat, "Pathetic, I thought he'd care.", CFSpeech | CFTimeout), SoundInterval(self.dogLongSpeech),
        Wait(3),
        LerpPosHprInterval(camera, duration=1, pos=Point3(-3, -22, 4), hpr=(-5, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ3.setChat, "Guess my theory was wrong.", CFSpeech | CFTimeout), SoundInterval(self.dogLongSpeech),
        Wait(3),
        Func(self.toon3.hideSmileMuzzle),
        Func(self.toon3.normalEyes),
        Func(self.toon3.blinkEyes),
        Func(self.nametagJ3.setChat, "Oh well, I love proving people wrong. It's so much fun.", CFSpeech | CFTimeout), SoundInterval(self.dogLongSpeech), Wait(0.2), SoundInterval(self.dogLongSpeech),
        Wait(3),
        Func(self.nametagJ3.setChat, "Especially if I get to mess with Master Cool Cat.", CFSpeech | CFTimeout), SoundInterval(self.dogLongSpeech),
        Wait(3),
        Func(self.nametagJ3.clearChat),
        LerpPosHprInterval(camera, duration=1, pos=Point3(0, -24, 4), hpr=(0, 0, 0), blendType='easeInOut'),
        LerpPosHprInterval(self.button, duration=0, pos=Point3(0, 0, 0), hpr=(3, 0, 0)), Func(self.button.reparentTo, self.toon3.leftHand), Func(self.button.show), Func(self.toon3.play, 'pushbutton', fromFrame=0, toFrame=70),
        Wait(2),
        LerpPosHprInterval(self.button, duration=0, pos=Point3(0, 0, 0), hpr=(3, 0, 0)), Func(self.button.reparentTo, self.toon3.leftHand), Func(self.button.show), Func(self.toon3.pose, 'pushbutton', 70),
        LerpPosHprInterval(camera, duration=1, pos=Point3(3, -22, 4), hpr=(30, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ3.setChat, "Get ready Master Cool Cat.", CFSpeech | CFTimeout), SoundInterval(self.dogLongSpeech),
        Wait(3),
        LerpPosHprInterval(camera, duration=0.5, pos=Point3(0, -26, 4), hpr=(0, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ3.setChat, "Redsonic will get you soon.", CFSpeech | CFTimeout), SoundInterval(self.dogLongSpeech),
        Wait(3),
        Func(self.nametagJ3.clearChat),
        Func(base.transitions.irisOut, 0),
        Func(self.button.hide),
        Func(self.sonicpreparesong.stop),
        Wait(2.5),
        LerpPosHprInterval(self.TableProp, duration=0, pos=Point3(-12, -20, -18), hpr=(0, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.TableProp2, duration=0, pos=Point3(-12, -20, -18), hpr=(0, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.TableProp3, duration=0, pos=Point3(-12, -20, -18), hpr=(0, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.TableProp4, duration=0, pos=Point3(-12, -20, -18), hpr=(0, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.TableProp5, duration=0, pos=Point3(0, 29, -20), hpr=(0, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.TableProp6, duration=0, pos=Point3(0, -29, -20), hpr=(180, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(camera, duration=0, pos=Point3(5.05647, 24.8354, 13), hpr=(0, 0, 0), blendType='easeInOut'),
        LerpPosHprInterval(self.toon3, duration=0, pos=Point3(0, -15, -20.5), hpr=(180, 0, 0), blendType='noBlend'),
        Func(self.factorysong.play),
        Func(base.transitions.irisIn, 1.5),
        Func(self.FactoryModels), Func(self.sceneFive))
        self.sceneFourTrack.start()
        
    def sceneFive(self):
        self.sceneFiveTrack = Sequence(
        LerpPosHprInterval(camera, duration=7, pos=Point3(20, 44.3581, 6), hpr=(180, 0, 0), blendType='easeInOut'),
        LerpPosHprInterval(camera, duration=2.5, pos=Point3(20, 33.8089, 6), hpr=(180, 0, 0), blendType='easeInOut'),
        Wait(2),
        LerpPosHprInterval(self.toon2, duration=0, pos=Point3(20, 11, 4), hpr=(0, 0, 0), blendType='noBlend'),
        Func(self.toon2.loop, 'jump'), Func(self.toon2.loop, 'jump'),
        Wait(1.5),
        Func(self.toon2.loop, 'neutral'), Func(self.toon2.loop, 'neutral'),
        LerpPosHprInterval(camera, duration=0, pos=Point3(20, 21, 6), hpr=(180, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "Ok. I'm here. Now what?", CFSpeech | CFTimeout), SoundInterval(self.catQuestionSpeech),
        Wait(3),
        Func(self.nametagJ2.setChat, "The map lead me to here for some reason...", CFSpeech | CFTimeout), SoundInterval(self.catEmotionalSpeech),
        Wait(3),
        LerpPosHprInterval(camera, duration=0.5, pos=Point3(15, 18, 6), hpr=(-140, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "But I'm not understanding why.", CFSpeech | CFTimeout), SoundInterval(self.catQuestionSpeech),
        Wait(3),
        Func(self.nametagJ2.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(21, 40, 8), hpr=(0, 0, 0), blendType='easeInOut'),
        Wait(3.5),
        LerpPosHprInterval(camera, duration=0, pos=Point3(15, 18, 6), hpr=(-140, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "Nevermind.", CFSpeech | CFTimeout), SoundInterval(self.catShortSpeech),
        Wait(2),
        LerpPosHprInterval(camera, duration=1, pos=Point3(15, 22, 6), hpr=(-160, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "Let's just explore.", CFSpeech | CFTimeout), SoundInterval(self.catLongSpeech),
        Wait(3),
        Func(self.nametagJ2.clearChat),
        Func(self.toon2.loop, 'run'), Func(self.toon2.loop, 'run'),
        LerpPosHprInterval(self.toon2, duration=7, pos=Point3(20, 73, 4), hpr=(0, 0, 0), blendType='noBlend'),
        Func(self.toon2.loop, 'neutral'), Func(self.toon2.loop, 'neutral'),
        LerpPosHprInterval(camera, duration=0, pos=Point3(14, 85, 7), hpr=(210, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "Ok. Now what?", CFSpeech | CFTimeout), SoundInterval(self.catQuestionSpeech),
        Wait(3),
        Func(self.nametagJ2.setChat, "I was told that there was a challenge here.", CFSpeech | CFTimeout), SoundInterval(self.catLongSpeech),
        Wait(3),
        Func(self.nametagJ2.clearChat),
        LerpPosHprInterval(camera, duration=1, pos=Point3(20, 94, 9), hpr=(0, 0, 0), blendType='easeInOut'),
        LerpPosHprInterval(self.suit, duration=2, pos=Point3(20, 106, 4), hpr=(180, 0, 0), blendType='noBlend'),
        Func(self.nametagJ5.setChat, "Aye, I'm Spongebob!", CFSpeech | CFTimeout), SoundInterval(self.cogGruntSpeech),
        Wait(3),
        Func(self.nametagJ5.setChat, "Do you wanna have some fun?", CFSpeech | CFTimeout), SoundInterval(self.cogQuestionSpeech),
        Wait(3),
        Func(self.nametagJ5.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(14, 85, 7), hpr=(210, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "Um. Who are you?", CFSpeech | CFTimeout), SoundInterval(self.catShortSpeech), SoundInterval(self.catQuestionSpeech),
        Wait(3),
        LerpPosHprInterval(camera, duration=0.5, pos=Point3(20, 80, 7), hpr=(180, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "I don't recall this being here.", CFSpeech | CFTimeout), SoundInterval(self.catLongSpeech),
        Wait(3),
        Func(self.nametagJ2.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(20, 94, 9), hpr=(0, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ5.setChat, "You're telling me.", CFSpeech | CFTimeout), SoundInterval(self.cogStatementSpeech),
        Wait(3),
        LerpPosHprInterval(camera, duration=1, pos=Point3(24, 94, 9), hpr=(15, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ5.setChat, "I actually came here to kill you, so yeah.", CFSpeech | CFTimeout), SoundInterval(self.cogMurmurSpeech),
        Wait(3),
        Func(self.nametagJ5.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(20, 80, 7), hpr=(180, 0, 0), blendType='easeInOut'),
        Func(self.toon2.showAngryMuzzle),
        Func(self.toon2.angryEyes),
        Func(self.toon2.blinkEyes),
        LerpPosHprInterval(camera, duration=0, pos=Point3(20, 80, 7), hpr=(180, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "Woooooooooooooooooooooow how real mature.", CFSpeech | CFTimeout), SoundInterval(self.catHowlSpeech),
        Wait(3),
        Func(self.toon2.loop, 'angry'), Func(self.toon2.loop, 'angry'),
        Func(self.nametagJ2.setChat, "I'm offended now.", CFSpeech | CFTimeout), SoundInterval(self.catLongSpeech),
        Wait(3),
        Func(self.toon2.loop, 'neutral'), Func(self.toon2.loop, 'neutral'),
        Parallel(LerpPosHprInterval(camera, duration=2.5, pos=Point3(16, 77, 7), hpr=(235, 0, 0), blendType='easeInOut'),
        Sequence(Func(self.nametagJ2.setChat, "Get ready to be blown to pieces!", CFSpeech | CFTimeout), SoundInterval(self.catExclaimSpeech),
        Wait(3),
        Func(self.nametagJ2.clearChat),
        LerpPosHprInterval(camera, duration=0.5, pos=Point3(20, 80, 7), hpr=(180, 0, 0), blendType='easeInOut'),
        LerpPosHprInterval(self.gun2, duration=0, pos=Point3(0.28, 0.1, 0.08), hpr=(85.6, -4.44, 94.43)), Func(self.gun2.reparentTo, self.toon2.leftHand), Func(self.gun2.show),
        LerpPosHprInterval(self.gun, duration=0, pos=Point3(0.28, 0.1, 0.08), hpr=(85.6, -4.44, 94.43)), Func(self.gun.reparentTo, self.toon2.rightHand), Func(self.gun.show), Func(self.toon2.loop, 'water-gun'),
        Wait(2.5),
        Func(self.toon2.pose, 'water-gun', 30), Func(self.toon2.pose, 'water-gun', 30),
        LerpPosHprInterval(camera, duration=0, pos=Point3(20, 94, 9), hpr=(0, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ5.setChat, "Oh no! I'm innocent!", CFSpeech | CFTimeout), SoundInterval(self.cogGruntSpeech),
        Wait(3),
        LerpPosHprInterval(camera, duration=0.5, pos=Point3(20, 97, 10.4), hpr=(0, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ5.setChat, "I uh surrender!", CFSpeech | CFTimeout), SoundInterval(self.cogGruntSpeech),
        Wait(3),
        Func(self.nametagJ5.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(20, 80, 7), hpr=(180, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "Then leave.", CFSpeech | CFTimeout), SoundInterval(self.catMedSpeech),
        Wait(2),
        Func(self.nametagJ2.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(20, 97, 10.4), hpr=(0, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ5.setChat, "OK OK OK OK!", CFSpeech | CFTimeout), SoundInterval(self.cogGruntSpeech),
        Wait(2),
        Func(self.nametagJ5.clearChat),
        LerpPosHprInterval(self.suit, duration=0, pos=Point3(20, 106, -30), hpr=(180, 0, 0), blendType='noBlend'),
        Func(self.toon2.loop, 'neutral'), Func(self.toon2.loop, 'neutral'),
        LerpPosHprInterval(camera, duration=0, pos=Point3(20, 92, 7), hpr=(180, 0, 0), blendType='easeInOut'), SoundInterval(self.ExplosionSfx),
        Wait(1.5),
        LerpPosHprInterval(camera, duration=0, pos=Point3(20, 85, 7), hpr=(180, 0, 0), blendType='easeInOut'),
        Func(self.toon2.hideAngryMuzzle),
        Func(self.toon2.normalEyes),
        Func(self.toon2.blinkEyes),
        Func(self.nametagJ2.setChat, "Lol.", CFSpeech | CFTimeout), SoundInterval(self.catShortSpeech),
        Wait(2),
        LerpPosHprInterval(camera, duration=0, pos=Point3(20, 79, 7), hpr=(180, 0, 0), blendType='easeInOut'),
        LerpPosHprInterval(self.gun2, duration=0, pos=Point3(0.28, 0.1, 0.08), hpr=(85.6, -4.44, 94.43)), Func(self.gun2.reparentTo, self.toon2.leftHand), Func(self.gun2.hide),
        LerpPosHprInterval(self.gun, duration=0, pos=Point3(0.28, 0.1, 0.08), hpr=(85.6, -4.44, 94.43)), Func(self.gun.reparentTo, self.toon2.rightHand), Func(self.gun.hide), Func(self.toon2.loop, 'water-gun'),
        LerpPosHprInterval(self.map, duration=0, pos=Point3(0.35, -0.40, 0.35), hpr=(90, -30, 45)), Func(self.map.reparentTo, self.toon2.rightHand), Func(self.map.show), Func(self.toon2.pose, 'book', 40),
        Func(self.nametagJ2.setChat, "Well. I guess my next objective would be...", CFSpeech | CFTimeout), SoundInterval(self.catLongSpeech),
        Wait(3),
        LerpPosHprInterval(camera, duration=0, pos=Point3(20, 77, 5), hpr=(180, 0, 0), blendType='easeInOut'), SoundInterval(self.HoldUpSfx),
        Func(self.factorysong.stop), 
        Wait(1.5),
        LerpPosHprInterval(camera, duration=0, pos=Point3(20, 79, 7), hpr=(180, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "You gotta be kidding...", CFSpeech | CFTimeout), SoundInterval(self.catEmotionalSpeech),
        Wait(3),
        Func(self.nametagJ2.setChat, "WHY DO I GOTTA GO IN THE BULLION? -_-", CFSpeech | CFTimeout), SoundInterval(self.catQuestionSpeech), SoundInterval(self.catQuestionSpeech), SoundInterval(self.catQuestionSpeech),
        Wait(3),
        LerpPosHprInterval(camera, duration=0, pos=Point3(16, 77, 7), hpr=(235, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "Here we go again...", CFSpeech | CFTimeout), SoundInterval(self.catEmotionalSpeech),
        Wait(3),
        Func(self.nametagJ2.clearChat),
        Func(base.transitions.irisOut, 0), 
        Wait(2.5),
        LerpPosHprInterval(self.TableProp, duration=0, pos=Point3(-12, -20, -18), hpr=(0, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.TableProp2, duration=0, pos=Point3(-12, -20, -18), hpr=(0, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.map, duration=0, pos=Point3(0, 0, 0), hpr=(0, 0, 0)), Func(self.map.reparentTo, self.toon2.rightHand), Func(self.map.show), Func(self.toon2.pose, 'book', 40),
        LerpPosHprInterval(self.TableProp3, duration=0, pos=Point3(-12, -20, -18), hpr=(0, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.TableProp4, duration=0, pos=Point3(-12, -20, -18), hpr=(0, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.TableProp5, duration=0, pos=Point3(0, 29, -20), hpr=(0, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.TableProp6, duration=0, pos=Point3(0, -29, -20), hpr=(180, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(camera, duration=0, pos=Point3(-5, 24.8354, 13), hpr=(90, 0, 0), blendType='easeInOut'),
        Func(self.mintsong.play),
        Func(base.transitions.irisIn, 1.5),
        Func(self.sceneSix))))
        self.sceneFiveTrack.start()
     
    def sceneSix(self):
        self.sceneSixTrack = Sequence(
        Func(self.otherModels),

        LerpPosHprInterval(camera, duration=3, pos=Point3(0, 10, 3), hpr=(180, 0, 0), blendType='easeInOut'),
        LerpPosHprInterval(camera, duration=2.5, pos=Point3(0, 0, 3), hpr=(180, 0, 0), blendType='easeInOut'),
        Wait(2),
        LerpPosHprInterval(self.toon2, duration=0, pos=Point3(0, -9, 0.5), hpr=(0, 0, 0), blendType='noBlend'),
        Func(self.toon2.loop, 'jump'), Func(self.toon2.loop, 'jump'),
        Wait(1.5),
        Func(self.toon2.loop, 'neutral'), Func(self.toon2.loop, 'neutral'),
        LerpPosHprInterval(camera, duration=0, pos=Point3(0, -3, 3.7), hpr=(180, 0, 0), blendType='easeInOut'),
        LerpPosHprInterval(self.map, duration=0, pos=Point3(0.35, -0.40, 0.35), hpr=(90, -30, 45)), Func(self.map.reparentTo, self.toon2.rightHand), Func(self.map.show), Func(self.toon2.pose, 'book', 40),
        Func(self.nametagJ2.setChat, "Alright, what is the map saying this time?", CFSpeech | CFTimeout), SoundInterval(self.catQuestionSpeech),
        Wait(3),
        LerpPosHprInterval(camera, duration=0.3, pos=Point3(-1, -1, 3.7), hpr=(200, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "It's saying that I should head over to the left, hm...", CFSpeech | CFTimeout), SoundInterval(self.catLongSpeech), SoundInterval(self.catEmotionalSpeech),
        Wait(3),
        Func(self.nametagJ2.clearChat),
        LerpPosHprInterval(camera, duration=1.2, pos=Point3(5, -9, 3.7), hpr=(90, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "Perhaps I should go to the left then.", CFSpeech | CFTimeout), SoundInterval(self.catLongSpeech),
        Wait(3),
        LerpPosHprInterval(camera, duration=1.2, pos=Point3(-5, -9, 3.7), hpr=(270, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "Or do I go to the right?", CFSpeech | CFTimeout), SoundInterval(self.catQuestionSpeech),
        Wait(3),
        LerpPosHprInterval(camera, duration=0.35, pos=Point3(-5, -5, 3.7), hpr=(240, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "We shall find out.", CFSpeech | CFTimeout), SoundInterval(self.catMedSpeech),
        Wait(3),
        Func(self.nametagJ2.clearChat),
        LerpPosHprInterval(self.map, duration=0, pos=Point3(0, 0, 0), hpr=(0, 0, 0)), Func(self.map.reparentTo, self.toon2.rightHand), Func(self.map.hide), Func(self.toon2.loop, 'neutral'),
        Func(self.toon2.loop, 'run'), Func(self.toon2.loop, 'run'),
        LerpPosHprInterval(self.toon2, duration=5, pos=Point3(0, 15, 0.5), hpr=(0, 0, 0), blendType='noBlend'),
        Wait(1.5),
        Func(self.toon2.loop, 'neutral'), Func(self.toon2.loop, 'neutral'),
        Func(self.sceneSeven))
        self.sceneSixTrack.start()

    def sceneSeven(self):
        self.sceneSevenTrack = Sequence(
        Func(self.mintModels),
        LerpPosHprInterval(self.suit2, duration=0, pos=Point3(0, 60, 10), hpr=(90, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.suit3, duration=0, pos=Point3(-15, 60, 10), hpr=(270, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.TableProp8, duration=0, pos=Point3(61, 6, 0), hpr=(270, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.TableProp9, duration=0, pos=Point3(0, 80, 10), hpr=(0, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.toon2, duration=0, pos=Point3(66, 6, 0.5), hpr=(90, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(camera, duration=0, pos=Point3(0, 6, 4), hpr=(270, 0, 0), blendType='easeInOut'),
        LerpPosHprInterval(camera, duration=2.5, pos=Point3(52, 6, 4), hpr=(270, 0, 0), blendType='easeInOut'),
        Func(self.toon2.loop, 'walk'), Func(self.toon2.loop, 'walk'),
        LerpPosHprInterval(self.toon2, duration=2, pos=Point3(59, 6, 0.5), hpr=(90, 0, 0), blendType='noBlend'),
        Func(self.toon2.loop, 'neutral'), Func(self.toon2.loop, 'neutral'),
        Func(self.nametagJ2.setChat, "Ok. Now what?", CFSpeech | CFTimeout), SoundInterval(self.catShortSpeech), SoundInterval(self.catQuestionSpeech),
        Wait(3),
        Func(self.nametagJ2.setChat, "This is really interesting.", CFSpeech | CFTimeout), SoundInterval(self.catLongSpeech),
        Wait(3),
        Func(self.nametagJ2.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(5, 60, 30), hpr=(20, 0, 0), blendType='easeInOut'),
        LerpPosHprInterval(camera, duration=3.5, pos=Point3(-2, 53, 18), hpr=(0, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ6.setChat, "So, Mimi, did you make sure to guard the facility doors?", CFSpeech | CFTimeout), SoundInterval(self.angelStatementSpeech), SoundInterval(self.angelQuestionSpeech),
        Wait(3),
        Func(self.nametagJ6.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(-10, 50, 17), hpr=(30, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ7.setChat, "Mhm. Sure did.", CFSpeech | CFTimeout), SoundInterval(self.mimiStatementSpeech),
        Wait(3),
        Func(self.nametagJ7.clearChat),
        Func(self.suit2.loop, 'effort'), Func(self.suit2.loop, 'effort'),
        LerpPosHprInterval(camera, duration=0, pos=Point3(-2, 50, 18), hpr=(-20, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ6.setChat, "Good. Now Amanda Rose and Elvis will be so proud of us. <:)", CFSpeech | CFTimeout), SoundInterval(self.angelMurmurSpeech), SoundInterval(self.angelStatementSpeech),
        Wait(2.5),
        Func(self.suit2.loop, 'neutral'), Func(self.suit2.loop, 'neutral'),
        LerpPosHprInterval(camera, duration=0, pos=Point3(-7, 60, 17), hpr=(270, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ6.setChat, "Wouldn't you agree?", CFSpeech | CFTimeout), SoundInterval(self.angelQuestionSpeech),
        Wait(3),
        Func(self.nametagJ6.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(-4, 60, 17), hpr=(90, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ7.setChat, "Yep. <:)", CFSpeech | CFTimeout), SoundInterval(self.mimiGruntSpeech),
        Wait(3),
        Func(self.nametagJ7.clearChat),
        LerpPosHprInterval(camera, duration=2.5, pos=Point3(52, 6, 4), hpr=(270, 0, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "Huh? I hear something.", CFSpeech | CFTimeout), SoundInterval(self.catShortSpeech), SoundInterval(self.catShortSpeech), SoundInterval(self.catQuestionSpeech),
        Wait(3),
        Func(self.nametagJ2.setChat, "I must explore.", CFSpeech | CFTimeout), SoundInterval(self.catMedSpeech),
        Wait(3),
        Func(self.nametagJ2.clearChat),
        Func(self.toon2.loop, 'walk'), Func(self.toon2.loop, 'walk'),
        LerpPosHprInterval(self.toon2, duration=6, pos=Point3(30, 6, 0.5), hpr=(90, 0, 0), blendType='noBlend'), 
        LerpPosHprInterval(camera, duration=0, pos=Point3(-25, 60, 18), hpr=(245, 0, 0), blendType='easeInOut'),
        Func(self.suit2.loop, 'neutral'), Func(self.suit2.loop, 'neutral'), 
        Func(self.nametagJ7.setChat, "Amanda will not be disappointed.", CFSpeech | CFTimeout), SoundInterval(self.mimiMurmurSpeech), 
        Func(self.toon2.loop, 'walk'), Func(self.toon2.loop, 'walk'), 
        LerpPosHprInterval(self.toon2, duration=6, pos=Point3(5, 6, 0.5), hpr=(90, 0, 0), blendType='noBlend'),
        Func(self.suit2.loop, 'neutral'), Func(self.suit2.loop, 'neutral'), 
        Func(self.nametagJ7.clearChat))

        self.sceneSevenTrack.start()
        
    def goToSceneTwo(self):
        self.GoodTrack.finish()
        
    def goToSceneThree(self): 
        self.sceneTwoTrack.finish()
        
    def goToSceneFour(self):
        self.sceneThreeTrack.finish()
        
    def goToSceneFive(self):
        self.sceneFourTrack.finish()
        
    def goToSceneSix(self):
        self.sceneFiveTrack.finish()

    def goToSceneSeven(self):
        self.sceneSixTrack.finish()
        
    def changeModels(self):
        self.houseVariable.removeNode()
        self.placeVariable.reparentTo(render)

    def CogHQModels(self):
        self.placeVariable.removeNode()
        self.HQVariable.reparentTo(render)

    def changeModels2(self):
        self.HQVariable.removeNode()
        self.sonicplaceVariable.reparentTo(render)

    def FactoryModels(self):
        self.sonicplaceVariable.removeNode()
        self.factoryVariable.reparentTo(render)

    def otherModels(self):
        self.factoryVariable.removeNode()
        self.otherVariable.reparentTo(render)

    def mintModels(self):
        self.otherVariable.removeNode()
        self.mintVariable.reparentTo(render)
