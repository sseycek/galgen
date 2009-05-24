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

import os
import shutil
import time
import wx
import codecs
from GalGenLib import Globals
from GalGenLib.Core import Core
from GalGenLib.Project import Project
from GalGenLib.Gallery import Gallery
from GalGenLib.Album import Album
from GalGenLib.Picture import Picture
from GalGenLib.CustomContentPage import CustomContentPage
from Splitter import *
from GenerationProgressDialog import GenerationProgressDialog

class Frame(wx.Frame):
    WX_ID_THIS_FRAME = 100
    WX_ID_FILE_MENU_NEW = 201
    WX_ID_FILE_MENU_OPEN = 202
    WX_ID_FILE_MENU_SAVE = 203
    WX_ID_FILE_MENU_GENERATE = 204
    WX_ID_FILE_MENU_EXIT = 210
    WX_ID_EDIT_MENU_ADD = 301
    WX_ID_EDIT_MENU_ADD_CUSTOM = 302
    WX_ID_EDIT_MENU_ADD_HIGHRES = 303
    WX_ID_EDIT_MENU_REMOVE = 304
    WX_ID_HELP_MENU_ABOUT = 401

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title, (0,0), (1024,700))
        self.__InitMenu()
        self.__InitStatusBar()
        self.__InitToolBar()
        self.__InitSplitter()
        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def __InitMenu(self):
        self.__menu_file = wx.Menu()
        self.__menu_file.Append(Frame.WX_ID_FILE_MENU_NEW, '&New\tCTRL+N')
        self.__menu_file.Append(Frame.WX_ID_FILE_MENU_OPEN, '&Open\tCTRL+O')
        self.__menu_file.Append(Frame.WX_ID_FILE_MENU_SAVE, '&Save\tCTRL+S')
        self.__menu_file.Append(Frame.WX_ID_FILE_MENU_GENERATE, '&Generate\tCTRL+G')
        self.__menu_file.AppendSeparator()
        self.__menu_file.Append(Frame.WX_ID_FILE_MENU_EXIT, 'E&xit\tCTRL+Q')
        self.__menu_edit = wx.Menu()
        self.__menu_edit_add = self.__menu_edit.Append(Frame.WX_ID_EDIT_MENU_ADD, '&Add\tCTRL+INS')
        self.__menu_edit_add_custom = self.__menu_edit.Append(Frame.WX_ID_EDIT_MENU_ADD_CUSTOM, '&Add custom page\tCTRL+SHIFT+INS')
        self.__menu_edit_add_highres = self.__menu_edit.Append(Frame.WX_ID_EDIT_MENU_ADD_HIGHRES, '&Add highres pictures ...\tCTRL+H')
        self.__menu_edit_remove = self.__menu_edit.Append(Frame.WX_ID_EDIT_MENU_REMOVE, '&Remove\tCTRL+DEL')
        self.__menu_help = wx.Menu()
        self.__menu_help.Append(Frame.WX_ID_HELP_MENU_ABOUT, '&About ...\tF1')
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
        self.Bind(wx.EVT_MENU, self.OnEditAddCustom, id=Frame.WX_ID_EDIT_MENU_ADD_CUSTOM)
        self.Bind(wx.EVT_MENU, self.OnEditAddHighres, id=Frame.WX_ID_EDIT_MENU_ADD_HIGHRES)
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

    def OnClose(self, event):
        if Core.getInstance().project and Core.getInstance().project.modified:
            dlg = wx.MessageDialog(self,
                                   '%s has been modified. Shall it be saved?' % Core.getInstance().project.name,
                                   'Quitting' ,
                                   wx.YES_NO | wx.YES_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION)
            ret = dlg.ShowModal()
            if ret == wx.ID_YES:
                self.OnSaveProject(None)
                self.Destroy()
            elif ret == wx.ID_NO:
                self.Destroy()
            else:
                pass
        else:
            self.Destroy()

    def OnAbout(self, event):
        license = ''' Copyright (c) 2009 Stepan Seycek. All rights reserved.
 
 Redistribution and use in source and binary forms, with or 
 without modification, are permitted provided that the following 
 conditions are met:
 
  1. Redistributions of source code must retain the above 
     copyright notice, this list of conditions and the 
     following disclaimer.
  2. Redistributions in binary form must reproduce the above 
     copyright notice, this list of conditions and the following 
     disclaimer in the documentation and/or other materials 
     provided with the distribution.
  3. All advertising materials mentioning features or use of this 
     software must display the following acknowledgement: 
     "This product includes software developed by Stepan Seycek."
  4. The name Stepan Seycek may not be used to endorse or promote 
     products derived from this software without specific prior 
     written permission. 

 THIS SOFTWARE IS PROVIDED "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, 
 INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY 
 AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL 
 THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, 
 EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, 
 PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; 
 OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
 WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
 OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED 
 OF THE POSSIBILITY OF SUCH DAMAGE. 
'''
        wx.MessageBox('%s\n\n%s\n\n%s' %
                      ('This is an application or creating photo gallery sites.',
                       'File tickets under https://galgen.seycek.net/', license),
        'About %s' % Globals.ProgName, wx.OK | wx.ICON_INFORMATION, self)

    def OnEditAdd(self, event):
        tree_item_id = self.__GetTree().GetSelection()
        element = self.__GetTree().GetPyData(tree_item_id).element
        if isinstance(element, Project):
            element.addChild(Gallery('Gallery', '', '', '', ''))
        elif isinstance(element, Gallery):
            element.addChild(Album('Album', '', '', '', '', ''))
        elif isinstance(element, Album):
            element.addChild(Picture('Picture', '', '', '', '', '', '', ''))
        else:
            raise Exception, 'Don\'t know what to add'

    def OnEditAddCustom(self, event):
        tree_item_id = self.__GetTree().GetSelection()
        element = self.__GetTree().GetPyData(tree_item_id).element
        if isinstance(element, Project):
            element.addChild(CustomContentPage('Custom page', '', '', '', '', '', ''))
        else:
            raise Exception, 'custom content pages only supported as direct child entries of project'

    def OnEditAddHighres(self, event):
        tree_item_id = self.__GetTree().GetSelection()
        element = self.__GetTree().GetPyData(tree_item_id).element
        if isinstance(element, Album):
            dlg = wx.DirDialog(self, "Highrs picture directory:", style = wx.DD_DEFAULT_STYLE)
            if dlg.ShowModal() == wx.ID_OK:
                dir = dlg.GetPath()
                for pic in element.children:
                    if os.path.lexists(os.path.join(dir, pic.pic_file_name)):
                        pic.highres_location = os.path.join(dir, pic.pic_file_name);
        else:
            raise Exception, 'hirhres pictures can only be added to album'

    def OnEditRemove(self, event):
        tree_item_id = self.__GetTree().GetSelection()
        element = self.__GetTree().GetPyData(tree_item_id).element
        element.parent.removeChild(element)

    def OnOpenProject(self, event):
        if Core.getInstance().project and Core.getInstance().project.modified:
            wx.MessageBox('%s has changes - save or close it' % Core.getInstance().project.name, 'Open project', wx.OK | wx.ICON_ERROR, self)
        else:
            dlg = wx.FileDialog(self,
                                message="Choose a file",
                                defaultDir=os.getcwd(),
                                defaultFile="",
                                wildcard="GalGen project file (*.ggp)|*.ggp|All files (*.*)|*.*",
                                style=wx.OPEN | wx.CHANGE_DIR)
            if dlg.ShowModal() == wx.ID_OK:
                Core.getInstance().project = Project(dlg.GetPath())
                Core.getInstance().project.load()
                self.__GetTree().Populate()

    def __CreateBackup(self, filename):
        if os.path.exists(filename):
            backup_filename = '%s.bak.%d' % (filename, int(time.time() * 100))
            shutil.copyfile(filename, backup_filename)

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
            self.__CreateBackup(Core.getInstance().project.filename)
            fd = codecs.open(Core.getInstance().project.filename, 'w', 'utf-8')
            Core.getInstance().project.save(fd)
            fd.close()

    def OnGenerateOutput(self, event):
        project = Core.getInstance().project
        if not project:
            wx.MessageBox('Nothing to generate', 'Save project', wx.OK | wx.ICON_INFORMATION, self)
        else:
            target_dir_path = self.__GetTargetDir()
            if target_dir_path: #and not os.listdir(target_dir_path):
                progress_dialog = GenerationProgressDialog(project.getPageCount(), self)
                try:
                    generated = project.generateOutput(target_dir_path, progress_dialog, 0)
                    if generated != project.getPageCount():
                        raise Exception, 'Unexpected: generated %d pages, while expected to generate %d' % (generated, project.getPageCount())
                except:
                    progress_dialog.destroy()
                    raise
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
                self.__menu_edit_add.SetText('&Add gallery\tCTRL+INS')
                self.__menu_edit_add.Enable(True)
                self.__menu_edit_add_custom.Enable(True)
                self.__menu_edit_add_highres.Enable(False)
                self.__menu_edit_remove.SetText('&Remove\tCTRL+DEL')
                self.__menu_edit_remove.Enable(False)
            elif isinstance(element, Gallery):
                self.__menu_edit_add.SetText('&Add album\tCTRL+INS')
                self.__menu_edit_add.Enable(True)
                self.__menu_edit_add_custom.Enable(False)
                self.__menu_edit_add_highres.Enable(False)
                self.__menu_edit_remove.SetText('&Remove gallery\tCTRL+DEL')
                self.__menu_edit_remove.Enable(True)
            elif isinstance(element, Album):
                self.__menu_edit_add.SetText('&Add picture\tCTRL+INS')
                self.__menu_edit_add.Enable(True)
                self.__menu_edit_add_custom.Enable(False)
                self.__menu_edit_add_highres.Enable(True)
                self.__menu_edit_remove.SetText('&Remove album\tCTRL+DEL')
                self.__menu_edit_remove.Enable(True)
            elif isinstance(element, Picture):
                self.__menu_edit_add.Enable(False)
                self.__menu_edit_add.SetText('&Add\tCTRL+INS')
                self.__menu_edit_add_custom.Enable(False)
                self.__menu_edit_add_highres.Enable(False)
                self.__menu_edit_remove.SetText('&Remove picture\tCTRL+DEL')
                self.__menu_edit_remove.Enable(True)
            elif isinstance(element, CustomContentPage):
                self.__menu_edit_add.Enable(False)
                self.__menu_edit_add.SetText('&Add\tCTRL+INS')
                self.__menu_edit_add_custom.Enable(False)
                self.__menu_edit_add_highres.Enable(False)
                self.__menu_edit_remove.SetText('&Remove custom page\tCTRL+DEL')
                self.__menu_edit_remove.Enable(True)
            else: raise Exception, 'unknown element type' 
