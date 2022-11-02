from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class mCalcApp(App):

    def build(self):
        self.formula = "0"
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        self.solution = TextInput(multiline=False, background_color='black', foreground_color='white',
                                  readonly=False, halign='left', font_size=100, text='0')
        main_layout.add_widget(self.solution)

        self.fast_solution = TextInput(multiline=False, background_color='black', foreground_color='white',
                                       readonly=True, halign='right', font_size=100)
        if self.solution.text != "0":
            self.fast_solution.text = self.solution.text
        main_layout.add_widget(BoxLayout())
        main_layout.add_widget(self.fast_solution)


        buttons = [
            ["C", "(", ")", "*"],
            ["7", "8", "9", "/"],
            ["4", "5", "6", "+"],
            ["1", "2", "3", "-"],
            [".", "0", "<<", "="],
        ]

        for row in buttons:
            h_layout = BoxLayout(spacing=10)
            for label in row:
                if label == "C":
                    button = Button(text=label, color='red', font_size=100, pos_hint={"center_x": 0.5, "center_y": 0.5},
                                    on_press=self.on_button_press)
                elif label == "<<":
                    button = Button(text=label, color='yellow', font_size=100, pos_hint={"center_x": 0.5, "center_y": 0.5},
                                    on_press=self.on_button_press)
                else:
                    button = Button(text=label, font_size=100, pos_hint={"center_x": 0.5, "center_y": 0.5},
                                    on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        return main_layout



    def on_button_press(self, instance):
        if instance.text == "C":
            self.solution.text = "0"
            self.fast_solution.text = ""
        elif instance.text == "." and self.solution.text == "0":
            self.solution.text = "0."
        elif instance.text == "<<":
            self.solution.text = self.solution.text[:-1]
            if self.solution.text == "":
                self.solution.text = "0"
            else:
                try:
                    self.fast_solution.text = str(eval(self.solution.text))
                except:
                    self.fast_solution.text = self.fast_solution.text
        else:
            if self.solution.text == "0":
                self.solution.text = ''
                self.solution.text += instance.text
                self.fast_solution.text += instance.text
            elif self.solution.text != "0":
                if instance.text == "=":
                    try:
                        self.solution.text = str(eval(self.solution.text))
                    except:
                        self.solution.text = "InvalidSyntax"
                else:
                    self.solution.text += instance.text
                    try:
                        self.fast_solution.text = str(eval(self.solution.text))
                    except:
                        self.fast_solution.text = self.fast_solution.text

if __name__ == '__main__':
    mCalcApp().run()