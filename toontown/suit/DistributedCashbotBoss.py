from direct.interval.IntervalGlobal import *
from direct.task.TaskManagerGlobal import *
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import TTLocalizer
import DistributedBossCog
from direct.task.Task import Task
import DistributedCashbotBossGoon
import SuitDNA
from toontown.toon import Toon
from toontown.toon import ToonDNA
from toontown.toon import NPCToons
from direct.fsm import FSM
from toontown.toonbase import ToontownGlobals
from otp.otpbase import OTPGlobals
from toontown.building import ElevatorUtils
from toontown.building import ElevatorConstants
from toontown.battle import MovieToonVictory
from toontown.battle import RewardPanel
from toontown.suit import DistributedSuitBase
from toontown.distributed import DelayDelete
from toontown.chat import ResistanceChat
from toontown.coghq import CogDisguiseGlobals
from panda3d.core import *
from panda3d.physics import *
from panda3d.direct import *
from libotp import *
import random
import math
OneBossCog = None
TTL = TTLocalizer

class DistributedCashbotBoss(DistributedBossCog.DistributedBossCog, FSM.FSM):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedCashbotBoss')
    numFakeGoons = 3

    def __init__(self, cr):
        DistributedBossCog.DistributedBossCog.__init__(self, cr)
        FSM.FSM.__init__(self, 'DistributedSellbotBoss')
        self.resistanceToon = None
        self.resistanceToonOnstage = 0
        self.cranes = {}
        self.safes = {}
        self.goons = []
        self.bossMaxDamage = ToontownGlobals.CashbotBossMaxDamage
        self.elevatorType = ElevatorConstants.ELEVATOR_CFO
        base.boss = self
       
        # Amanda Rose 
        self.suit = DistributedSuitBase.DistributedSuitBase(cr)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit('mh')
        self.suit.setDNA(suitDNA)
        self.suit.setDisplayName('Fashion Rose\nFashionbot\nLevel 10000')
        self.suit.setPickable(0)
        self.suit.doId = 0

        # Money Prize Wheel 
        self.suit1 = DistributedSuitBase.DistributedSuitBase(cr)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit('rb')
        self.suit1.setDNA(suitDNA)
        self.suit1.setDisplayName('Money Prize Wheel\nCarebot\nLevel 500')
        self.suit1.setPickable(0)
        self.suit1.doId = 0

    def announceGenerate(self):
        DistributedBossCog.DistributedBossCog.announceGenerate(self)
        self.setName(TTLocalizer.CashbotBossName)
        nameInfo = TTLocalizer.BossCogNameWithDept % {'name': self._name,
         'dept': SuitDNA.getDeptFullname(self.style.dept)}
        self.setDisplayName(nameInfo)
        target = CollisionSphere(2, 0, 0, 3)
        targetNode = CollisionNode('headTarget')
        targetNode.addSolid(target)
        targetNode.setCollideMask(ToontownGlobals.PieBitmask)
        self.headTarget = self.neck.attachNewNode(targetNode)
        shield = CollisionSphere(0, 0, 0.8, 7)
        shieldNode = CollisionNode('shield')
        shieldNode.addSolid(shield)
        shieldNode.setCollideMask(ToontownGlobals.PieBitmask)
        shieldNodePath = self.pelvis.attachNewNode(shieldNode)
        self.heldObject = None
        self.bossDamage = 0
        self.loadEnvironment()
        self.__makeResistanceToon()
        self.physicsMgr = PhysicsManager()
        integrator = LinearEulerIntegrator()
        self.physicsMgr.attachLinearIntegrator(integrator)
        fn = ForceNode('gravity')
        self.fnp = self.geom.attachNewNode(fn)
        gravity = LinearVectorForce(0, 0, -32)
        fn.addForce(gravity)
        self.physicsMgr.addLinearForce(gravity)
        localAvatar.chatMgr.chatInputSpeedChat.addCFOMenu()
        global OneBossCog
        if OneBossCog != None:
            self.notify.warning('Multiple BossCogs visible.')
        OneBossCog = self
        return

    def disable(self):
        global OneBossCog
        DistributedBossCog.DistributedBossCog.disable(self)
        self.demand('Off')
        self.unloadEnvironment()
        self.__cleanupResistanceToon()
        self.fnp.removeNode()
        self.physicsMgr.clearLinearForces()
        self.battleThreeMusic.stop()
        self.epilogueMusic.stop()
        localAvatar.chatMgr.chatInputSpeedChat.removeCFOMenu()
        if OneBossCog == self:
            OneBossCog = None
        return

    def __makeResistanceToon(self):
        if self.resistanceToon:
            return
        npc = NPCToons.createLocalNPC(555)
        npc.setName('Queen Berry Cat')
        npc.setPickable(0)
        npc.setPlayerType(NametagGroup.CCNonPlayer)
        npc.animFSM.request('neutral')
        self.resistanceToon = npc
        self.resistanceToon.setPosHpr(*ToontownGlobals.CashbotRTBattleOneStartPosHpr)
        state = random.getstate()
        random.seed(self.doId)
        self.resistanceToon.suitType = 'ls'
        random.setstate(state)
        self.fakeGoons = []
        for i in range(self.numFakeGoons):
            goon = DistributedCashbotBossGoon.DistributedCashbotBossGoon(base.cr)
            goon.doId = -1 - i
            goon.setBossCogId(self.doId)
            goon.generate()
            goon.announceGenerate()
            self.fakeGoons.append(goon)

        self.__hideFakeGoons()

    def __cleanupResistanceToon(self):
        self.__hideResistanceToon()
        if self.resistanceToon:
            self.resistanceToon.removeActive()
            self.resistanceToon.delete()
            self.resistanceToon = None
            for i in xrange(self.numFakeGoons):
                self.fakeGoons[i].disable()
                self.fakeGoons[i].delete()
                self.fakeGoons[i] = None

        return

    def __showResistanceToon(self, withSuit):
        if not self.resistanceToonOnstage:
            self.resistanceToon.addActive()
            self.resistanceToon.reparentTo(self.geom)
            self.resistanceToonOnstage = 1
        if withSuit:
            suit = self.resistanceToon.suitType
            self.resistanceToon.putOnSuit(suit, False)
        else:
            self.resistanceToon.takeOffSuit()

    def __hideResistanceToon(self):
        if self.resistanceToonOnstage:
            self.resistanceToon.removeActive()
            self.resistanceToon.detachNode()
            self.resistanceToonOnstage = 0

    def __hideFakeGoons(self):
        if self.fakeGoons:
            for goon in self.fakeGoons:
                goon.request('Off')

    def __showFakeGoons(self, state):
        print self.fakeGoons
        if self.fakeGoons:
            for goon in self.fakeGoons:
                goon.request(state)

    def loadEnvironment(self):
        DistributedBossCog.DistributedBossCog.loadEnvironment(self)
        self.midVault = loader.loadModel('phase_10/models/cogHQ/MidVault.bam')
        self.endVault = loader.loadModel('phase_10/models/cogHQ/EndVault.bam')
        self.lightning = loader.loadModel('phase_10/models/cogHQ/CBLightning.bam')
        self.magnet = loader.loadModel('phase_10/models/cogHQ/CBMagnet.bam')
        self.craneArm = loader.loadModel('phase_10/models/cogHQ/CBCraneArm.bam')
        self.controls = loader.loadModel('phase_10/models/cogHQ/CBCraneControls.bam')
        self.stick = loader.loadModel('phase_10/models/cogHQ/CBCraneStick.bam')
        self.safe = loader.loadModel('phase_10/models/cogHQ/CBSafe.bam')
        self.eyes = loader.loadModel('phase_10/models/cogHQ/CashBotBossEyes.bam')
        self.cableTex = self.craneArm.findTexture('MagnetControl')
        self.eyes.setPosHprScale(4.5, 0, -2.5, 90, 90, 0, 0.4, 0.4, 0.4)
        self.eyes.reparentTo(self.neck)
        self.eyes.hide()
        self.midVault.setPos(0, -222, -70.7)
        self.endVault.setPos(84, -201, -6)
        self.geom = NodePath('geom')
        self.midVault.reparentTo(self.geom)
        self.endVault.reparentTo(self.geom)
        self.endVault.findAllMatches('**/MagnetArms').detach()
        self.endVault.findAllMatches('**/Safes').detach()
        self.endVault.findAllMatches('**/MagnetControlsAll').detach()
        cn = self.endVault.find('**/wallsCollision').node()
        cn.setIntoCollideMask(OTPGlobals.WallBitmask | ToontownGlobals.PieBitmask)
        self.door1 = self.midVault.find('**/SlidingDoor1/')
        self.door2 = self.midVault.find('**/SlidingDoor/')
        self.door3 = self.endVault.find('**/SlidingDoor/')
        elevatorModel = loader.loadModel('phase_10/models/cogHQ/CFOElevator')
        elevatorOrigin = self.midVault.find('**/elevator_origin')
        elevatorOrigin.setScale(1)
        elevatorModel.reparentTo(elevatorOrigin)
        leftDoor = elevatorModel.find('**/left_door')
        leftDoor.setName('left-door')
        rightDoor = elevatorModel.find('**/right_door')
        rightDoor.setName('right-door')
        self.setupElevator(elevatorOrigin)
        ElevatorUtils.closeDoors(leftDoor, rightDoor, ElevatorConstants.ELEVATOR_CFO)
        walls = self.endVault.find('**/RollUpFrameCillison')
        walls.detachNode()
        self.evWalls = self.replaceCollisionPolysWithPlanes(walls)
        self.evWalls.reparentTo(self.endVault)
        self.evWalls.stash()
        floor = self.endVault.find('**/EndVaultFloorCollision')
        floor.detachNode()
        self.evFloor = self.replaceCollisionPolysWithPlanes(floor)
        self.evFloor.reparentTo(self.endVault)
        self.evFloor.setName('floor')
        plane = CollisionPlane(Plane(Vec3(0, 0, 1), Point3(0, 0, -50)))
        planeNode = CollisionNode('dropPlane')
        planeNode.addSolid(plane)
        planeNode.setCollideMask(ToontownGlobals.PieBitmask)
        self.geom.attachNewNode(planeNode)
        self.geom.reparentTo(render)
        self.elevatorMusic = base.loader.loadMusic('phase_10/audio/bgm/Carebot_elevator.ogg')
        self.betweenBattleMusic = base.loader.loadMusic('phase_10/audio/bgm/CB_boss_flee.ogg')
        self.promotionMusic = base.loadMusic('phase_10/audio/bgm/CFO_intro.ogg')
        self.battleOneMusic = base.loadMusic('phase_10/audio/bgm/cfo_round_1.ogg')
        self.battleTwoMusic = base.loadMusic('phase_10/audio/bgm/cfo_round_2.ogg')
        self.cutsceneMusic = base.loadMusic('phase_10/audio/bgm/CB_boss_flee_2.ogg')
        self.intermissionMusic = base.loadMusic('phase_10/audio/bgm/CB_boss_crane.ogg')
        self.battleThreeMusic = base.loadMusic('phase_10/audio/bgm/encntr_boss_bg.ogg')
        self.victoryMusic = base.loadMusic('phase_10/audio/bgm/CFO_win.ogg')

    def unloadEnvironment(self):
        DistributedBossCog.DistributedBossCog.unloadEnvironment(self)
        self.geom.removeNode()

    def replaceCollisionPolysWithPlanes(self, model):
        newCollisionNode = CollisionNode('collisions')
        newCollideMask = BitMask32(0)
        planes = []
        collList = model.findAllMatches('**/+CollisionNode')
        if not collList:
            collList = [model]
        for cnp in collList:
            cn = cnp.node()
            if not isinstance(cn, CollisionNode):
                self.notify.warning('Not a collision node: %s' % repr(cnp))
                break
            newCollideMask = newCollideMask | cn.getIntoCollideMask()
            for i in xrange(cn.getNumSolids()):
                solid = cn.getSolid(i)
                if isinstance(solid, CollisionPolygon):
                    plane = Plane(solid.getPlane())
                    planes.append(plane)
                else:
                    self.notify.warning('Unexpected collision solid: %s' % repr(solid))
                    newCollisionNode.addSolid(plane)

        newCollisionNode.setIntoCollideMask(newCollideMask)
        threshold = 0.1
        planes.sort(lambda p1, p2: p1.compareTo(p2, threshold))
        lastPlane = None
        for plane in planes:
            if lastPlane == None or plane.compareTo(lastPlane, threshold) != 0:
                cp = CollisionPlane(plane)
                newCollisionNode.addSolid(cp)
                lastPlane = plane

        return NodePath(newCollisionNode)

    def __makeGoonMovieForIntro(self):
        goonTrack = Parallel()
        goon = self.fakeGoons[0]
        goonTrack.append(Sequence(
            goon.posHprInterval(0, Point3(111, -287, 0), VBase3(165, 0, 0)),
            goon.posHprInterval(9, Point3(101, -323, 0), VBase3(165, 0, 0)),
            goon.hprInterval(1, VBase3(345, 0, 0)),
            goon.posHprInterval(9, Point3(111, -287, 0), VBase3(345, 0, 0)),
            goon.hprInterval(1, VBase3(165, 0, 0)),
            goon.posHprInterval(9.5, Point3(104, -316, 0), VBase3(165, 0, 0)),
            Func(goon.request, 'Stunned'),
            Wait(1)))
        goon = self.fakeGoons[1]
        goonTrack.append(Sequence(
            goon.posHprInterval(0, Point3(119, -315, 0), VBase3(357, 0, 0)),
            goon.posHprInterval(9, Point3(121, -280, 0), VBase3(357, 0, 0)),
            goon.hprInterval(1, VBase3(177, 0, 0)),
            goon.posHprInterval(9, Point3(119, -315, 0), VBase3(177, 0, 0)),
            goon.hprInterval(1, VBase3(357, 0, 0)),
            goon.posHprInterval(9, Point3(121, -280, 0), VBase3(357, 0, 0))))
        goon = self.fakeGoons[2]
        goonTrack.append(Sequence(
            goon.posHprInterval(0, Point3(102, -320, 0), VBase3(231, 0, 0)),
            goon.posHprInterval(9, Point3(127, -337, 0), VBase3(231, 0, 0)),
            goon.hprInterval(1, VBase3(51, 0, 0)),
            goon.posHprInterval(9, Point3(102, -320, 0), VBase3(51, 0, 0)),
            goon.hprInterval(1, VBase3(231, 0, 0)),
            goon.posHprInterval(9, Point3(127, -337, 0), VBase3(231, 0, 0))))
        return Sequence(Func(self.__showFakeGoons, 'Walk'), goonTrack, Func(self.__hideFakeGoons))

    def makeIntroductionMovie(self, delayDeletes):
        for toonId in self.involvedToons:
            toon = self.cr.doId2do.get(toonId)
            if toon:
                delayDeletes.append(DelayDelete.DelayDelete(toon, 'CashbotBoss.makeIntroductionMovie'))

        rtTrack = Sequence()
        startPos = Point3(ToontownGlobals.CashbotBossOffstagePosHpr[0], ToontownGlobals.CashbotBossOffstagePosHpr[1], ToontownGlobals.CashbotBossOffstagePosHpr[2])
        battlePos = Point3(ToontownGlobals.CashbotBossBattleOnePosHpr[0], ToontownGlobals.CashbotBossBattleOnePosHpr[1], ToontownGlobals.CashbotBossBattleOnePosHpr[2])
        battleHpr = VBase3(ToontownGlobals.CashbotBossBattleOnePosHpr[3], ToontownGlobals.CashbotBossBattleOnePosHpr[4], ToontownGlobals.CashbotBossBattleOnePosHpr[5])
        bossTrack = Sequence()
        bossTrack.append(Func(self.reparentTo, render))
        bossTrack.append(Func(self.getGeomNode().setH, 180))
        bossTrack.append(Func(self.pelvis.setHpr, self.pelvisForwardHpr))
        bossTrack.append(Func(self.loop, 'Ff_neutral'))
        track, hpr = self.rollBossToPoint(startPos, None, battlePos, None, 0)
        bossTrack.append(track)
        track, hpr = self.rollBossToPoint(battlePos, hpr, battlePos, battleHpr, 0)
        bossTrack.append(track)
        bossTrack.append(Func(self.getGeomNode().setH, 0))
        bossTrack.append(Func(self.pelvis.setHpr, self.pelvisReversedHpr))
        goonTrack = self.__makeGoonMovieForIntro()
        attackToons = TTL.CashbotBossCogAttack
        rToon = self.resistanceToon
        goon = self.fakeGoons[0]
        self.suit.setPosHpr(120, - 230, 0, 90, 0, 0)
        self.suit.show()
        strack = self.suit.beginSupaFlyMove(Point3(120, -255, 0), 1, 'fromSky', walkAfterLanding=False)
        self.suit1.setPosHpr(120, - 230, 0, 90, 0, 0)
        self.suit1.show()
        strack1 = self.suit1.beginSupaFlyMove(Point3(120, -215, 0), 1, 'fromSky', walkAfterLanding=False)
        rToon.setPosHpr(*ToontownGlobals.CashbotRTBattleOneStartPosHpr)
        track = Sequence(
            Func(base.camera.setPosHpr, 61.1, -228.8, 10.2, -90, 0, 0),
            Func(rToon.setChatAbsolute, "Yay! You Made it Toons!", CFSpeech),
            Wait(3),
            Func(rToon.clearChat),
            Func(rToon.setChatAbsolute, "Alright, just follow directions, and stay near me.", CFSpeech),
            Wait(3),
            Sequence(goonTrack, duration=0),
            Parallel(
                Func(self.suit.reparentTo, render), Func(self.suit.addActive), Func(strack.start),
                Func(self.suit1.reparentTo, render), Func(self.suit1.addActive), Func(strack1.start),
                Sequence(
                    Func(rToon.suit.setPlayRate, 1.4, 'walk'),
                    Func(rToon.suit.loop, 'walk'),
                    Parallel(
                        rToon.hprInterval(2, VBase3(270, 0, 0)),
                        Sequence(
                            Wait(2),
                            Func(rToon.clearChat))),
                        Func(rToon.suit.loop, 'neutral'),
                        self.door2.posInterval(2, VBase3(0, 0, 30)))),
                        Func(rToon.setHpr, 270, 0, 0),
                        Func(rToon.setChatAbsolute, "Huh? I don't remember this being here...", CFSpeech),
                        Func(base.camera.reparentTo, render),
                        Func(base.camera.setPosHpr, 61.1, -228.8, 10.2, -90, 0, 0),
                        self.door1.posInterval(2, VBase3(0, 0, 30)),
                        Parallel(
                            bossTrack,
                            Sequence(
                                Wait(2),
                                Func(rToon.clearChat),
                                self.door1.posInterval(1, VBase3(0, 0, 0)))),
                            camera.posHprInterval(1, Point3(93.3, -230, 0.7), VBase3(-92.9, 39.7, 8.3)),
                            Func(self.setChatAbsolute, "Welcome, everyone.", CFSpeech),
                            Wait(2.5),
                            Func(self.clearChat),
                            Func(self.setChatAbsolute, "I heard that you all came here for a meeting.", CFSpeech),
                            Wait(2.5),
                            Func(self.clearChat),
                            camera.posHprInterval(1, Point3(105, -215, 8.5), VBase3(-90, 0, 0)),
                            Func(self.suit1.setChatAbsolute, "However, the meeting got canceled due to things going the wrong direction.", CFSpeech),
                            Wait(2.5),
                            Func(self.suit1.clearChat),
                            Func(self.suit1.setChatAbsolute, "Fashion Rose and the others have taken care of some of our workers, however, we need more input.", CFSpeech),
                            Wait(2.5),
                            Func(self.suit1.clearChat),
                            camera.posHprInterval(0.5, Point3(110, -255, 7.5), VBase3(-90, 0, 0)),
                            Func(self.suit.setChatAbsolute, "And finally, the drama between the Fashionboss.", CFSpeech),
                            Wait(2.5),
                            Func(self.suit.clearChat),
                            base.camera.posHprInterval(1.5, Point3(74.3, -230, 20), VBase3(-92.9, 0, 0)),
                            Func(self.setChatAbsolute, "You, over there! Do you have anything to say?", CFSpeech),
                            Wait(2.5),
                            Func(self.clearChat),
                            base.camera.posHprInterval(2, Point3(61.1, -228.8, 10.2), VBase3(-90, 0, 0)),
		                    Func(rToon.setChatAbsolute, "I do, Boss.", CFSpeech),
                            Wait(2.5),
                            Func(rToon.clearChat),
		                    Func(rToon.setChatAbsolute, "You see, I don't think all this will be necessary.", CFSpeech),
                            Wait(2.5),
                            Func(rToon.clearChat),
		                    Func(rToon.setChatAbsolute, "I caught these Cogs trespassing here.", CFSpeech),
                            Wait(2.5),
                            Func(rToon.clearChat),
                            base.camera.posHprInterval(2, Point3(117, -220, 10.2), VBase3(-270, 0, 0)),
		                    Func(rToon.setChatAbsolute, "And I think we should throw them in prison.", CFSpeech),
                            Wait(2.5),
                            Func(rToon.clearChat),
                            base.camera.posHprInterval(1, Point3(104, -235, 7.5), VBase3(211, 0, 0)),
                            Parallel(Func(self.suit.setChatAbsolute, "Boss, I sense something!", CFSpeech), Func(self.suit.play, 'pie-small-react')),
                            Wait(3),
                            Func(self.suit.clearChat),
                            base.camera.posHprInterval(1, Point3(105, -215, 7.5), VBase3(270, 0, 0)),
                            Parallel(Func(self.suit1.setChatAbsolute, "We've been tricked! They're Toons!", CFSpeech), Func(self.suit1.play, 'effort')),
                            Wait(3),
                            Func(self.suit1.clearChat),
                            Func(self.suit.loop, 'neutral'),
                            base.camera.posHprInterval(1, Point3(61.1, -228.8, 10.2), VBase3(-90, 0, 0)),
		                    Func(rToon.setChatAbsolute, "What? no! That's no-", CFSpeech),
                            Wait(2.1),
                            Func(rToon.clearChat),
                            Func(self.suit1.loop, 'neutral'),
                            base.camera.posHprInterval(1.5, Point3(93.3, -230, 0.7), VBase3(-92.9, 39.7, 8.3)),
                            Func(self.setChatAbsolute, "What in the world, Toons?", CFSpeech),
                            Wait(1.5),
                            Func(self.clearChat),
                            Func(self.setChatAbsolute, "But wait, that can't be possible...", CFSpeech),
                            Wait(3),
                            Func(self.clearChat),
                            Func(self.setChatAbsolute, "If they're Toons, then, that means...", CFSpeech),
                            Wait(1),
                            Func(self.clearChat),
                            base.camera.posHprInterval(0, Point3(105, -215, 7.5), VBase3(-90, 0, 0)),
                            Parallel(Func(self.suit1.setChatAbsolute, "They're Toons in disguise!", CFSpeech), Func(self.suit1.setPlayRate, 10, 'glower'), Func(self.suit1.loop, 'glower')),
                            Wait(3),
                            Func(self.suit1.clearChat),
                            Func(self.suit1.setPlayRate, 1, 'neutral'), 
                            Func(self.suit1.loop, 'neutral'),
                            self.loseCogSuits(self.toonsA + self.toonsB, render, (113, -228, 10, 90, 0, 0)),
                            Wait(2),
                            Func(rToon.setHpr, 270, 0, 0),
                            self.loseCogSuits([rToon], render, (113, -217, 3, 90, 0, 0), True),
                            Func(rToon.normalEyes),
                            Func(rToon.blinkEyes),
                            Func(rToon.setChatAbsolute, "Um, um, um...", CFSpeech),
                            Wait(2.5),
                            Func(rToon.clearChat),
                            Func(rToon.setChatAbsolute, "He did it!", CFSpeech),
                            Wait(1.5),
                            Func(rToon.clearChat),
                            Func(self.__showResistanceToon, False),
                            Sequence(
                                Func(rToon.animFSM.request, 'run'),
                                rToon.hprInterval(1, VBase3(180, 0, 0)),
                                Parallel(
                                    Sequence(
                                        rToon.posInterval(1.5, VBase3(109, -294, 0)),
                                        Parallel(Func(rToon.animFSM.request, 'jump')),
                                        rToon.posInterval(1.5, VBase3(93.935, -341.065, 2))),
                                    self.door2.posInterval(3, VBase3(0, 0, 0))),
                                    Func(rToon.animFSM.request, 'neutral')),
                                    self.toonNormalEyes(self.involvedToons),
                                    self.toonNormalEyes([self.resistanceToon], True),
                                    Func(rToon.clearChat),
                                    Func(camera.setPosHpr, 93.3, -230, 0.7, -92.9, 39.7, 8.3),
                                    Func(base.camera.reparentTo, render),
                                    Func(base.camera.setPosHpr, 104, -235, 8.5, 211.5, 0, 0),
                                    Parallel(Func(self.suit.loop, 'walk'), self.suit.hprInterval(2, VBase3(0, 0, 0))),
                                    Func(self.suit.loop, 'neutral'),
                                    Func(self.suit.setChatAbsolute, "What did you do!?", CFSpeech),
                                    Wait(2),
                                    Func(self.suit.clearChat),
                                    base.camera.posHprInterval(0, Point3(105, -215, 7.5), VBase3(-90, 0, 0)),
                                    Parallel(Func(self.suit1.loop, 'walk'), self.suit1.hprInterval(1.5, VBase3(180, 0, 0))),
                                    Func(self.suit1.loop, 'neutral'),
                                    Func(self.suit1.setChatAbsolute, "I didn't do anything!", CFSpeech),
                                    Wait(3),
                                    Func(self.suit1.clearChat),
                                    Func(base.camera.setPosHpr, 104, -235, 8.5, 211.5, 0, 0),
                                    Func(self.suit.setChatAbsolute, "Then why did that Toon say so?!", CFSpeech),
                                    Wait(3),
                                    Func(self.suit.clearChat),
                                    base.camera.posHprInterval(1, Point3(75.3, -230, 18), VBase3(-92.9, 3, 0)),
                                    Func(self.setChatAbsolute, "Enough!", CFSpeech),
                                    Wait(1.5),
                                    Func(self.clearChat),
                                    Func(self.setChatAbsolute, "Fashion Rose, go get that Toon.", CFSpeech),
                                    Wait(3),
                                    Func(self.clearChat),
                                    Func(self.setChatAbsolute, "Money Prize, go monitor the vault.", CFSpeech),
                                    Wait(3),
                                    Func(self.clearChat),
                                    Func(base.camera.setPosHpr, 61.1, -228.8, 10.2, -90, 0, 0),
                                    Func(self.suit.setChatAbsolute, "Yes sir!", CFSpeech),
                                    Func(self.suit1.setChatAbsolute, "Yes sir!", CFSpeech),
                                    Wait(3),
                                    Func(self.suit.clearChat),
                                    Func(self.suit1.clearChat),
                                    Parallel(Func(self.suit.loop, 'walk'), self.suit.hprInterval(2, VBase3(180, 0, 0)),
                                    Func(self.suit1.loop, 'walk'), self.suit1.hprInterval(2, VBase3(0, 0, 0))),
                                    Parallel(self.door1.posInterval(3, VBase3(30, 0, 0)),
                                    self.door2.posInterval(3, VBase3(30, 0, 0))),
                                    Parallel(LerpPosInterval(self.suit1, duration=8, pos=Point3(120, -105, 0), blendType='noBlend'),
                                    self.suit.posInterval(8, Point3(self.suit.getX(), -347, 0)), Func(self.suit.loop, 'walk')),
                                    Parallel(self.door1.posInterval(3, VBase3(0, 0, 0)),
                                    self.door2.posInterval(3, VBase3(0, 0, 0))),
                                    base.camera.posHprInterval(1, Point3(75.3, -230, 18), VBase3(-92.9, 3, 0)),
                                    Func(self.suit1.hide),
                                    Parallel(Func(self.suit.loop, 'neutral'), LerpPosInterval(self.suit, duration=0, pos=Point3(108.458, -347.558,  0.038), blendType='noBlend')),
                                    Func(self.setChatAbsolute, "Ugh, this is just ridiculous...", CFSpeech),
                                    Wait(3),
                                    Func(self.clearChat),
                                    Func(self.setChatAbsolute, "I specifically put this security to the max, and look what happened...", CFSpeech),
                                    Wait(3),
                                    Func(self.clearChat),
                                    Func(self.setChatAbsolute, "Not to worry though, I have v2.0 Cogs on my end for the extra security.", CFSpeech),
                                    Wait(3),
                                    Func(self.clearChat),
                                    Func(self.setChatAbsolute, "Get rid of them!!!", CFSpeech),
                                    base.camera.posHprInterval(0.5, Point3(75.3, -230, 21), VBase3(-92.9, 0, 0)), 
                                    LerpColorScaleInterval(render, 2, Vec4(1.0, 0.2, 0.5, 1.0)),
                                    Func(self.clearChat),
                                    Wait(2))
        return track

    def __makeRollToBattleTwoMovie(self):
        startPos = Point3(ToontownGlobals.CashbotBossBattleOnePosHpr[0], ToontownGlobals.CashbotBossBattleOnePosHpr[1], ToontownGlobals.CashbotBossBattleOnePosHpr[2])
        battlePos = Point3(ToontownGlobals.CashbotBossBattleTwoPosHpr[0], ToontownGlobals.CashbotBossBattleTwoPosHpr[1], ToontownGlobals.CashbotBossBattleTwoPosHpr[2])
        battleHpr = VBase3(ToontownGlobals.CashbotBossBattleTwoPosHpr[3], ToontownGlobals.CashbotBossBattleTwoPosHpr[4], ToontownGlobals.CashbotBossBattleTwoPosHpr[5])
        bossTrack = Sequence()
        bossTrack.append(Func(self.getGeomNode().setH, 0))
        bossTrack.append(Func(self.loop, 'Fb_neutral'))
        track, hpr = self.rollBossToPoint(startPos, None, battlePos, None, 0)
        bossTrack.append(track)
        track, hpr = self.rollBossToPoint(battlePos, hpr, battlePos, battleHpr, 0)
        return Sequence(bossTrack, Func(self.getGeomNode().setH, 0), name=self.uniqueName('BattleTwo'))
        
        
    def makePrepareBattleTwoMovie(self, delayDeletes):
        for toonId in self.involvedToons:
            toon = self.cr.doId2do.get(toonId)
            if toon:
                delayDeletes.append(DelayDelete.DelayDelete(toon, 'CashbotBoss.makePrepareBattleTwoMovie'))
                
       
       
        startPos = Point3(ToontownGlobals.CashbotBossBattleOnePosHpr[0], ToontownGlobals.CashbotBossBattleOnePosHpr[1], ToontownGlobals.CashbotBossBattleOnePosHpr[2])
        battlePos = Point3(ToontownGlobals.CashbotBossBattleThreePosHpr[0], ToontownGlobals.CashbotBossBattleThreePosHpr[1], ToontownGlobals.CashbotBossBattleThreePosHpr[2])
        startHpr = Point3(ToontownGlobals.CashbotBossBattleOnePosHpr[3], ToontownGlobals.CashbotBossBattleOnePosHpr[4], ToontownGlobals.CashbotBossBattleOnePosHpr[5])
        battleHpr = VBase3(ToontownGlobals.CashbotBossBattleThreePosHpr[3], ToontownGlobals.CashbotBossBattleThreePosHpr[4], ToontownGlobals.CashbotBossBattleThreePosHpr[5])
        finalHpr = VBase3(105, 0, 0)
        bossTrack = Sequence()
        bossTrack.append(Func(self.reparentTo, render))
        bossTrack.append(Func(self.getGeomNode().setH, 180))
        bossTrack.append(Func(self.pelvis.setHpr, self.pelvisForwardHpr))
        bossTrack.append(Func(self.loop, 'Ff_neutral'))
        track, hpr = self.rollBossToPoint(startPos, startHpr, startPos, battleHpr, 0)
        bossTrack.append(track)
        track, hpr = self.rollBossToPoint(startPos, None, battlePos, None, 0)
        bossTrack.append(track)
        track, hpr = self.rollBossToPoint(battlePos, battleHpr, battlePos, finalHpr, 0)
        bossTrack.append(track)
        rToon = self.resistanceToon
        rToon.setPosHpr(93.935, -341.065, 0, -45, 0, 0)
        strack = self.suit.beginSupaFlyMove(Point3(120, -347.558, 0), 0, 'flyAway')
        track = Sequence(
            Func(base.camera.wrtReparentTo, self.geom),
            base.camera.posHprInterval(1.5, Point3(120, -332.612, 5), Point3(136.3, 0, 0), blendType='easeInOut'),
            Func(self.suit.loop, 'walk'),
            self.suit.hprInterval(1, VBase3(90, 0, 0)),
            Func(self.suit.loop, 'neutral'),
            base.camera.posHprInterval(1.5, Point3(100, -347.558, 7.5), Point3(270, 0, 0), blendType='easeInOut'),
            Func(self.suit.setChatAbsolute, 'Well, Toon...', CFSpeech),
            Wait(2),
            Func(self.suit.clearChat),
            Func(self.suit.setChatAbsolute, 'I got you now.', CFSpeech),
            Wait(3),
            Func(self.suit.clearChat),
            base.camera.posHprInterval(1, Point3(95, -347.558, 7.5), Point3(270, 0, 0), blendType='easeInOut'),
            Func(self.suit.setChatAbsolute, 'You will not get away with this...', CFSpeech),
            Wait(2.5),
            Func(self.suit.clearChat),
            Func(rToon.sadEyes),
            Func(rToon.blinkEyes),
            Func(rToon.setHpr, 270, 0, 0),
            base.camera.posHprInterval(1.5, Point3(110, -340.558, 4), Point3(90, 0, 0), blendType='easeInOut'),
            Func(rToon.setChatAbsolute, "No, don't hurt me!", CFSpeech),
            Wait(3),
            Func(rToon.clearChat),
            Func(rToon.setChatAbsolute, "Please... I'm begging you, just leave...", CFSpeech|CFTimeout),
            Wait(3),
            Func(rToon.clearChat),
            base.camera.posHprInterval(0.8, Point3(104, -340.558, 5), Point3(90, 0, 0), blendType='easeInOut'),
            Func(rToon.setChatAbsolute, "I don't want anything to do with this...", CFSpeech|CFTimeout),
            Wait(2),
            Func(rToon.clearChat),
            base.camera.posHprInterval(1.5, Point3(120, -332.612, 5), Point3(136.3, 10, 0), blendType='easeInOut'),
            Func(self.suit.setChatAbsolute, 'Did you really think you were going to get away with this?', CFSpeech),
            Wait(3),
            Func(self.suit.clearChat),
            base.camera.posHprInterval(1, Point3(98, -347.558, 7.5), Point3(270, 0, 0), blendType='easeInOut'),
            Func(self.suit.setChatAbsolute, 'You shall suffer the consequences for what you did to our vault.', CFSpeech),
            Wait(3),
            Func(self.suit.clearChat),
            base.camera.posHprInterval(1, Point3(95, -347.558, 7.5), Point3(270, 0, 0), blendType='easeInOut'),
            Func(self.suit.setChatAbsolute, 'You shall be eliminated!', CFSpeech),
            Wait(3),
            Func(self.suit.clearChat),
            base.camera.posHprInterval(0.8, Point3(104, -340.558, 5), Point3(90, 0, 0), blendType='easeInOut'),
            Func(rToon.setChatAbsolute, "Wait, no! </3", CFSpeech),
            Wait(3),
            Func(rToon.clearChat),
            Func(rToon.setChatAbsolute, "Don't do this... you don't have to do this... </3", CFSpeech),
            Wait(3),
            Func(rToon.clearChat),
            base.camera.posHprInterval(1, Point3(95, -347.558, 7.5), Point3(270, 0, 0), blendType='easeInOut'),
            Func(self.suit.setChatAbsolute, "Ugh, you know what? Fine.", CFSpeech),
            Wait(3),
            Func(self.suit.clearChat),
            Func(self.suit.setChatAbsolute, "I won't harm you, but you shall promise one thing.", CFSpeech),
            Wait(3),
            Func(self.suit.clearChat),
            Func(self.suit.setChatAbsolute, 'You will not go in here again, and you will not harm our cog kind.', CFSpeech),
            Wait(3),
            Func(self.suit.clearChat),
            base.camera.posHprInterval(1, Point3(90, -347.558, 7.5), Point3(270, 0, 0), blendType='easeInOut'),
            Func(self.suit.setChatAbsolute, 'I have something to attend to, see you later.', CFSpeech),
             Wait(3),                 
            Sequence(
                Wait(2),
                Func(strack.start)),
                Parallel(
                    Sequence(
                        Wait(2),
                        Func(self.suit.clearChat),  
                        Wait(2),
                        Func(self.suit.hide),                        
                        Wait(2),
                        base.camera.posHprInterval(1.5, Point3(94, -315, 20), Point3(-90, 11, 0), blendType='easeInOut'),
                        Func(self.setChatAbsolute, 'No! Rose! You get back here!', CFSpeech),
                        Wait(3),
                        Func(self.clearChat),
                        Func(self.setChatAbsolute, "Ugh, now what am I supposed to do?", CFSpeech),
                        Wait(3),
                        Func(self.clearChat),
                        Func(self.setChatAbsolute, "I can't attend the meeting with Toons in my way...", CFSpeech),
                        Wait(3),
                        Func(self.clearChat),
                        Func(self.setChatAbsolute, 'Luckily for me, I got another plan.',  CFSpeech),
                        Wait(3),
                        Func(self.clearChat),
                        Func(self.setChatAbsolute, "Looks like my security hasn't reached the max yet.",  CFSpeech),
                        Wait(3),
                        Func(self.clearChat),
                        base.camera.posHprInterval(1.5, Point3(170, -315, 4), Point3(-270, 10, 0), blendType='easeInOut'),
                        Func(self.setChatAbsolute, 'I can just use my Boss Cogs!',  CFSpeech),
                        Wait(3),
                        Func(self.clearChat),
                        Func(rToon.setHpr, 180, 0, 0),
                        Func(rToon.sadEyes),
                        Func(rToon.closeEyes),
                        base.camera.posHprInterval(1.5, Point3(100, -332.612, 5), Point3(136.3, 0, 0), blendType='easeInOut'),
                        Func(rToon.setChatAbsolute, "I wish Master Cool Cat was here... sniff... </3", CFSpeech),
                        Wait(3),
                        Func(rToon.clearChat),
                        base.camera.posHprInterval(1.5, Point3(95, -315, 20), Point3(-90, 11, 0), blendType='easeInOut'),
                        Func(self.setChatAbsolute, 'Shut it, Toon!', CFSpeech),
                        Wait(2),
                        Func(self.clearChat),
                        Func(self.setChatAbsolute, 'I did not come here for failure...', CFSpeech),
                        Wait(3),
                        Func(self.clearChat),
                        Func(self.setChatAbsolute, 'Toons like you had no accomplishment.', CFSpeech),
                        Wait(3),
                        Func(self.clearChat),
                        Func(self.setChatAbsolute, "Cogs like us have a goal, and that is making y'all go sad.", CFSpeech),
                        Wait(3),
                        Func(self.clearChat),
                        Func(rToon.sadEyes),
                        Func(rToon.blinkEyes),
                        base.camera.posHprInterval(1.5, Point3(78, -340.612, 5), Point3(270, 0, 0), blendType='easeInOut'),
                        Func(rToon.setChatAbsolute, "... Here we go again...", CFSpeech|CFTimeout),
                        Wait(3),
                        Func(rToon.clearChat),
                        base.camera.posHprInterval(1.5, Point3(95, -315, 20), Point3(-90, 11, 0), blendType='easeInOut'),
                        Func(self.setChatAbsolute, 'Boss Cogs...',  CFSpeech),
                        Wait(3),
                        Func(self.clearChat),
                        Func(self.setChatAbsolute, "Y'all know the drill...",  CFSpeech),
                        Wait(3),
                        Func(self.clearChat),
                        Func(self.setChatAbsolute, 'Leave no Toons here! Get them, get them all!',  CFSpeech),
                        base.camera.posHprInterval(1.5, Point3(86, -315, 20), Point3(-90, 5, 0), blendType='easeInOut'),
                        LerpColorScaleInterval(render, 2, Vec4(0.5, 1.0, 0.5, 1.0)),
                        Wait(3),
                        Func(self.clearChat),
                        Func(base.camera.wrtReparentTo, self.geom),
                        Wait(1))))
        return track
		
    
    def __makeGoonMovieForBattleThree(self):
        goonPosHprs = [[Point3(111, -287, 0),
          VBase3(165, 0, 0),
          Point3(101, -323, 0),
          VBase3(165, 0, 0)], [Point3(119, -315, 0),
          VBase3(357, 0, 0),
          Point3(121, -280, 0),
          VBase3(357, 0, 0)], [Point3(102, -320, 0),
          VBase3(231, 0, 0),
          Point3(127, -337, 0),
          VBase3(231, 0, 0)]]
        mainGoon = self.fakeGoons[0]
        goonLoop = Parallel()
        print(self.fakeGoons)
        for i in range(1, self.numFakeGoons):
            goon = self.fakeGoons[i]
            goonLoop.append(Sequence(goon.posHprInterval(8, goonPosHprs[i][0], goonPosHprs[i][1]), goon.posHprInterval(8, goonPosHprs[i][2], goonPosHprs[i][3])))

        goonTrack = Sequence(Func(self.__showFakeGoons, 'Walk'), Func(mainGoon.request, 'Stunned'), Func(goonLoop.loop), Wait(20))
        return goonTrack

    def makePrepareBattleThreeMovie(self, delayDeletes, crane, safe):
        for toonId in self.involvedToons:
            toon = self.cr.doId2do.get(toonId)
            if toon:
                delayDeletes.append(DelayDelete.DelayDelete(toon, 'CashbotBoss.makePrepareBattleThreeMovie'))

        startPos = Point3(ToontownGlobals.CashbotBossBattleOnePosHpr[0], ToontownGlobals.CashbotBossBattleOnePosHpr[1], ToontownGlobals.CashbotBossBattleOnePosHpr[2])
        battlePos = Point3(ToontownGlobals.CashbotBossBattleThreePosHpr[0], ToontownGlobals.CashbotBossBattleThreePosHpr[1], ToontownGlobals.CashbotBossBattleThreePosHpr[2])
        startHpr = Point3(ToontownGlobals.CashbotBossBattleOnePosHpr[3], ToontownGlobals.CashbotBossBattleOnePosHpr[4], ToontownGlobals.CashbotBossBattleOnePosHpr[5])
        battleHpr = VBase3(ToontownGlobals.CashbotBossBattleThreePosHpr[3], ToontownGlobals.CashbotBossBattleThreePosHpr[4], ToontownGlobals.CashbotBossBattleThreePosHpr[5])
        finalHpr = VBase3(135, 0, 0)
        bossTrack = Sequence()
        bossTrack.append(Func(self.reparentTo, render))
        bossTrack.append(Func(self.getGeomNode().setH, 180))
        bossTrack.append(Func(self.pelvis.setHpr, self.pelvisForwardHpr))
        bossTrack.append(Func(self.loop, 'Ff_neutral'))
        track, hpr = self.rollBossToPoint(startPos, startHpr, startPos, battleHpr, 0)
        bossTrack.append(track)
        track, hpr = self.rollBossToPoint(startPos, None, battlePos, None, 0)
        bossTrack.append(track)
        track, hpr = self.rollBossToPoint(battlePos, battleHpr, battlePos, finalHpr, 0)
        bossTrack.append(track)
        rToon = self.resistanceToon
        rToon.setPosHpr(93.935, -341.065, 0, -45, 0, 0)
        goon = self.fakeGoons[0]
        crane = self.cranes[0]
        track = Sequence(
            Func(self.__hideToons),
            Func(crane.request, 'Movie'),
            Func(crane.accomodateToon, rToon),
            Func(goon.request, 'Stunned'),
            Func(goon.setPosHpr, 104, -316, 0, 165, 0, 0),
            Func(rToon.loop, 'leverNeutral'),
            Func(base.camera.wrtReparentTo, self.geom),
            Func(rToon.normalEyes),
            Func(rToon.blinkEyes),
            base.camera.posHprInterval(1, Point3(105, -326, 5), Point3(136.3, 0, 0), blendType='easeInOut'),
            Func(rToon.setChatAbsolute, "Horray, I did it!", CFSpeech),
            Wait(2.5),
            Func(rToon.clearChat),
            Func(rToon.setChatAbsolute, "It's finally completed...", CFSpeech),
            Wait(2.5),
            Func(rToon.clearChat),
            base.camera.posHprInterval(1.5, Point3(96, -315, 20), Point3(-90, 11, 0), blendType='easeInOut'),
            Func(self.setChatAbsolute, "Listen, Queen, you're not getting away with this...", CFSpeech),
            Wait(2.5),
            Func(self.clearChat),
            Func(self.setChatAbsolute, "You may have tricked me, but these Toons haven't killed my Cogs.", CFSpeech),
            Wait(2.5),
            Func(self.clearChat),
            Func(self.setChatAbsolute, "Look at your friends, they're still fighting. >:)", CFSpeech),
            Wait(2.5),
            Func(self.clearChat),
            base.camera.posHprInterval(1, Point3(105, -326, 5), Point3(136.3, 0, 0), blendType='easeInOut'),
            Func(rToon.setChatAbsolute, "How's this, Money Cashout? >:)", CFSpeech),
            Wait(2.5),
            Func(rToon.clearChat),
            Func(rToon.setChatAbsolute, "They killed all your Cogs, hehe. <3", CFSpeech),
            Wait(2.5),
            Func(rToon.clearChat),
            base.camera.posHprInterval(0, Point3(82, -315, 20), Point3(-90, 11, 0), blendType='easeInOut'),
            Func(self.setChatAbsolute, TTL.CashbotBossGetAwayFromThat1, CFSpeech),
            Wait(0.7),
            Func(self.clearChat),
            base.camera.posHprInterval(0, Point3(86, -315, 20), Point3(-90, 11, 0), blendType='easeInOut'),
            Func(self.setChatAbsolute, TTL.CashbotBossGetAwayFromThat2, CFSpeech),
            Wait(0.7),
            Func(self.clearChat),
            base.camera.posHprInterval(0, Point3(90, -315, 20), Point3(-90, 11, 0), blendType='easeInOut'),
            Func(self.setChatAbsolute, TTL.CashbotBossGetAwayFromThat3, CFSpeech),
            Wait(1.5),
            Func(self.clearChat),
            base.camera.posHprInterval(1, Point3(95, -315, 20), Point3(-90, 11, 0), blendType='easeInOut'),
            Func(self.setChatAbsolute, TTL.CashbotBossGetAwayFromThat4, CFSpeech),
            Wait(3),
            Func(self.clearChat),
            base.camera.posHprInterval(1, Point3(105, -326, 5), Point3(136.3, 0, 0), blendType='easeInOut'),
            Func(rToon.setChatAbsolute, TTL.ResistanceToonCraneInstructions1, CFSpeech),
            Wait(2),
            Func(rToon.clearChat),
            Func(rToon.setChatAbsolute, TTL.ResistanceToonCraneInstructions2, CFSpeech),
            Wait(1),
            Func(rToon.clearChat),
            base.camera.posHprInterval(2, Point3(105, -336, 20), Point3(-45, 11, 0), blendType='easeInOut'),
            Func(self.setChatAbsolute, TTL.CashbotBossNotDealing1, CFSpeech),
            Wait(3),
            Func(self.clearChat),
            Func(self.setChatAbsolute, TTL.CashbotBossNotDealing2, CFSpeech),
            Wait(3),
            Func(self.clearChat),
            Func(self.setChatAbsolute, TTL.CashbotBossNotDealing3, CFSpeech),
            Wait(3),
            Func(self.clearChat),
            base.camera.posHprInterval(1, Point3(90, -315, 18), Point3(-90, 11, 0), blendType='easeInOut'),
            Func(self.setChatAbsolute, TTL.CashbotBossNotDealing4, CFSpeech),
            Wait(4),
            Func(self.clearChat),
            base.camera.posHprInterval(1, Point3(95, -315, 20), Point3(-90, 11, 0), blendType='easeInOut'),
            Func(self.setChatAbsolute, TTL.CashbotBossGoonsCommand, CFSpeech),
            Wait(2.5),
            Func(self.clearChat),
            base.camera.posHprInterval(1, Point3(89, -315, 10), Point3(-90, 30, 0), blendType='easeInOut'),
            Func(self.setChatAbsolute, TTL.CashbotBossGoonAttack, CFSpeech),
            Wait(2.5),
            Func(self.clearChat),
            base.camera.posHprInterval(1, Point3(102, -323.6, 0.9), VBase3(-10.6, 14, 0), blendType='easeInOut'),
            Func(goon.request, 'Recovery'),
            Wait(2),
            base.camera.posHprInterval(1, Point3(95.4, -332.6, 4.2), VBase3(167.1, -13.2, 0), blendType='easeInOut'),
            Func(rToon.setChatAbsolute, TTL.ResistanceToonGetaway, CFSpeech),
            Func(rToon.animFSM.request, 'jump'),
            Wait(1.8),
            Func(rToon.clearChat),
            base.camera.posHprInterval(1, Point3(109.1, -300.7, 13.9), VBase3(-15.6, -13.6, 0), blendType='easeInOut'),
            Func(rToon.setChatAbsolute, TTL.ResistanceToonRunaway, CFSpeech),
            Func(rToon.animFSM.request, 'run'),
            Func(goon.request, 'Walk'),
            Parallel(
                self.door3.posInterval(3, VBase3(0, 0, 0)),
                rToon.posHprInterval(3, Point3(136, -212.9, 0), VBase3(-14, 0, 0), startPos=Point3(110.8, -292.7, 0), startHpr=VBase3(-14, 0, 0)),
                goon.posHprInterval(3, Point3(125.2, -243.5, 0), VBase3(-14, 0, 0), startPos=Point3(104.8, -309.5, 0), startHpr=VBase3(-14, 0, 0))),
            Func(self.__hideFakeGoons),
            Func(self.intermissionMusic.stop),
            Func(crane.request, 'Free'),
            Func(self.getGeomNode().setH, 0),
            self.moveToonsToBattleThreePos(self.involvedToons),
            Func(self.__showToons))
        return Sequence(Func(camera.reparentTo, self), Func(camera.setPosHpr, 0, -27, 25, 0, -18, 0), track)

    def moveToonsToBattleThreePos(self, toons):
        track = Parallel()
        for i in range(len(toons)):
            toon = base.cr.doId2do.get(toons[i])
            if toon:
                posHpr = ToontownGlobals.CashbotToonsBattleThreeStartPosHpr[i]
                pos = Point3(*posHpr[0:3])
                hpr = VBase3(*posHpr[3:6])
                track.append(toon.posHprInterval(0.2, pos, hpr))

        return track

    def moveToonsToBattleThreePos(self, toons):
        track = Parallel()
        for i in range(len(toons)):
            toon = base.cr.doId2do.get(toons[i])
            if toon:
                posHpr = ToontownGlobals.CashbotToonsBattleThreeStartPosHpr[i]
                pos = Point3(*posHpr[0:3])
                hpr = VBase3(*posHpr[3:6])
                track.append(toon.posHprInterval(0.2, pos, hpr))

        return track

    def makeBossFleeMovie(self):
        hadEnough = TTLocalizer.CashbotBossHadEnough
        outtaHere = TTLocalizer.CashbotBossOuttaHere
        loco = loader.loadModel('phase_10/models/cogHQ/CashBotLocomotive')
        car1 = loader.loadModel('phase_10/models/cogHQ/CashBotBoxCar')
        car2 = loader.loadModel('phase_10/models/cogHQ/CashBotTankCar')
        trainPassingSfx = base.loader.loadSfx('phase_10/audio/sfx/CBHQ_TRAIN_pass.ogg')
        boomSfx = loader.loadSfx('phase_3.5/audio/sfx/ENC_cogfall_apart.ogg')
        rollThroughDoor = self.rollBossToPoint(fromPos=Point3(120, -280, 0), fromHpr=None, toPos=Point3(120, -250, 0), toHpr=None, reverse=0)
        rollTrack = Sequence(Func(self.getGeomNode().setH, 180), rollThroughDoor[0], Func(self.getGeomNode().setH, 0))
        g = 80.0 / 300.0
        trainTrack = Track(
            (0 * g, loco.posInterval(0.5, Point3(0, -242, 0), startPos=Point3(150, -242, 0))),
            (1 * g, car2.posInterval(0.5, Point3(0, -242, 0), startPos=Point3(150, -242, 0))),
            (2 * g, car1.posInterval(0.5, Point3(0, -242, 0), startPos=Point3(150, -242, 0))),
            (3 * g, car2.posInterval(0.5, Point3(0, -242, 0), startPos=Point3(150, -242, 0))),
            (4 * g, car1.posInterval(0.5, Point3(0, -242, 0), startPos=Point3(150, -242, 0))),
            (5 * g, car2.posInterval(0.5, Point3(0, -242, 0), startPos=Point3(150, -242, 0))),
            (6 * g, car1.posInterval(0.5, Point3(0, -242, 0), startPos=Point3(150, -242, 0))),
            (7 * g, car2.posInterval(0.5, Point3(0, -242, 0), startPos=Point3(150, -242, 0))),
            (8 * g, car1.posInterval(0.5, Point3(0, -242, 0), startPos=Point3(150, -242, 0))),
            (9 * g, car2.posInterval(0.5, Point3(0, -242, 0), startPos=Point3(150, -242, 0))),
            (10 * g, car1.posInterval(0.5, Point3(0, -242, 0), startPos=Point3(150, -242, 0))),
            (11 * g, car2.posInterval(0.5, Point3(0, -242, 0), startPos=Point3(150, -242, 0))),
            (12 * g, car1.posInterval(0.5, Point3(0, -242, 0), startPos=Point3(150, -242, 0))),
            (13 * g, car2.posInterval(0.5, Point3(0, -242, 0), startPos=Point3(150, -242, 0))),
            (14 * g, car1.posInterval(0.5, Point3(0, -242, 0), startPos=Point3(150, -242, 0))))
        bossTrack = Track(
            (0.0, Sequence(
                Func(camera.reparentTo, render),
                Func(camera.setPosHpr, 105, -280, 20, -158, -3, 0),
                Func(self.reparentTo, render),
                Func(self.show),
                Func(self.clearChat),
                Func(self.setPosHpr, *ToontownGlobals.CashbotBossBattleThreePosHpr),
                Func(self.reverseHead),
                ActorInterval(self, 'Fb_firstHit'),
                ActorInterval(self, 'Fb_down2Up'))),
            (1.0, Func(self.setChatAbsolute, hadEnough, CFSpeech)),
            (5.1, Func(self.clearChat)),
            (5.5, Parallel(
                Func(camera.setPosHpr, 100, -315, 16, -20, 0, 0),
                Func(self.hideBattleThreeObjects),
                Func(self.forwardHead),
                Func(self.loop, 'Ff_neutral'),
                rollTrack,
                self.door3.posInterval(2.5, Point3(0, 0, 25), startPos=Point3(0, 0, 18)))),
            (5.5, Func(self.setChatAbsolute, outtaHere, CFSpeech)),
            (5.5, SoundInterval(trainPassingSfx)),
            (8.1, Func(self.clearChat)),
            (9.4, Sequence(
                Func(loco.reparentTo, render),
                Func(car1.reparentTo, render),
                Func(car2.reparentTo, render),
                trainTrack,
                Func(loco.detachNode),
                Func(car1.detachNode),
                Func(car2.detachNode),
                Wait(2))),
            (9.5, SoundInterval(boomSfx)),
            (9.5, Sequence(
                self.posInterval(0.4, Point3(0, -250, 0)),
                LerpColorScaleInterval(render, 5, Vec4(1.0, 1.0, 1.0, 1.0)),
                Func(self.stash))))
        return bossTrack

    def grabObject(self, obj):
        obj.wrtReparentTo(self.neck)
        obj.hideShadows()
        obj.stashCollisions()
        if obj.lerpInterval:
            obj.lerpInterval.finish()
        obj.lerpInterval = Parallel(obj.posInterval(ToontownGlobals.CashbotBossToMagnetTime, Point3(-1, 0, 0.2)), obj.quatInterval(ToontownGlobals.CashbotBossToMagnetTime, VBase3(0, -90, 90)), Sequence(Wait(ToontownGlobals.CashbotBossToMagnetTime), ShowInterval(self.eyes)), obj.toMagnetSoundInterval)
        obj.lerpInterval.start()
        self.heldObject = obj

    def dropObject(self, obj):
        if obj.lerpInterval:
            obj.lerpInterval.finish()
            obj.lerpInterval = None
        obj = self.heldObject
        obj.wrtReparentTo(render)
        obj.setHpr(obj.getH(), 0, 0)
        self.eyes.hide()
        obj.showShadows()
        obj.unstashCollisions()
        self.heldObject = None
        return

    def setBossDamage(self, bossDamage):
        if bossDamage > self.bossDamage:
            delta = bossDamage - self.bossDamage
            self.flashRed()
            self.doAnimate('hit', now=1)
            self.showHpText(-delta, scale=5)
        self.bossDamage = bossDamage
        self.updateHealthBar()
        self.bossHealthBar.update(self.bossMaxDamage - bossDamage, self.bossMaxDamage)

    def setCraneSpawn(self, want, spawn, toonId):
        print(want)
        print(spawn)
        print(toonId)
        self.wantCustomCraneSpawns = want
        self.customSpawnPositions[toonId] = spawn

    def setRewardId(self, rewardId):
        self.rewardId = rewardId

    def d_applyReward(self):
        self.sendUpdate('applyReward', [])

    def stunAllGoons(self):
        for goon in self.goons:
            if goon.state == 'Walk' or goon.state == 'Battle':
                goon.demand('Stunned')
                goon.sendUpdate('requestStunned', [0])

    def destroyAllGoons(self):
        for goon in self.goons:
            if goon.state != 'Off' and not goon.isDead:
                goon.b_destroyGoon()

    def deactivateCranes(self):
        for crane in self.cranes.values():
            crane.demand('Free')

    def hideBattleThreeObjects(self):
        for goon in self.goons:
            goon.demand('Off')

        for safe in self.safes.values():
            safe.demand('Off')

        for crane in self.cranes.values():
            crane.demand('Off')

    def __doPhysics(self, task):
        dt = globalClock.getDt()
        self.physicsMgr.doPhysics(dt)
        return Task.cont

    def __hideToons(self):
        for toonId in self.involvedToons:
            toon = self.cr.doId2do.get(toonId)
            if toon:
                toon.hide()

    def __showToons(self):
        for toonId in self.involvedToons:
            toon = self.cr.doId2do.get(toonId)
            if toon:
                toon.show()

    def __arrangeToonsAroundResistanceToon(self):
        radius = 7
        numToons = len(self.involvedToons)
        center = (numToons - 1) / 2.0
        for i in xrange(numToons):
            toon = self.cr.doId2do.get(self.involvedToons[i])
            if toon:
                angle = 90 - 15 * (i - center)
                radians = angle * math.pi / 180.0
                x = math.cos(radians) * radius
                y = math.sin(radians) * radius
                toon.setPos(self.resistanceToon, x, y, 0)
                toon.headsUp(self.resistanceToon)
                toon.loop('neutral')
                toon.show()

    def __talkAboutPromotion(self, speech):
        if self.prevCogSuitLevel < ToontownGlobals.MaxCogSuitLevel:
            newCogSuitLevel = localAvatar.getCogLevels()[CogDisguiseGlobals.dept2deptIndex(self.style.dept)]
            if newCogSuitLevel == ToontownGlobals.MaxCogSuitLevel:
                speech += TTLocalizer.ResistanceToonLastPromotion % (ToontownGlobals.MaxCogSuitLevel + 1)
            if newCogSuitLevel in ToontownGlobals.CogSuitHPLevels:
                speech += TTLocalizer.ResistanceToonHPBoost
        else:
            speech += TTLocalizer.ResistanceToonMaxed % (ToontownGlobals.MaxCogSuitLevel + 1)
        return speech

    def enterOff(self):
        DistributedBossCog.DistributedBossCog.enterOff(self)
        if self.resistanceToon:
            self.resistanceToon.clearChat()

    def enterWaitForToons(self):
        DistributedBossCog.DistributedBossCog.enterWaitForToons(self)
        self.detachNode()
        self.geom.hide()
        self.resistanceToon.removeActive()

    def exitWaitForToons(self):
        DistributedBossCog.DistributedBossCog.exitWaitForToons(self)
        self.geom.show()
        self.resistanceToon.addActive()

    def enterElevator(self):
        DistributedBossCog.DistributedBossCog.enterElevator(self)
        self.detachNode()
        self.resistanceToon.removeActive()
        self.endVault.stash()
        self.midVault.unstash()
        self.__showResistanceToon(True)

    def exitElevator(self):
        DistributedBossCog.DistributedBossCog.exitElevator(self)
        self.resistanceToon.addActive()

    def enterIntroduction(self):
        self.detachNode()
        self.stopAnimate()
        self.endVault.unstash()
        self.evWalls.stash()
        self.midVault.unstash()
        self.__showResistanceToon(True)
        base.playMusic(self.stingMusic, looping=1, volume=0.9)
        DistributedBossCog.DistributedBossCog.enterIntroduction(self)

    def exitIntroduction(self):
        DistributedBossCog.DistributedBossCog.exitIntroduction(self)
        self.stingMusic.stop()

    def enterBattleOne(self):
        DistributedBossCog.DistributedBossCog.enterBattleOne(self)
        self.reparentTo(render)
        self.setPosHpr(*ToontownGlobals.CashbotBossBattleOnePosHpr)
        self.show()
        self.pelvis.setHpr(self.pelvisReversedHpr)
        self.doAnimate()
        self.endVault.stash()
        self.midVault.unstash()
        self.__hideResistanceToon()

    def exitBattleOne(self):
        DistributedBossCog.DistributedBossCog.exitBattleOne(self)
		
    def enterRollToBattleTwo(self):
        self.releaseToons()
        self.reparentTo(render)
        self.endVault.unstash()
        self.midVault.unstash()
        self.door3.stash()
        self.door2.stash()
        self.stickBossToFloor()
        intervalName = 'RollToBattleTwo'
        seq = Sequence(self.__makeRollToBattleTwoMovie(), Func(self.__onToPrepareBattleTwo), name=intervalName)
        seq.start()
        self.storeInterval(seq, intervalName)
        base.playMusic(self.betweenBattleMusic, looping=1, volume=0.9)
        self.__showResistanceToon(False)

    def __onToPrepareBattleTwo(self):
        self.door2.stash()
        self.door3.stash()
        self.unstickBoss()
        self.setPosHpr(*ToontownGlobals.CashbotBossBattleTwoPosHpr)
        self.doneBarrier('RollToBattleTwo')

    def exitRollToBattleTwo(self):
        self.unstickBoss()
        intervalName = 'RollToBattleTwo'
        self.clearInterval(intervalName)
        self.betweenBattleMusic.stop()



    def enterPrepareBattleTwo(self):
        self.door2.stash()
        self.door3.stash()
        self.controlToons()
        intervalName = 'PrepareBattleTwoMovie'
        delayDeletes = []
        seq = Sequence(self.makePrepareBattleTwoMovie(delayDeletes), Func(self.__beginBattleTwo), name=intervalName)
        seq.delayDeletes = delayDeletes
        seq.start()
        self.__showToons()
        self.storeInterval(seq, intervalName)
        self.endVault.unstash()
        self.evWalls.stash()
        self.midVault.unstash()
        self.door2.stash()
        base.playMusic(self.cutsceneMusic, looping=1, volume=0.9)
        taskMgr.add(self.__doPhysics, self.uniqueName('physics'), priority=25)
		
    def exitPrepareBattleTwo(self):
        intervalName = 'PrepareBattleTwoMovie'
        self.clearInterval(intervalName)
        ElevatorUtils.closeDoors(self.leftDoor, self.rightDoor, ElevatorConstants.ELEVATOR_CFO)
        self.cutsceneMusic.stop()

    def enterBattleTwo(self):
        self.cleanupIntervals()
        self.door2.stash()
        self.door3.stash()
        self.reparentTo(render)
        self.setPosHpr(*ToontownGlobals.CashbotBossBattleTwoPosHpr)
        self.show()
        self.toonsToBattlePosition(self.toonsA, self.battleANode)
        self.toonsToBattlePosition(self.toonsB, self.battleBNode)
        base.playMusic(self.battleTwoMusic, looping=1, volume=0.9)
        return

    def exitBattleTwo(self):
        intervalName = self.uniqueName('cageDrop')
        self.clearInterval(intervalName)
        self.cleanupBattles()
        self.battleTwoMusic.stop()
        localAvatar.inventory.setBattleCreditMultiplier(1)
        
    def __beginBattleTwo(self):
        intervalName = 'PrepareBattleTwoMovie'
        self.clearInterval(intervalName)
        self.doneBarrier('PrepareBattleTwo')

    def enterPrepareBattleThree(self):
        self.controlToons()
        NametagGlobals.setMasterArrowsOn(0)
        intervalName = 'PrepareBattleThreeMovie'
        delayDeletes = []
        self.movieCrane = self.cranes[0]
        self.movieSafe = self.safes[1]
        self.movieCrane.request('Movie')
        seq = Sequence(self.makePrepareBattleThreeMovie(delayDeletes, self.movieCrane, self.movieSafe), Func(self.__beginBattleThree), name=intervalName)
        seq.delayDeletes = delayDeletes
        seq.start()
        self.storeInterval(seq, intervalName)
        self.endVault.unstash()
        self.evWalls.stash()
        self.midVault.unstash()
        self.__showResistanceToon(False)
        taskMgr.add(self.__doPhysics, self.uniqueName('physics'), priority=25)
        base.playMusic(self.intermissionMusic, looping=1, volume=0.9)

    def __beginBattleThree(self):
        intervalName = 'PrepareBattleThreeMovie'
        self.clearInterval(intervalName)
        self.doneBarrier('PrepareBattleThree')

    def exitPrepareBattleThree(self):
        intervalName = 'PrepareBattleThreeMovie'
        self.clearInterval(intervalName)
        self.unstickToons()
        self.releaseToons()
        if self.newState == 'BattleThree':
            self.movieCrane.request('Free')
            self.movieSafe.request('Initial')
        NametagGlobals.setMasterArrowsOn(1)
        ElevatorUtils.closeDoors(self.leftDoor, self.rightDoor, ElevatorConstants.ELEVATOR_CFO)
        taskMgr.remove(self.uniqueName('physics'))
        self.cutsceneMusic.stop()

    def enterBattleThree(self):
        DistributedBossCog.DistributedBossCog.enterBattleThree(self)
        self.clearChat()
        self.resistanceToon.clearChat()
        self.reparentTo(render)
        self.setPosHpr(*ToontownGlobals.CashbotBossBattleThreePosHpr)
        self.happy = 1
        self.raised = 1
        self.forward = 1
        self.doAnimate()
        self.endVault.unstash()
        self.evWalls.unstash()
        self.midVault.stash()
        self.__hideResistanceToon()
        localAvatar.setCameraFov(ToontownGlobals.BossBattleCameraFov)
        self.generateHealthBar()
        self.updateHealthBar()
        base.playMusic(self.battleThreeMusic, looping=1, volume=0.9)
        taskMgr.add(self.__doPhysics, self.uniqueName('physics'), priority=25)
        self.bossHealthBar.initialize(self.bossMaxDamage - self.bossDamage, self.bossMaxDamage)

    def exitBattleThree(self):
        DistributedBossCog.DistributedBossCog.exitBattleThree(self)
        bossDoneEventName = self.uniqueName('DestroyedBoss')
        self.ignore(bossDoneEventName)
        self.stopAnimate()
        self.cleanupAttacks()
        self.setDizzy(0)
        self.bossHealthBar.deinitialize()
        localAvatar.setCameraFov(ToontownGlobals.CogHQCameraFov)
        if self.newState != 'Victory':
            self.battleThreeMusic.stop()
        taskMgr.remove(self.uniqueName('physics'))

    def enterVictory(self):
        self.cleanupIntervals()
        self.reparentTo(render)
        self.setPosHpr(*ToontownGlobals.CashbotBossBattleThreePosHpr)
        self.stopAnimate()
        self.endVault.unstash()
        self.evWalls.unstash()
        self.midVault.unstash()
        self.__hideResistanceToon()
        self.__hideToons()
        self.clearChat()
        self.resistanceToon.clearChat()
        self.deactivateCranes()
        if self.cranes:
            self.cranes[1].demand('Off')
        self.releaseToons(finalBattle=1)
        if self.hasLocalToon():
            self.toMovieMode()
        intervalName = 'VictoryMovie'
        seq = Sequence(self.makeBossFleeMovie(), Func(self.__continueVictory), name=intervalName)
        seq.start()
        self.storeInterval(seq, intervalName)
        self.bossHealthBar.deinitialize()
        if self.oldState != 'BattleThree':
            base.playMusic(self.victoryMusic, looping=1, volume=0.9)

    def __continueVictory(self):
        self.doneBarrier('Victory')

    def exitVictory(self):
        self.cleanupIntervals()
        if self.newState != 'Reward':
            if self.hasLocalToon():
                self.toWalkMode()
        self.__showToons()
        self.door3.setPos(0, 0, 0)
        if self.newState != 'Reward':
            self.battleThreeMusic.stop()

    def enterReward(self):
        self.cleanupIntervals()
        self.clearChat()
        self.resistanceToon.clearChat()
        self.stash()
        self.stopAnimate()
        self.controlToons()
        panelName = self.uniqueName('reward')
        self.rewardPanel = RewardPanel.RewardPanel(panelName)
        victory, camVictory, skipper = MovieToonVictory.doToonVictory(1, self.involvedToons, self.toonRewardIds, self.toonRewardDicts, self.deathList, self.rewardPanel, allowGroupShot=0, uberList=self.uberList, noSkip=True)
        ival = Sequence(Parallel(victory, camVictory), Func(self.__doneReward))
        intervalName = 'RewardMovie'
        delayDeletes = []
        for toonId in self.involvedToons:
            toon = self.cr.doId2do.get(toonId)
            if toon:
                delayDeletes.append(DelayDelete.DelayDelete(toon, 'CashbotBoss.enterReward'))

        ival.delayDeletes = delayDeletes
        ival.start()
        self.storeInterval(ival, intervalName)
        if self.oldState != 'Victory':
            base.playMusic(self.victoryMusic, looping=1, volume=0.9)

    def __doneReward(self):
        self.doneBarrier('Reward')
        self.toWalkMode()

    def exitReward(self):
        intervalName = 'RewardMovie'
        self.clearInterval(intervalName)
        if self.newState != 'Epilogue':
            self.releaseToons()
        self.unstash()
        self.rewardPanel.destroy()
        del self.rewardPanel
        self.battleThreeMusic.stop()

    def enterEpilogue(self):
        self.cleanupIntervals()
        self.clearChat()
        self.resistanceToon.clearChat()
        self.stash()
        self.stopAnimate()
        self.controlToons()
        self.__showResistanceToon(False)
        self.resistanceToon.setPosHpr(*ToontownGlobals.CashbotBossBattleThreePosHpr)
        self.resistanceToon.loop('neutral')
        self.__arrangeToonsAroundResistanceToon()
        camera.reparentTo(render)
        camera.setPos(self.resistanceToon, -9, 12, 6)
        camera.lookAt(self.resistanceToon, 0, 0, 3)
        intervalName = 'EpilogueMovie'
        text = ResistanceChat.getChatText(self.rewardId)
        menuIndex, itemIndex = ResistanceChat.decodeId(self.rewardId)
        value = ResistanceChat.getItemValue(self.rewardId)
        if menuIndex == ResistanceChat.RESISTANCE_TOONUP:
            if value == -1:
                instructions = TTLocalizer.ResistanceToonToonupAllInstructions
            else:
                instructions = TTLocalizer.ResistanceToonToonupInstructions % value
        elif menuIndex == ResistanceChat.RESISTANCE_MONEY:
            if value == -1:
                instructions = TTLocalizer.ResistanceToonMoneyAllInstructions
            else:
                instructions = TTLocalizer.ResistanceToonMoneyInstructions % value
        elif menuIndex == ResistanceChat.RESISTANCE_RESTOCK:
            if value == -1:
                instructions = TTLocalizer.ResistanceToonRestockAllInstructions
            else:
                trackName = TTLocalizer.BattleGlobalTracks[value]
                instructions = TTLocalizer.ResistanceToonRestockInstructions % trackName
        speech = TTLocalizer.ResistanceToonCongratulations % (text, instructions)
        speech = self.__talkAboutPromotion(speech)
        self.resistanceToon.setLocalPageChat(speech, 0)
        self.accept('nextChatPage', self.__epilogueChatNext)
        self.accept('doneChatPage', self.__epilogueChatDone)
        base.playMusic(self.epilogueMusic, looping=1, volume=0.9)

    def __epilogueChatNext(self, pageNumber, elapsed):
        if pageNumber == 1:
            toon = self.resistanceToon
            playRate = 0.75
            track = Sequence(ActorInterval(toon, 'victory', playRate=playRate, startFrame=0, endFrame=9), ActorInterval(toon, 'victory', playRate=playRate, startFrame=9, endFrame=0), Func(self.resistanceToon.loop, 'neutral'))
            intervalName = 'EpilogueMovieToonAnim'
            self.storeInterval(track, intervalName)
            track.start()
        elif pageNumber == 3:
            self.d_applyReward()
            ResistanceChat.doEffect(self.rewardId, self.resistanceToon, self.involvedToons)

    def __epilogueChatDone(self, elapsed):
        self.resistanceToon.setChatAbsolute(TTLocalizer.CagedToonGoodbye, CFSpeech)
        self.ignore('nextChatPage')
        self.ignore('doneChatPage')
        intervalName = 'EpilogueMovieToonAnim'
        self.clearInterval(intervalName)
        track = Parallel(Sequence(ActorInterval(self.resistanceToon, 'wave'), Func(self.resistanceToon.loop, 'neutral')), Sequence(Wait(0.5), Func(self.localToonToSafeZone)))
        self.storeInterval(track, intervalName)
        track.start()

    def exitEpilogue(self):
        self.clearInterval('EpilogueMovieToonAnim')
        self.unstash()
        self.epilogueMusic.stop()

    def enterFrolic(self):
        DistributedBossCog.DistributedBossCog.enterFrolic(self)
        self.setPosHpr(*ToontownGlobals.CashbotBossBattleOnePosHpr)
        self.releaseToons()
        if self.hasLocalToon():
            self.toWalkMode()
        self.door3.setZ(25)
        self.door2.setZ(25)
        self.endVault.unstash()
        self.evWalls.stash()
        self.midVault.unstash()
        self.__hideResistanceToon()

    def exitFrolic(self):
        self.door3.setZ(0)
        self.door2.setZ(0)
