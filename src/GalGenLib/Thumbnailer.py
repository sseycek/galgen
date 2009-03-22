# Copyright (c) 2009 Stepan Seycek. All rights reserved.
# 
# Redistribution and use in source and binary forms, with or 
# without modification, are permitted provided that the following 
# conditions are met:
# 
#  1. Redistributions of source code must retain the above 
#     copyright notice, this list of conditions and the 
#     following disclaimer.
#  2. Redistributions in binary form must reproduce the above 
#     copyright notice, this list of conditions and the following 
#     disclaimer in the documentation and/or other materials 
#     provided with the distribution.
#  3. All advertising materials mentioning features or use of this 
#     software must display the following acknowledgement: 
#     "This product includes software developed by Stepan Seycek."
#  4. The name Stepan Seycek may not be used to endorse or promote 
#     products derived from this software without specific prior 
#     written permission. 
#
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, 
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY 
# AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL 
# THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, 
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, 
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; 
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED 
# OF THE POSSIBILITY OF SUCH DAMAGE. 

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
            #logDebug('Got %dx%d thumbnail for %s from cache' % (size[0], size[1], path))
            return self.__cache[size][path]
        img = Image.open(path)
        img = self.__cropImg(img)
        img.thumbnail(size, Image.ANTIALIAS)
        if size not in self.__cache:
            self.__cache[size] = {}
        self.__cache[size][path] = img
        #logDebug('Added %dx%d thumbnail for %s to cache' % (size[0], size[1], path))
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
