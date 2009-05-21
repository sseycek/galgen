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

import os
import shutil
from CustomContentReferenceHTMLOutputter import CustomContentReferenceHTMLOutputter
from Core import Core
from xml.etree import cElementTree as etree

class CustomContentPageHTMLOutputter(CustomContentReferenceHTMLOutputter):

    def __init__(self, custom_content):
        CustomContentReferenceHTMLOutputter.__init__(self, custom_content)

    def generateOutput(self, target_dir, progress_updater, page_index):
        self.updateCssRef(0)
        self.updateStyleDirRefs(0)
        self.updateDocTitle()
        menu_id_href_mapping = Core.getInstance().project.getMenuIdHrefMapping(0)
        if menu_id_href_mapping: self.updateMenuHrefs(menu_id_href_mapping)
        self.updateTitleCell(self.entity.title, self.entity.subtitle)
        self.disableNaviControls(False)
        self._copyIframeDir(target_dir)
        self._copyCustomContentHtmlFile(target_dir)
        self._addIframe()
        file_name = '%s.html' % self.entity.name
        self.writeXHTML(self.html_tree, os.path.join(target_dir, file_name))
        return page_index
