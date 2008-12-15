import wx
import os
from PictureReferenceDetailView import PictureReferenceDetailView

class PictureDetailView(PictureReferenceDetailView):

    def __init__(self, panel, element):
        super(PictureDetailView, self).__init__(panel, element)

    def GetLabelCategory(self):
        return 'IMAGE'

    def ApplyChanges(self):
        super(PictureDetailView, self).ApplyChanges()

    def _FillPropertySizer(self):
        super(PictureDetailView, self)._FillPropertySizer()
        if self.element.pic_location and os.path.exists(self.element.pic_location):
            img = wx.Image(self.element.pic_location, wx.BITMAP_TYPE_ANY)
            bmp = wx.BitmapFromImage(img)
            self.__img = wx.StaticBitmap(self._main_panel, -1, bmp)
            self._control_grid.Add(self.__img, (4, 1), span = (1, 3))
        self._main_panel.Refresh()
