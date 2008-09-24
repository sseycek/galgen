from NamedObjectHTMLOutputter import NamedObjectHTMLOutputter
from Thumbnailer import Thumbnailer
from lxml import etree

class IndexHTMLOutputter(NamedObjectHTMLOutputter):
    __column_count = 5

    def __init__(self, index):
        NamedObjectHTMLOutputter.__init__(self, index)

    def addIndexTable(self):
        content_element = self.html_tree.xpath('id("%s")' % self.content_tag_name)[0]
        table = etree.SubElement(content_element, 'table')
        tr = None
        column_count = 0
        for child in self.entity.children:
            if tr is None or column_count == self.__column_count:
                tr = etree.SubElement(table, 'tr')
                column_count = 0
            column_count += 1
            td = etree.SubElement(tr, 'td')
            td.set('pic_location', child.pic_location)
            thumb = child.thumbnail
            td.text = child.name

    def generateOutput(self):
        self.updateTitle()
        self.addIndexTable()
        print etree.tostring(self.html_tree)
        for child in self.entity.children:
            child.generateOutput()
