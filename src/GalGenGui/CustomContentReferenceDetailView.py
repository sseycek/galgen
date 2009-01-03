import os
import wx
from NamedObjectDetailView import NamedObjectDetailView

class CustomContentReferenceDetailView(NamedObjectDetailView):

    def __init__(self, panel, element):
        super(CustomContentReferenceDetailView, self).__init__(panel, element)

    def _FillPropertySizer(self):
        super(CustomContentReferenceDetailView, self)._FillPropertySizer()
        label = wx.StaticText(self._main_panel, -1, 'HTML file location')
        self._html_location_edit = wx.TextCtrl(self._main_panel, -1, self.element.html_location, size = (600, -1))
        self._find_button = wx.Button(self._main_panel, -1, "Find ...", (20, 20))
        self._main_panel.Bind(wx.EVT_BUTTON, self.__OnFindButton, self._find_button)
        self._find_button.SetSize(self._find_button.GetBestSize())
        self._main_panel.Bind(wx.EVT_TEXT, self.__OnFieldEdited, self._html_location_edit)
        self._control_grid.Add(label, (5, 1))
        self._control_grid.Add(self._html_location_edit, (5,2))
        self._control_grid.Add(self._find_button, (5,3))
        label = wx.StaticText(self._main_panel, -1, 'Supplemental files directory')
        self._supplemental_dir_edit = wx.TextCtrl(self._main_panel, -1, self.element.supplemental_dir, size = (600, -1))
        self._find_dir_button = wx.Button(self._main_panel, -1, "Find ...", (20, 20))
        self._main_panel.Bind(wx.EVT_BUTTON, self.__OnFindDirButton, self._find_dir_button)
        self._find_dir_button.SetSize(self._find_dir_button.GetBestSize())
        self._main_panel.Bind(wx.EVT_TEXT, self.__OnFieldEdited, self._supplemental_dir_edit)
        self._control_grid.Add(label, (6, 1))
        self._control_grid.Add(self._supplemental_dir_edit, (6,2))
        self._control_grid.Add(self._find_dir_button, (6,3))

    def _IsHtmlLocationModified(self):
        return self._html_location_edit.GetValue() != self.element.html_location

    def _IsSupplementalDirModified(self):
        return self._supplemental_dir_edit.GetValue() != self.element.supplemental_dir

    def _IsModified(self):
        return (self._IsHtmlLocationModified() or self._IsSupplementalDirModified() or super(CustomContentReferenceDetailView, self)._IsModified())

    def __OnFieldEdited(self, event):
        self._OnEdited()

    def __OnFindButton(self, event):
        dlg = wx.FileDialog(self._main_panel,
                            message="Choose a file",
                            defaultDir=os.getcwd(),
                            defaultFile="",
                            wildcard="HTML files (*.html)|*.html",
                            style=wx.OPEN | wx.CHANGE_DIR)
        if dlg.ShowModal() == wx.ID_OK:
            self._html_location_edit.SetValue(dlg.GetPath())
            self._OnEdited()

    def __OnFindDirButton(self, event):
        dlg = wx.DirDialog(self._main_panel, "Supplemental files directory", style = wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            self._supplemental_dir_edit.SetValue(dlg.GetPath())
            self._OnEdited()
        
    def _OnApply(self, event):
        super(CustomContentReferenceDetailView, self)._OnApply(event)
        if self._IsHtmlLocationModified():
            self.element.html_location = self._html_location_edit.GetValue()
        if self._IsSupplementalDirModified():
            self.element.supplemental_dir = self._supplemental_dir_edit.GetValue()

    def _OnCancel(self, event):
        super(CustomContentReferenceDetailView, self)._OnCancel(event)
        if self._IsHtmlLocationModified():
            self._html_location_edit.SetValue(self.element.html_location)
        if self._IsSupplementalDirModified():
            self._supplemental_dir_edit.SetValue(self.element.supplemental_dir)
