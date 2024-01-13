import wx

from components.Button import cancel_button, default_button
from components.Input import input
from components.RadioButton import radio_button
from components.TextArea import text_area


class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Form")
        main_panel = wx.Panel(self)

        # input
        [lbl1, text_input1, block1] = input(main_panel, "Input 1", hint="Enter value")
        [lbl2, text_input2, block2] = input(main_panel, "Input 2", hint="Enter value")
        [lbl3, text_input3, block3] = input(main_panel, "Input 3", hint="Enter value")
        [lbl4, text_input4, block4] = input(main_panel, "Input 4", hint="Enter value")
        [lbl5, text_input5, block5] = text_area(
            main_panel, "Input 5", hint="Enter value"
        )

        # radio button
        radio_box1 = radio_button(
            main_panel,
            ["op1", "op2", "op3"],
            "Grupo1",
            "Grupo 1",
            lambda v: print(f"new value {v}"),
        )
        radio_box2 = radio_button(
            main_panel, ["op1", "op2", "op3"], "Grupo2", "Grupo 2"
        )

        # button
        btn = default_button(
            main_panel, "Registrar", [180, 40], lambda e: print("Button press")
        )
        btn_cancel = cancel_button(main_panel, "Cancelar", [180, 40])

        # container
        box_size = wx.BoxSizer(wx.VERTICAL)
        box_buttons = wx.BoxSizer(wx.HORIZONTAL)

        blocks = [
            block1,
            block2,
            block3,
            block4,
            block5,
            radio_box1,
            radio_box2,
            box_buttons,
        ]

        box_buttons.Add(btn, 0, wx.ALL | wx.CENTER, 5)
        box_buttons.Add(btn_cancel, 0, wx.ALL | wx.CENTER, 5)

        for b in blocks:
            box_size.Add(b, 0, wx.ALL | wx.CENTER)
            pass

        main_panel.SetSizer(box_size)

        self.Show()


if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()
