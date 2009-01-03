from Observable import Observable
from GalleryObject import GalleryObject

class NamedObject(GalleryObject, Observable):
    EVT_NAME_CHANGED = 'NamedObject.Evt.NameChanged'

    def __init__(self, name, menu_id, title, subtitle):
        GalleryObject.__init__(self, menu_id, title, subtitle)
        Observable.__init__(self)
        self.__name = name

    def setName(self, name):
        if self.__name != name:
            self.__name = name
            self._notify(NamedObject.EVT_NAME_CHANGED, self)

    def getName(self):
        return self.__name

    name = property(getName, setName)

    def _getHtmlPath(self):
        raise Exception, 'Abstract method call'
