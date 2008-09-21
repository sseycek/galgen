#!/usr/bin/env python

from lxml import etree

default_template = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="de" lang="de">
  <head>
    <title xml:id="title_tag"/>
  </head>
  <body>
    <div xml:id="content_tag"/>
  </body>
</html>'''


class DefaultProjectHTMLTemplate(object):
    def __init__(self, named_object):
        self.__named_object = named_objet

    def getHTML(self):
        global default_template
        html = etree.XML(default_template)
        title = self.__getTagWithId(html, 'title_tag')
        title.text = self.__named_object.name
        content = self.__getTagWithId(html, 'content_tag')
        content.text = 'This one takes the content'
        return html

    HTML = property(getHTML, None)

    def __getTagWithId(self, tree, id):
        return tree.xpath('id("%s")' % id)[0]
