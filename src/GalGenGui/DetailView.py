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
