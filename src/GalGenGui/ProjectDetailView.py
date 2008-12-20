import wx
from NamedObjectDetailView import NamedObjectDetailView

class ProjectDetailView(NamedObjectDetailView):

    def __init__(self, panel, element):
        super(ProjectDetailView, self).__init__(panel, element)

    def __AddXhtmlTemplateControl(self):
        label = wx.StaticText(self._main_panel, -1, 'XHTML Template')
        self.__xhtml_template_edit = wx.TextCtrl(self._main_panel, -1, self.element.xhtml_template, size = (200, -1))
        self._main_panel.Bind(wx.EVT_TEXT, self.__OnXhtmlTemplateEdited, self.__xhtml_template_edit)
        self._control_grid.Add(label, (2, 1))
        self._control_grid.Add(self.__xhtml_template_edit, (2, 2))

    def __AddStyleDirectoryControl(self):
        label = wx.StaticText(self._main_panel, -1, 'Style Directory')
        self.__style_directory_edit = wx.TextCtrl(self._main_panel, -1, self.element.style_directory, size = (200, -1))
        self._main_panel.Bind(wx.EVT_TEXT, self.__OnStyleDirectoryEdited, self.__style_directory_edit)
        self._control_grid.Add(label, (3, 1))
        self._control_grid.Add(self.__style_directory_edit, (3, 2))

    def _FillPropertySizer(self):
        super(ProjectDetailView, self)._FillPropertySizer()
        self.__AddXhtmlTemplateControl()
        self.__AddStyleDirectoryControl()

    def GetLabelCategory(self):
        return 'PROJECT'
    
    def __OnXhtmlTemplateEdited(self, event):
        if self._main_panel.event_handlers_enabled:
            self._OnEdited()

    def __OnStyleDirectoryEdited(self, event):
        if self._main_panel.event_handlers_enabled:
            self._OnEdited()

    def __IsXhtmlTemplateModified(self):
        return self.__xhtml_template_edit.GetValue() != self.element.xhtml_template

    def __IsStyleDirectoryModified(self):
        return self.__style_directory_edit.GetValue() != self.element.style_directory

    def _IsModified(self):
        return (self.__IsXhtmlTemplateModified() or
                self.__IsStyleDirectoryModified() or 
                super(ProjectDetailView, self)._IsModified())

    def _OnApply(self, event):
        super(ProjectDetailView, self)._OnApply(event)
        if self.__IsXhtmlTemplateModified():
            self.element.xhtml_template = self.__xhtml_template_edit.GetValue()
        if self.__IsStyleDirectoryModified():
            self.element.style_directory = self.__style_directory_edit.GetValue()

    def _OnCancel(self, event):
        super(ProjectDetailView, self)._OnCancel(event)
        if self.__IsXhtmlTemplateModified():
             self.__xhtml_template_edit.SetValue(self.element.xhtml_template)
        if self.__IsStyleDirectoryModified():
             self.__style_directory_edit.SetValue(self.element.style_directory)
    