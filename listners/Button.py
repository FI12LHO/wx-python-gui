from typing import Callable


def onButton(e, callback: Callable | None) -> None:
    if callback:
        callback(e)
    pass
