#!/usr/bin/env python
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


from GalGenLib.NamedObject import NamedObject
from GalGenLib.Container import Container

class TreeItem(object):
    property_expanded = 'tree_item_expanded'

    def __init__(self, tree, element, id):
        self.__tree = tree
        self.__element = element
        self.__id = id
        self.__Subscribe()

    def __Subscribe(self):
        # subscribe item for name changes of underlying object
        self.__element.subscribe(NamedObject.EVT_NAME_CHANGED, self)
        if isinstance(self.__element, Container):
            # subscribe TreePanel for add/remove events
            self.__element.subscribe(Container.EVT_CHILD_ADDED, self.__tree.GetParent())
            self.__element.subscribe(Container.EVT_CHILD_REMOVED, self.__tree.GetParent())

    def Unsubscribe(self):
        self.__element.unsubscribe(NamedObject.EVT_NAME_CHANGED, self)
        if isinstance(self.__element, Container):
            self.__element.unsubscribe(Container.EVT_CHILD_ADDED, self.__tree.GetParent())
            self.__element.unsubscribe(Container.EVT_CHILD_REMOVED, self.__tree.GetParent())

    def GetElement(self):
        return self.__element
    element = property(GetElement, None)

    def GetItemId(self, id):
        return self.__id
    item_id = property(GetItemId, None)

    def Notify(self, event, observed):
        if event == NamedObject.EVT_NAME_CHANGED:
            self.__tree.SetItemText(self.__id, observed.name)
