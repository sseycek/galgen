from ProjectXMLParser import ProjectXMLParser
from Logging import *
from NamedObject import NamedObject
from Container import Container
from Modifyable import Modifyable
from ProjectHTMLOutputter import ProjectHTMLOutputter
import Globals

class Project(NamedObject, Container, Modifyable):

    def __init__(self, filename = '', name = ''):
        NamedObject.__init__(self, name)
        Container.__init__(self)
        Modifyable.__init__(self)
        self.__filename = filename
        self.__top_level_indexes = []
        self.__destDirName = 'C:/GalGenTest/output'

    def SetFilename(self, filename):
        self.__filename = filename

    def GetFilename(self):
        return self.__filename

    filename = property(GetFilename, SetFilename)

    def GetDestDirName(self):
        return self.__destDirName

    def SetDestDirName(self, dir):
        self.__destDirName = dir

    destination_dir = property(GetDestDirName, SetDestDirName)

    def load(self):
        if not self.__filename:
            raise 'No filename provided for loading project'
        parser = ProjectXMLParser(self.__filename)
        parser.parse(self)

    def save(self, stream):
        self.__writeHeader(stream)
        self.__writeStartTag(stream)
        children = self.getChildren()
        for child in children:
            child.save(stream)
        self.__writeEndTag(stream)

    def __writeHeader(self, stream):
        stream.write(u'<?xml version="1.0" encoding="UTF-8"?>\n')

    def __writeStartTag(self, stream):
        stream.write(u'<project name="%s" galgen-version="%s">\n' % (self.getName(), Globals.ProgVersion))

    def __writeEndTag(self, stream):
        stream.write(u'</project>\n')

    def generateOutput(self, target_dir):
        outputter = ProjectHTMLOutputter(self)
        outputter.generateOutput(target_dir)
