#!/usr/bin/env python

class Core(object):
    __instance = None

    def __init__(self):
        if Core.__instance:
            raise 'Singleton Core has already been instantiated'
        Core.__instance = self
        self.__project = None

    def getInstance():
        if not Core.__instance:
            Core.__instance = Core()
        return Core.__instance
    getInstance = staticmethod(getInstance)

    def getProject(self):
        return self.__project

    def setProject(self, project):
        self.__project = project

    project = property(getProject, setProject)
