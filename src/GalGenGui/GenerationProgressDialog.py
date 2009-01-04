import wx

class GenerationProgressDialog(object):
    def __init__(self, count, parent):
        self.__max = count
        self.__dlg = wx.ProgressDialog("HTML Generation",
                                       "",
                                       maximum = count,
                                       parent = parent,
                                       style = wx.PD_CAN_ABORT
                                       | wx.PD_APP_MODAL
                                       | wx.PD_ELAPSED_TIME
                                       #| wx.PD_ESTIMATED_TIME
                                       | wx.PD_REMAINING_TIME)

    def update(self, new_count, msg):
        if new_count > self.__max:
            raise Exception, 'Invalid progress value %d' % new_count
        if not self.__dlg.Update(new_count, msg):
            raise Exception, 'HTML generation has been aborted'

    def destroy(self):
        self.__dlg.Destroy()