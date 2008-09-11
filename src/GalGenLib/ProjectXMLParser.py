import xml.sax
from Logging import *
from Index import Index
from Picture import Picture

class ProjectXMLParser(xml.sax.handler.ContentHandler):

    def __init__(self, filename):
        self.__filename = filename
        self.__top_level_indexes = []
        self.__element_stack = []
        self.__ignore_levels = 0

    def parse(self, project):
        if not self.__filename:
            raise 'XML filename not given'
        self.__project = project
        parser = xml.sax.make_parser()
        parser.setContentHandler(self)
        try:
            parser.parse(self.__filename)
        except Exception, e:
            msg = 'Error occured during parsing of project XML: %s' % str(e)
            logError(msg)
            raise e

    def startElement(self, name, attributes):
        if self.__ignore_levels:
            self.__ignore_levels += 1
        elif name == "project":
            self.__startElementProject(attributes)
        elif name == "index":
            self.__startElementIndex(attributes)
        elif name == "picture":
            self.__startElementPicture(attributes)
        else:
            logError('Unknown XML tag: %s' % name)
            self.__ignore_levels += 1

    def __startElementProject(self, attributes):
        # logDebug('startElementProject called for "%s"' % attributes['name'])
        self.__project.setName(attributes['name'])
        if self.__element_stack:
            raise 'Unexpected - deserialising project, while there are already elements on the stack'
        self.__element_stack.append(self.__project)

    def __startElementIndex(self, attributes):
        # logDebug('startElementIndex called for "%s"' % attributes['name'])
        if not self.__element_stack:
            raise 'Unexpected - deserialising index, while there is no project on the stack yet'
        index = Index(attributes['name'], attributes['pic'])
        self.__element_stack.append(index)

    def __startElementPicture(self, attributes):
        # logDebug('startElementPicture called for "%s" located at "%s"' % (attributes['name'], attributes['location']))
        if len(self.__element_stack) < 2:
            raise 'Unexpected - deserialising picture, while there is no index on the stack yet'
        picture = Picture(attributes['name'], attributes['location'])
        self.__element_stack.append(picture)

    def characters(self, data):
        if not self.__ignore_levels and data.strip():
            logDebug('characters called with data: "%s"' % data.strip())

    def endElement(self, name):
        # logDebug('endElement called for %s' % name)
        if self.__ignore_levels:
            self.__ignore_levels -= 1
        else:
            current_index = len(self.__element_stack) - 1
            if current_index > 0:
                # logDebug('Adding %s to %s' % (self.__element_stack[current_index].getName(), self.__element_stack[current_index - 1].getName()))
                self.__element_stack[current_index - 1].addChild(self.__element_stack[current_index])
            self.__element_stack.pop(current_index)

