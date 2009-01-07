from PictureReferenceDetailView import PictureReferenceDetailView

class AlbumDetailView(PictureReferenceDetailView):

    def __init__(self, panel, element):
        super(AlbumDetailView, self).__init__(panel, element)

    def GetLabelCategory(self):
        return 'ALBUM'
