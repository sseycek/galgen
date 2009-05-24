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
from ProjectXMLParser import ProjectXMLParser
from Logging import *
from CustomContentReference import CustomContentReference
from Container import Container
from Modifyable import Modifyable
from ProjectHTMLOutputter import ProjectHTMLOutputter
from XmlUtils import asXmlAttribute
import Globals

class Project(CustomContentReference, Container, Modifyable):
    parent = None

    def __init__(self, filename = '', name = '', template = '', style_directory = '',
                 menu_id = '', title = '', subtitle = '', html_location = '', supplemental_dir = '', description=''):
        CustomContentReference.__init__(self, name, menu_id, title, subtitle, html_location, supplemental_dir, description)
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
        self.modified = False

    def save(self, stream):
        self.__writeHeader(stream)
        self.__writeStartTag(stream)
        children = self.getChildren()
        for child in children:
            child.save(stream)
        self.__writeEndTag(stream)
        self.modified = False

    def __writeHeader(self, stream):
        stream.write(u'<?xml version="1.0" encoding="UTF-8"?>\n')

    def __writeStartTag(self, stream):
        stream.write(u'<project\n %s="%s"\n %s="%s"\n %s="%s"\n %s="%s"\n %s="%s"\n %s="%s"\n %s="%s"\n %s="%s"\n %s="%s">\n' %
                     ('name', asXmlAttribute(self.name),
                      'galgen-version', asXmlAttribute(Globals.ProgVersion),
                      'xhtml-template', asXmlAttribute(self.__xhtml_template),
                      'style-directory', asXmlAttribute(self.__style_directory),
                      'menu-id', asXmlAttribute(self.menu_id),
                      'title', asXmlAttribute(self.title),
                      'subtitle', asXmlAttribute(self.subtitle),
                      'html-location', asXmlAttribute(self.html_location),
                      'supplemental-dir', asXmlAttribute(self.supplemental_dir)))

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

