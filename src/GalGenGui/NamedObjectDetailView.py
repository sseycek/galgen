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
#     "This product includes software developed by Stepan Seycek."
#  4. The name Stepan Seycek may not be used to endorse or promote 
#     products derived from this software without specific prior 
#     written permission. 
#
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, 
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY 
# AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL 
# THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, 
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, 
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; 
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED 
# OF THE POSSIBILITY OF SUCH DAMAGE. 

import wx
from GalleryObjectDetailView import GalleryObjectDetailView

class NamedObjectDetailView(GalleryObjectDetailView):

    def __init__(self, panel, element):
        super(NamedObjectDetailView, self).__init__(panel, element)
        # not present in all subclasses
        self._description_edit = None

    def _FillPropertySizer(self):
        super(NamedObjectDetailView, self)._FillPropertySizer()
        label = wx.StaticText(self._main_panel, -1, 'Name')
        self._name_edit = wx.TextCtrl(self._main_panel, -1, self.element.name, size = (600, -1))
        self._name_edit.MoveBeforeInTabOrder(self._menu_id_edit)
        self._main_panel.Bind(wx.EVT_TEXT, self.__OnNameEdited, self._name_edit)
        self._control_grid.Add((10, 10), (0, 0))
        self._control_grid.Add(label, (1, 1))
        self._control_grid.Add(self._name_edit, (1, 2))

    def _AddDescription(self, vpos, predecessor):
        label = wx.StaticText(self._main_panel, -1, 'Description')
        self._description_edit = wx.TextCtrl(self._main_panel, -1, self.element.description, style = wx.TE_MULTILINE | wx.TE_AUTO_SCROLL, size = (600, 50))
        self._description_edit.MoveAfterInTabOrder(predecessor)
        self._main_panel.Bind(wx.EVT_TEXT, self.__OnDescriptionEdited, self._description_edit)
        #self._control_grid.Add((10, 10), (0, 0))
        self._control_grid.Add(label, (vpos, 1))
        self._control_grid.Add(self._description_edit, (vpos, 2))

    def __IsNameModified(self):
        return self._name_edit.GetValue() != self.element.name

    def __IsDescriptionModified(self):
        return self._description_edit and self._description_edit.GetValue() != self.element.description

    def _IsModified(self):
        return (self.__IsNameModified() or
                self.__IsDescriptionModified() or 
                super(NamedObjectDetailView, self)._IsModified())

    def __OnNameEdited(self, event):
        if self._main_panel.event_handlers_enabled:
            self._OnEdited()

    def __OnDescriptionEdited(self, event):
        if self._main_panel.event_handlers_enabled:
            self._OnEdited()

    def _OnApply(self, event):
        super(NamedObjectDetailView, self)._OnApply(event)
        if self.__IsNameModified():
            self.element.name = self._name_edit.GetValue()
            self.element.modified = True
        if self.__IsDescriptionModified():
            self.element.description = self._description_edit.GetValue()
            self.element.modified = True

    def _OnCancel(self, event):
        super(NamedObjectDetailView, self)._OnCancel(event)
        if self.__IsNameModified():
             self._name_edit.SetValue(self.element.name)
        if self.__IsDescriptionModified():
             self._description_edit.SetValue(self.element.description)
