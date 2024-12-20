from panda3d.core import *
from direct.gui.DirectGui import *
from direct.showbase import DirectObject
from otp.avatar import Avatar
from direct.distributed import DistributedObject
import SuitDNA
from toontown.toonbase import TTLocalizer
from otp.avatar import AvatarPanel
from toontown.friends import FriendsListPanel

class SuitAvatarPanel(AvatarPanel.AvatarPanel):
    currentAvatarPanel = None

    def __init__(self, avatar):
        AvatarPanel.AvatarPanel.__init__(self, avatar, FriendsListPanel=FriendsListPanel)
        self.avName = avatar.getName()
        gui = loader.loadModel('phase_3.5/models/gui/suit_detail_panel')
        self.frame = DirectFrame(geom=gui.find('**/avatar_panel'), geom_scale=0.21, geom_pos=(0, 0, 0.02), relief=None, pos=(-0.2348, 0, -0.475), parent=base.a2dTopRight)
        disabledImageColor = Vec4(1, 1, 1, 0.4)
        text0Color = Vec4(1, 1, 1, 1)
        text1Color = Vec4(0.5, 1, 0.5, 1)
        text2Color = Vec4(1, 1, 0.5, 1)
        text3Color = Vec4(1, 1, 1, 0.2)
        self.head = self.frame.attachNewNode('head')
        for part in avatar.headParts:
            copyPart = part.copyTo(self.head)
            copyPart.setDepthTest(1)
            copyPart.setDepthWrite(1)

        p1 = Point3()
        p2 = Point3()
        self.head.calcTightBounds(p1, p2)
        d = p2 - p1
        biggest = max(d[0], d[1], d[2])
        s = 0.3 / biggest
        self.head.setPosHprScale(0, 0, 0, 180, 0, 0, s, s, s)
        self.nameLabel = DirectLabel(parent=self.frame, pos=(0.0125, 0, 0.36), relief=None, text=self.avName, text_font=avatar.getFont(), text_fg=Vec4(0, 0, 0, 1), text_pos=(0, 0), text_scale=0.047, text_wordwrap=7.5, text_shadow=(1, 1, 1, 1))
        level = avatar.getActualLevel()
        dept = SuitDNA.getSuitDeptFullname(avatar.dna.name)
        revives = avatar.getMaxSkeleRevives() + 1
        levelText = TTLocalizer.AvatarPanelCogLevel % {'level': level}
        levelText += '\n' + str(avatar.getHP()) + '/' + str(avatar.getMaxHP())
        if revives == 1:
            self.levelLabel = DirectLabel(parent=self.frame, pos=(0, 0, -0.1), relief=None, text=levelText, text_font=avatar.getFont(), text_align=TextNode.ACenter, text_fg=Vec4(0, 0, 0, 1), text_pos=(0, 0), text_scale=0.05, text_wordwrap=8.0)
        elif revives > 1:
            self.levelLabel = DirectLabel(parent=self.frame, pos=(0, 0, -0.1), relief=None, text=levelText + TTLocalizer.AvatarPanelCogRevives % revives, text_font=avatar.getFont(), text_align=TextNode.ACenter, text_fg=Vec4(0, 0, 0, 1), text_pos=(0, 0), text_scale=0.05, text_wordwrap=8.0)
        corpIcon = avatar.corpMedallion.copyTo(hidden)
        corpIcon.setPosHprScale(0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.corpIcon = DirectLabel(parent=self.frame, geom=corpIcon, geom_scale=0.1, pos=(0, 0, -0.25), relief=None)
        corpIcon.removeNode()
        self.closeButton = DirectButton(parent=self.frame, relief=None, pos=(0.0, 0, -0.36), text=TTLocalizer.AvatarPanelCogDetailClose, text_font=avatar.getFont(), text0_fg=Vec4(0, 0, 0, 1), text1_fg=Vec4(0.5, 0, 0, 1), text2_fg=Vec4(1, 0, 0, 1), text_pos=(0, 0), text_scale=0.05, command=self.__handleClose)
        gui.removeNode()
        menuX = -0.05
        menuScale = 0.064
        base.localAvatar.obscureFriendsListButton(1)
        self.frame.show()
        messenger.send('avPanelDone')
        return

    def cleanup(self):
        if self.frame is None:
            return
        self.frame.destroy()
        del self.frame
        self.frame = None
        self.head.removeNode()
        del self.head
        base.localAvatar.obscureFriendsListButton(-1)
        AvatarPanel.AvatarPanel.cleanup(self)
        return

    def __handleClose(self):
        self.cleanup()
        AvatarPanel.currentAvatarPanel = None
        return