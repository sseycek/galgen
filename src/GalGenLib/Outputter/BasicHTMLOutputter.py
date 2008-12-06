#!/usr/bin/env python

from HTMLTemplate import HTMLTemplate
from xml.etree import cElementTree as etree

class BasicHTMLOutputter(object):
    title_tag_id = 'title'
    content_tag_id = 'content'

    def __init__(self, entity):
        self.__entity = entity
        template = HTMLTemplate()
        self.__html_tree = template.HTML

    def getHTMLTree(self):
        return self.__html_tree

    html_tree = property(getHTMLTree, None)

    def getEntity(self):
        return self.__entity

    entity = property(getEntity, None)

    def getElementById(self, id):
        for elem in self.__html_tree.getiterator():
            if 'id' in elem.attrib and elem.attrib['id'] == id:
                return elem
        return None
    
    def getContentTag(self):
        return self.getElementById(self.content_tag_id)

    def getTitleTag(self):
        return self.getElementById(self.title_tag_id)

    def getXHTMLHeader(self):
        return ''''''

    XHTMLHeader = property(getXHTMLHeader, None)
    
    def getXHTMLString(self, tree):
        output = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n%s' % etree.tostring(tree.getroot())
        output = output.replace('html:', '')
        output = output.replace(':html', '')
        output = output.replace('&amp;#', '&#')
        return output

    def writeXHTML(self, tree, file_path):
        output = self.getXHTMLString(tree)
        fd = open(file_path, 'w')
        fd.write(output)
        fd.close()
        