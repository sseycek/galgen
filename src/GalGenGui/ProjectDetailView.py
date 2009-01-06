import os
import wx
from CustomContentReferenceDetailView import CustomContentReferenceDetailView

class ProjectDetailView(CustomContentReferenceDetailView):
    
    def __init__(self, panel, element):
        super(ProjectDetailView, self).__init__(panel, element)

    def __AddXhtmlTemplateControl(self):
        label = wx.StaticText(self._main_panel, -1, 'XHTML Template')
        self.__xhtml_template_edit = wx.TextCtrl(self._main_panel, -1, self.element.xhtml_template, size = (600, -1))
        self.__xhtml_template_edit.MoveAfterInTabOrder(self._find_dir_button)
        self.__find_xhtml_template_button = wx.Button(self._main_panel, -1, "Find ...", (20, 20))
        self.__find_xhtml_template_button.MoveAfterInTabOrder(self.__xhtml_template_edit)
        self._main_panel.Bind(wx.EVT_BUTTON, self.__OnXhtmlTemplateFindButton, self.__find_xhtml_template_button)
        self.__find_xhtml_template_button.SetSize(self.__find_xhtml_template_button.GetBestSize())
        self._main_panel.Bind(wx.EVT_TEXT, self.__OnXhtmlTemplateEdited, self.__xhtml_template_edit)
        self._control_grid.Add(label, (7, 1))
        self._control_grid.Add(self.__xhtml_template_edit, (7, 2))
        self._control_grid.Add(self.__find_xhtml_template_button, (7, 3))

    def __AddStyleDirectoryControl(self):
        label = wx.StaticText(self._main_panel, -1, 'Style Directory')
        self.__style_directory_edit = wx.TextCtrl(self._main_panel, -1, self.element.style_directory, size = (600, -1))
        self.__style_directory_edit.MoveAfterInTabOrder(self.__find_xhtml_template_button)
        self.__find_style_directory_button = wx.Button(self._main_panel, -1, "Find ...", (20, 20))
        self._main_panel.Bind(wx.EVT_BUTTON, self.__OnStyleDirectoryFindButton, self.__find_style_directory_button)
        self.__find_style_directory_button.SetSize(self.__find_style_directory_button.GetBestSize())
        self.__find_style_directory_button.MoveAfterInTabOrder(self.__style_directory_edit)
        self._main_panel.Bind(wx.EVT_TEXT, self.__OnStyleDirectoryEdited, self.__style_directory_edit)
        self._control_grid.Add(label, (8, 1))
        self._control_grid.Add(self.__style_directory_edit, (8, 2))
        self._control_grid.Add(self.__find_style_directory_button, (8, 3))

    def _FillPropertySizer(self):
        super(ProjectDetailView, self)._FillPropertySizer()
        self.__AddXhtmlTemplateControl()
        self.__AddStyleDirectoryControl()

    def GetLabelCategory(self):
        return 'PROJECT'
    
    def __OnXhtmlTemplateEdited(self, event):
        if self._main_panel.event_handlers_enabled:
            self._OnEdited()

    def __OnXhtmlTemplateFindButton(self, event):
        dlg = wx.FileDialog(self._main_panel,
                            message="XHMTL template file",
                            defaultDir=os.getcwd(),
                            defaultFile="",
                            wildcard="HTML files (*.html)|*.html",
                            style=wx.OPEN | wx.CHANGE_DIR)
        if dlg.ShowModal() == wx.ID_OK:
            self.__xhtml_template_edit.SetValue(dlg.GetPath())
            self._OnEdited()

    def __OnStyleDirectoryEdited(self, event):
        if self._main_panel.event_handlers_enabled:
            self._OnEdited()

    def __OnStyleDirectoryFindButton(self, event):
        dlg = wx.DirDialog(self._main_panel, "Style Directory", style = wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.__style_directory_edit.SetValue(dlg.GetPath())
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
            self.element.modified = True
        if self.__IsStyleDirectoryModified():
            self.element.style_directory = self.__style_directory_edit.GetValue()
            self.element.modified = True

    def _OnCancel(self, event):
        super(ProjectDetailView, self)._OnCancel(event)
        if self.__IsXhtmlTemplateModified():
             self.__xhtml_template_edit.SetValue(self.element.xhtml_template)
        if self.__IsStyleDirectoryModified():
             self.__style_directory_edit.SetValue(self.element.style_directory)
    