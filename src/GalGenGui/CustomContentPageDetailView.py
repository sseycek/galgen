import os
import wx
from CustomContentReferenceDetailView import CustomContentReferenceDetailView

class CustomContentPageDetailView(CustomContentReferenceDetailView):
    
    def __init__(self, panel, element):
        super(CustomContentPageDetailView, self).__init__(panel, element)

    def _FillPropertySizer(self):
        super(CustomContentPageDetailView, self)._FillPropertySizer()

    def GetLabelCategory(self):
        return 'CUSTOM PAGE'
    
    def _OnApply(self, event):
        super(CustomContentPageDetailView, self)._OnApply(event)

    def _OnCancel(self, event):
        super(CustomContentPageDetailView, self)._OnCancel(event)
    