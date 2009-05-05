import os
import wx
from PictureDropTarget import PictureDropTarget

class PictureOnAlbumPanelDropTarget(PictureDropTarget):
    def __init__(self, view):
        wx.FileDropTarget.__init__(self)
        self.__view = view

    def _getAlbum(self, x, y):
        return self.__view.element

    def _getTree(self):
        return self.__view.panel.GetParent().tree_panel.tree
