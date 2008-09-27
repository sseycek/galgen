from Index import Index

class Gallery(Index):

    def __init__(self, name, pic_location):
        Index.__init__(self, name, pic_location)

    def __writeStartTag(self, stream):
        stream.write(u'<gallery name="%s" pic="%s">\n' % (self.getName(), self.pic_location))

    def __writeEndTag(self, stream):
        stream.write(u'</gallery>\n')
