#!/usr/bin/env python
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
#     “This product includes software developed by Stepan Seycek.”
#  4. The name Stepan Seycek may not be used to endorse or promote 
#     products derived from this software without specific prior 
#     written permission. 
#
# THIS SOFTWARE IS PROVIDED “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, 
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY 
# AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL 
# THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, 
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, 
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; 
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED 
# OF THE POSSIBILITY OF SUCH DAMAGE. 


class GalleryObject(object):
    def __init__(self, menu_id, title, subtitle):
        self.__menu_id = menu_id
        self.__title = title
        self.__subtitle = subtitle
        # container for gui properties associated with this object
        self.__gui_properties = {}

    def getMenuId(self):
        return self.__menu_id
    
    def setMenuId(self, id):
        self.__menu_id = id
        
    menu_id = property(getMenuId, setMenuId)
    
    def getTitle(self):
        return self.__title
    
    def setTitle(self, title):
        self.__title = title
        
    title = property(getTitle, setTitle)    
    
    def getSubtitle(self):
        return self.__subtitle
    
    def setSubtitle(self, subtitle):
        self.__subtitle = subtitle
        
    subtitle = property(getSubtitle, setSubtitle)
    
    def setGuiProperty(self, property, value):
        self.__gui_properties[property] = value
        
    def getGuiProperty(self, property):
        if property in self.__gui_properties:
            return self.__gui_properties[property]
        else:
            return None