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

import xml.sax
from Logging import *
from Album import Album
from Gallery import Gallery
from Picture import Picture
from CustomContentPage import CustomContentPage

class ProjectXMLParser(xml.sax.handler.ContentHandler):

    def __init__(self, filename):
        self.__filename = filename
        self.__top_level_indexes = []
        self.__element_stack = []
        self.__ignore_levels = 0

    def parse(self, project):
        if not self.__filename:
            raise 'XML filename not given'
        self.__project = project
        parser = xml.sax.make_parser()
        parser.setContentHandler(self)
        try:
            parser.parse(self.__filename)
        except Exception, e:
            msg = 'Error occured during parsing of project XML: %s' % str(e)
            logError(msg)
            raise e

    def startElement(self, name, attributes):
        if self.__ignore_levels:
            self.__ignore_levels += 1
        elif name == "project":
            self.__startElementProject(attributes)
        elif name == "gallery":
            self.__startElementGallery(attributes)
        elif name == "album":
            self.__startElementAlbum(attributes)
        elif name == "picture":
            self.__startElementPicture(attributes)
        elif name == "customcontent":
            self.__startElementCustomContentPage(attributes)
        else:
            logError('Unknown XML tag: %s' % name)
            self.__ignore_levels += 1

    def __startElementProject(self, attributes):
        # logDebug('startElementProject called for "%s"' % attributes['name'])
        self.__project.name = attributes['name']
        self.__project.html_location = attributes['html-location']
        self.__project.supplemental_dir = attributes['supplemental-dir']
        self.__project.xhtml_template = attributes['xhtml-template']
        self.__project.style_directory = attributes['style-directory']
        self.__project.menu_id = attributes['menu-id']
        self.__project.title = attributes['title']
        self.__project.subtitle = attributes['subtitle']
        if self.__element_stack:
            raise 'Unexpected - deserialising project, while there are already elements on the stack'
        self.__element_stack.append(self.__project)

    def __startElementGallery(self, attributes):
        # logDebug('startElementGallery called for "%s"' % attributes['name'])
        if not self.__element_stack:
            raise 'Unexpected - deserialising gallery, while there is no project on the stack yet'
        print attributes
        description = ''
        if 'description' in attributes: 
            description = attributes['description']
        gallery = Gallery(attributes['name'], attributes['menu-id'], attributes['title'], attributes['subtitle'], description)
        self.__element_stack.append(gallery)

    def __startElementAlbum(self, attributes):
        # logDebug('startElementAlbum called for "%s"' % attributes['name'])
        if not self.__element_stack:
            raise 'Unexpected - deserialising album, while there is no project on the stack yet'
        description = ''
        if 'description' in attributes: 
            description = attributes['description']
        album = Album(attributes['name'], attributes['pic'], attributes['menu-id'], attributes['title'], attributes['subtitle'], description)
        self.__element_stack.append(album)

    def __startElementPicture(self, attributes):
        # logDebug('startElementPicture called for "%s" located at "%s"' % (attributes['name'], attributes['location']))
        if len(self.__element_stack) < 2:
            raise 'Unexpected - deserialising picture, while there is no index on the stack yet'
        # make these optional for compatibility
        highres_location = ''
        if 'highres-location' in attributes:
            highres_location = attributes['highres-location']
        description = ''
        if 'description' in attributes: 
            description = attributes['description']
        exif = ''
        if 'exif' in attributes: 
            exif = attributes['exif']
        picture = Picture(attributes['name'], attributes['location'], highres_location, attributes['menu-id'], attributes['title'], attributes['subtitle'], description, exif)
        self.__element_stack.append(picture)

    def __startElementCustomContentPage(self, attributes):
        custom_page = CustomContentPage(attributes['name'], attributes['location'], attributes['dir-location'], attributes['menu-id'], attributes['title'], attributes['subtitle'], '')
        self.__element_stack.append(custom_page)

    def characters(self, data):
        if not self.__ignore_levels and data.strip():
            logDebug('characters called with data: "%s"' % data.strip())

    def endElement(self, name):
        # logDebug('endElement called for %s' % name)
        if self.__ignore_levels:
            self.__ignore_levels -= 1
        else:
            current_index = len(self.__element_stack) - 1
            if current_index > 0:
                # logDebug('Adding %s to %s' % (self.__element_stack[current_index].getName(), self.__element_stack[current_index - 1].getName()))
                self.__element_stack[current_index - 1].addChild(self.__element_stack[current_index])
            self.__element_stack.pop(current_index)

