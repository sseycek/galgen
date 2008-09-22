from NamedObjectHTMLOutputter import NamedObjectHTMLOutputter
from lxml import etree

class ProjectHTMLOutputter(NamedObjectHTMLOutputter):
    def __init__(self, project):
        NamedObjectHTMLOutputter.__init__(self, project)

    def generateOutput(self):
        self.updateTitle()
        print etree.tostring(self.html_tree)
        for child in self.entity.children:
            child.generateOutput()