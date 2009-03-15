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
import App
from Tree import Tree
from TreeItem import TreeItem
from GalGenLib.Container import Container

class TreePanel(wx.Panel):

    def __init__(self, parent, style):
        self.__tree = None
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
            self.Bind(wx.EVT_TREE_ITEM_EXPANDED, self.OnItemExpanded, self.__tree)
            self.Bind(wx.EVT_TREE_ITEM_COLLAPSED, self.OnItemCollapsed, self.__tree)
        except Exception,e:
            msg = str(e)
            print ('ERR: %s' % msg)

    def GetTree(self):
        return self.__tree

    def OnSize(self, event):
        w,h = self.GetClientSizeTuple()
        if self.__tree:
            self.__tree.SetDimensions(0, 0, w, h)

    def OnSelChanged(self, event):
        item = event.GetItem()
        if item:
            element = self.__tree.GetPyData(item).element
            self.GetParent().detail_panel.Display(element)
            # notify frame
            self.GetParent().GetParent().OnTreeSelChanged(event)

    def OnItemExpanded(self, event):
        item = event.GetItem()
        if item:
            element = self.__tree.GetPyData(item).element
            element.setGuiProperty(TreeItem.property_expanded, True)

    def OnItemCollapsed(self, event):
        item = event.GetItem()
        if item:
            element = self.__tree.GetPyData(item).element
            element.setGuiProperty(TreeItem.property_expanded, False)

    def Notify(self, event, observed):
         if event == Container.EVT_CHILD_ADDED or event == Container.EVT_CHILD_REMOVED:
            self.__tree.Populate(observed)
