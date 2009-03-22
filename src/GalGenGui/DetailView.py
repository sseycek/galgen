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

import wx
from GalGenLib.NamedObject import NamedObject

class DetailView(object):
    GALGEN_ID_APPLY_BUTTON = 111
    GALGEN_ID_CANCEL_BUTTON = 112


    def __init__(self, panel, element):
        self._main_panel = panel
        self._main_panel.SetAutoLayout(True)
        self._element = element

    def __CreateSizers(self):
        self._main_box = wx.BoxSizer(wx.VERTICAL)
        self._property_box = wx.BoxSizer(wx.VERTICAL)

    def __FillMainSizer(self):
        self._main_box.Add((-1,5))
        self._main_box.Add(self._name_text, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL)
        self._main_box.Add((-1,5))
        self._main_box.Add(self._property_box, 0, wx.EXPAND)
        self._main_panel.SetSizer(self._main_box)

    def __CreateLabel(self):
        self._name_text = wx.StaticText(self._main_panel, -1, self.GetLabelCategory(), style = wx.ALIGN_CENTER)

    def _FillPropertySizer(self):
        self._control_grid = wx.GridBagSizer(5, 5)
        self.property_box.Add(self._control_grid, 1, wx.EXPAND)

    def _FillPropertySizerBelowButtons(self):
        pass
    
    def FillPanel(self):
        self.__CreateSizers()
        self.__CreateLabel()
        self.__FillMainSizer()
        self._FillPropertySizer()
        self._AddButtons()
        self._FillPropertySizerBelowButtons()
        self._main_panel.Layout()

    def GetElement(self):
        return self._element
    element = property(GetElement, None)

    def GetMainPanel(self):
        return self._main_panel
    main_panel = property(GetMainPanel, None)

    def GetPropertySizer(self):
        return self._property_box
    property_box = property(GetPropertySizer, None)

    def _AddButtons(self):
        self._button_box = wx.FlexGridSizer(cols = 3, hgap = 5, vgap = 5)
        self._apply_button = wx.Button(self._main_panel, self.GALGEN_ID_APPLY_BUTTON, 'Apply', (20, 20))
        self._main_panel.Bind(wx.EVT_BUTTON, self._OnApply, self._apply_button)
        self._apply_button.SetSize(self._apply_button.GetBestSize())
        self._cancel_button = wx.Button(self._main_panel, self.GALGEN_ID_CANCEL_BUTTON, 'Cancel', (20, 20))
        self._main_panel.Bind(wx.EVT_BUTTON, self._OnCancel, self._cancel_button)
        self._cancel_button.SetSize(self._cancel_button.GetBestSize())
        self._button_box.AddMany(((10, 10), (10, 10), (10, 10),
                                  (10, 10), self._apply_button, self._cancel_button))
        self._EnableApplyButton(False)
        self._EnableCancelButton(False)
        self.property_box.Add(self._button_box, 0, wx.EXPAND)

    def _EnableApplyButton(self, val):
        self._apply_button.Enable(val)

    def _EnableCancelButton(self, val):
        self._cancel_button.Enable(val)

    def _OnApply(self, event):
        self._EnableApplyButton(False)
        self._EnableCancelButton(False)

    def Apply(self):
        self._OnApply(None)

    def _OnCancel(self, event):
        self._EnableApplyButton(False)
        self._EnableCancelButton(False)

    def _OnEdited(self):
        if self._main_panel.event_handlers_enabled:
            modified = self._IsModified()
            self._EnableApplyButton(modified == True)
            self._EnableCancelButton(modified == True)

    def _IsModified(self):
        return False

    def IsModified(self):
        return self._IsModified()
