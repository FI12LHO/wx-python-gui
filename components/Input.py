import wx
from wx import BoxSizer, StaticText, TextCtrl


def input(
    parent, label: str, size=[300, 20], hint=""
) -> list[StaticText | TextCtrl | BoxSizer]:
    lbl = wx.StaticText(parent, label=label)
    text_input = wx.TextCtrl(parent, size=size)
    text_input.SetHint(hint)
    box = wx.BoxSizer(wx.HORIZONTAL)

    box.Add(lbl, 0, wx.ALL, 5)
    box.Add(text_input, 0, wx.ALL, 5)

    return [lbl, text_input, box]
