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
        self.disableNaviControls()
        self._copyIframeDir(target_dir)
        self._copyCustomContentHtmlFile(target_dir)
        self._addIframe()
        file_name = '%s.html' % self.entity.name
        self.writeXHTML(self.html_tree, os.path.join(target_dir, file_name))
        return page_index
