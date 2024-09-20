from direct.directnotify import DirectNotifyGlobal
from direct.showbase.PythonUtil import invertDictLossless
from toontown.coghq import MintRoomSpecs
from toontown.toonbase import ToontownGlobals
from direct.showbase.PythonUtil import normalDistrib, lerp
import random

def printAllCashbotInfo():
    print 'roomId: roomName'
    for roomId, roomName in MintRoomSpecs.CashbotMintRoomId2RoomName.items():
        print '%s: %s' % (roomId, roomName)

    print '\nroomId: numBattles'
    for roomId, numBattles in MintRoomSpecs.roomId2numBattles.items():
        print '%s: %s' % (roomId, numBattles)

    print '\nmintId floor roomIds'
    printMintRoomIds()
    print '\nmintId floor numRooms'
    printNumRooms()
    print '\nmintId floor numForcedBattles'
    printNumBattles()


def iterateCashbotMints(func):
    from toontown.toonbase import ToontownGlobals
    for mintId in [ToontownGlobals.CashbotMintIntA, ToontownGlobals.CashbotMintIntB, ToontownGlobals.CashbotMintIntC]:
        for floorNum in xrange(ToontownGlobals.MintNumFloors[mintId]):
            func(MintLayout(mintId, floorNum))


def printMintInfo():

    def func(ml):
        print ml

    iterateCashbotMints(func)


def printMintRoomIds():

    def func(ml):
        print ml.getMintId(), ml.getFloorNum(), ml.getRoomIds()

    iterateCashbotMints(func)


def printMintRoomNames():

    def func(ml):
        print ml.getMintId(), ml.getFloorNum(), ml.getRoomNames()

    iterateCashbotMints(func)


def printNumRooms():

    def func(ml):
        print ml.getMintId(), ml.getFloorNum(), ml.getNumRooms()

    iterateCashbotMints(func)


def printNumBattles():

    def func(ml):
        print ml.getMintId(), ml.getFloorNum(), ml.getNumBattles()

    iterateCashbotMints(func)


