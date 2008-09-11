import wx
from TreePanel import TreePanel
from DetailPanel import DetailPanel

class Splitter(wx.SplitterWindow):
    def __init__(self, parent, ID):
        wx.SplitterWindow.__init__(self, parent, ID, style = wx.SP_LIVE_UPDATE)
        self.__tree_panel = TreePanel(self, style = wx.NO_BORDER)
        self.__detail_panel = DetailPanel(self, style = wx.SUNKEN_BORDER)
        self.SplitVertically(self.__tree_panel, self.__detail_panel, 150)
        self.SetMinimumPaneSize(10)

    def GetTreePanel(self):
        return self.__tree_panel
    tree_panel = property(GetTreePanel, None)

    def GetDetailPanel(self):
        return self.__detail_panel
    detail_panel = property(GetDetailPanel, None)

