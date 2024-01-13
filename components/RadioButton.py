from typing import Callable

import wx
from wx import RadioBox

from listners.RadioButton import onRadioBox


def radio_button(
    parent,
    choices: list[str],
    name: str,
    label: str = "",
    callback: Callable | None = None,
) -> RadioBox:
    radio_box = wx.RadioBox(
        parent,
        label=label,
        choices=choices,
        size=[300, 50],
        majorDimension=1,
        style=wx.RA_SPECIFY_ROWS,
    )

    radio_box.Bind(
        wx.EVT_RADIOBOX,
        lambda e: onRadioBox(e, radio_box, name, callback),
    )
    return radio_box
