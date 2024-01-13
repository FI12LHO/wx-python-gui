from typing import Callable

import wx
from wx import Button, Colour

from listners.Button import onButton


def default_button(
    parent, label: str, size=[300, 20], callback: None | Callable = None
) -> Button:
    btn = wx.Button(parent, label=label, size=size)

    btn.SetBackgroundColour(Colour(59, 130, 246, 0))
    btn.SetForegroundColour(Colour(255, 255, 255, 0))

    btn.Bind(wx.EVT_BUTTON, lambda e: onButton(e, callback))

    return btn


def cancel_button(parent, label: str, size=[300, 20]) -> Button:
    btn = wx.Button(parent, label=label, size=size)

    btn.SetBackgroundColour(Colour(239, 68, 68, 0))
    btn.SetForegroundColour(Colour(255, 255, 255, 0))
    return btn
