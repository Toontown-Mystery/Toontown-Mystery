from panda3d.core import *
from panda3d.direct import *
from toontown.toonbase import ToontownGlobals
from toontown.toonbase.ToontownBattleGlobals import *
from direct.directnotify import DirectNotifyGlobal
import string
from toontown.toon import LaffMeter
from toontown.battle import BattleBase
from toontown.battle import BattleProps
from direct.task.Task import Task
from direct.gui.DirectGui import *
from panda3d.core import *
from panda3d.direct import *
from toontown.toonbase import TTLocalizer

class TownBattleCogPanel(DirectFrame):
    notify = DirectNotifyGlobal.directNotify.newCategory('TownBattleCogPanel')
    healthColors = (
        Vec4(0, 1, 0, 1),
        Vec4(0.5, 1, 0, 1), 
        Vec4(0.75, 1, 0, 1),  
        Vec4(1, 1, 0, 1),
        Vec4(1, 0.866, 0, 1), 
        Vec4(1, 0.6, 0, 1),
        Vec4(1, 0.5, 0, 1),
        Vec4(1, 0.25, 0, 1.0),
        Vec4(1, 0, 0, 1),
        Vec4(0.3, 0.3, 0.3, 1)
    )
    healthGlowColors = (
        Vec4(0.25, 1, 0.25, 0.5),
        Vec4(0.5, 1, 0.25, .5),
        Vec4(0.75, 1, 0.25, .5),
        Vec4(1, 1, 0.25, 0.5),
        Vec4(1, 0.866, 0.25, .5),
        Vec4(1, 0.6, 0.25, .5),
        Vec4(1, 0.5, 0.25, 0.5),
        Vec4(1, 0.25, 0.25, 0.5),
        Vec4(1, 0.25, 0.25, 0.5),
        Vec4(0.3, 0.3, 0.3, 0)
    )

    def __init__(self, id):
        if base.settings.getBool('game', 'newGui', True) == True:
            gui = loader.loadModel('phase_3.5/models/gui/battle_gui_new')
        else:
            gui = loader.loadModel('phase_3.5/models/gui/battle_gui_old')
        
        DirectFrame.__init__(self, relief=None, image=gui.find('**/ToonBtl_Status_BG'), image_color=Vec4(0.7, 0.7, 0.7, 0.8))
        self.hpText = DirectLabel(parent=self, text='', pos=(-0.06, 0, -0.0325), text_scale=0.045)
        self.setScale(0.8)
        self.initialiseoptions(TownBattleCogPanel)
        self.hidden = False
        self.cog = None
        self.isLoaded = 0
        self.notify.info("Loading Cog Battle Panel!")
        self.healthText = DirectLabel(parent=self, text='', pos=(0, 0, -0.075), text_scale=0.05)
        healthGui = loader.loadModel('phase_3.5/models/gui/matching_game_gui')
        button = healthGui.find('**/minnieCircle')
        button.setScale(0.5)
        button.setH(180)
        button.setColor(Vec4(0, 1, 0, 1))
        self.accept('inventory-levels', self.__handleToggle)
        self.healthNode = self.attachNewNode('health')
        self.healthNode.setPos(-0.06, 0, 0.05)
        button.reparentTo(self.healthNode)
        glow = BattleProps.globalPropPool.getProp('glow')
        glow.reparentTo(button)
        glow.setScale(0.28)
        glow.setPos(-0.005, 0.01, 0.015)
        glow.setColor(Vec4(0.25, 1, 0.25, 0.5))
        self.button = button
        self.glow = glow
        self.head = None
        self.blinkTask = None
        self.hide()
        healthGui.removeNode()
        gui.removeNode()

    def setCogInformation(self, cog):
        self.cog = cog
        self.updateHealthBar()
        if self.head:
            self.head.removeNode()
        
        self.head = self.attachNewNode('head')
        for part in cog.headParts:
            copyPart = part.copyTo(self.head)
            copyPart.setDepthTest(1)
            copyPart.setDepthWrite(1)

        p1, p2 = Point3(), Point3()
        self.head.calcTightBounds(p1, p2)
        d = p2 - p1
        biggest = max(d[0], d[1], d[2])
        s = 0.1 / biggest
        self.head.setPosHprScale(0.1, 0, 0.01, 180, 0, 0, s, s, s)
        self.setLevelText(cog.getActualLevel(), cog.getSkeleRevives())

    def setLevelText(self, hp, revives = 0):
        if revives > 0:
            self.healthText['text'] = TTLocalizer.DisguisePageCogLevel % str(hp) + TTLocalizer.SkeleRevivePostFix
        else:
            self.healthText['text'] = TTLocalizer.DisguisePageCogLevel % str(hp)

    def updateHealthBar(self):
        condition = self.cog.healthCondition
        if condition == 9:
            self.blinkTask = Task.loop(Task(self.__blinkRed), Task.pause(0.75), Task.pause(0.1))
            taskMgr.add(self.blinkTask, self.uniqueName('blink-task'))
        elif condition == 10:
            taskMgr.remove(self.uniqueName('blink-task'))
            blinkTask = Task.loop(Task(self.__blinkRed), Task.pause(0.25), Task(self.__blinkGray), Task.pause(0.1))
            taskMgr.add(blinkTask, self.uniqueName('blink-task'))
        else:
            taskMgr.remove(self.uniqueName('blink-task'))
            if not self.button.isEmpty():
                self.button.setColor(self.healthColors[condition], 1)
            
            if not self.glow.isEmpty():
                self.glow.setColor(self.healthGlowColors[condition], 1)
        self.hp = self.cog.getHP()
        self.maxHp = self.cog.getMaxHP()
        self.hpText['text'] = str(self.hp) + '/' + str(self.maxHp)

    def show(self):
        if base.settings.getBool('game', 'show-cog-levels', True) == True:
            if self.cog:
                self.updateHealthBar()
            if hasattr(self.cog, 'isElite'):
                self['image_color'] = Vec4(0.4, 0.4, 0.4, 0.8)
            else:
                self['image_color'] = Vec4(0.7, 0.7, 0.7, 0.8)
            self.hidden = False
            self.healthNode.show()
            self.button.show()
            self.glow.show()
            DirectFrame.show(self)
        else:
            self.notify.debug('Tried to unhide Cog levels when settings have not been updated!')

    def __handleToggle(self):
        if self.cog:
            if self.hidden:
                self.show()
            else:
                self.hide()

    def __blinkRed(self, task):
        if not self.button.isEmpty():
            self.button.setColor(self.healthColors[8], 1)

        if not self.glow.isEmpty():
            self.glow.setColor(self.healthGlowColors[8], 1)
        
        return Task.done
		
    def __blinkGray(self, task):
        if not self.button.isEmpty():
            self.button.setColor(self.healthColors[9], 1)

        if not self.glow.isEmpty():
            self.glow.setColor(self.healthGlowColors[9], 1)
        
        return Task.done

    def hide(self):
        if self.blinkTask:
            taskMgr.remove(self.blinkTask)
            self.blinkTask = None
        
        self.hidden = True
        self.healthNode.hide()
        self.button.hide()
        self.glow.hide()
        DirectFrame.hide(self)
        
    def unload(self):
        if self.isLoaded == 0:
            return
        self.isLoaded = 0
        self.exit()
        del self.glow
        del self.cog
        del self.button
        del self.blinkTask
        del self.hpText
        DirectFrame.destroy(self)

    def cleanup(self):
        self.ignoreAll()
        if self.head:
            self.head.removeNode()
            del self.head
        
        if self.blinkTask:
            taskMgr.remove(self.blinkTask)
            self.blinkTask = None
        
        del self.blinkTask
        self.healthNode.removeNode()
        self.button.removeNode()
        self.glow.removeNode()
        DirectFrame.destroy(self)
