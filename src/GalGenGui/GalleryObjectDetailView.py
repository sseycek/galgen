import wx
from DetailView import DetailView

class GalleryObjectDetailView(DetailView):

    def __init__(self, panel, element):
        super(GalleryObjectDetailView, self).__init__(panel, element)

    def __AddMenuIdEdit(self):
        label = wx.StaticText(self._main_panel, -1, 'Menu ID')
        self._menu_id_edit = wx.TextCtrl(self._main_panel, -1, self.element.menu_id, size = (600, -1))
        self._main_panel.Bind(wx.EVT_TEXT, self.__OnEdited, self._menu_id_edit)
        self._control_grid.Add(label, (2, 1))
        self._control_grid.Add(self._menu_id_edit, (2, 2))
    
    def __AddDetails(self):
        title_label = wx.StaticText(self._main_panel, -1, 'Title')
        self._title_edit = wx.TextCtrl(self._main_panel, -1, self.element.title, size = (600, -1))
        self._title_edit.MoveAfterInTabOrder(self._menu_id_edit)
        self._main_panel.Bind(wx.EVT_TEXT, self.__OnEdited, self._title_edit)
        self._control_grid.Add(title_label, (3, 1))
        self._control_grid.Add(self._title_edit, (3, 2))
        subtitle_label = wx.StaticText(self._main_panel, -1, 'Subtitle')
        self._subtitle_edit = wx.TextCtrl(self._main_panel, -1, self.element.subtitle, size = (600, -1))
        self._subtitle_edit.MoveAfterInTabOrder(self._title_edit)
        self._main_panel.Bind(wx.EVT_TEXT, self.__OnEdited, self._subtitle_edit)
        self._control_grid.Add(subtitle_label, (4, 1))
        self._control_grid.Add(self._subtitle_edit, (4, 2))

    def _FillPropertySizer(self):
        super(GalleryObjectDetailView, self)._FillPropertySizer()
        self.__AddMenuIdEdit()
        self.__AddDetails()

    def __OnEdited(self, event):
        if self._main_panel.event_handlers_enabled:
            self._OnEdited()

    def __IsMenuIdModified(self):
        return self._menu_id_edit.GetValue() != self.element.menu_id

    def __IsTitleModified(self):
        return self._title_edit.GetValue() != self.element.title

    def __IsSubtitleModified(self):
        return self._subtitle_edit.GetValue() != self.element.subtitle

    def _IsModified(self):
        return (self.__IsMenuIdModified() or
                self.__IsTitleModified() or
                self.__IsSubtitleModified() or 
                super(GalleryObjectDetailView, self)._IsModified())

    def _OnApply(self, event):
        super(GalleryObjectDetailView, self)._OnApply(event)
        if self.__IsMenuIdModified():
            self.element.menu_id = self._menu_id_edit.GetValue()
        if self.__IsTitleModified():
            self.element.title = self._title_edit.GetValue()
        if self.__IsSubtitleModified():
            self.element.subtitle = self._subtitle_edit.GetValue()

    def _OnCancel(self, event):
        super(GalleryObjectDetailView, self)._OnCancel(event)
        if self.__IsMenuIdModified():
            self._menu_id_edit.SetValue(self.element.menu_id)
        if self.__IsTitleModified():
            self._title_edit.SetValue(self.element.title)
        if self.__IsSubtitleModified():
            self._subtitle_edit.SetValue(self.element.subtitle)
