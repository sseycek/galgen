from Index import Index
from Contained import Contained
from AlbumHTMLOutputter import AlbumHTMLOutputter

class Album(Index, Contained):

    def __init__(self, name, pic_location, menu_id, title, subtitle):
        Index.__init__(self, name, pic_location, menu_id, title, subtitle)
        Contained.__init__(self)

    def _writeStartTag(self, stream):
        stream.write(u'<album name="%s" pic="%s" menu-id="%s" title="%s" subtitle="%s">\n'
                     % (self.name, self.pic_location, self.menu_id, self.title, self.subtitle))

    def _writeEndTag(self, stream):
        stream.write(u'</album>\n')

    def _getHtmlPath(self):
        return '%s/%s/index.html' % (self.parent.name, self.name)

    def generateOutput(self, target_dir):
        outputter = AlbumHTMLOutputter(self)
        outputter.generateOutput(target_dir)