#!/usr/bin/env python

from lxml import etree

default_template = '''<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="de" lang="de">
  <head/>
  <body/>
</html>'''


class ProjectHTMLTemplate(object):
    def __init__(self, project):
        self.__project = project

    def getHTML(self):
        global default_template
        html = etree.parse(default_template)
        head = html.xpath('html/head')
        title = SubElement(head, 'title')
        tile.text = self.__project.name
        return html

    HTML = property(getHTML, None)