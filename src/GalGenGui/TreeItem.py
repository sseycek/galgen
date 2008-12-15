#!/usr/bin/env python

from GalGenLib.NamedObject import NamedObject
from GalGenLib.Container import Container

class TreeItem(object):

    def __init__(self, tree, element, id):
        self.__tree = tree
        self.__element = element
        self.__id = id
        # subscribe item for name changes of underlying object
        element.subscribe(NamedObject.EVT_NAME_CHANGED, self)
        if isinstance(element, Container):
            # subscribe TreePanel for add/remove events
            element.subscribe(Container.EVT_CHILD_ADDED, self.__tree.GetParent())
            element.subscribe(Container.EVT_CHILD_REMOVED, self.__tree.GetParent())

    def GetElement(self):
        return self.__element
    element = property(GetElement, None)

    def GetItemId(self, id):
        return self.__id
    item_id = property(GetItemId, None)

    def Notify(self, event, observed):
        if event == NamedObject.EVT_NAME_CHANGED:
            self.__tree.SetItemText(self.__id, observed.name)
