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
import urllib
from Core import Core
from NamedObjectHTMLOutputter import NamedObjectHTMLOutputter
from Thumbnailer import Thumbnailer
from xml.etree import cElementTree as etree

class AlbumHTMLOutputter(NamedObjectHTMLOutputter):
    __column_count = 6
    __row_count = 6
    __picture_page_dir = '.'

    def __init__(self, index):
        NamedObjectHTMLOutputter.__init__(self, index)

    def addIndexTable(self):
        thumb_size = Thumbnailer.getInstance().album_thumb_size
        thumb_dir = 'thumbs/%dx%d' % (thumb_size[0], thumb_size[1])
        content_element = self.getContentTag()
        table = etree.SubElement(content_element, 'table')
        table.set('class', 'table1')
        table.set('cellspacing', '0')
        table.set('cellpadding', '0')
        colgroup = etree.SubElement(table, 'colgroup')
        colgroup.set('span', str(self.__column_count))
        colgroup.set('id', 'album-index-column')
        tr = None
        column_count = 0
        cell_count = 0
        for child in self.entity.children:
            if tr is None or column_count == self.__column_count:
                tr = etree.SubElement(table, 'tr')
                tr.set('align', 'center')
                column_count = 0
            td = etree.SubElement(tr, 'td')
            td.set('class', 'bildzelle')
            column_count += 1
            cell_count += 1
            a = etree.SubElement(td, 'a')
            a.set('href', '%s/%s' % (self.__picture_page_dir, child.html_file_name))
            img = etree.SubElement(a, 'img')
            img.set('class', 'thumb')
            img.set('src', '%s/%s' % (thumb_dir, child.pic_file_name))

        # fill up with empty cells
        for i in range(self.__column_count * self.__row_count - cell_count):
            if tr is None or column_count == self.__column_count:
                tr = etree.SubElement(table, 'tr')
                tr.set('align', 'center')
                column_count = 0
            td = etree.SubElement(tr, 'td')
            td.set('class', 'bildzelle')
            column_count += 1
            cell_count += 1

    def __createSubDirs(self, album_dir):
        os.mkdir(os.path.join(album_dir, 'pics'))
        os.mkdir(os.path.join(album_dir, 'thumbs'))
        album_thumb_size = Thumbnailer.getInstance().album_thumb_size
        os.mkdir(os.path.join(album_dir, 'thumbs', '%dx%d' % album_thumb_size))
        slide_thumb_size = Thumbnailer.getInstance().slide_thumb_size
        if slide_thumb_size != album_thumb_size:
             os.mkdir(os.path.join(album_dir, 'thumbs', '%dx%d' % slide_thumb_size))

    def generateOutput(self, target_dir, progress_updater, page_index):
        self.updateCssRef(2)
        self.updateStyleDirRefs(2)
        self.updateDocTitle()
        menu_id_href_mapping = Core.getInstance().project.getMenuIdHrefMapping(2)
        if menu_id_href_mapping: self.updateMenuHrefs(menu_id_href_mapping)
        self.updateTitleCell(self.entity.title, self.entity.subtitle)
        self.disableNaviControls()
        self.addIndexTable()
        target_dir = os.path.join(target_dir, self.entity.name)
        os.mkdir(target_dir)
        self.__createSubDirs(target_dir)
        self.writeXHTML(self.html_tree, os.path.join(target_dir, 'index.html'))
        for child in self.entity.children:
            page_index = child.generateOutput(target_dir, progress_updater, page_index)
        return page_index