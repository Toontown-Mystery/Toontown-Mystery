import random

from direct.distributed import ClockDelta
from direct.task import Task
from toontown.coghq import LaserGameBase


class LaserGameAvoid(LaserGameBase.LaserGameBase):
    def __init__(self, funcSuccess, funcFail, funcSendGrid, funcSetGrid):
        LaserGameBase.LaserGameBase.__init__(self, funcSuccess, funcFail, funcSendGrid, funcSetGrid)
        self.setGridSize(15, 15)
        self.blankGrid()
        self.cycleName = simbase.air.trueUniqueName('AvoidGame')


    def delete(self):
        LaserGameBase.LaserGameBase.delete(self)
        self.endTask()


    def win(self):
        if not self.finshed:
            self.blankGrid()
            self.funcSendGrid()
            self.endTask()

        LaserGameBase.LaserGameBase.win(self)


    def lose(self):
        self.endTask()
        self.blankGrid()
        self.funcSendGrid()
        LaserGameBase.LaserGameBase.lose(self)


    def endTask(self):
        taskMgr.remove(self.cycleName)


    def startGrid(self):
        LaserGameBase.LaserGameBase.startGrid(self)
        for column in xrange(0, self.gridNumX):
            for row in xrange(0, self.gridNumY):
                tile = random.choice([
                    0,
                    14,
                    12])
                self.gridData[column][row] = tile


        taskMgr.doMethodLater(1.0, self._LaserGameAvoid__cycle, self.cycleName)


    def _LaserGameAvoid__cycle(self, taskMgrFooler = 0):
        if not hasattr(self, 'gridNumX'):
            return Task.done

        for column in xrange(0, self.gridNumX):
            for row in xrange(0, self.gridNumY):
                if self.gridData[column][row] == 0:
                    tile = random.choice([
                        0,
                        14])
                    self.gridData[column][row] = tile
                    continue
                if self.gridData[column][row] == 14:
                    tile = 12
                    self.gridData[column][row] = tile
                    continue
                if self.gridData[column][row] == 12:
                    tile = 0
                    self.gridData[column][row] = tile
                    continue


        if not self.finshed:
            taskMgr.doMethodLater(5.0, self._LaserGameAvoid__cycle, self.cycleName)
            self.funcSendGrid()

        return Task.done
