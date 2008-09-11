import wx
from GalGenLib import Globals
from GalGenGui.Frame import *

instance = None

class App(wx.App):
    WX_ID_FRAME = 1

    def __init__(self):
        wx.App.__init__(self)

    def OnInit(self):
        global instance
        name = '%s %s' % (Globals.ProgName, Globals.ProgVersion)
        self.__frame = Frame(parent = None, title = name)
        self.__frame.Show()
        instance = self
        return True

    def GetFrame(self):
        return self.__frame
    frame = property(GetFrame, None)
