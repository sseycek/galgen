from ProjectHTMLTemplate import ProjectHTMLTemplate

class ProjectHTMLOutputter(object):
    def __init__(self, project):
        self.__project = project

    def generateOutput(self):
        template = ProjectHTMLTemplate(self.__project)
        print template.HTML