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
from toontown.login import YourAnim
class AnimSelector2():

    def __init__(self, leaveFunction):
        self.enterMusic = base.loader.loadMusic('phase_4/audio/bgm/m_match_bg2.ogg')
        
    def create(self):
        gui = loader.loadModel('phase_3/models/gui/quit_button')
        self.YB = gui.find('**/QuitBtn_DN')
        self.YB = self.YB
        self.Hover = gui.find('**/QuitBtn_RLVR')
        self.Hover = self.Hover
        
        self.AnimButton = DirectButton(image=(self.YB, self.Hover), relief=None, text="Trailer", text_font=ToontownGlobals.getToonFont(), text_fg=(0.1, 0.1, 0.1, 1), text_pos=TTLocalizer.AnimationsButtonPos, text_scale=0.05, image_scale=1, image1_scale=0.9, image2_scale=0.9, scale=0.9, pos=(0, 0, 0.5), command=self.loadAnimationOne)
        self.AnimButton = self.AnimButton
        
        self.toontownsky = loader.loadModel('phase_3.5/models/props/TT_sky.bam')
        self.toontownsky.reparentTo(render)
        self.toontownsky = self.toontownsky
        
        self.tagArena = loader.loadModel('phase_4/models/minigames/tag_arena.bam')
        self.tagArena.reparentTo(render)
        self.tagArena = self.tagArena
        self.SpinTask = LerpHprInterval(self.tagArena, duration=50, hpr=Point3(360, 0, 0))
        self.SpinTask.loop()
        
        camera.setX(0)
        camera.setZ(20)
        camera.setP(-5)
        
        base.playMusic(self.enterMusic, looping=1, volume=1.0)
		
    def TheSandwitchAnimation(self):
		LoadInTrack = Sequence(Func(self.AnimButton.hide), Func(base.transitions.irisOut, 1.0), Wait(1.5), Func(self.loadSandwichAnim))
		LoadInTrack.start()
		
    def loadAnimationOne(self):
		self.tagArena.hide()
		self.toontownsky.hide()
		self.enterMusic.stop()
		self.SpinTask.finish()
		self.AnimButton.hide()
		YourAnim.YourAnim(self).create()
		
