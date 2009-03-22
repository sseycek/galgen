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
            self.element.modified = True
        if self.__IsTitleModified():
            self.element.title = self._title_edit.GetValue()
            self.element.modified = True
        if self.__IsSubtitleModified():
            self.element.subtitle = self._subtitle_edit.GetValue()
            self.element.modified = True

    def _OnCancel(self, event):
        super(GalleryObjectDetailView, self)._OnCancel(event)
        if self.__IsMenuIdModified():
            self._menu_id_edit.SetValue(self.element.menu_id)
        if self.__IsTitleModified():
            self._title_edit.SetValue(self.element.title)
        if self.__IsSubtitleModified():
            self._subtitle_edit.SetValue(self.element.subtitle)
