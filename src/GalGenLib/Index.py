from NamedObject import NamedObject
from Container import Container
from PictureReference import PictureReference

class Index(NamedObject, Container,PictureReference):

    def __init__(self, name, pic_location):
        NamedObject.__init__(self, name)
        Container.__init__(self)
        PictureReference.__init__(self, pic_location)

    def save(self, stream):
        self.__writeStartTag(stream)
        children = self.getChildren()
        for child in children:
            child.save(stream)
        self.__writeEndTag(stream)

    def __writeStartTag(self, stream):
        stream.write(u'<index name="%s" pic="%s">\n' % (self.getName(), self.pic_location))

    def __writeEndTag(self, stream):
        stream.write(u'</index>\n')

