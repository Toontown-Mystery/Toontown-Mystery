from direct.gui.DirectGui import OnscreenImage, DirectLabel, DirectButton, OnscreenText
from panda3d.core import *
from direct.interval.IntervalGlobal import *
from libotp import *
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from toontown.animations import AnimationFirstTestKaren, AnimationDoughnut, AnimationThing, AnimationRedSonic, AnimationClones
###################################
# Animation Selector              #
#                                 #   
#                                 #
# Author: Joey 900                #
# Creation Date: June 19th, 2021  #
###################################

class AnimationSelector():

    def __init__(self, leaveFunction):
        self.enterMusic = base.loader.loadMusic('phase_4/audio/bgm/m_match_bg2.ogg')
        
        Button = loader.loadModel('phase_3/models/gui/quit_button')
        self.YB = Button.find('**/QuitBtn_DN')
        self.Hover = Button.find('**/QuitBtn_RLVR')
        
    def create(self):
        #Karens property
        self.AnimButton = DirectButton(image=(self.YB, self.Hover), relief=None, text='Karens Property', text_font=ToontownGlobals.getToonFont(), text_fg=(0.1, 0.1, 0.1, 1), text_pos=TTLocalizer.AnimationsButtonPos, text_scale=0.05, image_scale=1, image1_scale=0.9, image2_scale=0.9, scale=0.9, pos=(0, 0, 0.8), command=self.TransitionOne)
        
        #Amandas Donuts
        self.AnimButton2 = DirectButton(image=(self.YB, self.Hover), relief=None, text='Amandas Donuts', text_font=ToontownGlobals.getToonFont(), text_fg=(0.1, 0.1, 0.1, 1), text_pos=TTLocalizer.AnimationsButtonPos, text_scale=0.05, image_scale=1, image1_scale=0.9, image2_scale=0.9, scale=0.9, pos=(0, 0, 0.5), command=self.TransitionTwo)
        
        #Clones
        self.AnimButton3 = DirectButton(image=(self.YB, self.Hover), relief=None, text='And His Pal Timinator!', text_font=ToontownGlobals.getToonFont(), text_fg=(0.1, 0.1, 0.1, 1), text_pos=TTLocalizer.AnimationsButtonPos, text_scale=0.05, image_scale=1, image1_scale=0.9, image2_scale=0.9, scale=0.9, pos=(0, 0, 0.2), command=self.TransitionThree)

        #Red sonic
        self.AnimButton3 = DirectButton(image=(self.YB, self.Hover), relief=None, text='Red sonic', text_font=ToontownGlobals.getToonFont(), text_fg=(0.1, 0.1, 0.1, 1), text_pos=TTLocalizer.AnimationsButtonPos, text_scale=0.05, image_scale=1, image1_scale=0.9, image2_scale=0.9, scale=0.9, pos=(0, 0, 0.9), command=self.TransitionFour)
          
        self.ExitButton = DirectButton(image=(self.YB, self.Hover), relief=None, text='Exit', text_font=ToontownGlobals.getToonFont(), text_fg=(0.1, 0.1, 0.1, 1), text_pos=TTLocalizer.AnimationsButtonPos, text_scale=0.05, image_scale=1, image1_scale=0.9, image2_scale=0.9, scale=0.9, pos=(-0.8, 0, -0.8), command=self.exit)
        
        #Setting
        self.sky = loader.loadModel('phase_3.5/models/props/TT_sky.bam')
        self.sky.reparentTo(render)
        self.tagArena = loader.loadModel('phase_4/models/minigames/tag_arena.bam')
        self.tagArena.reparentTo(render)

        self.SpinTask = LerpHprInterval(self.tagArena, duration=50, hpr=Point3(360, 0, 0))
        self.SpinTask.loop()
        
        camera.setX(0)
        camera.setZ(20)
        camera.setP(-5)
    
        #play the music 
        base.playMusic(self.enterMusic, looping=1, volume=1.0)
        
    #First the transition plays, then the animation is loaded.
    def TransitionOne(self):
        IrisTrack = Sequence(Func(self.removeButtons), Func(base.transitions.irisOut, 1), Wait(1.5), Func(self.loadAnimationOne), Wait(2))
        IrisTrack.start()
		
    def TransitionTwo(self):
        IrisTrack = Sequence(Func(self.removeButtons), Func(base.transitions.irisOut, 1), Wait(1.5), Func(self.loadAnimationTwo), Wait(2))
        IrisTrack.start()
		
    def TransitionThree(self):
        IrisTrack = Sequence(Func(self.removeButtons), Func(base.transitions.irisOut, 1), Wait(1.5), Func(self.loadAnimationThree), Wait(2))
        IrisTrack.start()	
    def TransitionFour(self):
        IrisTrack = Sequence(Func(self.removeButtons), Func(base.transitions.irisOut, 1), Wait(1.5), Func(self.loadAnimationFour), Wait(2))
        IrisTrack.start()
    def TransitionFive(self):
        IrisTrack = Sequence(Func(self.removeButtons), Func(base.transitions.irisOut, 1), Wait(1.5), Func(self.loadAnimationFive), Wait(2))
        IrisTrack.start()	
	
	#Functions for loading each animation
    def loadAnimationOne(self):
        self.removeSetting()
        self.enterMusic.stop()
        self.SpinTask.finish()
        AnimationFirstTestKaren.AnimationFirstTestKaren(self).create()
		
    def loadAnimationTwo(self):
        self.removeSetting()
        self.enterMusic.stop()
        self.SpinTask.finish()
        AnimationDoughnut.AnimationDoughnut(self).create()
		
    def loadAnimationThree(self):
        self.removeSetting()
        self.enterMusic.stop()
        self.SpinTask.finish()
        AnimationClones.AnimationClones(self).create()

    def loadAnimationFour(self):
        self.removeSetting()
        self.enterMusic.stop()
        self.SpinTask.finish()
        AnimationRedSonic.AnimationRedSonic(self).create()

    def exit(self):
        avList = []
        self.removeButtons()
        self.removeSetting()
        base.cr.enterChooseAvatar(avList)
        
    def removeSetting(self):
        self.sky.removeNode()
        self.tagArena.removeNode()
        
    def removeButtons(self):
        self.AnimButton.removeNode()
        self.AnimButton2.removeNode()
        self.AnimButton3.removeNode()
        self.ExitButton.removeNode()
		