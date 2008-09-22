#!/usr/bin/env python

from lxml import etree
from NamedObject import NamedObject
from BasicHTMLOutputter import BasicHTMLOutputter

class NamedObjectHTMLOutputter(BasicHTMLOutputter):

    def __init__(self, named_object):
        BasicHTMLOutputter.__init__(self, named_object)

    def updateTitle(self):
        title = self.html_tree.xpath('id("%s")' % self.title_tag_name)[0]
        title.text = self.entity.name