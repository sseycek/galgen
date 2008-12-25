#!/usr/bin/env python

class GalleryObject(object):
    def __init__(self, menu_id, title, subtitle):
        self.__menu_id = menu_id
        self.__title = title
        self.__subtitle = subtitle

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