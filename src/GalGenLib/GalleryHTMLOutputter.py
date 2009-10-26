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
from Core import Core
from NamedObjectHTMLOutputter import NamedObjectHTMLOutputter
from xml.etree import cElementTree as etree
from Thumbnailer import Thumbnailer
from Album import Album

class GalleryHTMLOutputter(NamedObjectHTMLOutputter):
    __column_count = 3
    __row_count = 6

    def __init__(self, index):
        NamedObjectHTMLOutputter.__init__(self, index)

    def __addIndexTable(self):
        thumb_size = Thumbnailer.getInstance().gallery_thumb_size
        thumb_dir = 'thumbs/%dx%d' % (thumb_size[0], thumb_size[1])
        content_element = self.getContentTag()
        table = etree.SubElement(content_element, 'table')
        table.set('cellpadding', '0')
        table.set('cellspacing', '0')
        table.set('class', 'table1')
        colgroup = etree.SubElement(table, 'colgroup')
        colgroup.set('span', str(self.__column_count))
        colgroup.set('id', 'gallery-index-column')
        tr = None
        column_count = 0
        row_count = 0
        cell_count = 0
        for child in self.entity.children:
            if tr is None or column_count == self.__column_count:
                tr = etree.SubElement(table, 'tr')
                row_count += 1
                column_count = 0
            column_count += 1
            cell_count += 1
            if row_count % 2: pic_first = True
            else: pic_first = False
            td = etree.SubElement(tr, 'td')
            td.set('class', 'albumzelle')
            a = etree.SubElement(td, 'a')
            div = etree.SubElement(td, 'div')
            a.set('href', '%s/index.html' % child.name)
            img = etree.SubElement(a, 'img')
            img.set('class', 'thumb')
            img.set('src', '%s/%s' % (thumb_dir, child.pic_file_name))
            img.set('alt', '%s' % child.name)
            if pic_first:
                div.set('align', 'left')
                img.set('style', 'float: left; margin-left: 2px;')
            else:
                div.set('align', 'right')
                img.set('style', 'float: right; margin-right: 2px;')
            title_a = etree.SubElement(div, 'a')
            title_a.set('class', 'album')
            title_a.set('href', '%s/index.html' % child.name)
            etree.SubElement(title_a, 'br')
            etree.SubElement(title_a, 'br')
            title_span = etree.SubElement(title_a, 'span')
            title_span.text = child.title
            etree.SubElement(title_a, 'br')
            subtitle_span = etree.SubElement(title_a, 'span')
            subtitle_span.set('style', 'font-size: 11px;')
            subtitle_span.text = child.subtitle
        # fill up with empty cells
        for i in range(self.__column_count * self.__row_count - cell_count):
            if tr is None or column_count == self.__column_count:
                tr = etree.SubElement(table, 'tr')
                row_count += 1
                column_count = 0
            td = etree.SubElement(tr, 'td')
            td.set('class', 'albumzelle')
            column_count += 1
            cell_count += 1
            
    def __createSubDirs(self, gallery_dir):
        os.mkdir(os.path.join(gallery_dir, 'thumbs'))
        gallery_thumb_size = Thumbnailer.getInstance().gallery_thumb_size
        os.mkdir(os.path.join(gallery_dir, 'thumbs', '%dx%d' % gallery_thumb_size))

    def __generateAlbumThumbs(self, gallery_dir):
        thumbnailer = Thumbnailer.getInstance()
        (width, height) = thumbnailer.gallery_thumb_size
        for child in self.entity.children:
            thumb_path = os.path.join(gallery_dir, 'thumbs', '%dx%d' % (width, height), child.pic_file_name)
            if not os.path.lexists(thumb_path):
                thumb = thumbnailer.getThumbnail(child.pic_location, 'gallery')
                thumb.save(thumb_path, 'JPEG')
    
    def generateOutput(self, target_dir, progress_updater, page_index):
        target_dir = os.path.join(target_dir, self.entity.name)
        os.mkdir(target_dir)
        self.__createSubDirs(target_dir)
        self.__generateAlbumThumbs(target_dir)
        self.updateCssRef(1)
        self.updateStyleDirRefs(1)
        self.updateDocTitle()
        menu_id_href_mapping = Core.getInstance().project.getMenuIdHrefMapping(1)
        if menu_id_href_mapping: self.updateMenuHrefs(menu_id_href_mapping)
        self.activateMenuItem()
        self.updateTitleCell(self.entity.title, self.entity.subtitle)
        self.disableNaviControls(True, False)
        self._fillMetaDataTag('')
        self.__addIndexTable()
        self.writeXHTML(self.html_tree, os.path.join(target_dir, 'index.html'))
        for child in self.entity.children:
            page_index = child.generateOutput(target_dir, progress_updater, page_index)
        return page_index