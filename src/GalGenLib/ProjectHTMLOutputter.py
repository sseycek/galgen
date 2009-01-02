import os
from Core import Core
from CustomContentReferenceHTMLOutputter import CustomContentReferenceHTMLOutputter
from xml.etree import cElementTree as etree

class ProjectHTMLOutputter(CustomContentReferenceHTMLOutputter):
    def __init__(self, project):
        CustomContentReferenceHTMLOutputter.__init__(self, project)

    def generateOutput(self, target_dir):
        self.updateCssRef(0)
        self.updateDocTitle()
        menu_id_href_mapping = Core.getInstance().project.getMenuIdHrefMapping(0)
        if menu_id_href_mapping: self.updateMenuHrefs(menu_id_href_mapping)
        self.updateTitleCell(self.entity.title, self.entity.subtitle)
        self.disableNaviControls()
        self._copyIframeDir(target_dir)
        self._copyCustomContentHtmlFile(target_dir)
        self._addIframe()
        self.writeXHTML(self.html_tree, os.path.join(target_dir, 'index.html'))
        for child in self.entity.children:
            child.generateOutput(target_dir)