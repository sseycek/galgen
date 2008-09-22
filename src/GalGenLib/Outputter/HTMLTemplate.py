#!/usr/bin/env python

from lxml import etree

default_template = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="de" lang="de">
  <head>
    <title xml:id="title"/>
  </head>
  <body>
    <div xml:id="content"/>
  </body>
</html>'''


class HTMLTemplate(object):
    def __init__(self):
        pass

    def getHTML(self):
        global default_template
        html = etree.XML(default_template)
        return html

    HTML = property(getHTML, None)