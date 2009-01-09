#!/usr/bin/env python
# comment should go here

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
        if os.path.exists(self.entity.supplemental_dir):
            shutil.copytree(self.entity.supplemental_dir, os.path.join(target_dir, os.path.split(self.entity.supplemental_dir)[1]))
        else:
            raise Exception, 'Index page supplemental directory not found'
        