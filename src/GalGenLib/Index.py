from NamedObject import NamedObject
from Container import Container
from PictureReference import PictureReference

class Index(NamedObject, Container,PictureReference):
    __output_grid_rows = 6
    __output_grid_columns = 6
    __output_element_name = 'img_grid'

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
        raise 'abstract method called'

    def __writeEndTag(self, stream):
        raise 'abstract method called'
