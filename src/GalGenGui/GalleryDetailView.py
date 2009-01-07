from NamedObjectDetailView import NamedObjectDetailView

class GalleryDetailView(NamedObjectDetailView):

    def __init__(self, panel, element):
        super(GalleryDetailView, self).__init__(panel, element)

    def GetLabelCategory(self):
        return 'GALLERY'
