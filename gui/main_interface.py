from kivy.app import App
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config

from gui.login import *
from gui.components import *

LabelBase.register(name='Macondo', fn_regular='assets/Macondo.ttf')
LabelBase.register(name='Kalam', fn_regular='assets/Kalam-Regular.ttf')

Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '720')
Config.write()

Builder.load_file('gui/main_interface.kv')


class MainScreen(Screen):

    def login_screen(self):
        ui.switch_screen('login_screen', "left")

    def signup_screen(self):
        ui.switch_screen('signup_screen', "left")

    def check_gen_screen(self):
        ui.switch_screen('check_gen_screen', "left")


class MainInterface(ScreenManager):
    pass


class Interface(App):
    def build(self):
        self.title = "Password Manager"

        ui.s_manager = MainInterface()
        self.root = root = ui.s_manager

        ui.screens['main_screen'] = MainScreen()
        root.add_widget(ui.screens['main_screen'])

        ui.screens['login_screen'] = LoginScreen()
        root.add_widget(ui.screens['login_screen'])

        return root
