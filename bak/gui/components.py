from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

Builder.load_file("gui/components.kv")


class KvRoundButtonUi(Button):
    button_color = ListProperty([0, 0, 0, 0])
    button_label_text = StringProperty()

    def remove_flash(self):
        self.button_color = [self.button_color[0] - .09, self.button_color[1] - .09, self.button_color[2] - .09]

    def add_flash(self):
        self.button_color = [self.button_color[0] + .09, self.button_color[1] + .09, self.button_color[2] + .09]


class KvPreviousButtonUi(Button):
    pass


class KvTextFieldUi(TextInput):
    pass

