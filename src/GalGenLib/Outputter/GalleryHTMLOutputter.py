from NamedObjectHTMLOutputter import NamedObjectHTMLOutputter
from Thumbnailer import Thumbnailer
from xml.etree import cElementTree as etree

class GalleryHTMLOutputter(NamedObjectHTMLOutputter):
    __column_count = 3

    def __init__(self, index):
        NamedObjectHTMLOutputter.__init__(self, index)

    def addIndexTable(self):
        content_element = self.getContentTag()
        table = etree.SubElement(content_element, 'table')
        tr = None
        column_count = 0
        for child in self.entity.children:
            if tr is None or column_count == self.__column_count:
                tr = etree.SubElement(table, 'tr')
                column_count = 0
            column_count += 1
            td = etree.SubElement(tr, 'td')
#            td.set('pic_location', child.pic_location)
            thumb = child.thumbnail
            td.text = child.name
            img = etree.SubElement(tr, 'img')
            img.set('src', 'thumbs/Album_Kanada.jpg')
            img.set('style', 'float:left; margin-left:2px')
            img.set('alt', 'Kanada-Album')
            img.set('class', 'thumb')
            div = etree.SubElement(td, 'div')
            div.set('align', 'left')
            a = etree.SubElement(div, 'a')
            a.set('href', 'kanada.html')
            a.set('class', 'album')
            etree.SubElement(a, 'br')
            etree.SubElement(a, 'br')
            a.text = 'Kanada'
            etree.SubElement(a, 'br')
            span = etree.SubElement(a, 'span')
            span.set('style', 'font-size:11px')
            span.text = '2007'

    def generateOutput(self):
        self.updateTitle()
        self.addIndexTable()
        print etree.tostring(self.html_tree)
        for child in self.entity.children:
            child.generateOutput()
