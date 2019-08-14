from win10toast import ToastNotifier


def winNoMain():
    toaster = ToastNotifier()
    toaster.show_toast(u'真的嗷', u'就两行嗷', 'favicon.ico')
