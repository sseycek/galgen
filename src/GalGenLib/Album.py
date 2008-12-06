from Index import Index
from AlbumHTMLOutputter import AlbumHTMLOutputter

class Album(Index):

    def __init__(self, name, pic_location):
        Index.__init__(self, name, pic_location)

    def __writeStartTag(self, stream):
        stream.write(u'<album name="%s" pic="%s">\n' % (self.getName(), self.pic_location))

    def __writeEndTag(self, stream):
        stream.write(u'</album>\n')

    def generateOutput(self, target_dir):
        outputter = AlbumHTMLOutputter(self)
        outputter.generateOutput(target_dir)