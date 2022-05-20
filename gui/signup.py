from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout

from gui import ui_manager as ui
from kivy.uix.screenmanager import Screen

Builder.load_file('gui/signup.kv')


class SignupScreen(Screen):

    def back_main_screen(self):
        ui.switch_screen('main_screen', 'right')


class SignupLayout(GridLayout):

    def validate_signup_request(self):
        print("Signup Success")