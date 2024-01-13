from typing import Callable

from wx import RadioBox


def onRadioBox(e, radio_box: RadioBox, name: str, callback: Callable | None) -> None:
    print(f"{radio_box.GetStringSelection()} is clicked from Radio Box in {name}")

    if callback:
        callback(radio_box.GetStringSelection())
    pass
