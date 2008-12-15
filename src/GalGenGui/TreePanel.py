import wx
import App
from Tree import Tree
from Container import Container

class TreePanel(wx.Panel):

    def __init__(self, parent, style):
        wx.Panel.__init__(self, parent = parent, style = style)
        self.__InitTree()
        self.Bind(wx.EVT_SIZE, self.OnSize)

    def __InitTree(self):
        try:
            self.__tree = Tree(self,
                               -1,
                               wx.DefaultPosition,
                               wx.DefaultSize,
                               wx.TR_DEFAULT_STYLE)
            self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelChanged, self.__tree)
        except Exception,e:
            msg = str(e)
            print ('ERR: %s' % msg)

    def GetTree(self):
        return self.__tree

    def OnSize(self, event):
        w,h = self.GetClientSizeTuple()
        self.__tree.SetDimensions(0, 0, w, h)

    def OnSelChanged(self, event):
        item = event.GetItem()
        if item:
            element = self.__tree.GetPyData(item).element
            self.GetParent().detail_panel.Display(element)
            # notify frame
            self.GetParent().GetParent().OnTreeSelChanged(event)

    def Notify(self, event, observed):
         if event == Container.EVT_CHILD_ADDED or event == Container.EVT_CHILD_REMOVED:
            self.__tree.Populate()
