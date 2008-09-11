class Modifyable(object):

    def __init__(self):
        self.__modified = False

    def getModified(self):
        return self.__modified

    def setModified(self, modified):
        self.__modified = modified

    modified = property(getModified, setModified)