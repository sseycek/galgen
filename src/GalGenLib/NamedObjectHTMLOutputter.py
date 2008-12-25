#!/usr/bin/env python

from xml.etree import cElementTree as etree
from NamedObject import NamedObject
from BasicHTMLOutputter import BasicHTMLOutputter

class NamedObjectHTMLOutputter(BasicHTMLOutputter):

    def __init__(self, named_object):
        BasicHTMLOutputter.__init__(self, named_object)

    def updateDocTitle(self):
        title = self.getDocTitleTag()
        title.text = self.entity.name
        