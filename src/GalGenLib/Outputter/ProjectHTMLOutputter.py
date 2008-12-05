from NamedObjectHTMLOutputter import NamedObjectHTMLOutputter
from xml.etree import cElementTree as etree

class ProjectHTMLOutputter(NamedObjectHTMLOutputter):
    def __init__(self, project):
        NamedObjectHTMLOutputter.__init__(self, project)

    def generateOutput(self):
        self.updateTitle()
        print etree.tostring(self.html_tree.getroot())
        for child in self.entity.children:
            child.generateOutput()