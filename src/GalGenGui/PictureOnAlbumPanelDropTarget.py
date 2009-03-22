import os
import wx
from PictureDropTarget import PictureDropTarget

class PictureOnAlbumPanelDropTarget(PictureDropTarget):
    def __init__(self, panel):
        wx.FileDropTarget.__init__(self)
        self.__panel = panel

    def _getAlbum(self, x, y):
        return self.__panel.element
