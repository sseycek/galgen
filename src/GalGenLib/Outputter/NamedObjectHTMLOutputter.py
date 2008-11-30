#!/usr/bin/env python

from xml.etree import cElementTree as etree
from NamedObject import NamedObject
from BasicHTMLOutputter import BasicHTMLOutputter

class NamedObjectHTMLOutputter(BasicHTMLOutputter):

    def __init__(self, named_object):
        BasicHTMLOutputter.__init__(self, named_object)

    def updateTitle(self):
        title = self.html_tree.getroot().find('{http://www.w3.org/1999/xhtml}head/{http://www.w3.org/1999/xhtml}title')
        title.text = self.entity.name