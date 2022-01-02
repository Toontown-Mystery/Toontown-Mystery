from direct.task.Task import Task
from toontown.battle import BattleProps
from panda3d.core import Vec4
from toontown.toonbase import ToontownGlobals

HEALTH_COLORS = (Vec4(0, 0.7, 0.9, 1),
	 Vec4(0, 0.6, 0.65, 1),
	 Vec4(0.5, 1, 0.6, 1),
	 Vec4(0, 1, 0, 1),
     Vec4(0.0, 0.0, 1.0, 1),
	 Vec4(0.5, 0.0, 1.0, 1),
	 Vec4(0.7, 0.0, 0.9, 1),
     Vec4(0.95, 0.95, 1, 1),
     Vec4(1, 0, 0, 1),
	 Vec4(0, 0, 0, 1),
     Vec4(0, 0, 0, 1),
     ToontownGlobals.CogImmuneColor)
HEALTH_GLOW_COLORS = (Vec4(0, 0.7, 0.9, 0.5),
	 Vec4(0, 0.6, 0.65, 0.5),
	 Vec4(0.5, 1, 0.6, 0.5),
	 Vec4(0, 1, 0, 0.5),
     Vec4(0.25, 0.25, 1.0, 0.5),
	 Vec4(0.5, 0.0, 1.0, 0.5),
	 Vec4(0.7, 0.0, 0.9, 0.5),
     Vec4(0.95, 0.95, 1, 0.5),
     Vec4(1, 0, 0, 0.5),
	 Vec4(0, 0, 0, 0.5),
     Vec4(0, 0, 0, 0),
     ToontownGlobals.CogImmuneGlowColor)

class SuitHealthBar:

    def __init__(self):
        self.geom = None
        self.geomGlow = None
        self.healthCondition = 0

    def delete(self):
        if self.geom:
            self.geom.removeNode()
            self.geom = None
        self.geomGlow = None
        taskMgr.remove('blink-task-%s' % id(self))
        self.healthCondition = 0
    
    def generate(self):
        self.delete()
        model = loader.loadModel('phase_3.5/models/gui/matching_game_gui')
        button = model.find('**/minnieCircle')
        model.removeNode()

        button.setH(180.0)
        button.setColor(HEALTH_COLORS[0])
        self.geom = button

        glow = BattleProps.globalPropPool.getProp('glow')
        glow.reparentTo(self.geom)
        glow.setScale(0.28)
        glow.setPos(-0.005, 0.01, 0.015)
        glow.setColor(HEALTH_GLOW_COLORS[0])

        button.flattenLight()
        self.geomGlow = glow
        self.geom.hide()
        self.healthCondition = 0
    
    def getHealthCondition(self, health):
        if health > 0.95:
            return 0
        elif health > 0.9:
            return 1
        elif health > 0.8:
            return 2
        elif health > 0.7:
            return 3
        elif health > 0.6:
            return 4
        elif health > 0.5:
            return 5
        elif health > 0.3:
            return 6
        elif health > 0.15:
            return 7
        elif health > 0.10:
            return 8
        elif health > 0.05:
            return 9
        elif health > 0.0:
            return 10
        return 11

    def update(self, hp, forceUpdate = 0):
        if not self.geom:
            return
        condition = self.getHealthCondition(hp)

        if self.healthCondition != condition or forceUpdate:
            taskMgr.remove('blink-task-%s' % id(self))

            if condition in (10, 11):
                blinkTask = Task.loop(Task(self.__blinkRed), Task.pause(0.75 if condition == 10 else 0.25), Task(self.__blinkGray), Task.pause(0.1))
                taskMgr.add(blinkTask, 'blink-task-%s' % id(self))
            else:
                self.geom.setColor(HEALTH_COLORS[condition], 1)
                self.geomGlow.setColor(HEALTH_GLOW_COLORS[condition], 1)
    
            self.healthCondition = condition

    def __blink(self, color):
        if not self.geom:
            return

        self.geom.setColor(HEALTH_COLORS[color], 1)
        self.geomGlow.setColor(HEALTH_GLOW_COLORS[color], 1)
    
    def __blinkRed(self, task):
        self.__blink(9)
    
    def __blinkGray(self, task):
        self.__blink(10)