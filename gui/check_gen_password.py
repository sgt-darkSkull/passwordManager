from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen

from gui import ui_manager as ui
from api.generate_password import generate
from api.check_password import check_password

Builder.load_file('gui/check_gen_password.kv')


class CheckGenScreen(Screen):
    def back_main_screen(self):
        ui.switch_screen('main_screen', 'right')


class CheckGenScreenLayout(GridLayout):

    def check_password(self):
        password = self.ids['user_inp_txt'].text
        self.ids['disp_label'].text = check_password(password)

    def generate_password(self):

        max_len = self.ids['user_inp_txt'].text
        self.ids['disp_label'].text = generate(max_len)
