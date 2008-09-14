import Image

class Thumbnailer(object):
    __instance = None
    __thumnail_size = (108,108)

    def getInstance():
        if not __instance:
            __instance = Thumbnailer()
        return __instance
    getInstance = staticmethod(getInstance)

    def __init__(self):
        self.__cache = {}
        __instance = self

    def getThumbnail(self, path):
        if path in self.__cache:
            return self.__cache[path]
        img = Image.open(path)
        thumb = img.thumbnail(self.__thumnail_size)
        self.__cache[path] = thumb
        return thumb


