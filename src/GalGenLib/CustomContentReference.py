#!/usr/bin/env pyton

import os
from NamedObject import NamedObject

class CustomContentReference(NamedObject):

    def __init__(self, name, menu_id, title, subtitle, html_location, supplemental_dir):
        NamedObject.__init__(self, name, menu_id, title, subtitle)
        self.__html_location = html_location
        self.__supplemental_path = supplemental_dir

    def _getHtmlLocation(self):
        return self.__html_location
    
    def _setHtmlLocation(self, html_location):
        self.__html_location = html_location
        
    html_location = property(_getHtmlLocation, _setHtmlLocation)

    def _getContentReferenceRelativeHtmlPath(self):
        return os.path.split(self.html_location)[1]
    
    custom_content_reference_relative_html_path = property(_getContentReferenceRelativeHtmlPath, None)
    
    def _getSupplementalDir(self):
        return self.__supplemental_dir
    
    def _setSupplementalDir(self, supplemental_dir):
        self.__supplemental_dir = supplemental_dir
        
    supplemental_dir = property(_getSupplementalDir, _setSupplementalDir)