BakedFloorLayouts = {12500: {0: (0,
             4,
             9,
             6,
             11,
             14,
             1,
             17),
         1: (0,
             4,
             9,
             6,
             11,
             14,
             1,
             22),
         2: (0,
             4,
             9,
             6,
             11,
             14,
             1,
             19),
         3: (0,
             4,
             9,
             6,
             11,
             14,
             1,
             24),
         4: (0,
             4,
             9,
             6,
             11,
             14,
             1,
             21),
         5: (0,
             4,
             9,
             6,
             11,
             14,
             1,
             18),
         6: (0,
             4,
             9,
             6,
             11,
             14,
             1,
             23),
         7: (0,
             4,
             9,
             6,
             11,
             14,
             1,
             20),
         8: (0,
             4,
             9,
             6,
             11,
             14,
             1,
             25),
         9: (0,
             4,
             9,
             6,
             11,
             14,
             1,
             22),
         10: (0,
              4,
              9,
              6,
              11,
              14,
              1,
              19),
         11: (0,
              4,
              9,
              6,
              11,
              14,
              1,
              24),
         12: (0,
              4,
              9,
              6,
              11,
              14,
              1,
              21),
         13: (0,
              4,
              9,
              6,
              11,
              14,
              1,
              17),
         14: (0,
              4,
              9,
              6,
              11,
              14,
              1,
              23),
         15: (0,
              4,
              9,
              6,
              11,
              14,
              1,
              20),
         16: (0,
              4,
              9,
              6,
              11,
              14,
              1,
              25),
         17: (0,
              4,
              9,
              6,
              11,
              14,
              1,
              22),
         18: (0,
              4,
              9,
              6,
              11,
              14,
              1,
              18),
         19: (0,
              4,
              9,
              6,
              11,
              14,
              1,
              24)},
 12600: {0: (0,
             4,
             9,
             2,
             15,
             1,
             11,
             5,
             25),
         1: (0,
             2,
             4,
             9,
             15,
             1,
             11,
             5,
             25),
         2: (0,
             2,
             4,
             9,
             15,
             1,
             11,
             5,
             25),
         3: (0,
             2,
             4,
             9,
             15,
             1,
             11,
             5,
             25),
         4: (0,
             2,
             4,
             9,
             15,
             1,
             11,
             5,
             25),
         5: (0,
             2,
             4,
             9,
             15,
             1,
             11,
             5,
             25),
         6: (0,
             2,
             4,
             9,
             15,
             1,
             11,
             5,
             25),
         7: (0,
             2,
             4,
             9,
             15,
             1,
             11,
             5,
             25),
         8: (0,
             2,
             4,
             9,
             15,
             1,
             11,
             5,
             25),
         9: (0,
             2,
             4,
             9,
             15,
             1,
             11,
             5,
             25),
         10: (0,
              2,
              4,
              9,
              15,
              1,
              11,
              5,
              25),
         11: (0,
              2,
              4,
              9,
              15,
              1,
              11,
              5,
              25),
         12: (0,
              2,
              4,
              9,
              15,
              1,
              11,
              5,
              25),
         13: (0,
              2,
              4,
              9,
              15,
              1,
              11,
              5,
              25),
         14: (0,
              2,
              4,
              9,
              15,
              1,
              11,
              5,
              25),
         15: (0,
              2,
              4,
              9,
              15,
              1,
              11,
              5,
              25),
         16: (0,
              2,
              4,
              9,
              15,
              1,
              11,
              5,
              25),
         17: (0,
              2,
              4,
              9,
              15,
              1,
              11,
              5,
              25),
         18: (0,
              2,
              4,
              9,
              15,
              1,
              11,
              5,
              25),
         19: (0,
              2,
              4,
              9,
              15,
              1,
              11,
              5,
              25)},
 12700: {0: (0,
             6,
             2,
             15,
             12,
             4,
             9,
             1,
             11,
             5,
             23),
         1: (0,
             6,
             2,
             15,
             12,
             4,
             9,
             1,
             11,
             5,
             23),
         2: (0,
             6,
             2,
             15,
             12,
             4,
             9,
             1,
             11,
             5,
             23),
         3: (0,
             6,
             2,
             15,
             12,
             4,
             9,
             1,
             11,
             5,
             23),
         4: (0,
             6,
             2,
             15,
             12,
             4,
             9,
             1,
             11,
             5,
             23),
         5: (0,
             6,
             2,
             15,
             12,
             4,
             9,
             1,
             11,
             5,
             23),
         6: (0,
             6,
             2,
             15,
             12,
             4,
             9,
             1,
             11,
             5,
             23),
         7: (0,
             6,
             2,
             15,
             12,
             4,
             9,
             1,
             11,
             5,
             23),
         8: (0,
             6,
             2,
             15,
             12,
             4,
             9,
             1,
             11,
             5,
             23),
         9: (0,
             6,
             2,
             15,
             12,
             4,
             9,
             1,
             11,
             5,
             23),
         10: (0,
              6,
              2,
              15,
              12,
              4,
              9,
              1,
              11,
              5,
              23),
         11: (0,
              6,
              2,
              15,
              12,
              4,
              9,
              1,
              11,
              5,
              23),
         12: (0,
              6,
              2,
              15,
              12,
              4,
              9,
              1,
              11,
              5,
              23),
         13: (0,
              6,
              2,
              15,
              12,
              4,
              9,
              1,
              11,
              5,
              23),
         14: (0,
              6,
              2,
              15,
              12,
              4,
              9,
              1,
              11,
              5,
              23),
         15: (0,
              6,
              2,
              15,
              12,
              4,
              9,
              1,
              11,
              5,
              23),
         16: (0,
              6,
              2,
              15,
              12,
              4,
              9,
              1,
              11,
              5,
              23),
         17: (0,
              6,
              4,
              9,
              2,
              15,
              12,
              1,
              11,
              5,
              23),
         18: (0,
              6,
              4,
              9,
              2,
              15,
              12,
              1,
              11,
              5,
              23),
         19: (0,
              6,
              4,
              9,
              2,
              15,
              12,
              1,
              11,
              5,
              23)}}

