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

import os
import wx
from NamedObjectDetailView import NamedObjectDetailView

class PictureReferenceDetailView(NamedObjectDetailView):

    def __init__(self, panel, element):
        super(PictureReferenceDetailView, self).__init__(panel, element)

    def _FillPropertySizer(self):
        super(PictureReferenceDetailView, self)._FillPropertySizer()
        label = wx.StaticText(self._main_panel, -1, 'Image location')
        self._img_location_edit = wx.TextCtrl(self._main_panel, -1, self.element.pic_location, size = (600, -1))
        self._find_button = wx.Button(self._main_panel, -1, "Find ...", (20, 20))
        self._main_panel.Bind(wx.EVT_BUTTON, self.__OnFindButton, self._find_button)
        self._find_button.SetSize(self._find_button.GetBestSize())
        self._main_panel.Bind(wx.EVT_TEXT, self.__OnImgLocationEdited, self._img_location_edit)
        self._control_grid.Add(label, (5, 1))
        self._control_grid.Add(self._img_location_edit, (5,2))
        self._control_grid.Add(self._find_button, (5,3))

    def _IsImgLocationModified(self):
        return self._img_location_edit.GetValue() != self.element.pic_location

    def _IsModified(self):
        return (self._IsImgLocationModified() or super(PictureReferenceDetailView, self)._IsModified())

    def __OnImgLocationEdited(self, event):
        self._OnEdited()

    def __OnFindButton(self, event):
        dlg = wx.FileDialog(self._main_panel,
                            message="Choose a file",
                            defaultDir=os.getcwd(),
                            defaultFile="",
                            wildcard="All files (*.*)|*.*",
                            style=wx.OPEN | wx.CHANGE_DIR)
        if dlg.ShowModal() == wx.ID_OK:
            self._img_location_edit.SetValue(dlg.GetPath())
            self._OnEdited()

    def _OnApply(self, event):
        super(PictureReferenceDetailView, self)._OnApply(event)
        if self._IsImgLocationModified():
            self.element.pic_location = self._img_location_edit.GetValue()
            self.element.modified = True
            self._PicLocationUpdated()

    def _PicLocationUpdated(self):
        # hook for subclasses
        pass

    def _OnCancel(self, event):
        super(PictureReferenceDetailView, self)._OnCancel(event)
        if self._IsImgLocationModified():
            self._img_location_edit.SetValue(self.element.pic_location)
