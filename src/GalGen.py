# Copyright (c) 2009 Stepan Seycek. All rights reserved.
# 
# Redistribution and use in source and binary forms, with or 
# without modification, are permitted provided that the following 
# conditions are met:
# 
#  1. Redistributions of source code must retain the above 
#     copyright notice, this list of conditions and the 
#     following disclaimer.
#  2. Redistributions in binary form must reproduce the above 
#     copyright notice, this list of conditions and the following 
#     disclaimer in the documentation and/or other materials 
#     provided with the distribution.
#  3. All advertising materials mentioning features or use of this 
#     software must display the following acknowledgement: 
#     “This product includes software developed by Stepan Seycek.”
#  4. The name Stepan Seycek may not be used to endorse or promote 
#     products derived from this software without specific prior 
#     written permission. 
#
# THIS SOFTWARE IS PROVIDED “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, 
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY 
# AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL 
# THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, 
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, 
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; 
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED 
# OF THE POSSIBILITY OF SUCH DAMAGE. 

import os
import sys
sys.path.append('./GalGenLib')

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
