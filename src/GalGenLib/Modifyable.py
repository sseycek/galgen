#!/usr/bin/env python
from Container import Container

class Modifyable(object):

    def __init__(self):
        self.__modified = False

    def getModified(self):
        return self.__modified

    def setModified(self, modified):
        if self.__modified != modified:
            self.__modified = modified
            # if this is not modified any more, children are not either
            # TODO: this approach is not compatible with undo
            if not modified and isinstance(self, Container):
                for child in self.children:
                    child.modified = modified
            # if this object is modified, all parents are as well
            if modified and self.parent:
                self.parent.modified = modified

    modified = property(getModified, setModified)
