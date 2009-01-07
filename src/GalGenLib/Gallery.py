from NamedObject import NamedObject
from Container import Container
from Contained import Contained
from GalleryHTMLOutputter import GalleryHTMLOutputter

class Gallery(NamedObject, Container, Contained):

    def __init__(self, name, menu_id, title, subtitle):
        NamedObject.__init__(self, name, menu_id, title, subtitle)
        Container.__init__(self)
        Contained.__init__(self)

    def save(self, stream):
        self._writeStartTag(stream)
        children = self.getChildren()
        for child in children:
            child.save(stream)
        self._writeEndTag(stream)

    def _writeStartTag(self, stream):
        stream.write(u'<gallery name="%s" menu-id="%s" title="%s" subtitle="%s">\n'
                     % (self.name, self.menu_id, self.title, self.subtitle))

    def _writeEndTag(self, stream):
        stream.write(u'</gallery>\n')

    def _getHtmlPath(self):
        return '%s/index.html' % self.name

    def generateOutput(self, target_dir, progress_updater, page_index):
        page_index += 1
        progress_updater.update(page_index, '%s: %s' % (self.__class__.__name__, self.name))
        outputter = GalleryHTMLOutputter(self)
        return outputter.generateOutput(target_dir, progress_updater, page_index)
