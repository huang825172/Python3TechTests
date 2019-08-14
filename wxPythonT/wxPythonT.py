import wx
import wx.lib.scrolledpanel as scrolled


def openfile(event, path_text, content_text):
    path = path_text.GetValue()
    with open(path, "r", encoding="utf-8") as f:
        content_text.SetValue(f.read())


def wxmainloop():
    app = wx.App()
    frame = wx.Frame(None, title="Gui Test Editor", pos=(1000, 200), size=(500, 400))
    panel = wx.Panel(frame)
    path_text = wx.TextCtrl(panel)
    content_text = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
    open_button = wx.Button(panel, label="打开")
    open_button.Bind(wx.EVT_BUTTON, lambda evt, p=path_text, c=content_text: openfile(evt, p, c))
    save_button = wx.Button(panel, label="保存")

    box = wx.BoxSizer()
    box.Add(path_text, proportion=5, flag=wx.EXPAND | wx.ALL, border=3)
    box.Add(open_button, proportion=2, flag=wx.EXPAND | wx.ALL, border=3)
    box.Add(save_button, proportion=2, flag=wx.EXPAND | wx.ALL, border=3)

    v_box = wx.BoxSizer(wx.VERTICAL)
    v_box.Add(box, proportion=1, flag=wx.EXPAND | wx.ALL, border=3)
    v_box.Add(content_text, proportion=5, flag=wx.EXPAND | wx.ALL, border=3)

    panel.SetSizer(v_box)
    frame.Show()
    app.MainLoop()


class MsgWin(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, pos=(640, 0))

        self.scroller = wx.ScrolledWindow(self, -1)
        self.scroller.SetScrollbars(0, 1, 1, 900)

        self.pnl = pnl = wx.Panel(self.scroller)
        self.ms = ms = wx.BoxSizer(wx.VERTICAL)
        # for bid in range(10):
        #     listBut = wx.Button(self.pnl, label=bid.__str__())
        #     self.ms.Add(listBut, proportion=1, flag=wx.EXPAND | wx.ALL, border=3)

        listBut = wx.Button(self.pnl, label="hello")
        self.ms.Add(listBut, proportion=1, flag=wx.EXPAND | wx.ALL, border=3)

        self.SetMinSize((300, 600))
        self.pnl.SetSizer(self.ms)
        self.ms.Fit(self)


def wxScrWin():
    app = wx.App(redirect=False)
    msgW = MsgWin(None, -1, u"消息")
    msgW.Show(True)
    app.MainLoop()


class ScrolledPanelFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Combo Box Example")

        mainFlexSizer = wx.FlexGridSizer(2, 1, 25, -1)
        panelFlexSizer = wx.FlexGridSizer(3, 4, 6, 6)

        headLabel = wx.StaticText(self, -1, "Head label, you will always see it")

        panel = scrolled.ScrolledPanel(self, -1)

        staticText1 = wx.StaticText(panel, -1, "First name:")
        textBox1 = wx.TextCtrl(panel, -1, size=(210, 50))
        staticText2 = wx.StaticText(panel, -1, "Second name:")
        textBox2 = wx.TextCtrl(panel, -1, size=(210, 50))
        staticText3 = wx.StaticText(panel, -1, "Last name:")
        textBox3 = wx.TextCtrl(panel, -1, size=(210, 50))
        staticText4 = wx.StaticText(panel, -1, "Sex:")
        textBox4 = wx.TextCtrl(panel, -1, size=(210, 50))
        staticText5 = wx.StaticText(panel, -1, "First name:")
        textBox5 = wx.TextCtrl(panel, -1, size=(210, 50))
        staticText6 = wx.StaticText(panel, -1, "Second name:")
        textBox6 = wx.TextCtrl(panel, -1, size=(210, 50))

        panelFlexSizer.AddMany([
            (staticText1, 0, wx.SHAPED | wx.ALIGN_LEFT), (textBox1, 0, wx.SHAPED),
            (staticText2, 0, wx.SHAPED | wx.ALIGN_LEFT), (textBox2, 0, wx.SHAPED),
            (staticText3, 0, wx.SHAPED | wx.ALIGN_LEFT), (textBox3, 0, wx.SHAPED),
            (staticText4, 0, wx.SHAPED | wx.ALIGN_LEFT), (textBox4, 0, wx.SHAPED),
            (staticText5, 0, wx.SHAPED | wx.ALIGN_LEFT), (textBox5, 0, wx.SHAPED),
            (staticText6, 0, wx.SHAPED | wx.ALIGN_LEFT), (textBox6, 0, wx.SHAPED),
        ])

        panelFlexSizer.AddGrowableCol(1)
        panelFlexSizer.AddGrowableCol(3)

        panel.SetSizerAndFit(panelFlexSizer)
        panel.SetAutoLayout(1)
        panel.SetupScrolling()

        mainFlexSizer.AddMany([
            (headLabel, 0, wx.SHAPED | wx.ALIGN_LEFT),
            (panel, 1, wx.EXPAND)
        ])
        mainFlexSizer.AddGrowableCol(0)
        mainFlexSizer.AddGrowableRow(1)

        self.SetSizerAndFit(mainFlexSizer)

        self.SetMinSize((300,200))


def wxSmain():
    app = wx.App()
    ScrolledPanelFrame().Show()
    app.MainLoop()
