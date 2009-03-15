# Copyright (c) 2009 Stepan Seycek. All rights reserved.
# 
# Redistribution and use in source and binary forms, with or 
# without modification, are permitted provided that the following 
# conditions are met:
# 
#  1. Redistributions of source code must retain the above 
#     copyright notice, this list of conditions and the 
#     following disclaimer.
#  2. Redistributions in binary form must reproduce the above 
#     copyright notice, this list of conditions and the following 
#     disclaimer in the documentation and/or other materials 
#     provided with the distribution.
#  3. All advertising materials mentioning features or use of this 
#     software must display the following acknowledgement: 
#     “This product includes software developed by Stepan Seycek.”
#  4. The name Stepan Seycek may not be used to endorse or promote 
#     products derived from this software without specific prior 
#     written permission. 
#
# THIS SOFTWARE IS PROVIDED “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, 
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY 
# AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL 
# THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, 
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, 
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; 
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED 
# OF THE POSSIBILITY OF SUCH DAMAGE. 

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
        self._html_location_edit.MoveAfterInTabOrder(self._subtitle_edit)
        self._find_button = wx.Button(self._main_panel, -1, "Find ...", (20, 20))
        self._main_panel.Bind(wx.EVT_BUTTON, self.__OnFindButton, self._find_button)
        self._find_button.SetSize(self._find_button.GetBestSize())
        self._find_button.MoveAfterInTabOrder(self._html_location_edit)
        self._main_panel.Bind(wx.EVT_TEXT, self.__OnFieldEdited, self._html_location_edit)
        self._control_grid.Add(label, (5, 1))
        self._control_grid.Add(self._html_location_edit, (5,2))
        self._control_grid.Add(self._find_button, (5,3))
        label = wx.StaticText(self._main_panel, -1, 'Supplemental files directory')
        self._supplemental_dir_edit = wx.TextCtrl(self._main_panel, -1, self.element.supplemental_dir, size = (600, -1))
        self._supplemental_dir_edit.MoveAfterInTabOrder(self._find_button)
        self._find_dir_button = wx.Button(self._main_panel, -1, "Find ...", (20, 20))
        self._find_dir_button.MoveAfterInTabOrder(self._supplemental_dir_edit)
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
            self.element.modified = True
        if self._IsSupplementalDirModified():
            self.element.supplemental_dir = self._supplemental_dir_edit.GetValue()
            self.element.modified = True

    def _OnCancel(self, event):
        super(CustomContentReferenceDetailView, self)._OnCancel(event)
        if self._IsHtmlLocationModified():
            self._html_location_edit.SetValue(self.element.html_location)
        if self._IsSupplementalDirModified():
            self._supplemental_dir_edit.SetValue(self.element.supplemental_dir)
