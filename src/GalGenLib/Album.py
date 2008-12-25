from Index import Index
from Contained import Contained
from AlbumHTMLOutputter import AlbumHTMLOutputter

class Album(Index, Contained):

    def __init__(self, name, pic_location, menu_id):
        Index.__init__(self, name, pic_location, menu_id)
        Contained.__init__(self)

    def _writeStartTag(self, stream):
        stream.write(u'<album name="%s" pic="%s" menu-id="%s">\n'
                     % (self.name, self.pic_location, self.menu_id))

    def _writeEndTag(self, stream):
        stream.write(u'</album>\n')

    def generateOutput(self, target_dir):
        outputter = AlbumHTMLOutputter(self)
        outputter.generateOutput(target_dir)