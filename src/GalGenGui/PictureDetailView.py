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

    def _FillPropertySizerBelowButtons(self):
        super(PictureDetailView, self)._FillPropertySizerBelowButtons()
        if self.element.pic_location and os.path.exists(self.element.pic_location):
            self.__img_box = wx.FlexGridSizer(cols = 2, hgap = 5, vgap = 5)
            img = wx.Image(self.element.pic_location, wx.BITMAP_TYPE_ANY)
            bmp = wx.BitmapFromImage(img)
            self.__img = wx.StaticBitmap(self._main_panel, -1, bmp)
            self.__img_box.AddMany(((10, 10), (10, 10),
                                    (10, 10), self.__img))
            self.property_box.Add(self.__img_box, 0, wx.EXPAND)
        self._main_panel.Refresh()
