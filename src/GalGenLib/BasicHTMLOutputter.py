#!/usr/bin/env python
# Copyright (c) 2009 Stepan Seycek. All rights reserved.
# 
# Redistribution and use in source and binary forms, with or 
# without modification, are permitted provided that the following 
# conditions are met:
# 
#  1. Redistributions of source code must retain the above 
#     copyright notice, this list of conditions and the 
#     following disclaimer.
#  2. Redistributions in binary form must reproduce the above 
#     copyright notice, this list of conditions and the following 
#     disclaimer in the documentation and/or other materials 
#     provided with the distribution.
#  3. All advertising materials mentioning features or use of this 
#     software must display the following acknowledgement: 
#     "This product includes software developed by Stepan Seycek."
#  4. The name Stepan Seycek may not be used to endorse or promote 
#     products derived from this software without specific prior 
#     written permission. 
#
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, 
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY 
# AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL 
# THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, 
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, 
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; 
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED 
# OF THE POSSIBILITY OF SUCH DAMAGE. 


from HTMLTemplate import HTMLTemplate
from xml.etree import cElementTree as etree

class BasicHTMLOutputter(object):
    doc_title_tag_id = 'doctitle'
    content_tag_id = 'hauptzelle'
    thumb_stripe_tag_id = 'thumbzelle'
    css_tag_id = 'css_ref'
    navi_tag_id = 'navizelle'
    navi_prev_tag_id = 'navi-prev'
    navi_next_tag_id = 'navi-next'
    navi_album_tag_id = 'navi-album'
    navi_highres_tag_id = 'navi-highres'
    title_tag_id = 'title'
    subtitle_tag_id = 'subtitle'
    active_menu_item_class = 'effect1'

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

    def getThumbStripeTag(self):
        return self.getElementById(self.thumb_stripe_tag_id)

    def getDocTitleTag(self):
        return self.getElementById(self.doc_title_tag_id)

    def getCSSTag(self):
        return self.getElementById(self.css_tag_id)

    def getNaviTag(self):
        return self.getElementById(self.navi_tag_id)

    def getNaviPrevTag(self):
        return self.getElementById(self.navi_prev_tag_id)

    def getNaviNextTag(self):
        return self.getElementById(self.navi_next_tag_id)

    def getNaviHighresTag(self):
        return self.getElementById(self.navi_highres_tag_id)

    def getNaviAlbumTag(self):
        return self.getElementById(self.navi_album_tag_id)

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

    def activateMenuItem(self):
        if self.entity.menu_id:
            a = self.getElementById(self.entity.menu_id)
            if a is not None:
                a.set('class', self.active_menu_item_class) 
                