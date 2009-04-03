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
#     "This product includes software developed by Stepan Seycek."
#  4. The name Stepan Seycek may not be used to endorse or promote 
#     products derived from this software without specific prior 
#     written permission. 
#
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, 
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY 
# AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL 
# THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, 
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, 
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; 
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED 
# OF THE POSSIBILITY OF SUCH DAMAGE. 

from Contained import Contained
from Observable import Observable

class Container(Observable):
    EVT_CHILD_ADDED = 'Container.Evt.ChildAdded'
    EVT_CHILD_REMOVED = 'Container.Evt.ChildRemoved'
    DIRECTION_LEFT = True
    DIRECTION_RIGHT = False

    def __init__(self):
        self.__contained = []
        Observable.__init__(self)

    def addChild(self, child, index = -1):
        if index >= 0 and index < len(self.__contained):
            self.__contained.insert(index, child)
        else:
            self.__contained.append(child)
        child.parent = self
        self._notify(Container.EVT_CHILD_ADDED, (self, child, child))

    def addChildBeforeChild(self, child, before_child):
        if before_child not in self.__contained:
            raise 'BeforeChild invalid'
        index = self.__contained.index(before_child)
        self.addChild(child, index)

    def removeChild(self, child):
        if child in self.__contained:
            index = self.__contained.index(child)
            self.__contained.remove(child)
            if index > 0: selected = self.__contained[index - 1]
            else: selected = self
            self._notify(Container.EVT_CHILD_REMOVED, (self, child, selected))
            
    def getChildren(self):
        return self.__contained

    children = property(getChildren, None)
    
    def __getNeighbour(self, child, direction, wrap):
        try:
            idx = self.__contained.index(child)
            if direction == self.DIRECTION_LEFT:
                if idx > 0: return self.__contained[idx - 1]
                elif wrap: return self.__contained[len(self.__contained) - 1]
                else: return None
            else:
                if idx < len(self.__contained) - 1: return self.__contained[idx + 1]
                elif wrap: return self.__contained[0]
                else: return None
        except ValueError:
            raise Exception, 'Child not owned by container'
    
    def getNextChild(self, child, wrap):
        return self.__getNeighbour(child, self.DIRECTION_RIGHT, wrap)
    
    def getPreviousChild(self, child, wrap):
        return self.__getNeighbour(child, self.DIRECTION_LEFT, wrap)
    
    def getIndex(self, child):
        return self.__contained.index(child)
    