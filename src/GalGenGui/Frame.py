import os
import wx
from GalGenLib import Globals
from GalGenLib.Core import Core
from GalGenLib.Project import Project
from GalGenLib.Gallery import Gallery
from GalGenLib.Album import Album
from GalGenLib.Picture import Picture
from Splitter import *

class Frame(wx.Frame):
    WX_ID_THIS_FRAME = 100
    WX_ID_FILE_MENU_NEW = 201
    WX_ID_FILE_MENU_OPEN = 202
    WX_ID_FILE_MENU_SAVE = 203
    WX_ID_FILE_MENU_GENERATE = 204
    WX_ID_FILE_MENU_EXIT = 210
    WX_ID_EDIT_MENU_ADD = 301
    WX_ID_EDIT_MENU_REMOVE = 302
    WX_ID_HELP_MENU_ABOUT = 401

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title)
        self.__InitMenu()
        self.__InitStatusBar()
        self.__InitToolBar()
        self.__InitSplitter()

    def __InitMenu(self):
        self.__menu_file = wx.Menu()
        self.__menu_file.Append(Frame.WX_ID_FILE_MENU_NEW, '&New\tCTRL+N')
        self.__menu_file.Append(Frame.WX_ID_FILE_MENU_OPEN, '&Open\tCTRL+O')
        self.__menu_file.Append(Frame.WX_ID_FILE_MENU_SAVE, '&Save\tCTRL+S')
        self.__menu_file.Append(Frame.WX_ID_FILE_MENU_GENERATE, '&Generate\tCTRL+G')
        self.__menu_file.AppendSeparator()
        self.__menu_file.Append(Frame.WX_ID_FILE_MENU_EXIT, 'E&xit\tCTRL+Q')
        self.__menu_edit = wx.Menu()
        self.__menu_edit.Append(Frame.WX_ID_EDIT_MENU_ADD, '&Add...\tINS')
        self.__menu_edit.Append(Frame.WX_ID_EDIT_MENU_REMOVE, '&Remove\tDEL')
        self.__menu_help = wx.Menu()
        self.__menu_help.Append(Frame.WX_ID_HELP_MENU_ABOUT, '&About...\tF1')
        self.__menu_bar = wx.MenuBar()
        self.__menu_bar.Append(self.__menu_file, '&File')
        self.__menu_bar.Append(self.__menu_edit, '&Edit')
        self.__menu_bar.Append(self.__menu_help, '&Help')
        self.SetMenuBar(self.__menu_bar)
        self.Bind(wx.EVT_MENU, self.OnNewProject, id=Frame.WX_ID_FILE_MENU_NEW)
        self.Bind(wx.EVT_MENU, self.OnOpenProject, id=Frame.WX_ID_FILE_MENU_OPEN)
        self.Bind(wx.EVT_MENU, self.OnSaveProject, id=Frame.WX_ID_FILE_MENU_SAVE)
        self.Bind(wx.EVT_MENU, self.OnGenerateOutput, id=Frame.WX_ID_FILE_MENU_GENERATE)
        self.Bind(wx.EVT_MENU, self.OnEditAdd, id=Frame.WX_ID_EDIT_MENU_ADD)
        self.Bind(wx.EVT_MENU, self.OnEditRemove, id=Frame.WX_ID_EDIT_MENU_REMOVE)
        self.Bind(wx.EVT_MENU, self.OnAbout, id=Frame.WX_ID_HELP_MENU_ABOUT)
        self.Bind(wx.EVT_MENU, self.OnQuit, id=Frame.WX_ID_FILE_MENU_EXIT)

    def __InitStatusBar(self):
        self.CreateStatusBar()
        self.SetStatusText('Hallo!');

    def __InitToolBar(self):
        icon_size = (16, 16)
        self.__toolbar = self.CreateToolBar()
        self.__toolbar.SetToolBitmapSize(icon_size)
        new_ico = wx.ArtProvider.GetBitmap(wx.ART_NEW, wx.ART_TOOLBAR, icon_size)
        new_proj_tool = self.__toolbar.AddSimpleTool(wx.ID_ANY, new_ico, "New project", "Creates new project")
        self.Bind(wx.EVT_MENU, self.OnNewProject, new_proj_tool)
        open_ico = wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_TOOLBAR, icon_size)
        open_tool = self.__toolbar.AddSimpleTool(wx.ID_ANY, open_ico, "Open project", "Opens project")
        self.Bind(wx.EVT_MENU, self.OnOpenProject, open_tool)
        save_ico = wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE, wx.ART_TOOLBAR, icon_size)
        save_tool = self.__toolbar.AddSimpleTool(wx.ID_ANY, save_ico, "Save project", "Saves project")
        self.Bind(wx.EVT_MENU, self.OnSaveProject, save_tool)
        self.__toolbar.AddSeparator()
        gen_ico = wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE_AS, wx.ART_TOOLBAR, icon_size)
        gen_tool = self.__toolbar.AddSimpleTool(wx.ID_ANY, gen_ico, "Generate", "Generates XHTML Output")
        self.Bind(wx.EVT_MENU, self.OnGenerateOutput, gen_tool)
        self.__toolbar.Realize()

    def __InitSplitter(self):
        self.__splitter = Splitter(self, - 1)

    def __GetTree(self):
        return self.__splitter.GetTreePanel().GetTree()

    def OnQuit(self, event):
        self.Close()

    def OnAbout(self, event):
        wx.MessageBox('This is an application or creating photo gallery sites.',
        'About %s' % Globals.ProgName, wx.OK | wx.ICON_INFORMATION, self)

    def OnEditAdd(self, event):
        tree_item_id = self.__GetTree().GetSelection()
        element = self.__GetTree().GetPyData(tree_item_id).element
        if isinstance(element, Project):
            element.addChild(Gallery('Gallery', '', ''))
        elif isinstance(element, Gallery):
            element.addChild(Album('Album', '', ''))
        elif isinstance(element, Album):
            element.addChild(Picture('Picture', '', ''))
        else:
            raise Exception, 'Don\'t know what to add'

    def OnEditRemove(self, event):
        tree_item_id = self.__GetTree().GetSelection()
        element = self.__GetTree().GetPyData(tree_item_id).element
        element.parent.removeChild(element)

    def OnOpenProject(self, event):
        dlg = wx.FileDialog(self,
                            message="Choose a file",
                            defaultDir=os.getcwd(),
                            defaultFile="",
                            wildcard="GalGen project file (*.ggp)|*.ggp|All files (*.*)|*.*",
                            style=wx.OPEN | wx.CHANGE_DIR)
        if dlg.ShowModal() == wx.ID_OK:
            if Core.getInstance().project and Core.getInstance().project.modified:
                wx.MessageBox('%s has changes - save or close it' % Core.getInstance().project.name, 'Open project', wx.OK | wx.ICON_INFORMATION, self)
            Core.getInstance().project = Project(dlg.GetPath())
            Core.getInstance().project.load()
            self.__GetTree().Populate()

    def OnSaveProject(self, event):
        if not Core.getInstance().project:
            wx.MessageBox('Nothing to save', 'Save project', wx.OK | wx.ICON_INFORMATION, self)
        else:
            if not Core.getInstance().project.filename:
                dlg = wx.FileDialog(self,
                                    message="Choose a file",
                                    defaultDir=os.getcwd(),
                                    defaultFile="",
                                    wildcard="GalGen project file (*.ggp)|*.ggp|All files (*.*)|*.*",
                                    style=wx.SAVE | wx.CHANGE_DIR)
                if dlg.ShowModal() != wx.ID_OK: return
                Core.getInstance().project.filename = dlg.GetPath()
            fd = open(Core.getInstance().project.filename, 'w')
            Core.getInstance().project.save(fd)
            fd.close()

    def OnGenerateOutput(self, event):
        project = Core.getInstance().project
        if not project:
            wx.MessageBox('Nothing to generate', 'Save project', wx.OK | wx.ICON_INFORMATION, self)
        else:
            target_dir_path = self.__GetTargetDir()
            if target_dir_path: #and not os.listdir(target_dir_path):
                print 'Generating output into %s ...' % target_dir_path 
                project.generateOutput(target_dir_path)
            else:
                dlg = wx.MessageDialog(self, 'You have to select an empty target directory!',
                                       'Generate output',
                                       wx.OK | wx.ICON_ERROR)
                dlg.ShowModal()

    def __GetTargetDir(self):
        ret = None
        dlg = wx.DirDialog(self, "Target directory:", style = wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            ret = dlg.GetPath()
        return ret

    def OnNewProject(self, event):
        if Core.getInstance().project:
            wx.MessageBox('There already is a project (%s)' % Core.getInstance().project.name, 'New project', wx.OK | wx.ICON_INFORMATION, self)
        else:
            Core.getInstance().project = Project()
            Core.getInstance().project.name = 'New project'
            self.__GetTree().Populate()

    def OnTreeSelChanged(self, event):
        item = event.GetItem()
        if item:
            element = self.__GetTree().GetPyData(item).element
            if isinstance(element, Project):
                self.__menu_edit.Enable(Frame.WX_ID_EDIT_MENU_ADD, True)
                self.__menu_edit.Enable(Frame.WX_ID_EDIT_MENU_REMOVE, False)
            elif isinstance(element, Picture):
                self.__menu_edit.Enable(Frame.WX_ID_EDIT_MENU_ADD, False)
                self.__menu_edit.Enable(Frame.WX_ID_EDIT_MENU_REMOVE, True)
            else:
                self.__menu_edit.Enable(Frame.WX_ID_EDIT_MENU_ADD, True)
                self.__menu_edit.Enable(Frame.WX_ID_EDIT_MENU_REMOVE, True)
        
