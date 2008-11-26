import os
from Thumbnailer import Thumbnailer

class PictureReference(object):
    __html_extension = 'html'
    
    def __init__(self, location):
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
        basename = os.path.split(self.__location)[1]
        root = os.path.splitext(basename)[0]
        return '%s.%s' % (root, self.__html_extension)

    html_file_name = property(getHtmlFileName, None)

    def getThumbnail(self):
        return Thumbnailer.getInstance().getThumbnail(self.pic_location)

    thumbnail = property(getThumbnail, None)