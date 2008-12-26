import os
from NamedObjectHTMLOutputter import NamedObjectHTMLOutputter
from xml.etree import cElementTree as etree
from Thumbnailer import Thumbnailer
from Album import Album

class GalleryHTMLOutputter(NamedObjectHTMLOutputter):
    __column_count = 6

    def __init__(self, index):
        NamedObjectHTMLOutputter.__init__(self, index)

    def __addIndexTable(self):
        thumb_size = Thumbnailer.getInstance().gallery_thumb_size
        thumb_dir = 'thumbs/%dx%d' % (thumb_size[0], thumb_size[1])
        content_element = self.getContentTag()
        table = etree.SubElement(content_element, 'table')
        table.set('cellpadding', '0')
        table.set('cellcpacing', '0')
        tr = None
        column_count = 0
        row_count = 0
        for child in self.entity.children:
            if tr is None or column_count == self.__column_count:
                tr = etree.SubElement(table, 'tr')
                row_count += 1
                column_count = 0
            column_count += 1
            if row_count % 2:
                title_td = etree.SubElement(tr, 'td')
                pic_td = etree.SubElement(tr, 'td')
            else:
                pic_td = etree.SubElement(tr, 'td')
                title_td = etree.SubElement(tr, 'td')
            pic_td.set('class', 'albumzelle')
            title_td.set('class', 'albumzelle')
            pic_a = etree.SubElement(pic_td, 'a')
            pic_a.set('href', '%s/index.html' % child.name)
            img = etree.SubElement(pic_a, 'img')
            img.set('src', '%s/%s' % (thumb_dir, child.pic_file_name))
            img.set('class', 'thumb')
            title_a = etree.SubElement(title_td, 'a')
            title_a.set('href', '%s/index.html' % child.name)
            title_a.text = child.title
            if not title_a.text:
                title_a.text = child.name

            
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
    
    def generateOutput(self, target_dir):
        target_dir = os.path.join(target_dir, self.entity.name)
        os.mkdir(target_dir)
        self.__createSubDirs(target_dir)
        self.__generateAlbumThumbs(target_dir)
        self.updateCssRef(1)
        self.updateStyleDirRefs(1)
        self.updateDocTitle()
        self.updateTitleCell(self.entity.title, self.entity.subtitle)
        self.disableNaviControls()
        self.__addIndexTable()
        self.writeXHTML(self.html_tree, os.path.join(target_dir, 'index.html'))
        for child in self.entity.children:
            child.generateOutput(target_dir)
