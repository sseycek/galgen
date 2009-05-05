import os
import wx
from GalGenLib.Album import Album
from PictureDropTarget import PictureDropTarget

class PictureOnTreeDropTarget(PictureDropTarget):
    def __init__(self, tree):
        wx.FileDropTarget.__init__(self)
        self.__tree = tree
        self.__detail_panel_refresh = False

    def _getAlbum(self, x, y):
        (id, flag) = self.__tree.HitTest((x, y))
        if id.IsOk():
            item = self.__tree.GetPyData(id).element
            if isinstance(item, Album):
                return item
        return None

    def _getTree(self):
        return self.__tree
