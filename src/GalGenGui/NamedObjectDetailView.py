import wx
from GalleryObjectDetailView import GalleryObjectDetailView

class NamedObjectDetailView(GalleryObjectDetailView):

    def __init__(self, panel, element):
        super(NamedObjectDetailView, self).__init__(panel, element)

    def _FillPropertySizer(self):
        super(NamedObjectDetailView, self)._FillPropertySizer()
        label = wx.StaticText(self._main_panel, -1, 'Name')
        self._name_edit = wx.TextCtrl(self._main_panel, -1, self.element.name, size = (600, -1))
        self._name_edit.MoveBeforeInTabOrder(self._menu_id_edit)
        self._main_panel.Bind(wx.EVT_TEXT, self.__OnNameEdited, self._name_edit)
        self._control_grid.Add((10, 10), (0, 0))
        self._control_grid.Add(label, (1, 1))
        self._control_grid.Add(self._name_edit, (1, 2))

    def __IsNameModified(self):
        return self._name_edit.GetValue() != self.element.name

    def _IsModified(self):
        return (self.__IsNameModified() or super(NamedObjectDetailView, self)._IsModified())

    def __OnNameEdited(self, event):
        if self._main_panel.event_handlers_enabled:
            self._OnEdited()

    def _OnApply(self, event):
        super(NamedObjectDetailView, self)._OnApply(event)
        if self.__IsNameModified():
            self.element.name = self._name_edit.GetValue()

    def _OnCancel(self, event):
        super(NamedObjectDetailView, self)._OnCancel(event)
        if self.__IsNameModified():
             self._name_edit.SetValue(self.element.name)
