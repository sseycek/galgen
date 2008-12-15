from Contained import Contained
from Observable import Observable

class Container(Observable):
    EVT_CHILD_ADDED = 'Container.Evt.ChildAdded'
    EVT_CHILD_REMOVED = 'Container.Evt.ChildRemoved'

    def __init__(self):
        self.__contained = []
        Observable.__init__(self)

    def addChild(self, child):
        self.__contained.append(child)
        child.parent = self
        self._notify(Container.EVT_CHILD_ADDED)

    def removeChild(self, child):
        if child in self.__contained:
            self.__contained.remove(child)
            self._notify(Container.EVT_CHILD_REMOVED)
            
    def getChildren(self):
        return self.__contained

    children = property(getChildren, None)