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
        

