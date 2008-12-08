from IndexDetailView import IndexDetailView

class AlbumDetailView(IndexDetailView):

    def __init__(self, panel, element):
        super(AlbumDetailView, self).__init__(panel, element)

    def GetLabelCategory(self):
        return 'ALBUM'
