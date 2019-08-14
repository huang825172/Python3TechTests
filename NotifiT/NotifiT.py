import wx
import wx.adv


class TaskBarIcon(wx.adv.TaskBarIcon):
    ID_EXIT = wx.NewId()

    def __init__(self, frame):
        wx.adv.TaskBarIcon.__init__(self)
        self.frame = frame
        self.SetIcon(wx.Icon(name="favicon.ico", type=wx.BITMAP_TYPE_ICO), "TaskBarIcon!")
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DCLICK, self.OnTaskBarLeftDClick)
        self.Bind(wx.EVT_MENU, self.OnExit, id=self.ID_EXIT)

    def OnTaskBarLeftDClick(self, event):
        if self.frame.IsIconized():
            self.frame.Iconize(False)
        if not self.frame.IsShown():
            self.frame.Show(True)
        self.frame.Raise()

    def OnExit(self, event):
        self.Destroy()
        wx.Exit()

    def CreatePopupMenu(self):
        menu = wx.Menu()
        menu.Append(self.ID_EXIT, 'Exit')
        return menu


class Frame(wx.Frame):
    def __init__(
            self, parent=None, id=wx.ID_ANY, title='TaskBarIcon', pos=wx.DefaultPosition,
            size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE
    ):
        wx.Frame.__init__(self, parent, id, title, pos, size, style)
        self.taskBarIcon = TaskBarIcon(self)


def NotifiTmain():
    App = wx.App()
    Frame().Show()
    App.MainLoop()
