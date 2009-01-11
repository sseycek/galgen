from Modifyable import Modifyable
from CustomContentReference import CustomContentReference
from Contained import Contained
from CustomContentPageHTMLOutputter import CustomContentPageHTMLOutputter

class CustomContentPage(Modifyable, CustomContentReference, Contained):

    def __init__(self, name, html_location, supplemental_dir, menu_id, title, subtitle):
        Modifyable.__init__(self)
        CustomContentReference.__init__(self, name, menu_id, title, subtitle, html_location, supplemental_dir)
        Contained.__init__(self)

    def save(self, stream):
        self.__writeStartTag(stream)
        self.__writeEndTag(stream)

    def __writeStartTag(self, stream):
        stream.write(u'<customcontent name="%s" location="%s" dir-location="%s" menu-id="%s" title="%s" subtitle="%s">\n'
                     % (self.name, self.html_location, self.supplemental_dir, self.menu_id, self.title, self.subtitle))

    def __writeEndTag(self, stream):
        stream.write(u'</customcontent>\n')

    def _getHtmlPath(self):
        return '%s.html' % self.name

    def generateOutput(self, target_dir, progress_updater, page_index):
        page_index += 1
        progress_updater.update(page_index, '%s: %s' % (self.__class__.__name__, self.name))
        outputter = CustomContentPageHTMLOutputter(self)
        return outputter.generateOutput(target_dir, progress_updater, page_index)