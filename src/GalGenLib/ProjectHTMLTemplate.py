#!/usr/bin/env python

from lxml import etree

default_template = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="de" lang="de">
  <head/>
  <body/>
</html>'''


class ProjectHTMLTemplate(object):
    def __init__(self, project):
        self.__project = project

    def getHTML(self):
        global default_template
        html = etree.XML(default_template)
        head = html.xpath('/html/head')[0]
        title = etree.SubElement(head, 'title')
        tile.text = self.__project.name
        return html

    HTML = property(getHTML, None)