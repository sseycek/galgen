from Contained import Contained
from Observable import Observable

class Container(Observable):
    EVT_CHILD_ADDED = 'Container.Evt.ChildAdded'
    EVT_CHILD_REMOVED = 'Container.Evt.ChildRemoved'
    DIRECTION_LEFT = True
    DIRECTION_RIGHT = False

    def __init__(self):
        self.__contained = []
        Observable.__init__(self)

    def addChild(self, child):
        self.__contained.append(child)
        child.parent = self
        self._notify(Container.EVT_CHILD_ADDED, child)

    def removeChild(self, child):
        if child in self.__contained:
            index = self.__contained.index(child)
            self.__contained.remove(child)
            if index > 0: object = self.__contained[index - 1]
            else: object = self
            self._notify(Container.EVT_CHILD_REMOVED, object)
            
    def getChildren(self):
        return self.__contained

    children = property(getChildren, None)
    
    def __getNeighbour(self, child, direction, wrap):
        try:
            idx = self.__contained.index(child)
            if direction == self.DIRECTION_LEFT:
                if idx > 0: return self.__contained[idx - 1]
                elif wrap: return self.__contained[len(self.__contained) - 1]
                else: return None
            else:
                if idx < len(self.__contained) - 1: return self.__contained[idx + 1]
                elif wrap: return self.__contained[0]
                else: return None
        except ValueError:
            raise Exception, 'Child not owned by container'
    
    def getNext(self, child, wrap):
        return self.__getNeighbour(child, self.DIRECTION_RIGHT, wrap)
    
    def getPrevious(self, child, wrap):
        return self.__getNeighbour(child, self.DIRECTION_LEFT, wrap)
    
