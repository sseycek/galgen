import wx
from GalGenLib.Picture import Picture
from GalGenLib.Project import Project
from GalGenLib.Album import Album
from GalGenLib.Gallery import Gallery
from ProjectDetailView import ProjectDetailView
from AlbumDetailView import AlbumDetailView
from GalleryDetailView import GalleryDetailView
from PictureDetailView import PictureDetailView

class DetailPanel(wx.Panel):

    def __init__(self, parent, style):
        wx.Panel.__init__(self, parent = parent, style = style)
        self.__event_handlers_enabled = True

    def GetEventHandlersEnabled(self):
        return self.__event_handlers_enabled;
    event_handlers_enabled = property(GetEventHandlersEnabled, None)

    def Display(self, element):
        self.__event_handlers_enabled = False
        view = self.__GetViewForElement(element)
        self.DestroyChildren()
        view.FillPanel()
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

