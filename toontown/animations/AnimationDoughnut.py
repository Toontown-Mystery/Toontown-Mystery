from direct.gui.DirectGui import OnscreenImage, DirectLabel, DirectButton, OnscreenText
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
class AnimationDoughnut():

    def __init__(self, leaveFunction):
        self.coolintro = base.loader.loadMusic('phase_4/audio/bgm/building_shop.ogg')
        self.coolencounter = base.loader.loadMusic('phase_7/audio/bgm/encntr_suit_winning_indoor.ogg')
        self.coolkaren = base.loader.loadMusic('phase_7/audio/bgm/encntr_building_final.ogg')
        
    def create(self):
        self.cogVariable = loader.loadModel('phase_7/models/modules/boss_suit_office.bam')
        self.cogVariable.reparentTo(render)
        
        self.Elvis = Suit.Suit()
        self.Elvis.dna = SuitDNA.SuitDNA()
        self.Elvis.dna.newSuit('le')
        self.Elvis.setDNA(self.Elvis.dna)
        self.Elvis.setPos(0, 0, 0)
        self.Elvis.loop('neutral')
        self.Elvis.reparentTo(render)
        self.Elvis = self.Elvis
        
        self.nametagJ = None
        self.nametagS = None
        self.nametagJ = NametagGroup()
        self.nametagJ.setAvatar(self.Elvis)
        self.nametagJ.setFont(ToontownGlobals.getToonFont())
        self.nametagJ.setName('')
        self.nametagJ.manage(base.marginManager)
        self.nametagJ.getNametag3d().setBillboardOffset(4)
        nametagNode = self.nametagJ.getNametag3d().upcastToPandaNode()
        self.nametagS = self.Elvis.attachNewNode(nametagNode)
        self.nametagS.setPos(0, 0, 9.5)
        
        self.Rose = Suit.Suit()
        self.Rose.dna = SuitDNA.SuitDNA()
        self.Rose.dna.newSuit('mh')
        self.Rose.setDNA(self.Rose.dna)
        self.Rose.setPos(0, 40, -20)
        self.Rose.setHpr(180, 0, 0)
        self.Rose.loop('neutral')
        self.Rose.reparentTo(render)
        self.Rose = self.Rose
        
        self.nametagJ2 = None
        self.nametagS2 = None
        self.nametagJ2 = NametagGroup()
        self.nametagJ2.setAvatar(self.Rose)
        self.nametagJ2.setFont(ToontownGlobals.getToonFont())
        self.nametagJ2.setName('')
        self.nametagJ2.manage(base.marginManager)
        self.nametagJ2.getNametag3d().setBillboardOffset(4)
        nametagNode2 = self.nametagJ2.getNametag3d().upcastToPandaNode()
        self.nametagS2 = self.Rose.attachNewNode(nametagNode2)
        self.nametagS2.setPos(0, 0, 9.5)

        self.TableProp = loader.loadModel('phase_5.5/models/estate/TABLE_Bedroom_Desat.bam')
        self.TableProp.setPos(28, 0, 0)
        self.TableProp.setScale(2.2)
        self.TableProp.reparentTo(render)

        self.DoughProp = loader.loadModel('phase_4/models/minigames/ice_game_tirestack.bam')
        self.DoughProp.setPos(27, 0, 2)
        self.DoughProp.setScale(1.2)
        self.DoughProp.reparentTo(render)

        self.ElevatorProp = loader.loadModel('phase_9/models/cogHQ/cogHQ_elevator.bam')
        self.ElevatorProp.setPos(0, -35, 0)
        self.ElevatorProp.setHpr(180, 0, 0)
        self.ElevatorProp.setScale(0.5)
        self.ElevatorProp.reparentTo(render)

        self.Elevator2Prop = loader.loadModel('phase_5/models/cogdominium/tt_m_ara_csa_elevator.bam')
        self.Elevator2Prop.setPos(0, 37, 0)
        self.Elevator2Prop.setHpr(0, 0, 0)
        self.Elevator2Prop.setScale(0.9)
        self.Elevator2Prop.reparentTo(render)
        
        camera.setPos(-20, -15, 7)

        self.cogGirlGruntSpeech = base.loader.loadSfx('phase_3.5/audio/dial/COG_VO_grunt_f.ogg')
        self.cogGirlMurmurSpeech = base.loader.loadSfx('phase_3.5/audio/dial/COG_VO_murmur_f.ogg')
        self.cogGirlQuestionSpeech = base.loader.loadSfx('phase_3.5/audio/dial/COG_VO_question_1_f.ogg')
        self.cogGirlStatementSpeech = base.loader.loadSfx('phase_3.5/audio/dial/COG_VO_statement_f.ogg')
        self.cogGirlRageSpeech = base.loader.loadSfx('phase_3.5/audio/dial/COG_VO_rage.ogg')
        self.cogGirlAngrySpeech = base.loader.loadSfx('phase_3.5/audio/dial/COG_VO_angry.ogg')
        self.cogGruntSpeech = base.loader.loadSfx('phase_3.5/audio/dial/COG_VO_grunt.ogg')
        self.cogMurmurSpeech = base.loader.loadSfx('phase_3.5/audio/dial/COG_VO_murmur.ogg')
        self.cogQuestionSpeech = base.loader.loadSfx('phase_3.5/audio/dial/COG_VO_question.ogg')
        self.cogStatementSpeech = base.loader.loadSfx('phase_3.5/audio/dial/COG_VO_statement.ogg')

        
        GoodTrack = Sequence(Func(base.transitions.irisOut, 2), Wait(5), Func(base.transitions.irisIn, 2), Func(self.coolintro.play),
        LerpPosHprInterval(camera, duration=4, pos=Point3(10, 25, 10), hpr=(180, 10, 0), blendType='easeInOut'),
        Wait(2),
        LerpPosHprInterval(camera, duration=2, pos=Point3(4, 10, 5), hpr=(165, 10, 0), blendType='easeInOut'),
        Func(self.nametagJ.setChat, "What a lovely day here.", CFSpeech | CFTimeout), SoundInterval(self.cogStatementSpeech),
        Wait(3),
        Func(self.nametagJ.clearChat),
        Func(self.Elvis.loop, 'walk'), Func(self.Elvis.loop, 'walk'),
        LerpPosHprInterval(self.Elvis, duration=2, pos=Point3(0, 0, 0), hpr=(270, 0, 0), blendType='noBlend'), 
        Func(self.Elvis.loop, 'neutral'), Func(self.Elvis.loop, 'neutral'),
        Func(self.nametagJ.setChat, "What is that?", CFSpeech | CFTimeout), SoundInterval(self.cogQuestionSpeech),
        Wait(3),
        Func(self.nametagJ.clearChat),
        LerpPosHprInterval(camera, duration=2, pos=Point3(0, 0, 4), hpr=(270, 10, 0), blendType='easeInOut'),
        LerpPosHprInterval(camera, duration=1.5, pos=Point3(15, 0, 4), hpr=(270, 10, 0), blendType='easeInOut'),
        Wait(1),
        Func(self.Elvis.loop, 'slip-backward'), Func(self.Elvis.loop, 'slip-backward'), 
        LerpPosHprInterval(camera, duration=0, pos=Point3(5, 14, 5), hpr=(165, 10, 0), blendType='easeInOut'),
        Wait(1),
        Func(self.nametagJ.setChat, "Oh my goodness!", CFSpeech | CFTimeout), SoundInterval(self.cogGruntSpeech),
        Wait(2.5),
        LerpPosHprInterval(camera, duration=0.6, pos=Point3(5, 11, 5), hpr=(165, 10, 0), blendType='easeInOut'),
        Func(self.Elvis.loop, 'neutral'), Func(self.Elvis.loop, 'neutral'), 
        Func(self.nametagJ.setChat, "D- d- doughnuts????", CFSpeech | CFTimeout), SoundInterval(self.cogQuestionSpeech),
        Wait(3),
        Func(self.nametagJ.clearChat),
        LerpPosHprInterval(camera, duration=0.5, pos=Point3(7, 5, 7), hpr=(130, 10, 0), blendType='easeInOut'),
        Func(self.Elvis.loop, 'effort'), Func(self.Elvis.loop, 'effort'), 
        Func(self.nametagJ.setChat, "Ha! I can finally have some doughnuts!", CFSpeech | CFTimeout), SoundInterval(self.cogGruntSpeech),
        Wait(4.5),
        Func(self.nametagJ.clearChat),
        Func(self.Elvis.loop, 'neutral'), Func(self.Elvis.loop, 'neutral'),
        Parallel(LerpPosHprInterval(camera, duration=2, pos=Point3(-10, -2, 5), hpr=(270, 10, 0), blendType='easeInOut')),
        Func(self.Elvis.loop, 'walk'), Func(self.Elvis.loop, 'walk'),
        LerpPosHprInterval(self.Elvis, duration=4, pos=Point3(22, 0, 0), hpr=(270, 0, 0), blendType='noBlend'), 
        Func(self.Elvis.loop, 'sit'), Func(self.Elvis.loop, 'sit'),
        LerpPosHprInterval(camera, duration=2, pos=Point3(22, -11, 5), hpr=(0, 10, 0), blendType='easeInOut'),
        Func(self.nametagJ.setChat, "Mmm... Can't wait to eat these.", CFSpeech | CFTimeout), SoundInterval(self.cogMurmurSpeech),
        Wait(3),
        Func(self.nametagJ.clearChat),
        Func(self.Elvis.loop, 'sit-eat-loop'), Func(self.Elvis.loop, 'sit-eat-loop'),
        LerpPosHprInterval(camera, duration=2, pos=Point3(0, -11, 5), hpr=(0, 10, 0), blendType='easeInOut'),
        Func(self.coolencounter.play),
        LerpPosInterval(self.Rose, duration=4, pos=Point3(0, 40, 0), blendType='noBlend'),
        Wait(1.5),
        Func(self.Rose.loop, 'walk'), Func(self.Rose.loop, 'walk'),
        LerpPosInterval(self.Rose, duration=4, pos=Point3(0, 0, 0), blendType='noBlend'),
        Func(self.Rose.loop, 'walk'), Func(self.Rose.loop, 'walk'),
        LerpPosHprInterval(self.Rose, duration=2.5, pos=Point3(0, 0, 0), hpr=(270, 0, 0), blendType='noBlend'),
        Func(self.Rose.loop, 'neutral'), Func(self.Rose.loop, 'neutral'),
        LerpPosHprInterval(camera, duration=1.5, pos=Point3(16, 4, 5), hpr=(90, 10, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "Stop right there!", CFSpeech | CFTimeout), SoundInterval(self.cogGirlGruntSpeech),
        Wait(1),
        Func(self.nametagJ2.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(40, 0, 5), hpr=(90, 10, 0), blendType='easeInOut'),
        Func(self.Elvis.loop, 'slip-backward'), Func(self.Elvis.loop, 'slip-backward'),
        Func(self.nametagJ.setChat, "What was that???", CFSpeech | CFTimeout), SoundInterval(self.cogQuestionSpeech),
        Wait(2.5),
        LerpPosHprInterval(camera, duration=2, pos=Point3(11, 0, 5), hpr=(90, 10, 0), blendType='easeInOut'),
        Func(self.Rose.loop, 'finger-wag', fromFrame=0, toFrame=100), Func(self.Rose.setPlayRate, 3, 'fingerwag'),
        Func(self.nametagJ2.setChat, "Put those doughnuts down!", CFSpeech | CFTimeout), SoundInterval(self.cogGirlGruntSpeech),
        Wait(3),
        Func(self.nametagJ2.clearChat),
        Func(self.Elvis.loop, 'neutral'), Func(self.Elvis.loop, 'neutral'),
        LerpPosHprInterval(camera, duration=1.5, pos=Point3(40, 0, 5), hpr=(90, 10, 0), blendType='easeInOut'),
        Func(self.Rose.loop, 'walk'), Func(self.Rose.loop, 'walk'),
        LerpPosHprInterval(self.Rose, duration=3, pos=Point3(14, 0, 0), hpr=(270, 0, 0), blendType='noBlend'),
        Func(self.Rose.loop, 'neutral'), Func(self.Rose.loop, 'neutral'),
        LerpPosHprInterval(camera, duration=2, pos=Point3(20, -14, 7), hpr=(0, 10, 0), blendType='easeInOut'),
        Func(self.Rose.loop, 'speak', fromFrame=0, toFrame=150), Func(self.Rose.setPlayRate, 5, 'speak'),
        Func(self.nametagJ2.setChat, "Give them to me, or else!", CFSpeech | CFTimeout), SoundInterval(self.cogGirlGruntSpeech),
        Wait(3),
        Func(self.nametagJ2.clearChat),
        Func(self.Rose.loop, 'neutral'), Func(self.Rose.loop, 'neutral'),
        LerpPosHprInterval(camera, duration=0, pos=Point3(25, -14, 7), hpr=(30, 10, 0), blendType='easeInOut'),
        Func(self.Elvis.loop, 'walk'), Func(self.Elvis.loop, 'walk'),
        LerpPosHprInterval(self.Elvis, duration=1.5, pos=Point3(22, 0, 0), hpr=(90, 0, 0), blendType='noBlend'),
        Func(self.Elvis.loop, 'neutral'), Func(self.Elvis.loop, 'neutral'),
        Func(self.nametagJ.setChat, "Why should I?", CFSpeech | CFTimeout), SoundInterval(self.cogQuestionSpeech),
        Wait(3),
        Func(self.nametagJ.clearChat),
        LerpPosHprInterval(camera, duration=1, pos=Point3(14, 0, 7), hpr=(270, 10, 0), blendType='easeInOut'),
        Func(self.nametagJ.setChat, "I found these first.", CFSpeech | CFTimeout), SoundInterval(self.cogMurmurSpeech),
        Wait(2),
        Func(self.nametagJ.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(22, 0, 7), hpr=(90, 10, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "Lies!", CFSpeech | CFTimeout), SoundInterval(self.cogGirlGruntSpeech),
        Wait(3),
        Func(self.nametagJ2.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(27, -5, 4), hpr=(0, 10, 0), blendType='easeInOut'),
        Wait(2),
        LerpPosInterval(self.DoughProp, duration=0, pos=Point3(0, 0, 0), blendType='noBlend'),
        Func(self.coolencounter.stop),
        Wait(2.5),
        Func(self.coolkaren.play),
        LerpPosHprInterval(camera, duration=0.6, pos=Point3(22, 0, 7), hpr=(90, 10, 0), blendType='easeInOut'),
        Sequence(LerpPosHprInterval(camera, duration=0.1, pos=Point3(22, 0, 6), hpr=(90, 10, 0), blendType='easeInOut')),
        Func(self.Rose.loop, 'effort', fromFrame=90, toFrame=180), Func(self.Rose.setPlayRate, 1, 'effort'),
        Parallel(Func(self.nametagJ2.setChat, "My doughnuts!", CFSpeech | CFTimeout), SoundInterval(self.cogGirlAngrySpeech)),
        Parallel(LerpPosHprInterval(camera, duration=0.1, pos=Point3(22, 0, 7), hpr=(90, 10, 0), blendType='easeInOut')),
        LerpPosHprInterval(camera, duration=0.1, pos=Point3(22, 0, 6), hpr=(90, 10, 0), blendType='easeInOut'),
        LerpPosHprInterval(camera, duration=0.1, pos=Point3(22, 0, 7), hpr=(90, 10, 0), blendType='easeInOut'),
        LerpPosHprInterval(camera, duration=0.1, pos=Point3(22, 0, 6), hpr=(90, 10, 0), blendType='easeInOut'),
        LerpPosHprInterval(camera, duration=0.1, pos=Point3(22, 0, 7), hpr=(90, 10, 0), blendType='easeInOut'),
        LerpPosHprInterval(camera, duration=0.1, pos=Point3(22, 0, 6), hpr=(90, 10, 0), blendType='easeInOut'),
        LerpPosHprInterval(camera, duration=0.1, pos=Point3(22, 0, 7), hpr=(90, 10, 0), blendType='easeInOut'),
        Wait(2),
        Func(self.nametagJ2.clearChat),
        LerpPosHprInterval(camera, duration=0, pos=Point3(13, 7, 7), hpr=(180, 10, 0), blendType='easeInOut'),
        Func(self.Rose.loop, 'finger-wag', fromFrame=0, toFrame=150), Func(self.Rose.setPlayRate, 2, 'fingerwag'),
        Func(self.nametagJ2.setChat, "You'll regret that!", CFSpeech | CFTimeout), SoundInterval(self.cogGirlRageSpeech),
        Wait(1),
        Func(self.nametagJ2.clearChat),
        Func(self.Rose.loop, 'neutral'), Func(self.Rose.loop, 'neutral'),
        LerpPosHprInterval(camera, duration=1, pos=Point3(14, 0, 7), hpr=(270, 10, 0), blendType='easeInOut'),
        Func(self.nametagJ.setChat, "Gulp... gotta run!", CFSpeech | CFTimeout), SoundInterval(self.cogGruntSpeech),
        Wait(2),
        Func(self.nametagJ.clearChat),
        Func(self.Elvis.loop, 'walk'), Func(self.Elvis.loop, 'walk'),
        LerpPosHprInterval(self.Elvis, duration=1, pos=Point3(22, 0, 0), hpr=(180, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.Elvis, duration=0.8, pos=Point3(22, -100, 0), hpr=(180, 0, 0), blendType='noBlend'),
        Wait(2),
        LerpPosHprInterval(camera, duration=0, pos=Point3(22, 0, 7), hpr=(90, 10, 0), blendType='easeInOut'),
        Func(self.nametagJ2.setChat, "Hey, get back here!", CFSpeech | CFTimeout), SoundInterval(self.cogGirlGruntSpeech),
        Wait(2.5),
        Func(self.nametagJ.clearChat),
        Func(self.Rose.loop, 'walk'), Func(self.Rose.loop, 'walk'),
        LerpPosHprInterval(self.Rose, duration=1, pos=Point3(14, 0, 0), hpr=(180, 0, 0), blendType='noBlend'),
        LerpPosHprInterval(self.Rose, duration=0.8, pos=Point3(14, -100, 0), hpr=(180, 0, 0), blendType='noBlend'),
        Func(self.coolkaren.stop),
        Func(base.transitions.irisOut, 2),
        Wait(6))

        GoodTrack.start()