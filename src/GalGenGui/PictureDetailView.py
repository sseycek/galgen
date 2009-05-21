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
import os
from PictureReferenceDetailView import PictureReferenceDetailView

class PictureDetailView(PictureReferenceDetailView):

    def __init__(self, panel, element):
        super(PictureDetailView, self).__init__(panel, element)

    def GetLabelCategory(self):
        return 'IMAGE'

    def _FillPropertySizer(self):
        super(PictureDetailView, self)._FillPropertySizer()
        self.__AddHighresLocation()
        self._AddDescription(7, self.__highres_find_button)
        self.__AddExif()

    def __AddHighresLocation(self):
        label = wx.StaticText(self._main_panel, -1, 'Highres location')
        self.__highres_location_edit = wx.TextCtrl(self._main_panel, -1, self.element.highres_location, size = (600, -1))
        self.__highres_find_button = wx.Button(self._main_panel, -1, "Find ...", (20, 20))
        self._main_panel.Bind(wx.EVT_BUTTON, self.__OnHighresFindButton, self.__highres_find_button)
        self.__highres_find_button.SetSize(self.__highres_find_button.GetBestSize())
        self._main_panel.Bind(wx.EVT_TEXT, self.__OnHighresLocationEdited, self.__highres_location_edit)
        self._control_grid.Add(label, (6, 1))
        self._control_grid.Add(self.__highres_location_edit, (6,2))
        self._control_grid.Add(self.__highres_find_button, (6,3))

    def __AddExif(self):
        label = wx.StaticText(self._main_panel, -1, 'EXIF')
        self.__exif_edit = wx.TextCtrl(self._main_panel, -1, self.element.exif, size = (600, -1))
        self._main_panel.Bind(wx.EVT_TEXT, self.__OnExifEdited, self.__exif_edit)
        self.__exif_update_button = wx.Button(self._main_panel, -1, "Update", (20, 20))
        self._main_panel.Bind(wx.EVT_BUTTON, self.__OnExifUpdateButton, self.__exif_update_button)
        self.__exif_update_button.SetSize(self.__exif_update_button.GetBestSize())
        self._control_grid.Add(label, (8, 1))
        self._control_grid.Add(self.__exif_edit, (8,2))
        self._control_grid.Add(self.__exif_update_button, (8,3))

    def __AddImage(self):
        if self.element.pic_location and os.path.exists(self.element.pic_location):
            img = wx.Image(self.element.pic_location, wx.BITMAP_TYPE_ANY)
            bmp = wx.BitmapFromImage(img)
            self.__img = wx.StaticBitmap(self._main_panel, -1, bmp)
            self.__img_box.AddMany(((10, 10), (10, 10),
                                    (10, 10), self.__img))

    def __AddImageBox(self):
        self.__img_box = wx.FlexGridSizer(cols = 2, hgap = 5, vgap = 5)
        self.__AddImage()
        self.property_box.Add(self.__img_box, 0, wx.EXPAND)
    
    def _FillPropertySizerBelowButtons(self):
        super(PictureDetailView, self)._FillPropertySizerBelowButtons()
        self.__AddImageBox()
        self._main_panel.Refresh()

    def _OnApply(self, event):
        img_changed = self._IsImgLocationModified()
        super(PictureDetailView, self)._OnApply(event)
        if img_changed:
            # have repaint problems here, refresh the complete panel
            # TODO: remove this ugly hack
            self._main_panel.Display(self.element)

    def __OnHighresLocationEdited(self, event):
        self._OnEdited()

    def __OnExifEdited(self, event):
        self._OnEdited()

    def __OnHighresFindButton(self, event):
        dlg = wx.FileDialog(self._main_panel,
                            message="Choose a file",
                            defaultDir=os.getcwd(),
                            defaultFile="",
                            wildcard="All files (*.*)|*.*",
                            style=wx.OPEN | wx.CHANGE_DIR)
        if dlg.ShowModal() == wx.ID_OK:
            self.__highres_location_edit.SetValue(dlg.GetPath())
            self._OnEdited()

    def __OnExifUpdateButton(self, event):
        exif = self.element.extractExifFromPicture()
        self.__exif_edit.SetValue(exif)
        self._OnEdited()
    
    def __IsHighresLocationModified(self):
        return self.__highres_location_edit.GetValue() != self.element.highres_location

    def __IsExifModified(self):
        return self.__exif_edit.GetValue() != self.element.exif

    def _IsModified(self):
        return (self.__IsHighresLocationModified() or
                self.__IsExifModified() or
                super(PictureDetailView, self)._IsModified())

    def _OnApply(self, event):
        super(PictureDetailView, self)._OnApply(event)
        if self.__IsHighresLocationModified():
            self.element.highres_location = self.__highres_location_edit.GetValue()
            self.element.modified = True
        if self.__IsExifModified():
            self.element.exif = self.__exif_edit.GetValue()
            self.element.modified = True

    def _OnCancel(self, event):
        super(PictureDetailView, self)._OnCancel(event)
        if self.__IsHighresLocationModified():
            self.__highres_location_edit.SetValue(self.element.highres_location)
        if self.__IsExifModified():
            self.__exif_edit.SetValue(self.element.exif)

    def _PicLocationUpdated(self):
        # update exif control
        self.__exif_edit.SetValue(self.element.exif)