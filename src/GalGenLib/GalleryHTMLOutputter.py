import os
from NamedObjectHTMLOutputter import NamedObjectHTMLOutputter
from xml.etree import cElementTree as etree
from Thumbnailer import Thumbnailer
from Album import Album

class GalleryHTMLOutputter(NamedObjectHTMLOutputter):
    __column_count = 3

    def __init__(self, index):
        NamedObjectHTMLOutputter.__init__(self, index)

    def __addIndexTable(self):
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
        self.updateTitle()
        self.disableNaviControls()
        self.__addIndexTable()
        self.writeXHTML(self.html_tree, os.path.join(target_dir, 'index.html'))
        for child in self.entity.children:
            child.generateOutput(target_dir)
