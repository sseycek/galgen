#!/usr/bin/env python

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