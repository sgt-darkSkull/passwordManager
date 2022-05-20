from kivy.app import App
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config

from gui.check_gen_password import CheckGenScreen
from gui.login import LoginScreen
from gui.signup import SignupScreen
from gui.components import *
from gui import ui_manager as ui

LabelBase.register(name='Macondo', fn_regular='assets/Macondo.ttf')
LabelBase.register(name='Kalam', fn_regular='assets/Kalam-Regular.ttf')
LabelBase.register(name='Ubuntu', fn_regular='assets/UbuntuMono.ttf')

Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '720')
Config.write()

Builder.load_file('gui/main_interface.kv')


class MainScreen(Screen):

    def login_screen(self):
        ui.switch_screen(screen='login_screen', dirct="left")

    def signup_screen(self):
        ui.switch_screen(screen='signup_screen', dirct="left")

    def check_gen_screen(self):
        ui.switch_screen(screen='check_gen_screen', dirct="left")


class MainInterface(ScreenManager):
    pass


class Interface(App):
    def build(self):
        self.title = "Password Manager"

        ui.s_manager = MainInterface()
        self.root = root = ui.s_manager

        ui.screens['main_screen'] = MainScreen(name="main_screen")
        root.add_widget(ui.screens['main_screen'])

        ui.screens['login_screen'] = LoginScreen(name="login_screen")
        root.add_widget(ui.screens['login_screen'])

        ui.screens['signup_screen'] = SignupScreen(name="signup_screen")
        root.add_widget(ui.screens['signup_screen'])

        ui.screens['check_gen_screen'] = CheckGenScreen(name="check_gen_screen")
        root.add_widget(ui.screens['check_gen_screen'])

        return root
