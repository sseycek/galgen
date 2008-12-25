import os
import wx
from NamedObjectDetailView import NamedObjectDetailView

class PictureReferenceDetailView(NamedObjectDetailView):

    def __init__(self, panel, element):
        super(PictureReferenceDetailView, self).__init__(panel, element)

    def _FillPropertySizer(self):
        super(PictureReferenceDetailView, self)._FillPropertySizer()
        label = wx.StaticText(self._main_panel, -1, 'Image location')
        self._img_location_edit = wx.TextCtrl(self._main_panel, -1, self.element.pic_location, size = (200, -1))
        self._find_button = wx.Button(self._main_panel, -1, "Find ...", (20, 20))
        self._main_panel.Bind(wx.EVT_BUTTON, self.__OnFindButton, self._find_button)
        self._find_button.SetSize(self._find_button.GetBestSize())
        self._main_panel.Bind(wx.EVT_TEXT, self.__OnImgLocationEdited, self._img_location_edit)
        self._control_grid.Add(label, (5, 1))
        self._control_grid.Add(self._img_location_edit, (5,2))
        self._control_grid.Add(self._find_button, (5,3))

    def _IsImgLocationModified(self):
        return self._img_location_edit.GetValue() != self.element.pic_location

    def _IsModified(self):
        return (self._IsImgLocationModified() or super(PictureReferenceDetailView, self)._IsModified())

    def __OnImgLocationEdited(self, event):
        self._OnEdited()

    def __OnFindButton(self, event):
        dlg = wx.FileDialog(self._main_panel,
                            message="Choose a file",
                            defaultDir=os.getcwd(),
                            defaultFile="",
                            wildcard="All files (*.*)|*.*",
                            style=wx.OPEN | wx.CHANGE_DIR)
        if dlg.ShowModal() == wx.ID_OK:
            self._img_location_edit.SetValue(dlg.GetPath())
            self._OnEdited()

    def _OnApply(self, event):
        super(PictureReferenceDetailView, self)._OnApply(event)
        if self._IsImgLocationModified():
            self.element.pic_location = self._img_location_edit.GetValue()

    def _OnCancel(self, event):
        super(PictureReferenceDetailView, self)._OnCancel(event)
        if self._IsImgLocationModified():
            self._img_location_edit.SetValue(self.element.pic_location)
