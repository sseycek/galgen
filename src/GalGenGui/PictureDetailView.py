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
