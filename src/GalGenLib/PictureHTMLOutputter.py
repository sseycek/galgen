import os
import shutil
from NamedObjectHTMLOutputter import NamedObjectHTMLOutputter
from Thumbnailer import Thumbnailer
from Core import Core
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

    def generateOutput(self, target_dir):
        self.__copyPicture(target_dir)
        self.__generateThumbs(target_dir)
        self.updateCssRef(2)
        self.updateStyleDirRefs(2)
        self.updateDocTitle()
        menu_id_href_mapping = Core.getInstance().project.getMenuIdHrefMapping(2)
        if menu_id_href_mapping: self.updateMenuHrefs(menu_id_href_mapping)
        self.updateTitleCell(self.entity.title, self.entity.subtitle)
        self.addPicture()
        file_name = '%s.html' % self.entity.name
        self.writeXHTML(self.html_tree, os.path.join(target_dir, file_name))
        