from NamedObjectDetailView import NamedObjectDetailView

class ProjectDetailView(NamedObjectDetailView):

    def __init__(self, panel, element):
        super(ProjectDetailView, self).__init__(panel, element)

    def GetLabelCategory(self):
        return 'PROJECT'