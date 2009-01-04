from Index import Index
from Contained import Contained
from GalleryHTMLOutputter import GalleryHTMLOutputter

class Gallery(Index, Contained):

    def __init__(self, name, pic_location, menu_id, title, subtitle):
        Index.__init__(self, name, pic_location, menu_id, title, subtitle)
        Contained.__init__(self)

    def _writeStartTag(self, stream):
        stream.write(u'<gallery name="%s" pic="%s" menu-id="%s" title="%s" subtitle="%s">\n'
                     % (self.name, self.pic_location, self.menu_id, self.title, self.subtitle))

    def _writeEndTag(self, stream):
        stream.write(u'</gallery>\n')

    def _getHtmlPath(self):
        return '%s/index.html' % self.name

    def generateOutput(self, target_dir, progress_updater, page_index):
        page_index += 1
        progress_updater.update(page_index, '%s: %s' % (self.__class__.__name__, self.name))
        outputter = GalleryHTMLOutputter(self)
        return outputter.generateOutput(target_dir, progress_updater, page_index)