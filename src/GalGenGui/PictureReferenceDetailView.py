import wx
from NamedObjectDetailView import NamedObjectDetailView

class PictureReferenceDetailView(NamedObjectDetailView):
    GALGEN_ID_IMG_EDIT = 301

    def __init__(self, panel, element):
        super(PictureReferenceDetailView, self).__init__(panel, element)

    def _FillPropertySizer(self):
        super(PictureReferenceDetailView, self)._FillPropertySizer()
        label = wx.StaticText(self._main_panel, -1, 'Image location')
        self._img_location_edit = wx.TextCtrl(self._main_panel, self.GALGEN_ID_IMG_EDIT, self.element.pic_location, size = (200, -1))
        self._main_panel.Bind(wx.EVT_TEXT, self.__OnImgLocationEdited, self._img_location_edit)
        self._control_grid.Add(label, (2, 1))
        self._control_grid.Add(self._img_location_edit, (2,2))

    def __IsImgLocationModified(self):
        return self._img_location_edit.GetValue() != self.element.pic_location

    def _IsModified(self):
        return (self.__IsImgLocationModified() or super(PictureReferenceDetailView, self)._IsModified())

    def __OnImgLocationEdited(self, event):
        self._OnEdited()

    def _OnApply(self, event):
        super(PictureReferenceDetailView, self)._OnApply(event)
        if self.__IsImgLocationModified():
            self.element.pic_location = self._img_location_edit.GetValue()

    def _OnCancel(self, event):
        super(PictureReferenceDetailView, self)._OnCancel(event)
        if self.__IsImgLocationModified():
            self._img_location_edit.SetValue(self.element.pic_location)
