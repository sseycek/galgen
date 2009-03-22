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
from GalGenLib.Picture import Picture
from GalGenLib.Project import Project
from GalGenLib.Album import Album
from GalGenLib.Gallery import Gallery
from GalGenLib.CustomContentPage import CustomContentPage
from ProjectDetailView import ProjectDetailView
from AlbumDetailView import AlbumDetailView
from GalleryDetailView import GalleryDetailView
from PictureDetailView import PictureDetailView
from CustomContentPageDetailView import CustomContentPageDetailView

class DetailPanel(wx.Panel):

    def __init__(self, parent, style):
        wx.Panel.__init__(self, parent = parent, style = style | wx.TAB_TRAVERSAL)
        self.__event_handlers_enabled = True
        self.__element = None
        self.__view = None

    def GetEventHandlersEnabled(self):
        return self.__event_handlers_enabled;
    event_handlers_enabled = property(GetEventHandlersEnabled, None)

    def __ShowApplyCancelDlg(self, new_element):
        txt = '%s has been modified. Shall the modifications\nbe applied before switching to %s?' % (self.__view.element.name, new_element.name)
        dlg = wx.MessageDialog(self, txt,
                               'Apply changes',
                                wx.YES_NO | wx.YES_DEFAULT | wx.ICON_INFORMATION)
        if dlg.ShowModal() == wx.ID_YES:
            self.__view.Apply()

    def Display(self, element):
        if element != self.__element:
            self.SetDropTarget(None)
            if self.__view and self.__view.IsModified():
                self.__ShowApplyCancelDlg(element)
            self.__event_handlers_enabled = False
            view = self.__GetViewForElement(element)
            self.DestroyChildren()
            view.FillPanel()
            self.__view = view
            self.__event_handlers_enabled = True

    def __GetViewForElement(self, element):
        if isinstance(element, Project):
            return ProjectDetailView(self, element)
        elif isinstance(element, Album):
            return AlbumDetailView(self, element)
        elif isinstance(element, Gallery):
            return GalleryDetailView(self, element)
        elif isinstance(element, Picture):
            return PictureDetailView(self, element)
        elif isinstance(element, CustomContentPage):
            return CustomContentPageDetailView(self, element)
        else:
            raise Exception, 'no detail view available for element'
        

