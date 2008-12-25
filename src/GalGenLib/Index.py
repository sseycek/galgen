from Container import Container
from PictureReference import PictureReference

class Index(Container,PictureReference):
    __output_grid_rows = 6
    __output_grid_columns = 6
    __output_element_name = 'img_grid'

    def __init__(self, name, pic_location, menu_id, title, subtitle):
        Container.__init__(self)
        PictureReference.__init__(self, name, pic_location, menu_id, title, subtitle)

    def save(self, stream):
        self._writeStartTag(stream)
        children = self.getChildren()
        for child in children:
            child.save(stream)
        self._writeEndTag(stream)

    def _writeStartTag(self, stream):
        raise 'abstract method called'

    def _writeEndTag(self, stream):
        raise 'abstract method called'
