import wx
from NamedObjectDetailView import NamedObjectDetailView

class ProjectDetailView(NamedObjectDetailView):

    def __init__(self, panel, element):
        super(ProjectDetailView, self).__init__(panel, element)

    def __AddXhtmlTemplateControl(self):
        label = wx.StaticText(self._main_panel, -1, 'XHTML Template')
        self._xhtml_template_edit = wx.TextCtrl(self._main_panel, -1, self.element.xhtml_template, size = (200, -1))
        self._main_panel.Bind(wx.EVT_TEXT, self.__OnXhtmlTemplateEdited, self._xhtml_template_edit)
        #self._control_grid.Add((10, 10), (0, 0))
        self._control_grid.Add(label, (2, 1))
        self._control_grid.Add(self._xhtml_template_edit, (2, 2))

    def _FillPropertySizer(self):
        super(ProjectDetailView, self)._FillPropertySizer()
        self.__AddXhtmlTemplateControl()

    def GetLabelCategory(self):
        return 'PROJECT'
    
    def __OnXhtmlTemplateEdited(self, event):
        if self._main_panel.event_handlers_enabled:
            self._OnEdited()

    def __IsXhtmlTemplateModified(self):
        return self._xhtml_template_edit.GetValue() != self.element.xhtml_template

    def _IsModified(self):
        return (self.__IsXhtmlTemplateModified() or super(ProjectDetailView, self)._IsModified())

    def _OnApply(self, event):
        super(ProjectDetailView, self)._OnApply(event)
        if self.__IsXhtmlTemplateModified():
            self.element.xhtml_template = self._xhtml_template_edit.GetValue()

    def _OnCancel(self, event):
        super(ProjectDetailView, self)._OnCancel(event)
        if self.__IsXhtmlTemplateModified():
             self._xhtml_template_edit.SetValue(self.element.xhtml_template)
    