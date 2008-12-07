import Image
from Logging import *
#from time import time

class Thumbnailer(object):
    __instance = None

    def getInstance():
        if not Thumbnailer.__instance:
            Thumbnailer.__instance = Thumbnailer()
        return Thumbnailer.__instance
    getInstance = staticmethod(getInstance)

    def __init__(self):
        self.__cache = {}
        self.__thumb_sizes = {'gallery': (108, 108), 'album': (108, 108), 'slide': (72, 72)}
        Thumbnailer.__instance = self

    def __cropImg(self, img):
        (width, height) = img.size
        if height == width:
            return img
        if height > width:
            diff = height - width
            x1 =  0
            x2 = width
            y1 = diff / 2
            y2 = height - diff/2
            if diff % 2 == 1:
                y2 -= 1
        elif width > height:
            diff = width - height
            y1 = 0
            y2 = height
            x1 = diff / 2
            x2 = width - diff/2
            if diff % 2 == 1:
                x2 -= 1
        return img.crop((x1, y1, x2, y2))

    def getThumbnail(self, path, type):
        if type not in self.__thumb_sizes.iterkeys():
            msg = 'Thumbnailer does not know category %s' % type
            raise msg
        size = self.__thumb_sizes[type]
        if size in self.__cache and path in self.__cache[size]:
            logDebug('Got %dx%d thumbnail for %s from cache' % (size[0], size[1], path))
            return self.__cache[size][path]
        img = Image.open(path)
        img = self.__cropImg(img)
        img.thumbnail(size, Image.ANTIALIAS)
        if size not in self.__cache:
            self.__cache[size] = {}
        self.__cache[size][path] = img
        logDebug('Added %dx%d thumbnail for %s to cache' % (size[0], size[1], path))
        return img

    def getGalleryThumbnailSize(self):
        return self.__thumb_sizes['gallery']
    
    gallery_thumb_size = property(getGalleryThumbnailSize, None)

    def getAlbumThumbnailSize(self):
        return self.__thumb_sizes['album']
    
    album_thumb_size = property(getAlbumThumbnailSize, None)

    def getSlideThumbnailSize(self):
        return self.__thumb_sizes['slide']

    slide_thumb_size = property(getSlideThumbnailSize, None)
