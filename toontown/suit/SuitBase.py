from panda3d.toontown import *
from direct.distributed.ClockDelta import *
import math
import random
from direct.directnotify import DirectNotifyGlobal
from toontown.battle import SuitBattleGlobals
import SuitTimings
import SuitDNA
from toontown.toonbase import TTLocalizer
TIME_BUFFER_PER_WPT = 0.25
TIME_DIVISOR = 100
DISTRIBUTE_TASK_CREATION = 0

class SuitBase:
    notify = DirectNotifyGlobal.directNotify.newCategory('SuitBase')

    def __init__(self):
        self.dna = None
        self.level = 0
        self.maxHP = 10
        self.currHP = 10
        self.isSkelecog = 0
        self.isBossEncounter = 0
        self.isFacilityBoss = 0
        self.isFacilityAssistant = 0
        self.isImmune = 0
        return

    def delete(self):
        pass

    def getCurrHp(self):
        if hasattr(self, 'currHP') and self.currHP:
            return self.currHP
        else:
            self.notify.error('currHP is None')
            return 'unknown'

    def getMaxHp(self):
        if hasattr(self, 'maxHP') and self.maxHP:
            return self.maxHP
        else:
            self.notify.error('maxHP is None')
            return 'unknown'

    def getStyleName(self):
        if hasattr(self, 'dna') and self.dna:
            return self.dna.name
        else:
            self.notify.error('called getStyleName() before dna was set!')
            return 'unknown'

    def getStyleDept(self):
        if hasattr(self, 'dna') and self.dna:
            return SuitDNA.getDeptFullname(self.dna.dept)
        else:
            self.notify.error('called getStyleDept() before dna was set!')
            return 'unknown'

    def getLevel(self):
        return self.level

    def setLevel(self, level):
        self.level = level
        self.nameWLevel = TTLocalizer.SuitBaseNameWithLevel % {'name': self.name,
         'dept': self.getStyleDept(),
         'level': self.getActualLevel(),
         'bec': self.getBossEncounterTitle(),
         'fb': self.getFacilityBossTitle(),
         'fa': self.getFacilityAssistantTitle()}
        self.setDisplayName(self.nameWLevel)
        attributes = SuitBattleGlobals.SuitAttributes[self.dna.name]
        self.maxHP = attributes['hp'][self.level]
        self.currHP = self.maxHP

    def getSkelecog(self):
        return self.isSkelecog

    def getBossEncounter(self):
        return self.isBossEncounter

    def getBossEncounterTitle(self):
        return TTLocalizer.SuitBossEncounterTitle if self.getBossEncounter() else ''

    def setBossEncounter(self, flag):
        wasBossEncounter = self.getBossEncounter()
        if wasBossEncounter:
            return
        self.isBossEncounter = flag
        self.nameWLevel()

    def getFacilityBoss(self):
        return self.isFacilityBoss

    def getFacilityBossTitle(self):
        return TTLocalizer.SuitFacilityBossTitle if self.getFacilityBoss() else ''

    def setFacilityBoss(self, flag):
        wasFacilityBoss = self.getFacilityBoss()
        if wasFacilityBoss:
            return
        self.isFacilityBoss = flag
        self.nameWLevel()

    def getFacilityAssistant(self):
        return self.isFacilityAssistant

    def getFacilityAssistantTitle(self):
        return TTLocalizer.SuitFacilityAssistantTitle if self.getFacilityAssistant() else ''

    def setFacilityAssistant(self, flag):
        wasFacilityAssistant = self.getFacilityAssistant()
        if wasFacilityAssistant:
            return
        self.isFacilityAssistant = flag
        self.nameWLevel()

    def setSkelecog(self, flag):
        self.isSkelecog = flag

    def setImmuneStatus(self, num):
        if num == None:
            num = 0
        else:
            self.isImmune = num

    def getImmuneStatus(self):
        return self.isImmune

    def getActualLevel(self):
        if hasattr(self, 'dna'):
            return SuitBattleGlobals.getActualFromRelativeLevel(self.getStyleName(), self.level) + 1
        else:
            self.notify.warning('called getActualLevel with no DNA, returning 1 for level')
            return 1

    def setPath(self, path):
        self.path = path
        self.pathLength = self.path.getNumPoints()

    def getPath(self):
        return self.path

    def printPath(self):
        print '%d points in path' % self.pathLength
        for currPathPt in xrange(self.pathLength):
            indexVal = self.path.getPointIndex(currPathPt)
            print '\t', self.sp.dnaStore.getSuitPointWithIndex(indexVal)

    def makeLegList(self):
        self.legList = SuitLegList(self.path, self.sp.dnaStore, self.sp.suitWalkSpeed, SuitTimings.fromSky, SuitTimings.toSky, SuitTimings.fromSuitBuilding, SuitTimings.toSuitBuilding, SuitTimings.toToonBuilding)
