#!/usr/bin/python
# -*- coding: utf-8 -*-
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

import os
import pyexiv2
from Modifyable import Modifyable
from PictureReference import PictureReference
from Contained import Contained
from PictureHTMLOutputter import PictureHTMLOutputter
from XmlUtils import asXmlAttribute

META_DATA_TAGS = ('Exif.Image.Model',
                  'Exif.Photo.DateTimeOriginal',
                  'Exif.Photo.FocalLengthIn35mmFilm',
                  'Exif.Photo.ExposureTime',
                  'Exif.Photo.FNumber',
                  'Exif.Photo.ISOSpeedRatings')

class Picture(Modifyable, PictureReference, Contained):

    def __init__(self, name, pic_location, highres_location, menu_id, title, subtitle, description, exif):
        Modifyable.__init__(self)
        PictureReference.__init__(self, name, pic_location, menu_id, title, subtitle, description)
        self.__highres_location = highres_location
        Contained.__init__(self)
        self.__exif = exif

    def __getExif(self):
        return self.__exif
    
    def __setExif(self, exif):
        if exif != self.__exif:
            self.__exif = exif
            self.modified = True
           
    exif = property(__getExif, __setExif)
            
    def save(self, stream):
        self.__writeStartTag(stream)
        self.__writeEndTag(stream)

    def __writeStartTag(self, stream):
        stream.write(u'<picture name="%s" location="%s" highres-location="%s" menu-id="%s" title="%s" subtitle="%s" description="%s" exif="%s">\n'
                     % (asXmlAttribute(self.name), asXmlAttribute(self.pic_location), asXmlAttribute(self.highres_location),
                        asXmlAttribute(self.menu_id), asXmlAttribute(self.title), asXmlAttribute(self.subtitle),
                        asXmlAttribute(self.description), asXmlAttribute(self.exif)))

    def __writeEndTag(self, stream):
        stream.write(u'</picture>\n')

    def _getHtmlPath(self):
        return '%s/%s/%s' % (self.parent.parent.name, self.parent.name, self.html_file_name)

    def __getHighresLocation(self):
        return self.__highres_location
    
    def __setHighresLocation(self, location):
        if location != self.__highres_location:
            self.__highres_location = location
            self.modified = True
    
    highres_location = property(__getHighresLocation, __setHighresLocation)
    
    def getHighresPicFileName(self):
        if self.highres_location:
            return os.path.split(self.highres_location)[1]
        else: return None

    highres_pic_file_name = property(getHighresPicFileName, None)

    def generateOutput(self, target_dir, progress_updater, page_index):
        page_index += 1
        progress_updater.update(page_index, '%s: %s' % (self.__class__.__name__, self.name))
        outputter = PictureHTMLOutputter(self)
        return outputter.generateOutput(target_dir, progress_updater, page_index)
    
    def extractExifFromPicture(self):
        exif = ''
        global META_DATA_TAGS
        try:
            meta_data = pyexiv2.ImageMetadata(self.pic_location)
            meta_data.read() # readMetadata()
            exif_keys = meta_data.exif_keys
            for k in META_DATA_TAGS:
                if k in exif_keys:
                    val = meta_data[k]
                    if k == 'Exif.Photo.DateTimeOriginal':
                        val = val.strftime('%Y-%m-%d')
                    elif k == 'Exif.Photo.FocalLengthIn35mmFilm':
                        val = 'f=%d mm (KB)' % val
                    elif k == 'Exif.Photo.ExposureTime':
                        if val.denominator > val.numerator:
                            val = '1/%d s' % (val.denominator/val.numerator)
                        else:
                            val = ('%.1f s' % (1.0 * val.numerator / val.denominator)).replace('.',',')
                    elif k == 'Exif.Photo.FNumber':
                        val = 1.0 * val.numerator / val.denominator
                        if not val % 1: val = 'f/%d' % val
                        else: val = ('f/%.1f' % val).replace('.',',')
                    elif k == 'Exif.Photo.ISOSpeedRatings':
                        val = 'ISO %d' % val    
                    if exif:
                        exif += u' ● '
                    exif += str(val)
        except:
            # ignore error opening file
            # pass
            raise
        return exif
            
    def _picLocationUpdated(self):
        self.exif = self.extractExifFromPicture()
        
