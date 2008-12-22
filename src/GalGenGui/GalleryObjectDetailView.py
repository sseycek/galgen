import wx
from DetailView import DetailView

class GalleryObjectDetailView(DetailView):

    def __init__(self, panel, element):
        super(GalleryObjectDetailView, self).__init__(panel, element)

    def _FillPropertySizer(self):
        super(GalleryObjectDetailView, self)._FillPropertySizer()
        label = wx.StaticText(self._main_panel, -1, 'Menu ID')
        self._menu_id_edit = wx.TextCtrl(self._main_panel, -1, self.element.menu_id, size = (200, -1))
        self._main_panel.Bind(wx.EVT_TEXT, self.__OnMenuIdEdited, self._menu_id_edit)
        self._control_grid.Add(label, (2, 1))
        self._control_grid.Add(self._menu_id_edit, (2, 2))

    def __OnMenuIdEdited(self, event):
        if self._main_panel.event_handlers_enabled:
            self._OnEdited()

    def __IsMenuIdModified(self):
        return self._menu_id_edit.GetValue() != self.element.menu_id

    def _IsModified(self):
        return (self.__IsMenuIdModified() or super(NamedObjectDetailView, self)._IsModified())

    def _OnApply(self, event):
        super(GalleryObjectDetailView, self)._OnApply(event)

    def _OnCancel(self, event):
        super(GalleryObjectDetailView, self)._OnCancel(event)
