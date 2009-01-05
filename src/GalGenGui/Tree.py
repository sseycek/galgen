import wx
from GalGenLib.Core import Core
from GalGenLib.Picture import Picture
from TreeItem import TreeItem

class Tree(wx.TreeCtrl):
    def __init__(self, parent, id, pos, size, style):
        self.__root_id = None
        wx.TreeCtrl.__init__(self, parent, id, pos, size, style)
        img_size = (16,16)
        img_list = wx.ImageList(img_size[0], img_size[1])
        self.__folder_img = img_list.Add(wx.ArtProvider.GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, img_size))
        self.__folder_open_img = img_list.Add(wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_OTHER, img_size))
        self.__file_img = img_list.Add(wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, img_size))
        self.AssignImageList(img_list)
        self.Populate()

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
            item = TreeItem(self, project, self.__root_id)
            self.SetItemPyData(self.__root_id, item)
            self.SetItemImage(self.__root_id, self.__folder_img, wx.TreeItemIcon_Normal)
            self.SetItemImage(self.__root_id, self.__folder_open_img, wx.TreeItemIcon_Expanded)
            if selected_element == project:
                self.SelectItem(self.__root_id)
            self.__AddChildren(self.__root_id, selected_element)
        self.__RestoreExpansionState(self.__root_id)

    def __AddChildren(self, parent_id, selected_element):
        for child in self.GetItemPyData(parent_id).element.getChildren():
            child_id = self.AppendItem(parent_id, child.getName())
            item = TreeItem(self, child, child_id)
            self.SetItemPyData(child_id, item)
            if selected_element == child:
                self.SelectItem(child_id)
            if isinstance(child, Picture):
                self.SetItemImage(child_id, self.__file_img, wx.TreeItemIcon_Normal)
            else:
                self.SetItemImage(child_id, self.__folder_img, wx.TreeItemIcon_Normal)
                self.SetItemImage(child_id, self.__folder_open_img, wx.TreeItemIcon_Expanded)
                self.__AddChildren(child_id, selected_element)

    def OnCompareItems(self, item1, item2):
        item1_data = self.GetItemPyData(item1).element
        item2_data = self.GetItemPyData(item2).element
        if item1_data < item2_data: return -1
        if item1_data == item2_data: return 0
        return 1
