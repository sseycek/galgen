import os
from NamedObjectHTMLOutputter import NamedObjectHTMLOutputter
from xml.etree import cElementTree as etree

class ProjectHTMLOutputter(NamedObjectHTMLOutputter):
    def __init__(self, project):
        NamedObjectHTMLOutputter.__init__(self, project)

    def generateOutput(self, target_dir):
        self.updateTitle()
        self.html_tree.write(os.path.join(target_dir, 'index.html'))
        for child in self.entity.children:
            child.generateOutput(target_dir)