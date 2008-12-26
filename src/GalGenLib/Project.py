import os
import shutil
from ProjectXMLParser import ProjectXMLParser
from Logging import *
from NamedObject import NamedObject
from Container import Container
from Modifyable import Modifyable
from ProjectHTMLOutputter import ProjectHTMLOutputter
import Globals

class Project(NamedObject, Container, Modifyable):

    def __init__(self, filename = '', name = '', template = '', style_directory = '',
                 menu_id = '', title = '', subtitle = ''):
        NamedObject.__init__(self, name, menu_id, title, subtitle)
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
        stream.write(u'<project\n %s="%s"\n %s="%s"\n %s="%s"\n %s="%s"\n %s="%s"\n %s="%s"\n %s="%s">\n' %
                     ('name', self.name,
                      'galgen-version', Globals.ProgVersion,
                      'xhtml-template', self.__xhtml_template,
                      'style-directory', self.__style_directory,
                      'menu-id', self.menu_id,
                      'title', self.title,
                      'subtitle', self.subtitle))

    def __writeEndTag(self, stream):
        stream.write(u'</project>\n')

    def generateOutput(self, target_dir):
        if os.path.exists(self.style_directory):
            shutil.copytree(self.style_directory, os.path.join(target_dir, 'style'))
        else:
            raise Exception, 'Style directory not found'
        outputter = ProjectHTMLOutputter(self)
        outputter.generateOutput(target_dir)

    def getMenuIdHrefMapping(self, level):
        ret = []
        for gal in self.children:
            if gal.menu_id:
                ret.append((gal.menu_id, '%s%s/index.html' % (level * '../', gal.name)))
        return ret