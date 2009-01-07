from PictureReference import PictureReference
from Container import Container
from Contained import Contained
from AlbumHTMLOutputter import AlbumHTMLOutputter

class Album(PictureReference, Container, Contained):

    def __init__(self, name, pic_location, menu_id, title, subtitle):
        PictureReference.__init__(self, name, pic_location, menu_id, title, subtitle)
        Container.__init__(self)
        Contained.__init__(self)

    def save(self, stream):
        self._writeStartTag(stream)
        children = self.getChildren()
        for child in children:
            child.save(stream)
        self._writeEndTag(stream)

    def _writeStartTag(self, stream):
        stream.write(u'<album name="%s" pic="%s" menu-id="%s" title="%s" subtitle="%s">\n'
                     % (self.name, self.pic_location, self.menu_id, self.title, self.subtitle))

    def _writeEndTag(self, stream):
        stream.write(u'</album>\n')

    def _getHtmlPath(self):
        return '%s/%s/index.html' % (self.parent.name, self.name)

    def generateOutput(self, target_dir, progress_updater, page_index):
        page_index += 1
        progress_updater.update(page_index, '%s: %s' % (self.__class__.__name__, self.name))
        outputter = AlbumHTMLOutputter(self)
        return outputter.generateOutput(target_dir, progress_updater, page_index)