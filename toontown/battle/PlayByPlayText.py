from panda3d.core import *
from toontown.toonbase import TTLocalizer
from toontown.toonbase.ToontownBattleGlobals import *
from toontown.toonbase.ToontownGlobals import *
from SuitBattleGlobals import *
from direct.interval.IntervalGlobal import *
from direct.directnotify import DirectNotifyGlobal
import string
from direct.gui import OnscreenText
import BattleBase

class PlayByPlayText(OnscreenText.OnscreenText):
    notify = DirectNotifyGlobal.directNotify.newCategory('PlayByPlayText')

    def __init__(self):
        OnscreenText.OnscreenText.__init__(self, mayChange=1, pos=(0.0, 0.75), scale=TTLocalizer.PBPTonscreenText, fg=(0, 0, 1, 1), font=getSignFont(), wordwrap=13)

    def getShowInterval(self, text, duration):
        return Sequence(Func(self.hide), 
        LerpScaleInterval(self, duration=0, scale=(1, 1, 1)), 
        LerpColorScaleInterval(self, duration=0, colorScale=(0, 0, 1, 1)), 
        self.posInterval(0, (0, 0, 0)), Func(self.setText, text), 
        Func(self.show), 
        Parallel(self.scaleInterval(0.3, (1.8, 1.8, 1.8)), 
        self.posInterval(0.3, (0, 0, -0.595))), 
        Parallel(self.scaleInterval(0.3, (1.1, 1.1, 1.1)),
        self.posInterval(0.3, (0, 0, -0.035))), 
        Wait(1.5), 
        Parallel(self.scaleInterval(0.3, (0.0, 0.0, 0.0)), 
        self.posInterval(0.3, (0, 0, -0.5)), 
        LerpColorScaleInterval(self, duration=0.3, colorScale=(0, 0, 1, 0))), Func(self.hide))

    def getToonsDiedInterval(self, textList, duration):
        track = Sequence(Func(self.hide), Wait(duration * 0.3))
        waitGap = 0.6 / len(textList) * duration
        for text in textList:
            newList = [Func(self.setText, text),
             Func(self.show),
             Wait(waitGap),
             Func(self.hide)]
            track += newList

        track.append(Wait(duration * 0.1))
        return track
