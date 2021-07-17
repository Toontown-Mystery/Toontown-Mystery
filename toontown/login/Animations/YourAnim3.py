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
        
        self.Karen = Suit.Suit()
        self.Karen.dna = SuitDNA.SuitDNA()
        self.Karen.dna.newSuit('ka')
        self.Karen.setDNA(self.Karen.dna)
        self.Karen.setPos(3, -45, 6.3)
        self.Karen.loop('neutral')
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

        deathSuit = self.Karen.getLoseActor()
        deathSuit.setPos(self.Karen.getX(), self.Karen.getY(), self.Karen.getZ())
        deathSuit.setBlend(frameBlend=True)

        self.cake = BattleProps.globalPropPool.getProp('birthday-cake')
        self.cake.setScale(1.2)
        
        self.splat = loader.loadModel('phase_3.5/models/props/splat-mod.bam')
        self.splat.setPos(3, -45, 9)
        self.splat.setH(180)
        self.splat.setColor(0, 0, 0, 1)

        self.BombProp = loader.loadModel('phase_5/models/props/birthday-cake-mod.bam')
        self.BombProp.reparentTo(render)
        
        camera.setPos(0, -30, 15)
        
        self.catExclaimSpeech = base.loader.loadSfx('phase_3.5/audio/dial/AV_cat_exclaim.ogg')
        self.catHowlSpeech = base.loader.loadSfx('phase_3.5/audio/dial/AV_cat_howl.ogg')
        self.catLongSpeech = base.loader.loadSfx('phase_3.5/audio/dial/AV_cat_long.ogg')
        self.catMedSpeech = base.loader.loadSfx('phase_3.5/audio/dial/AV_cat_med.ogg')
        self.catQuestionSpeech = base.loader.loadSfx('phase_3.5/audio/dial/AV_cat_question.ogg')
        self.catShortSpeech = base.loader.loadSfx('phase_3.5/audio/dial/AV_cat_short.ogg')
        self.catLongMedSpeech = base.loader.loadSfx('phase_3.5/audio/dial/AV_Med_Long.ogg')
        self.cogGruntSpeech = base.loader.loadSfx('phase_3.5/audio/dial/COG_VO_grunt_f.ogg')
        self.cogMurmurSpeech = base.loader.loadSfx('phase_3.5/audio/dial/COG_VO_murmur_f.ogg')
        self.cogQuestionSpeech = base.loader.loadSfx('phase_3.5/audio/dial/COG_VO_question_1_f.ogg')
        self.cogStatementSpeech = base.loader.loadSfx('phase_3.5/audio/dial/COG_VO_statement_f.ogg')
        self.cogAngrySpeech = base.loader.loadSfx('phase_3.5/audio/dial/COG_VO_angry_f.ogg')
        self.throwCakeSpamSfx = base.loader.loadSfx('phase_3.5/audio/dial/Bomb_cake_spam.ogg')
        self.dropFallSfx = base.loader.loadSfx('phase_5/audio/sfx/cogbldg_drop.ogg')
        self.spinSfx = base.loader.loadSfx('phase_3.5/audio/sfx/Cog_Death_1.ogg')
        self.explodeSfx = base.loader.loadSfx('phase_3.5/audio/sfx/ENC_cogfall_apart.ogg')
        self.spamTrack = Sequence(Parallel(LerpPosHprInterval(self.cake, duration=0, pos=Point3(93.5, -345, 2.5), hpr=(0, 0, 90)), LerpScaleInterval(self.splat, duration=0, scale=(2, 2, 2))), Parallel(LerpPosInterval(self.cake, duration=0.15, pos=Point3(0, -45, 6.3)), LerpScaleInterval(self.splat, duration=0.15, scale=(2, 2, 2))))
        
        GoodTrack = Sequence(Func(base.transitions.irisOut, 2), Func(base.transitions.irisIn, 2), Wait(3), Func(self.karenintro.play),
        LerpPosInterval(self.toon, duration=5, pos=Point3(15, 15, 7), blendType='noBlend'), 
        Func(self.toon.loop, 'walk'), Parallel(Func(self.toon.loop, 'cringe'), 
        Func(self.nametagJ.setChat, "Brrr. I'm so cold!", CFSpeech | CFTimeout), SoundInterval(self.catExclaimSpeech), 
        LerpPosHprInterval(camera, duration=4, pos=Point3(15, 30, 10), hpr=(180, 10, 0), blendType='easeInOut')), 
        Wait(1.5), 
        Func(self.nametagJ.clearChat),
        LerpPosHprInterval(camera, duration=2, pos=Point3(15, 25, 10), hpr=(180, 10, 0), blendType='easeInOut'), 
        Func(self.nametagJ.setChat, "Why must everything be so cold here....?", CFSpeech | CFTimeout), SoundInterval(self.catQuestionSpeech), 
        Wait(3), 
        Func(self.nametagJ.clearChat),
        LerpPosHprInterval(camera, duration=2, pos=Point3(3, -33, 11), hpr=(180, 10, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "You!!", CFSpeech | CFTimeout), SoundInterval(self.cogGruntSpeech), 
        Wait(3),
        Func(self.nametagJ2.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(15, 30, 10), hpr=(180, 10, 0), blendType='easeInOut'), 
        Parallel(LerpPosHprInterval(self.toon, duration=3, pos=Point3(15, 15, 7), hpr=(160, 0, 0), blendType='noBlend'), 
        Func(self.toon.loop, 'walk')), Func(self.toon.loop, 'neutral'),  
        Func(self.nametagJ.setChat, "Huh, what are you doing here?", CFSpeech | CFTimeout), SoundInterval(self.catQuestionSpeech),
        Wait(3),
        Func(self.nametagJ.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(3, -31, 11), hpr=(185, 10, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "You think you're smart? Think again.", CFSpeech | CFTimeout), SoundInterval(self.cogQuestionSpeech),
        Wait(3),
        Func(self.nametagJ2.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(15, 4, 10), hpr=(0, 10, 0), blendType='easeInOut'),
        Func(self.nametagJ.setChat, "Oh no.", CFSpeech | CFTimeout), SoundInterval(self.catShortSpeech),
        Wait(2),
        Func(self.nametagJ.clearChat),
        LerpPosHprInterval(camera, duration=1.5, pos=Point3(15, 9, 10), hpr=(0, 10, 0), blendType='easeInOut'),
        Func(self.nametagJ.setChat, "But... I didn't do anything!", CFSpeech | CFTimeout), SoundInterval(self.catExclaimSpeech),
        Wait(3),
        Func(self.nametagJ.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(3, -33, 11), hpr=(180, 10, 0), blendType='easeInOut'),
        Func(self.Karen.loop, 'speak', fromFrame=50, toFrame=70), Func(self.Karen.setPlayRate, 10, 'speak'),
        Func(self.nametagJ2.setChat, "You're in my property, Toon.", CFSpeech | CFTimeout), SoundInterval(self.cogStatementSpeech),
        Wait(3),
        Func(self.nametagJ2.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(15, 5, 10), hpr=(3, 10, 0), blendType='easeInOut'),
        Func(self.nametagJ.setChat, "SERIOUSLY!?", CFSpeech | CFTimeout), SoundInterval(self.catExclaimSpeech),
        Wait(2),
        Func(self.nametagJ.clearChat),
        LerpPosHprInterval(camera, duration=1.5, pos=Point3(10, 4, 10), hpr=(330, 10, 0), blendType='easeInOut'),
        Func(self.nametagJ.setChat, "IT'S A TOON'S PLAYGROUND FOR PEEP SAKE!!!", CFSpeech | CFTimeout), SoundInterval(self.catExclaimSpeech),
        Wait(3),
        Func(self.nametagJ.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(3, -33, 11), hpr=(180, 10, 0), blendType='easeInOut'),
        Func(self.Karen.loop, 'neutral'), Func(self.Karen.loop, 'neutral'),
        Func(self.nametagJ2.setChat, "Are you backtalking me?", CFSpeech | CFTimeout), SoundInterval(self.cogQuestionSpeech),
        Wait(3),
        Func(self.nametagJ2.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(10, 4, 10), hpr=(330, 10, 0), blendType='easeInOut'),
        Func(self.nametagJ.setChat, "Yes.", CFSpeech | CFTimeout), SoundInterval(self.catShortSpeech),
        Wait(2),
        Func(self.nametagJ.clearChat),
        LerpPosHprInterval(camera, duration=3, pos=Point3(3, -55, 11), hpr=(0, 10, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "Alright. I had enough of you...", CFSpeech | CFTimeout), SoundInterval(self.cogStatementSpeech),
        Wait(3),
        Func(self.nametagJ2.clearChat),
        Parallel(Func(self.karenintro.stop),
        Func(self.karenbattle.play)),
        LerpPosHprInterval(camera, duration=1, pos=Point3(14, -36, 11), hpr=(140, 10, 0), blendType='easeInOut'),
        Func(self.Karen.loop, 'effort', fromFrame=80, toFrame=100), Func(self.Karen.setPlayRate, 8, 'effort'),
        Func(self.nametagJ2.setChat, "NOW GET OUT OF MY PLAYGROUND!!!", CFSpeech | CFTimeout), SoundInterval(self.cogAngrySpeech),
        Wait(3),
        Func(self.nametagJ2.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(15, 7, 10), hpr=(5, 10, 0), blendType='easeInOut'),
        Func(self.nametagJ.setChat, "Ugh...", CFSpeech | CFTimeout), SoundInterval(self.catShortSpeech),
        Wait(2),
        Func(self.nametagJ.clearChat),
        Func(self.toon.loop, 'think'), Func(self.toon.loop, 'think'),
        Func(self.nametagJ.setChat, "Hm, what do I do?", CFSpeech | CFTimeout), SoundInterval(self.catQuestionSpeech),
        Wait(2),
        Func(self.nametagJ.clearChat),
        LerpPosHprInterval(camera, duration=1.5, pos=Point3(13, 7, 9), hpr=(340, 10, 0), blendType='easeInOut'), 
        Func(self.nametagJ.setChat, "Oh... I know...", CFSpeech | CFTimeout), SoundInterval(self.catLongSpeech),
        Wait(2),
        Func(self.nametagJ.clearChat),
        Func(self.Karen.loop, 'speak', fromFrame=0, toFrame=200), Func(self.Karen.setPlayRate, 1, 'speak'),
        LerpPosHprInterval(camera, duration=1, pos=Point3(3, -33, 11), hpr=(180, 10, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "What are you going to do?", CFSpeech | CFTimeout), SoundInterval(self.cogQuestionSpeech),
        Wait(5),
        Func(self.nametagJ2.clearChat),
        Func(self.Karen.loop, 'neutral'), Func(self.Karen.loop, 'neutral'),
        LerpPosHprInterval(camera, duration=1, pos=Point3(3, -35, 11), hpr=(180, 10, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "It's not like whatever you're going to do is going to solve anything.", CFSpeech | CFTimeout), SoundInterval(self.cogMurmurSpeech),
        Wait(3),
        Func(self.nametagJ2.clearChat),
        Func(self.toon.loop, 'neutral'), Func(self.toon.loop, 'neutral'),
        LerpPosHprInterval(camera, duration=1.5, pos=Point3(12.2, 7.4, 10), hpr=(340, 10, 0), blendType='easeInOut'), 
        Func(self.nametagJ.setChat, "You know exactly what I mean...", CFSpeech | CFTimeout), SoundInterval(self.catLongSpeech),
        Wait(2),
        Func(self.nametagJ.clearChat),
        Func(self.toon.loop, 'walk'), Func(self.toon.loop, 'walk'),
        LerpPosHprInterval(camera, duration=1.5, pos=Point3(0, -10, 11), hpr=(0, 10, 0), blendType='easeInOut'),
        LerpPosHprInterval(self.toon, duration=3, pos=Point3(3, 15, 7), hpr=(90, 0, 0), blendType='noBlend'),
        Func(self.toon.loop, 'walk'), Func(self.toon.loop, 'walk'),
        LerpPosHprInterval(self.toon, duration=2, pos=Point3(3, 15, 7), hpr=(0, 0, 0), blendType='noBlend'),
        Func(self.toon.loop, 'walk'), Func(self.toon.loop, 'walk'),
        LerpPosHprInterval(self.toon, duration=1, pos=Point3(3, 20, 7), hpr=(0, 0, 0), blendType='noBlend'),
        Func(self.toon.loop, 'walk'), Func(self.toon.loop, 'walk'),
        LerpPosHprInterval(self.toon, duration=3, pos=Point3(3, 20, 7), hpr=(180, 0, 0), blendType='noBlend'),
        Func(self.toon.loop, 'walk'), Func(self.toon.loop, 'walk'),
        Func(self.toon.loop, 'neutral'), Func(self.toon.loop, 'neutral'),
        Wait(2),
        LerpPosHprInterval(camera, duration=1.5, pos=Point3(26, -40, 11), hpr=(90, 10, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "What do you think you're doing?", CFSpeech | CFTimeout), SoundInterval(self.cogQuestionSpeech),
        Wait(3),
        Func(self.nametagJ2.clearChat),
        LerpPosHprInterval(camera, duration=2.5, pos=Point3(3, 12, 9), hpr=(20, 10, 0), blendType='easeInOut'), 
        Func(self.nametagJ.setChat, "You'll see.", CFSpeech | CFTimeout), SoundInterval(self.catMedSpeech),
        Wait(2),
        Func(self.nametagJ.clearChat),       
        LerpPosHprInterval(camera, duration=2, pos=Point3(10, 40, 11), hpr=(180, 10, 0), blendType='easeInOut'), 
        Parallel(LerpPosHprInterval(self.cake, duration=0, pos=Point3(0, 0, 0), hpr=(0, 0, 0)), Func(self.cake.reparentTo, self.toon.rightHand), Func(self.cake.show), Func(self.toon.play, 'throw', fromFrame=0, toFrame=50)),
        Wait(1.5),
        Func(self.nametagJ2.setChat, "???", CFSpeech | CFTimeout), SoundInterval(self.cogQuestionSpeech),
        Func(self.nametagJ2.clearChat),
        Parallel(Func(self.toon.setPlayRate, 8, 'throw'), Func(self.toon.loop, 'throw', fromFrame=45, toFrame=70), SoundInterval(self.throwCakeSpamSfx, node=self.toon, volume=1), Func(self.cake.reparentTo, render), Func(self.Karen.loop, 'pie-small-react', fromFrame=50, toFrame=70), Func(self.Karen.setPlayRate, 10, 'pie-small-react'), Func(self.splat.reparentTo, render), Func(self.spamTrack.loop)), Parallel(Func(self.spamTrack.finish), Func(self.splat.hide), Func(self.cake.hide), Func(self.Karen.setPlayRate, 1, 'pie-small-react'), Sequence(Func(self.Karen.play, 'pie-small-react', fromFrame=60, toFrame=100), Wait(1.5), Func(self.Karen.loop, 'neutral')), Func(self.toon.setPlayRate, 1, 'throw'), Func(self.toon.play, 'throw', fromFrame=70, toFrame=100), Wait(0.8), Func(self.toon.loop, 'neutral')),
        LerpPosHprInterval(camera, duration=0, pos=Point3(3, -32, 11), hpr=(160, 10, 0), blendType='easeInOut'),
        Func(self.Karen.loop, 'slip-forward'), Func(self.Karen.loop, 'slip-forward'),
        Func(self.nametagJ2.setChat, "Ahh!", CFSpeech | CFTimeout), SoundInterval(self.cogGruntSpeech),
        Wait(1),
        Func(self.nametagJ2.clearChat),
        Func(self.nametagJ2.setChat, "Make it stop!", CFSpeech | CFTimeout), SoundInterval(self.cogGruntSpeech),
        Wait(2),
        Func(self.nametagJ2.clearChat), 
        Func(self.Karen.loop, 'neutral'), Func(self.Karen.loop, 'neutral'),
        LerpPosHprInterval(camera, duration=1.5, pos=Point3(3, 9, 10), hpr=(0, 10, 0), blendType='easeInOut'), 
        Func(self.nametagJ.setChat, "How does it feel, huh?", CFSpeech | CFTimeout), SoundInterval(self.catQuestionSpeech),
        Wait(2),
        Func(self.nametagJ.clearChat),
        LerpPosHprInterval(camera, duration=1.5, pos=Point3(3, 11, 9), hpr=(0, 10, 0), blendType='easeInOut'), 
        Func(self.toon.loop, 'bored'), Func(self.toon.loop, 'bored'),
        Func(self.nametagJ.setChat, "Taste your own Karen Karmas.", CFSpeech | CFTimeout), SoundInterval(self.catHowlSpeech),
        Wait(1.7),
        Func(self.nametagJ.clearChat),
        Func(self.toon.loop, 'neutral'), Func(self.toon.loop, 'neutral'),
        LerpPosHprInterval(camera, duration=0, pos=Point3(3, -35, 11), hpr=(180, 10, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "I see, where you came with that...", CFSpeech | CFTimeout), SoundInterval(self.cogStatementSpeech),
        Wait(2),
        Func(self.nametagJ2.clearChat),   
        LerpPosHprInterval(camera, duration=2, pos=Point3(3, -32, 11), hpr=(180, 10, 0), blendType='easeInOut'),
        Func(self.Karen.loop, 'walk'), Func(self.Karen.loop, 'walk'),
        LerpPosInterval(self.Karen, duration=2, pos=Point3(3, -40, 6.3), blendType='noBlend'),
        Func(self.Karen.loop, 'neutral'), Func(self.Karen.loop, 'neutral'),
        Func(self.nametagJ2.setChat, "You have no match for us Karen Cogs...", CFSpeech | CFTimeout), SoundInterval(self.cogStatementSpeech),
        Wait(2),
        Func(self.nametagJ2.clearChat),
        LerpPosHprInterval(camera, duration=2, pos=Point3(3, -20, 11), hpr=(180, 10, 0), blendType='easeInOut'),
        Func(self.Karen.loop, 'walk'), Func(self.Karen.loop, 'walk'),
        LerpPosInterval(self.Karen, duration=2, pos=Point3(3, -28, 6.3), blendType='noBlend'),
        Func(self.Karen.loop, 'neutral'), Func(self.Karen.loop, 'neutral'),
        Func(self.nametagJ2.setChat, "Did you really think you could beat me?", CFSpeech | CFTimeout), SoundInterval(self.cogQuestionSpeech),
        Wait(2),
        Func(self.nametagJ2.clearChat),
        LerpPosHprInterval(camera, duration=1.5, pos=Point3(3, 11, 9), hpr=(0, 10, 0), blendType='easeInOut'), 
        Func(self.toon.loop, 'neutral'), Func(self.toon.loop, 'neutral'),
        Func(self.nametagJ.setChat, "I did, actually.", CFSpeech | CFTimeout), SoundInterval(self.catMedSpeech),
        Wait(1.5),
        Func(self.nametagJ.clearChat),
        LerpPosHprInterval(camera, duration=2, pos=Point3(3, -10, 11), hpr=(180, 10, 0), blendType='easeInOut'),
        Func(self.Karen.loop, 'walk'), Func(self.Karen.loop, 'walk'),
        LerpPosInterval(self.Karen, duration=2, pos=Point3(3, -18, 6.3), blendType='noBlend'),
        Func(self.Karen.loop, 'neutral'), Func(self.Karen.loop, 'neutral'),
        Func(self.nametagJ2.setChat, "You have little to know, and learn.", CFSpeech | CFTimeout), SoundInterval(self.cogMurmurSpeech),
        Wait(2),
        Func(self.nametagJ2.clearChat),
        Func(self.Karen.loop, 'soak', fromFrame=1, toFrame=50), Func(self.Karen.setPlayRate, 1, 'soak'),
        Func(self.nametagJ2.setChat, "Huh? What's that noise?", CFSpeech | CFTimeout), SoundInterval(self.cogQuestionSpeech),
        Func(self.nametagJ2.clearChat),
        Wait(2),
        Func(self.Karen.loop, 'soak', fromFrame=50, toFrame=44), Func(self.Karen.setPlayRate, 0, 'soak'),
        Wait(1),
        LerpPosHprInterval(camera, duration=1.5, pos=Point3(3, 8, 10), hpr=(0, 10, 0), blendType='easeInOut'), 
        Func(self.toon.loop, 'shrug'), Func(self.toon.loop, 'shrug'),
        Func(self.nametagJ.setChat, "No idea lol.", CFSpeech | CFTimeout), SoundInterval(self.catMedSpeech),
        Wait(1.5),
        Func(self.nametagJ.clearChat),
        Func(self.toon.loop, 'neutral'), Func(self.toon.loop, 'neutral'),
        Func(self.karenbattle.stop),
        LerpPosHprInterval(camera, duration=0, pos=Point3(3, -10, 11), hpr=(180, 90, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "", CFSpeech | CFTimeout), SoundInterval(self.dropFallSfx),
        Func(self.Karen.loop, 'soak', fromFrame=50, toFrame=44), Func(self.Karen.setPlayRate, 0, 'soak'),
        LerpPosHprInterval(camera, duration=2, pos=Point3(3, -10, 11), hpr=(180, 10, 0), blendType='easeInOut'),
        Wait(1.5),
        Sequence(Func(self.Karen.loop, 'neutral'), Func(self.Karen.loop, 'neutral'),
        Func(self.nametagJ2.setChat, "Typical...", CFSpeech | CFTimeout), SoundInterval(self.cogMurmurSpeech),
        Wait(1.5),
        Func(self.nametagJ2.clearChat),
        Func(self.nametagJ2.setChat, "This isn't over, I will come back!", CFSpeech | CFTimeout), SoundInterval(self.cogGruntSpeech),
        Wait(2),
        Func(self.nametagJ2.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(3, -29, 11), hpr=(180, 15, 0), blendType='easeInOut'),
        Func(self.Karen.reparentTo, hidden), Func(deathSuit.reparentTo, render), Func(deathSuit.play, 'lose', fromFrame=0, toFrame=150), Wait(0.8), SoundInterval(self.spinSfx, duration=1.2, startTime=1.5, volume=0.35, node=deathSuit), SoundInterval(self.spinSfx, duration=3.0, startTime=0.6, volume=0.8), SoundInterval(self.explodeSfx, volume=0.8, node=self.Karen), Func(deathSuit.reparentTo, hidden), Func(deathSuit.removeNode), Func(self.Karen.removeNode),
        Wait(1),
        LerpPosHprInterval(camera, duration=1.5, pos=Point3(3, 8, 10), hpr=(0, 10, 0), blendType='easeInOut'), 
        Func(self.nametagJ.setChat, "Lol, that was easy.", CFSpeech | CFTimeout), SoundInterval(self.catLongSpeech),
        Wait(2),
        Func(self.nametagJ.clearChat),
        Func(self.toon.loop, 'taunt'), Func(self.toon.loop, 'taunt'),
        LerpPosHprInterval(camera, duration=1.5, pos=Point3(3, 0, 8), hpr=(0, 10, 0), blendType='easeInOut'),
        Func(self.nametagJ.setChat, "Time to dance like the generic playtime now.", CFSpeech | CFTimeout), SoundInterval(self.catLongSpeech),
        Wait(2),
        Func(self.nametagJ.clearChat),
        Parallel(LerpPosHprInterval(camera, duration=1.5, pos=Point3(3, 4, 9), hpr=(0, 10, 0), blendType='easeInOut')),
        Func(self.karendefeat.play),
        Func(self.toon.loop, 'victory', fromFrame=0, toFrame=100), Func(self.toon.setPlayRate, 4, 'victory'),
        Wait(15),
        LerpPosHprInterval(camera, duration=3, pos=Point3(3, 30, 10), hpr=(180, 10, 0), blendType='easeInOut'),
        Wait(13),
        Func(self.toon.loop, 'neutral'), Func(self.toon.loop, 'neutral'),
        Func(self.karendefeat.stop)))
        GoodTrack.start()