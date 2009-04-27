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
from NamedObjectHTMLOutputter import NamedObjectHTMLOutputter
from Thumbnailer import Thumbnailer
from Core import Core
from xml.etree import cElementTree as etree

class PictureHTMLOutputter(NamedObjectHTMLOutputter):
    SLIDE_THUMB_COUNT = 7

    def __init__(self, picture):
        NamedObjectHTMLOutputter.__init__(self, picture)

    def __addPicture(self):
        content_element = self.getContentTag()
        table = etree.SubElement(content_element, 'table')
        table.set('height', '696px');
        table.set('width', '696px');
        table.set('style', 'border-collapse:collapse; border:1px solid #333333');
        tr = etree.SubElement(table, 'tr')
        td = etree.SubElement(tr, 'td')
        td.set('align', 'center')
        td.set('valign', 'middle')
        img = etree.SubElement(td, 'img')
        img.set('src', 'pics/%s' % self.entity.pic_file_name)
        img.set('alt', 'Robson River')

    def __copyPicture(self, album_dir):
        shutil.copyfile(self.entity.pic_location, os.path.join(album_dir, 'pics', self.entity.pic_file_name))

    def __copyHighresPicture(self, album_dir):
        if os.path.lexists(self.entity.highres_location):
            shutil.copyfile(self.entity.highres_location, os.path.join(album_dir, 'pics', 'highres', self.entity.highres_pic_file_name))

    def __generateThumbs(self, album_dir):
        project = Core.getInstance().project
        thumbnailer = Thumbnailer.getInstance()
        slide_thumb_size = thumbnailer.slide_thumb_size
        thumb_path = os.path.join(album_dir, 'thumbs', '%dx%d' % (slide_thumb_size[0], slide_thumb_size[1]), self.entity.pic_file_name)
        if not os.path.lexists(thumb_path):
            thumb = thumbnailer.getThumbnail(self.entity.pic_location, 'slide')
            thumb.save(thumb_path, 'JPEG')
        album_thumb_size = thumbnailer.album_thumb_size
        thumb_path = os.path.join(album_dir, 'thumbs', '%dx%d' % (album_thumb_size[0], album_thumb_size[1]), self.entity.pic_file_name)
        if not os.path.lexists(thumb_path):
            thumb = thumbnailer.getThumbnail(self.entity.pic_location, 'album')
            thumb.save(os.path.join(album_dir, 'thumbs', '%dx%d' % (album_thumb_size[0], album_thumb_size[1]), self.entity.pic_file_name), 'JPEG')

    def __getThumbStripePictures(self):
        left_neighours = []
        right_neighbours = []
        current = self.entity
        while current:
            current = current.getPrevious()
            if current: left_neighours.append(current)
        current = self.entity
        while current:
            current = current.getNext()
            if current: right_neighbours.append(current)
        picture_seq = [self.entity]
        progress = True
        while len(picture_seq) < self.SLIDE_THUMB_COUNT and progress:
            progress = False
            if left_neighours:
                pic = left_neighours.pop(0)
                picture_seq.insert(0, pic)
                progress = True
                if len(picture_seq) == self.SLIDE_THUMB_COUNT: break
            if right_neighbours:
                pic = right_neighbours.pop(0)
                picture_seq.append(pic)
                progress = True
        return picture_seq
        
    def __updateThumbStripe(self):
        thumb_tag = self.getThumbStripeTag()
        if thumb_tag == None: raise Exception, 'No thumb stripe tag contained in template'
        slide_thumb_size = Thumbnailer.getInstance().slide_thumb_size
        #<table class="table1" cellspacing="0" cellpadding="0">
        table = etree.SubElement(thumb_tag, 'table')
        table.set('class', 'table1');
        table.set('cellspacing', '0');
        table.set('cellpadding', '0');
        pictures = self.__getThumbStripePictures()
        for i in range(self.SLIDE_THUMB_COUNT):
            if i >= len(pictures): break
            #<tr><td class="thumbzelle_small"><a href="peyto_lake.html"><img src="navithumbs/Peyto_Lake.jpg" class="navithumb"></a></td></tr>
            tr = etree.SubElement(table, 'tr')
            td = etree.SubElement(tr, 'td')
            td.set('class', 'thumbzelle_small')
            a = etree.SubElement(td, 'a')
            a.set('href', pictures[i].html_file_name)
            img = etree.SubElement(a, 'img')
            if not pictures[i].pic_file_name.endswith('.jpg'): raise Exception, 'currently only jpg files are supported'
            img.set('src', 'thumbs/%dx%d/%s' % (slide_thumb_size[0], slide_thumb_size[1], pictures[i].pic_file_name))
            img.set('class', 'navithumb')
            if pictures[i] == self.entity:
                img.set('id', 'effect2')

    def __updateNaviControls(self):
        tag = self.getNaviAlbumTag()
        if tag: tag.set('href', 'index.html')
        prev = self.entity.getPrevious()
        if prev:
            tag = self.getNaviPrevTag()
            if tag: tag.set('href', prev.html_file_name)
        next = self.entity.getNext()
        if next:
            tag = self.getNaviNextTag()
            if tag: tag.set('href', next.html_file_name)
        if os.path.lexists(self.entity.highres_location):
            tag = self.getNaviHighresTag()
            if tag: tag.set('href', 'pics/highres/%s' % self.entity.highres_pic_file_name)

    def generateOutput(self, target_dir, progress_updater, page_index):
        self.__copyPicture(target_dir)
        self.__copyHighresPicture(target_dir)
        self.__generateThumbs(target_dir)
        self.updateCssRef(2)
        self.updateStyleDirRefs(2)
        self.updateDocTitle()
        menu_id_href_mapping = Core.getInstance().project.getMenuIdHrefMapping(2)
        if menu_id_href_mapping: self.updateMenuHrefs(menu_id_href_mapping)
        self.updateTitleCell(self.entity.title, self.entity.subtitle)
        self.__addPicture()
        self.__updateThumbStripe()
        self.__updateNaviControls()
        file_name = '%s.html' % self.entity.name
        self.writeXHTML(self.html_tree, os.path.join(target_dir, file_name))
        return page_index
        