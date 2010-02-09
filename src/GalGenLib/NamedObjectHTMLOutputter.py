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


from xml.etree import cElementTree as etree
from NamedObject import NamedObject
from BasicHTMLOutputter import BasicHTMLOutputter

class NamedObjectHTMLOutputter(BasicHTMLOutputter):

    def __init__(self, named_object):
        BasicHTMLOutputter.__init__(self, named_object)

    def updateDocTitle(self):
        title = self.getDocTitleTag()
        title.text = self.entity.name

    def _fillMetaDataTag(self, extra_text):
        tag = self.getMetaDataTag()
        if tag is not None:
            table = etree.SubElement(tag, 'table')
            table.set('class', 'meta-data-table');
            tr = etree.SubElement(table, 'tr')
            tr.set('class', 'meta-data-tr');
            td = etree.SubElement(tr, 'td')
            td.set('class', 'meta-data-td');
            texts = self.entity.description.split('<br/>')
            td.text = texts[0]
            if len(texts) > 1:
                texts = texts[1:]
                for text in texts:
                    br = etree.SubElement(td, 'br')
                    br.tail = text
            if extra_text:
                tr = etree.SubElement(table, 'tr')
                tr.set('class', 'meta-data-tr');
                td = etree.SubElement(tr, 'td')
                td.set('class', 'meta-data-td');
                td.text = " "
                tr = etree.SubElement(table, 'tr')
                tr.set('class', 'meta-data-tr');
                td = etree.SubElement(tr, 'td')
                td.set('class', 'meta-data-td');
                td.text = extra_text