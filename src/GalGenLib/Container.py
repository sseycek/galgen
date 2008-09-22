class Container(object):

    def __init__(self):
        self.__contained = []

    def addChild(self, child):
        self.__contained.append(child)

    def getChildren(self):
        return self.__contained

    children = property(getChildren, None)