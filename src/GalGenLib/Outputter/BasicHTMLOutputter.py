#!/usr/bin/env python

from HTMLTemplate import HTMLTemplate

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

