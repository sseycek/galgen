import os
from Thumbnailer import Thumbnailer
from NamedObject import NamedObject

class PictureReference(NamedObject):
    __html_extension = 'html'
    
    def __init__(self, name, location):
        NamedObject.__init__(self, name)
        self.__location = location

    def getPicLocation(self):
        return self.__location

    def setPicLocation(self, location):
        self.__location = location

    pic_location = property(getPicLocation, setPicLocation)

    def getPicFileName(self):
        return os.path.split(self.__location)[1]

    pic_file_name = property(getPicFileName, None)

    def getHtmlFileName(self):
        return '%s.html' % self.name

    html_file_name = property(getHtmlFileName, None)
