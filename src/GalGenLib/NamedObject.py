from Observable import Observable

class NamedObject(Observable):
    EVT_NAME_CHANGED = 'NamedObject.Evt.NameChanged'

    def __init__(self, name):
        super(NamedObject, self).__init__()
        self.__name = name

    def setName(self, name):
        if self.__name != name:
            self.__name = name
            self._notify(NamedObject.EVT_NAME_CHANGED)

    def getName(self):
        return self.__name

    name = property(getName, setName)
