from kivy.app import App
from kivy.core.text import LabelBase
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.config import Config


LabelBase.register(name='Macondo', fn_regular='assets/Macondo.ttf')
LabelBase.register(name='Kalam', fn_regular='assets/Kalam-Regular.ttf')

Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '720')
Config.write()


class PScreenManager(ScreenManager):
    pass


class MainScreen(Screen):
    pass


class MainLayout(GridLayout):
    pass


class MainInterface(RelativeLayout):
    pass


class LoginScreen(Screen):
    pass


class LoginLayout(GridLayout):

    def validate_login_request(self):
        username = self.ids["username"].text
        passwd = self.ids["passwd"].text

        if username == "user1" and passwd == "user1":
            print("Access Granted")
            self.ids["login_label"].text = "Access Granted"
        else:
            print("Access Denied, to : ", username, ":", passwd)
    pass


class Interface(App):
    def build(self):
        self.title = "Password Manager"
        return MainInterface()
