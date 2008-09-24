import Image
from Logging import *
#from time import time

class Thumbnailer(object):
    __instance = None
    __thumnail_size = (108,108)

    def getInstance():
        if not Thumbnailer.__instance:
            Thumbnailer.__instance = Thumbnailer()
        return Thumbnailer.__instance
    getInstance = staticmethod(getInstance)

    def __init__(self):
        self.__cache = {}
        self.__cachedir = 'C:/GalGenTest/thumbcache'
        Thumbnailer.__instance = self

    def __cropImg(self, img):
        (width, height) = img.size
        logDebug('bbox: %dx%d' % (width, height))
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

    def getThumbnail(self, path):
        if path in self.__cache:
            logDebug('Got thumbnail for %s from cache' % path)
            return self.__cache[path]
        img = Image.open(path)
        #start_time = time()
        img = self.__cropImg(img)
        img.thumbnail(self.__thumnail_size, Image.ANTIALIAS)
        #logDebug('Thumbnail creation for %s took %f ms' % (path, (time() - start_time) * 1000))
        self.__cache[path] = img
        img.save('%s/%d.jpg' % (self.__cachedir, len(self.__cache)), 'JPEG')
        logDebug('Added thumbnail for %s to cache' % path)
        return img


