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

import os
import shutil
from xml.etree import cElementTree as etree
from CustomContentReference import CustomContentReference
from NamedObjectHTMLOutputter import NamedObjectHTMLOutputter

class CustomContentReferenceHTMLOutputter(NamedObjectHTMLOutputter):

    def __init__(self, named_object):
        NamedObjectHTMLOutputter.__init__(self, named_object)

    def _addIframe(self):
        content_element = self.getContentTag()
        iframe = etree.SubElement(content_element, 'iframe')
        iframe.set('src', self.entity.custom_content_reference_relative_html_path)
        iframe.set('width', '696')
        iframe.set('height', '696')
        iframe.set('scrolling', 'no')
        iframe.set('frameborder', '0')
        iframe.text = "Iframes must be supported!"
    
    def _copyCustomContentHtmlFile(self, target_dir):
        if os.path.exists(self.entity.html_location):
            shutil.copy(self.entity.html_location, os.path.join(target_dir, self.entity.custom_content_reference_relative_html_path))
        else:
            raise Exception, 'Index page not found'
    
    def _copyIframeDir(self, target_dir):
        if self.entity.supplemental_dir:
            if os.path.exists(self.entity.supplemental_dir):
                shutil.copytree(self.entity.supplemental_dir, os.path.join(target_dir, os.path.split(self.entity.supplemental_dir)[1]))
            else:
                raise Exception, 'Index page supplemental directory not found'
        