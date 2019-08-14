import wx
from wx.html2 import WebView


class MyHtmlFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title, size=(1024, 768))
        web_view = WebView.New(self)
        web_view.LoadURL("https://huang825172.info")


def webViewTmain():
    app = wx.App()
    frm = MyHtmlFrame(None, "Simple HTML Browser")
    frm.Show()
    app.MainLoop()
