import os
import wx
from GalGenLib.Album import Album
from GalGenLib.Picture import Picture

class PictureDropTarget(wx.FileDropTarget):
    def __init__(self, tree):
        wx.FileDropTarget.__init__(self)
        self.__tree = tree

    def __accept(self, filenames):
        for filename in filenames:
            ext = os.path.splitext(os.path.split(filename)[1])[1]
            if ext not in ('.jpg', '.JPG', '.jpeg', '.JPEG', '.gif', '.GIF', '.png', '.PNG'):
                return False
        return True

    def _getAlbum(self, x, y):
        return None

    def OnDragOver(self, x, y, default):
        album = self._getAlbum(x, y)
        if album is not None:
            return default
        return wx.DragNone
    
    def OnDropFiles(self, x, y, filenames):
        album = self._getAlbum(x, y)
        if album is not None and self.__accept(filenames):
            for filename in filenames:
                name = os.path.splitext(os.path.split(filename)[1])[0]
                picture = Picture(name, filename, '', '', name, '')
                album.addChild(picture)
            return True
        return False
    