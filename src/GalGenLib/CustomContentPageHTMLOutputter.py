import os
import shutil
from NamedObjectHTMLOutputter import NamedObjectHTMLOutputter
from Core import Core
from xml.etree import cElementTree as etree

class CustomContentPageHTMLOutputter(NamedObjectHTMLOutputter):

    def __init__(self, custom_content):
        NamedObjectHTMLOutputter.__init__(self, custom_content)

    def generateOutput(self, target_dir):
        self.updateCssRef(0)
        self.updateStyleDirRefs(0)
        self.updateDocTitle()
        menu_id_href_mapping = Core.getInstance().project.getMenuIdHrefMapping(0)
        if menu_id_href_mapping: self.updateMenuHrefs(menu_id_href_mapping)
        self.updateTitleCell(self.entity.title, self.entity.subtitle)
        file_name = '%s.html' % self.entity.name
        if self.entity.supplemental_dir:
            dir_name = os.path.split(self.entity.supplemental_dir)[1]
            if not dir_name: raise Exception, 'Invalid supplemental path'
            shutil.copytree(self.entity.supplemental_dir, os.path.join(target_dir, dir_name))
        self.writeXHTML(self.html_tree, os.path.join(target_dir, file_name))
