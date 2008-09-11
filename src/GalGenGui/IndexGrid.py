import wx
from wx.grid import Grid as wxGrid
from wx.lib.anchors import LayoutAnchors
from GalGenLib.Index import Index

class IndexGrid(wxGrid):

    def __init__(self, parent, view):
        wxGrid.__init__(self, parent, -1)
        self.__view = view
        self.__CreateGrid()

    def __FillWithContent(self):
        row = 0
        for element in self.__view.element.getChildren():
            self.SetCellValue(row, 0, element.name)
            self.SetCellValue(row, 1, element.pic_location)
            row += 1

    def __CreateGrid(self):
        index = self.__view.element
        row_count = len(index.getChildren())
        self.CreateGrid(row_count, 2)
        self.SetConstraints(LayoutAnchors(self, 1, 1, 1, 1))
        self.SetColLabelValue(0, 'Name')
        self.SetColLabelValue(1, 'Image location')
        self.__FillWithContent()

