from Index import Index
from Contained import Contained
from GalleryHTMLOutputter import GalleryHTMLOutputter

class Gallery(Index, Contained):

    def __init__(self, name, pic_location):
        Index.__init__(self, name, pic_location)
        Contained.__init__(self)

    def _writeStartTag(self, stream):
        stream.write(u'<gallery name="%s" pic="%s">\n' % (self.getName(), self.pic_location))

    def _writeEndTag(self, stream):
        stream.write(u'</gallery>\n')

    def generateOutput(self, target_dir):
        outputter = GalleryHTMLOutputter(self)
        outputter.generateOutput(target_dir)