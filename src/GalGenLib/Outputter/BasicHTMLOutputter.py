#!/usr/bin/env python

from HTMLTemplate import HTMLTemplate

class BasicHTMLOutputter(object):
    title_tag_name = 'title'
    content_tag_name = 'content'

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
