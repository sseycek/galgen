#!/usr/bin/env python

from GalGenLib.NamedObject import NamedObject
from GalGenLib.Container import Container

class TreeItem(object):
    property_expanded = 'tree_item_expanded'

    def __init__(self, tree, element, id):
        self.__tree = tree
        self.__element = element
        self.__id = id
        self.__Subscribe()

    def __Subscribe(self):
        # subscribe item for name changes of underlying object
        self.__element.subscribe(NamedObject.EVT_NAME_CHANGED, self)
        if isinstance(self.__element, Container):
            # subscribe TreePanel for add/remove events
            self.__element.subscribe(Container.EVT_CHILD_ADDED, self.__tree.GetParent())
            self.__element.subscribe(Container.EVT_CHILD_REMOVED, self.__tree.GetParent())

    def Unsubscribe(self):
        self.__element.unsubscribe(NamedObject.EVT_NAME_CHANGED, self)
        if isinstance(self.__element, Container):
            self.__element.unsubscribe(Container.EVT_CHILD_ADDED, self.__tree.GetParent())
            self.__element.unsubscribe(Container.EVT_CHILD_REMOVED, self.__tree.GetParent())

    def GetElement(self):
        return self.__element
    element = property(GetElement, None)

    def GetItemId(self, id):
        return self.__id
    item_id = property(GetItemId, None)

    def Notify(self, event, observed):
        if event == NamedObject.EVT_NAME_CHANGED:
            self.__tree.SetItemText(self.__id, observed.name)
