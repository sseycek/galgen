from IndexDetailView import IndexDetailView

class GalleryDetailView(IndexDetailView):

    def __init__(self, panel, element):
        super(GalleryDetailView, self).__init__(panel, element)

    def GetLabelCategory(self):
        return 'GALLERY'
