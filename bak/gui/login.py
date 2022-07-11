from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout

from gui import ui_manager as ui
from kivy.uix.screenmanager import Screen

Builder.load_file('gui/login.kv')


class LoginScreen(Screen):

    def back_main_screen(self):
        ui.switch_screen('main_screen', "right")


class LoginLayout(GridLayout):

    def validate_login_request(self):
        username = self.ids["username"].text
        passwd = self.ids["passwd"].text

        if username == "user1" and passwd == "user1":
            self.ids["login_label"].text = "Access Granted"
