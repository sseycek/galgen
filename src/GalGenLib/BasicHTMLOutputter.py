#!/usr/bin/env python

from HTMLTemplate import HTMLTemplate
from xml.etree import cElementTree as etree

class BasicHTMLOutputter(object):
    doc_title_tag_id = 'doctitle'
    content_tag_id = 'hauptzelle'
    css_tag_id = 'css_ref'
    navi_tag_id = 'navizelle'
    title_tag_id = 'title'
    subtitle_tag_id = 'subtitle'

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

    def getDocTitleTag(self):
        return self.getElementById(self.doc_title_tag_id)

    def getCSSTag(self):
        return self.getElementById(self.css_tag_id)

    def getNaviTag(self):
        return self.getElementById(self.navi_tag_id)

    def getTitleTag(self):
        return self.getElementById(self.title_tag_id)

    def getSubtitleTag(self):
        return self.getElementById(self.subtitle_tag_id)

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
        
    def updateCssRef(self, level):
        tag = self.getCSSTag()
        value = './%sstyle/styles.css' % (level * '../')
        tag.set('href', value)

    def updateStyleDirRefs(self, level):
        ref_attributes = ['href', 'src']
        if level:
            for elem in self.__html_tree.getiterator():
                for attr in ref_attributes:
                    if attr in elem.attrib and (elem.attrib[attr].startswith('style') or elem.attrib[attr].startswith('./style')):
                        value = '%s%s' % (level * '../', elem.attrib[attr].lstrip('./'))
                        elem.set(attr, value)
                    
    def updateTitleCell(self, title, subtitle):
        title = self.getTitleTag()
        if self.entity.title: title.text = self.entity.title
        else: title.text = self.entity.name
        subtitle = self.getSubtitleTag()
        if self.entity.subtitle: subtitle.text = self.entity.subtitle

    def updateMenuHrefs(self, id_href_mapping):
        for (id, href) in id_href_mapping:
            a = self.getElementById(id)
            if a is not None:
                a.set('href', href)
                
    def disableNaviControls(self):
        tag = self.getNaviTag()
        tag.clear()

