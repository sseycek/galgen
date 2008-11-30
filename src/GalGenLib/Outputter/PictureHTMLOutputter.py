from NamedObjectHTMLOutputter import NamedObjectHTMLOutputter
from Thumbnailer import Thumbnailer
from xml.etree import cElementTree as etree

class PictureHTMLOutputter(NamedObjectHTMLOutputter):

    def __init__(self, picture):
        NamedObjectHTMLOutputter.__init__(self, picture)

    def addPicture(self):
        content_element = self.html_tree.xpath('id("%s")' % self.content_tag_name)[0]
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

    def generateOutput(self):
        self.updateTitle()
        self.addPicture()
        print etree.tostring(self.html_tree)
        