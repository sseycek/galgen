from ProjectHTMLTemplate import ProjectHTMLTemplate
from lxml import etree

class ProjectHTMLOutputter(object):
    def __init__(self, project):
        self.__project = project

    def generateOutput(self):
        template = ProjectHTMLTemplate(self.__project)
        print etree.tostring(template.HTML)