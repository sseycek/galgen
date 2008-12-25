import os
import urllib
from NamedObjectHTMLOutputter import NamedObjectHTMLOutputter
from Thumbnailer import Thumbnailer
from xml.etree import cElementTree as etree

class AlbumHTMLOutputter(NamedObjectHTMLOutputter):
    __column_count = 6
    __picture_page_dir = '.'

    def __init__(self, index):
        NamedObjectHTMLOutputter.__init__(self, index)

    def addIndexTable(self):
        thumb_size = Thumbnailer.getInstance().album_thumb_size
        thumb_dir = 'thumbs/%dx%d' % (thumb_size[0], thumb_size[1])
        content_element = self.getContentTag()
        table = etree.SubElement(content_element, 'table')
        table.set('cellspacing', '0')
        table.set('cellpadding', '0')
        table.set('style', 'border-collapse:collapse; border:1px solid #333333; width:696px; height:696px')
        tr = None
        column_count = 0
        for child in self.entity.children:
            if tr is None or column_count == self.__column_count:
                tr = etree.SubElement(table, 'tr')
                tr.set('align', 'center')
                column_count = 0
            column_count += 1
            td = etree.SubElement(tr, 'td')
            a = etree.SubElement(td, 'a')
            a.set('href', '%s/%s' % (self.__picture_page_dir, child.html_file_name))
            img = etree.SubElement(a, 'img')
            img.set('class', 'thumb')
            img.set('src', '%s/%s' % (thumb_dir, child.pic_file_name))

    def __createSubDirs(self, album_dir):
        os.mkdir(os.path.join(album_dir, 'pics'))
        os.mkdir(os.path.join(album_dir, 'thumbs'))
        album_thumb_size = Thumbnailer.getInstance().album_thumb_size
        os.mkdir(os.path.join(album_dir, 'thumbs', '%dx%d' % album_thumb_size))
        slide_thumb_size = Thumbnailer.getInstance().slide_thumb_size
        if slide_thumb_size != album_thumb_size:
             os.mkdir(os.path.join(album_dir, 'thumbs', '%dx%d' % slide_thumb_size))

    def generateOutput(self, target_dir):
        self.updateCssRef(2)
        self.updateStyleDirRefs(2)
        self.updateTitle()
        self.disableNaviControls()
        self.addIndexTable()
        target_dir = os.path.join(target_dir, self.entity.name)
        os.mkdir(target_dir)
        self.__createSubDirs(target_dir)
        self.writeXHTML(self.html_tree, os.path.join(target_dir, 'index.html'))
        for child in self.entity.children:
            child.generateOutput(target_dir)
