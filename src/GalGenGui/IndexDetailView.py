import wx
from PictureReferenceDetailView import PictureReferenceDetailView
from IndexGrid import IndexGrid

class IndexDetailView(PictureReferenceDetailView):

    def __init__(self, panel, element):
        super(IndexDetailView, self).__init__(panel, element)

    def _FillPropertySizer(self):
        super(IndexDetailView, self)._FillPropertySizer()
        self.__grid = IndexGrid(self.main_panel, self)
        self._control_grid.Add(self.__grid, (3, 1), span = (1, 2))

    def GetLabelCategory(self):
        return 'INDEX'
