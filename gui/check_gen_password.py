from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen

from gui import ui_manager as ui

Builder.load_file('gui/check_gen_password.kv')


class CheckGenScreen(Screen):
    def back_main_screen(self):
        ui.switch_screen('main_screen', 'right')


class CheckGenScreenLayout(GridLayout):

    def check_password(self):
        print("Strong Password")
        pass

    def generate_password(self):
        print("This is aSuper Password")
        pass
