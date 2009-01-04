import os
import sys
sys.path.append('./GalGenLib')
#sys.path.append('./GalGenLib/Outputter')

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
    if project_file:
        project = Project(project_file)
        project.load()
        Core.getInstance().project = project
    startGui()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        project_file = sys.argv[1]
    elif os.path.exists('C:\\Data\\dev\\eclipse\\galgen_trunk\\test\\sample_project.ggp'):
        project_file = 'C:\\Data\\dev\\eclipse\\galgen_trunk\\test\\sample_project.ggp'
    elif os.path.exists('/home/stepan/dev/galgen_trunk/test/sample_project_lin.ggp'):
        project_file = '/home/stepan/dev/galgen_trunk/test/sample_project_lin.ggp'
    else:
        project_file = ''
    main(project_file)
