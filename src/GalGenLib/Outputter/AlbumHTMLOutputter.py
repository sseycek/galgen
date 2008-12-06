import os
from NamedObjectHTMLOutputter import NamedObjectHTMLOutputter
from Thumbnailer import Thumbnailer
from xml.etree import cElementTree as etree

class AlbumHTMLOutputter(NamedObjectHTMLOutputter):
    __column_count = 6
    __thumb_dir = 'thumbs/album'
    __picture_page_dir = '.'

    def __init__(self, index):
        NamedObjectHTMLOutputter.__init__(self, index)

    def addIndexTable(self):
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
            a.set('href', '%s/%s' % (self.__picture_page_dir, self.entity.html_file_name))
            img = etree.SubElement(a, 'img')
            img.set('class', 'thumb')
            img.set('src', '%s/%s' % (self.__thumb_dir, self.entity.pic_file_name))

    def generateOutput(self, target_dir):
        self.updateTitle()
        self.addIndexTable()
        target_dir = os.path.join(target_dir, self.entity.name)
        os.mkdir(target_dir)
        self.writeXHTML(self.html_tree, os.path.join(target_dir, 'index.html'))
        for child in self.entity.children:
            child.generateOutput(target_dir)
