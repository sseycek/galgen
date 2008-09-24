from Thumbnailer import Thumbnailer

class PictureReference(object):

    def __init__(self, location):
        self.__location = location

    def getPicLocation(self):
        return self.__location

    def setPicLocation(self, location):
        self.__location = location

    pic_location = property(getPicLocation, setPicLocation)

    def getThumbnail(self):
        return Thumbnailer.getInstance().getThumbnail(self.pic_location)

    thumbnail = property(getThumbnail, None)