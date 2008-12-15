class Contained(object):
    def __init__(self):
        self.__parent = None
    
    def setParent(self, parent):
        self.__parent = parent

    def getParent(self):
        return self.__parent

    parent = property(getParent, setParent)