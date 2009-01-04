import os
import shutil
from ProjectXMLParser import ProjectXMLParser
from Logging import *
from CustomContentReference import CustomContentReference
from Container import Container
from Modifyable import Modifyable
from ProjectHTMLOutputter import ProjectHTMLOutputter
import Globals

class Project(CustomContentReference, Container, Modifyable):
    parent = None

    def __init__(self, filename = '', name = '', template = '', style_directory = '',
                 menu_id = '', title = '', subtitle = '', html_location = '', supplemental_dir = ''):
        CustomContentReference.__init__(self, name, menu_id, title, subtitle, html_location, supplemental_dir)
        Container.__init__(self)
        Modifyable.__init__(self)
        self.__filename = filename
        self.__top_level_indexes = []
        self.__xhtml_template = template
        self.__style_directory = style_directory

    def SetFilename(self, filename):
        self.__filename = filename

    def GetFilename(self):
        return self.__filename

    filename = property(GetFilename, SetFilename)

    def SetXhtmlTemplate(self, template):
        self.__xhtml_template = template

    def GetXhtmlTemplate(self):
        return self.__xhtml_template

    xhtml_template = property(GetXhtmlTemplate, SetXhtmlTemplate)

    def SetStyleDirectory(self, dir):
        self.__style_directory = dir

    def GetStyleDirectory(self):
        return self.__style_directory

    style_directory = property(GetStyleDirectory, SetStyleDirectory)

    def _getHtmlPath(self):
        return 'index.html'

    def load(self):
        if not self.__filename:
            raise 'No filename provided for loading project'
        parser = ProjectXMLParser(self.__filename)
        parser.parse(self)

    def save(self, stream):
        self.__writeHeader(stream)
        self.__writeStartTag(stream)
        children = self.getChildren()
        for child in children:
            child.save(stream)
        self.__writeEndTag(stream)

    def __writeHeader(self, stream):
        stream.write(u'<?xml version="1.0" encoding="UTF-8"?>\n')

    def __writeStartTag(self, stream):
        stream.write(u'<project\n %s="%s"\n %s="%s"\n %s="%s"\n %s="%s"\n %s="%s"\n %s="%s"\n %s="%s"\n %s="%s"\n %s="%s">\n' %
                     ('name', self.name,
                      'galgen-version', Globals.ProgVersion,
                      'xhtml-template', self.__xhtml_template,
                      'style-directory', self.__style_directory,
                      'menu-id', self.menu_id,
                      'title', self.title,
                      'subtitle', self.subtitle,
                      'html-location', self.html_location,
                      'supplemental-dir', self.supplemental_dir))

    def __writeEndTag(self, stream):
        stream.write(u'</project>\n')

    def generateOutput(self, target_dir, progress_updater, page_index):
        page_index += 1
        progress_updater.update(page_index, '%s: %s' % (self.__class__.__name__, self.name))
        if os.path.exists(self.style_directory):
            shutil.copytree(self.style_directory, os.path.join(target_dir, 'style'))
        else:
            raise Exception, 'Style directory not found'
        outputter = ProjectHTMLOutputter(self)
        return outputter.generateOutput(target_dir, progress_updater, page_index)

    def __getMenuIdHrefMappingRecoursive(self, element, level, ret):
        if isinstance(element, Container):
            for child in element.children:
                if child.menu_id:
                    ret.append((child.menu_id, '%s%s' % (level * '../', child._getHtmlPath())))
                self.__getMenuIdHrefMappingRecoursive(child, level, ret)

    def getMenuIdHrefMapping(self, level):
        ret = []
        self.__getMenuIdHrefMappingRecoursive(self, level, ret)
        return ret

    def __recursiveGetPageCount(self, element, count):
        count +=1
        if isinstance(element, Container):
            for child in element.children:
                count = self.__recursiveGetPageCount(child, count)
        return count
    
    def getPageCount(self):
        return self.__recursiveGetPageCount(self, 0)