class MintLayout:
    notify = DirectNotifyGlobal.directNotify.newCategory('MintLayout')

    def __init__(self, mintId, floorNum):
        self.mintId = mintId
        self.floorNum = floorNum
        self.roomIds = []
        self.hallways = []
        self.numRooms = 1 + ToontownGlobals.MintNumRooms[self.mintId][self.floorNum]
        self.numHallways = self.numRooms - 1
        if self.mintId in BakedFloorLayouts and self.floorNum in BakedFloorLayouts[self.mintId]:
            self.roomIds = list(BakedFloorLayouts[self.mintId][self.floorNum])
        else:
            self.roomIds = self._genFloorLayout()
        hallwayRng = self.getRng()
        connectorRoomNames = MintRoomSpecs.CashbotMintConnectorRooms
        for i in xrange(self.numHallways):
            self.hallways.append(hallwayRng.choice(connectorRoomNames))

    def _genFloorLayout(self):
        rng = self.getRng()
        startingRoomIDs = MintRoomSpecs.CashbotMintEntranceIDs
        middleRoomIDs = MintRoomSpecs.CashbotMintMiddleRoomIDs
        finalRoomIDs = MintRoomSpecs.CashbotMintFinalRoomIDs

        numBattlesLeft = ToontownGlobals.MintNumBattles[self.mintId]

        finalRoomId = rng.choice(finalRoomIDs)
        numBattlesLeft -= MintRoomSpecs.getNumBattles(finalRoomId)

        middleRoomIds = []
        middleRoomsLeft = self.numRooms - 2

        numBattles2middleRoomIds = invertDictLossless(MintRoomSpecs.middleRoomId2numBattles)

        allBattleRooms = []
        for num, roomIds in numBattles2middleRoomIds.items():
            if num > 0:
                allBattleRooms.extend(roomIds)
        while 1:
            allBattleRoomIds = list(allBattleRooms)
            rng.shuffle(allBattleRoomIds)
            battleRoomIds = self._chooseBattleRooms(numBattlesLeft,
                                                    allBattleRoomIds)
            if battleRoomIds is not None:
                break

            MintLayout.notify.info('could not find a valid set of battle rooms, trying again')

        middleRoomIds.extend(battleRoomIds)
        middleRoomsLeft -= len(battleRoomIds)

        if middleRoomsLeft > 0:
            actionRoomIds = numBattles2middleRoomIds[0]
            for i in xrange(middleRoomsLeft):
                roomId = rng.choice(actionRoomIds)
                actionRoomIds.remove(roomId)
                middleRoomIds.append(roomId)

        roomIds = []

        roomIds.append(rng.choice(startingRoomIDs))

        rng.shuffle(middleRoomIds)
        roomIds.extend(middleRoomIds)

        roomIds.append(finalRoomId)

        return roomIds

    def getNumRooms(self):
        return len(self.roomIds)

    def getRoomId(self, n):
        return self.roomIds[n]

    def getRoomIds(self):
        return self.roomIds[:]

    def getRoomNames(self):
        names = []
        for roomId in self.roomIds:
            names.append(MintRoomSpecs.CashbotMintRoomId2RoomName[roomId])

        return names

    def getNumHallways(self):
        return len(self.hallways)

    def getHallwayModel(self, n):
        return self.hallways[n]

    def getNumBattles(self):
        numBattles = 0
        for roomId in self.getRoomIds():
            numBattles += MintRoomSpecs.roomId2numBattles[roomId]

        return numBattles

    def getMintId(self):
        return self.mintId

    def getFloorNum(self):
        return self.floorNum

    def getRng(self):
        return random.Random(self.mintId * self.floorNum)

    def _chooseBattleRooms(self, numBattlesLeft, allBattleRoomIds, baseIndex = 0, chosenBattleRooms = None):
        if chosenBattleRooms is None:
            chosenBattleRooms = []
        while baseIndex < len(allBattleRoomIds):
            nextRoomId = allBattleRoomIds[baseIndex]
            baseIndex += 1
            newNumBattlesLeft = numBattlesLeft - MintRoomSpecs.middleRoomId2numBattles[nextRoomId]
            if newNumBattlesLeft < 0:
                continue
            elif newNumBattlesLeft == 0:
                chosenBattleRooms.append(nextRoomId)
                return chosenBattleRooms
            chosenBattleRooms.append(nextRoomId)
            result = self._chooseBattleRooms(newNumBattlesLeft, allBattleRoomIds, baseIndex, chosenBattleRooms)
            if result is not None:
                return result
            else:
                del chosenBattleRooms[-1:]
        else:
            return

        return

    def __str__(self):
        return 'MintLayout: id=%s, floor=%s, numRooms=%s, numBattles=%s' % (self.mintId,
         self.floorNum,
         self.getNumRooms(),
         self.getNumBattles())

    def __repr__(self):
        return str(self)
