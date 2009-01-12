from Modifyable import Modifyable
from PictureReference import PictureReference
from Contained import Contained
from PictureHTMLOutputter import PictureHTMLOutputter

class Picture(Modifyable, PictureReference, Contained):

    def __init__(self, name, pic_location, menu_id, title, subtitle):
        Modifyable.__init__(self)
        PictureReference.__init__(self, name, pic_location, menu_id, title, subtitle)
        Contained.__init__(self)

    def save(self, stream):
        self.__writeStartTag(stream)
        self.__writeEndTag(stream)

    def __writeStartTag(self, stream):
        stream.write(u'<picture name="%s" location="%s" menu-id="%s" title="%s" subtitle="%s">\n'
                     % (self.name, self.pic_location, self.menu_id, self.title, self.subtitle))

    def __writeEndTag(self, stream):
        stream.write(u'</picture>\n')

    def _getHtmlPath(self):
        return '%s/%s/%s' % (self.parent.parent.name, self.parent.name, self.html_file_name)

    def generateOutput(self, target_dir, progress_updater, page_index):
        page_index += 1
        progress_updater.update(page_index, '%s: %s' % (self.__class__.__name__, self.name))
        outputter = PictureHTMLOutputter(self)
        return outputter.generateOutput(target_dir, progress_updater, page_index)
    
