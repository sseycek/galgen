import os
import shutil
from NamedObjectHTMLOutputter import NamedObjectHTMLOutputter
from Thumbnailer import Thumbnailer
from xml.etree import cElementTree as etree

class PictureHTMLOutputter(NamedObjectHTMLOutputter):

    def __init__(self, picture):
        NamedObjectHTMLOutputter.__init__(self, picture)

    def addPicture(self):
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

    def generateOutput(self, target_dir):
        self.__copyPicture(target_dir)
        self.updateTitle()
        self.addPicture()
        file_name = '%s.html' % self.entity.name
        self.writeXHTML(self.html_tree, os.path.join(target_dir, file_name))
        