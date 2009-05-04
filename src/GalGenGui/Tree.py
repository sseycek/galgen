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
from GalGenLib.Core import Core
from GalGenLib.Picture import Picture
from GalGenLib.Album import Album
from GalGenLib.Gallery import Gallery
from GalGenLib.CustomContentPage import CustomContentPage
from TreeItem import TreeItem
from PictureOnTreeDropTarget import PictureOnTreeDropTarget

class Tree(wx.TreeCtrl):
    def __init__(self, parent, id, pos, size, style):
        self.__root_id = None
        wx.TreeCtrl.__init__(self, parent, id, pos, size, style)
        img_size = (16,16)
        img_list = wx.ImageList(img_size[0], img_size[1])
        self.__folder_img = img_list.Add(wx.ArtProvider.GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, img_size))
        self.__folder_open_img = img_list.Add(wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_OTHER, img_size))
        self.__file_img = img_list.Add(wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, img_size))
        self.__object_to_id = {}
        self.AssignImageList(img_list)
        self.Populate()
        dt = PictureOnTreeDropTarget(self)
        self.SetDropTarget(dt)
        self.drag_item = None
        self.Bind(wx.EVT_TREE_BEGIN_DRAG, self.OnBeginDrag)
        self.Bind(wx.EVT_TREE_END_DRAG, self.OnEndDrag)


    def __RestoreExpansionState(self, item_id):
        if item_id and item_id.IsOk():
            element = self.GetItemPyData(item_id).element
            if element.getGuiProperty(TreeItem.property_expanded):
                self.Expand(item_id)
            child, child_cookie = self.GetFirstChild(item_id)
            while child.IsOk():
                self.__RestoreExpansionState(child)
                child, child_cookie = self.GetNextChild(item_id, child_cookie)

    def __UnsubscribeObservers(self, item_id):
        if item_id and item_id.IsOk():
            tree_item = self.GetItemPyData(item_id)
            tree_item.Unsubscribe()
            child, child_cookie = self.GetFirstChild(item_id)
            while child.IsOk():
                self.__UnsubscribeObservers(child)
                child, child_cookie = self.GetNextChild(item_id, child_cookie)
    
    def Populate(self, selected_element = None):
        if not selected_element:
            selection = self.GetSelection()
            if selection.IsOk():
                selected_element = self.GetItemPyData(selection).element
        if self.__root_id:
            self.__UnsubscribeObservers(self.__root_id)
        self.DeleteAllItems()
        project = Core.getInstance().project
        if project:
            self.__root_id = self.AddRoot(project.name)
            self.__object_to_id[project] = self.__root_id
            item = TreeItem(self, project, self.__root_id)
            self.SetItemPyData(self.__root_id, item)
            self.SetItemImage(self.__root_id, self.__folder_img, wx.TreeItemIcon_Normal)
            self.SetItemImage(self.__root_id, self.__folder_open_img, wx.TreeItemIcon_Expanded)
            self.__AddChildren(self.__root_id)
        self.__RestoreExpansionState(self.__root_id)
        if selected_element:
            self.SelectItem(self.__object_to_id[selected_element])

    def __AddChild(self, parent, parent_id, child, index = -1):
        if index >= 0:
            child_id = self.InsertItemBefore(parent_id, index, child.getName())
        else:
            child_id = self.AppendItem(parent_id, child.getName())
        self.__object_to_id[child] = child_id
        item = TreeItem(self, child, child_id)
        self.SetItemPyData(child_id, item)
        if isinstance(child, Picture) or isinstance(child, CustomContentPage):
            self.SetItemImage(child_id, self.__file_img, wx.TreeItemIcon_Normal)
        else:
            self.SetItemImage(child_id, self.__folder_img, wx.TreeItemIcon_Normal)
            self.SetItemImage(child_id, self.__folder_open_img, wx.TreeItemIcon_Expanded)
            self.__AddChildren(child_id)
    
    def __AddChildren(self, parent_id):
        parent = self.GetItemPyData(parent_id).element
        for child in parent.getChildren():
            self.__AddChild(parent, parent_id, child)
            
    def OnCompareItems(self, item1, item2):
        item1_data = self.GetItemPyData(item1).element
        item2_data = self.GetItemPyData(item2).element
        if item1_data < item2_data: return -1
        if item1_data == item2_data: return 0
        return 1

    def OnBeginDrag(self, event):
        item = event.GetItem()
        if item:
            element = self.GetPyData(item).element
            if isinstance(element, Picture) or \
            isinstance(element, Album) or \
            isinstance(element, Gallery):
                event.Allow()
                self.drag_item = element

    def OnEndDrag(self, event):
        if not event.GetItem().IsOk():
            return
        item = event.GetItem()
        if item and self.drag_item:
            drop_item = self.GetPyData(item).element
            if isinstance(self.drag_item, Picture) and isinstance(drop_item, Picture) or \
            isinstance(self.drag_item, Album) and isinstance(drop_item, Album) or \
            isinstance(self.drag_item, Gallery) and isinstance(drop_item, Gallery):
                self.MoveItemBeforeItem(self.drag_item, drop_item)
            elif isinstance(self.drag_item, Picture) and isinstance(drop_item, Album) or \
            isinstance(self.drag_item, Album) and isinstance(drop_item, Gallery):
                self.MoveItemToContainer(self.drag_item, drop_item)
            self.drag_item = None

    def MoveItemBeforeItem(self, drag_item, drop_item):
        if drag_item != drop_item and \
        drag_item != drop_item.getPrevious():
            drag_item.parent.removeChild(drag_item)
            drop_item.parent.addChildBeforeChild(drag_item, drop_item)
            
    def MoveItemToContainer(self, drag_item, drop_item):
            drag_item.parent.removeChild(drag_item)
            drop_item.addChild(drag_item)
        
    def OnItemAdded(self, parent, child, selected):
        index = parent.getIndex(child)
        self.__AddChild(parent, self.__object_to_id[parent], child, index)
        self.SelectItem(self.__object_to_id[selected])

    def OnItemRemoved(self, parent, child, selected):
        self.Delete(self.__object_to_id[child])
        self.SelectItem(self.__object_to_id[selected])
        del(self.__object_to_id[child])
        