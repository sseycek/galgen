import sys
sys.path.append('./GalGenLib')
sys.path.append('./GalGenLib/Outputter')

from GalGenLib.Project import Project
from GalGenLib.Core import Core
from GalGenLib.Logging import *

def writeNames(elem, indent = ''):
    print '%s%s' % (indent, elem.getName())
    try:
        children = elem.getChildren()
        for child in children:
            writeNames(child, indent + ' ')
    except Exception, e:
        pass

def startGui():
    from GalGenGui import App
    a = App.App()
    a.MainLoop()

def main(project_file):
    project = Project(project_file)
    project.load()
    Core.getInstance().project = project
    #writeNames(project)
    #fd = open('C:/GalGenTest/out.xml', 'w')
    #project.save(fd)
    #fd.close()
    #print('Saved project file ...')
    startGui()

if __name__ == '__main__':
    project_file = 'C:/GalGenTest/sample_project.ggp'
    #project_file = '/home/stepan/GalGenTest/sample_project.ggp'
    if len(sys.argv) > 1: project_file = sys.argv[1]
    main(project_file)
