import wx

from components.Button import cancel_button, default_button
from components.Input import input
from components.RadioButton import radio_button
from components.TextArea import text_area
from functions.Sheet import append_row


class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Form")
        main_panel = wx.Panel(self)

        self.value_radio_group: dict = {
            "genderGroup": "male",
            "maritalGroup": "single",
        }

        # input
        [lbl1, text_input1, block1] = input(main_panel, "Name", hint="Enter name")
        [lbl2, text_input2, block2] = input(main_panel, "E-mail", hint="Enter email")
        [lbl3, text_input3, block3] = input(main_panel, "Phone", hint="Enter phone")
        [lbl4, text_input4, block4] = input(main_panel, "Date", hint="Enter date")
        [lbl5, text_input5, block5] = text_area(
            main_panel, "Message", hint="Enter message"
        )

        # radio button
        radio_box1 = radio_button(
            main_panel,
            ["male", "female"],
            "genderGroup",
            "Gender",
            lambda v: self.onRadioChangeValue("gender", v),
        )
        radio_box2 = radio_button(
            main_panel,
            ["single", "married", "widower"],
            "maritalGroup",
            "Marital status",
            lambda v: self.onRadioChangeValue("marital_group", v),
        )

        # button
        btn = default_button(
            main_panel,
            "Registrar",
            callback=lambda e: self.onSubmitForm(
                [
                    text_input1,
                    text_input2,
                    text_input3,
                    text_input4,
                    text_input5,
                ]
            ),
        )
        btn_cancel = cancel_button(
            main_panel,
            "Cancelar",
            callback=lambda e: self.onCancel(
                [
                    text_input1,
                    text_input2,
                    text_input3,
                    text_input4,
                    text_input5,
                ]
            ),
        )

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

    def onSubmitForm(self, inputs: list):
        content = []
        for input in inputs:
            content.append(input.GetValue())
            pass

        for value in self.value_radio_group:
            content.append(self.value_radio_group.get(value))
            pass

        try:
            print(content)
            append_row(content)
        except:
            print("Fail")
        finally:
            self.onCancel(inputs)

        pass

    def onCancel(self, inputs: list):
        for input in inputs:
            input.SetValue("")
            pass
        pass

    def onRadioChangeValue(self, name: str, value: str):
        self.value_radio_group[name] = value
        pass


if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()
