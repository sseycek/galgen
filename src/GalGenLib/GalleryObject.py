#!/usr/bin/env python

class GalleryObject(object):
    def __init__(self):
        self.__menu_id = ''

    def getMenuId(self):
        return self.__menu_id
    
    def setMenuId(self, id):
        self.__menu_id = id
        
    menu_id = property(getMenuId, setMenuId)