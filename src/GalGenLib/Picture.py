from NamedObject import NamedObject
from Modifyable import Modifyable
from PictureReference import PictureReference

class Picture(NamedObject, Modifyable, PictureReference):

    def __init__(self, name, pic_location):
        NamedObject.__init__(self, name)
        Modifyable.__init__(self)
        PictureReference.__init__(self, pic_location)

    def save(self, stream):
        self.__writeStartTag(stream)
        self.__writeEndTag(stream)

    def __writeStartTag(self, stream):
        stream.write(u'<picture name="%s" location="%s">\n' % (self.getName(), self.pic_location))

    def __writeEndTag(self, stream):
        stream.write(u'</picture>\n')

    def generateOutput(self):
        pass