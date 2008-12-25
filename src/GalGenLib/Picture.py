from Modifyable import Modifyable
from PictureReference import PictureReference
from Contained import Contained
from PictureHTMLOutputter import PictureHTMLOutputter

class Picture(Modifyable, PictureReference, Contained):

    def __init__(self, name, pic_location, menu_id):
        Modifyable.__init__(self)
        PictureReference.__init__(self, name, pic_location, menu_id)
        Contained.__init__(self)

    def save(self, stream):
        self.__writeStartTag(stream)
        self.__writeEndTag(stream)

    def __writeStartTag(self, stream):
        stream.write(u'<picture name="%s" location="%s" menu-id="%s">\n'
                     % (self.name, self.pic_location, self.menu_id))

    def __writeEndTag(self, stream):
        stream.write(u'</picture>\n')

    def generateOutput(self, target_dir):
        outputter = PictureHTMLOutputter(self)
        outputter.generateOutput(target_dir)