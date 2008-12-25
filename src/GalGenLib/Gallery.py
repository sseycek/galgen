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

    def generateOutput(self, target_dir):
        outputter = GalleryHTMLOutputter(self)
        outputter.generateOutput(target_dir)