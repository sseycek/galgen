import Image

class Thumbnailer(object):
    def __init__(self):
        self.__cache = {}

    def getThumbnail(self, path):