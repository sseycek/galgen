from GalGenLib.NamedObject import NamedObject

class TreeItem(object):

    def __init__(self, tree, element, id):
        self.__tree = tree
        self.__element = element
        self.__id = id
        element.subscribe(NamedObject.EVT_NAME_CHANGED, self)

    def GetElement(self):
        return self.__element
    element = property(GetElement, None)

    def GetItemId(self, id):
        return self.__id
    item_id = property(GetItemId, None)

    def Notify(self, event, observed):
        if event == NamedObject.EVT_NAME_CHANGED:
            self.__tree.SetItemText(self.__id, observed.name)