#!/usr/bin/env pyton
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
from NamedObject import NamedObject

class CustomContentReference(NamedObject):

    def __init__(self, name, menu_id, title, subtitle, html_location, supplemental_dir, description):
        NamedObject.__init__(self, name, menu_id, title, subtitle, description)
        self.__html_location = html_location
        self.__supplemental_dir = supplemental_dir

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