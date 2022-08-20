from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.toast import toast
from kivy.clock import Clock

from uix.uix_design import *
from uix.password_list_screen import UserScreen, UtilityDialog, DataItem


class PasswordManager(MDApp):
    def __init__(self, **kwargs):
        super().__init__()
        self.user_data = None
        self.title = "Deadlock Password Manager"
        self.nav_menu = None
        self.mn_theme_color = None
        self.main_root = None
        self.screenManager = None
        self.util_dialogs = UtilityDialog()
        self.navDrawer = Builder.load_string(nav_drawer)
        self.mainScreen = Builder.load_string(main_screen)
        self.userInputField = Builder.load_string(userInputField)
        self.passwdInputField = Builder.load_string(passwdInputField)
        self.loginButton = Builder.load_string(loginButton)
        self.signupButton = Builder.load_string(singupButton)
        self.confirm_button = Builder.load_string(confirmButton)
        self.signup_cnt = Builder.load_string(signup_cnt)
        self.confirm_passwd_dialog = MDDialog(title="Signup Form :", size_hint=(0.6, None),
                                              buttons=[self.confirm_button], type="custom",
                                              content_cls=self.signup_cnt, radius=[24, 24, 24, 24])
        self.userScreen = UserScreen()

    def build(self):
        self.theme_cls.primary_palette = "Green"  # PRIMARY COLOR
        self.theme_cls.theme_style = "Dark"
        self.main_root = Builder.load_string(root)
        self.screenManager = MDScreenManager()
        self.screenManager.add_widget(self.mainScreen)
        self.screenManager.add_widget(self.userScreen)
        self.main_root.add_widget(self.screenManager)
        return self.main_root

    def create_nav_menu(self):
        self.nav_menu = Builder.load_string(nav_menu)
        self.navDrawer.add_widget(self.nav_menu)

    def on_start(self):
        self.create_nav_menu()
        self.main_root.add_widget(self.navDrawer)
        self.loginButton.on_release = self.log_in
        self.signupButton.on_release = self.sign_up
        self.mainScreen.ids.main_form.add_widget(self.userInputField)
        self.mainScreen.ids.main_form.add_widget(self.passwdInputField)
        self.mainScreen.ids.main_form.add_widget(self.loginButton)
        self.mainScreen.ids.main_form.add_widget(self.signupButton)
        self.mainScreen.ids.settings_button.on_release = self.show_settings
        self.main_root.add_widget(self.userScreen.usr_drawer)

    def validate_input(self):
        if self.passwdInputField.text != "" and self.userInputField.text != "":
            return True
        elif self.userInputField.text == "":
            self.userInputField.error = True
        elif self.passwdInputField.text == "":
            self.passwdInputField.error = True

    def add_items_in_scroll(self):
        self.user_data = DataItem('riva')
        for item in self.user_data.ui_list:
            self.userScreen.mdlist.add_widget(item)

    def log_in(self):
        self.screenManager.switch_to(self.userScreen, direction="left")  # REMOVE
        self.add_items_in_scroll()  # REMOVE
        if self.validate_input():
            print("Logging In :", self.userInputField.text, self.passwdInputField.text)
            self.add_items_in_scroll()
            self.screenManager.switch_to(self.mainScreen, direction="right")

    def sign_up(self):
        if self.validate_input():
            def confirm_password():
                if self.passwdInputField.text == self.signup_cnt.ids.confirm_password.text:
                    print(
                        f"Password Confirmed for {self.userInputField.text} ({self.signup_cnt.ids.full_name.text})",
                        self.signup_cnt.ids.confirm_password.text)
                else:
                    toast("Passwords Do Not Match!")
                    self.passwdInputField.error = True

                self.confirm_passwd_dialog.dismiss()

            self.confirm_button.on_release = confirm_password
            self.confirm_passwd_dialog.open()

    def show_settings(self):
        self.navDrawer.set_state("open")

    def change_theme(self):
        if self.theme_cls.theme_style == "Light":
            self.theme_cls.theme_style = "Dark"
            self.mainScreen.ids.login_card.md_bg_color = self.theme_cls.bg_dark
            self.mn_theme_color = [1, 1, 1, 1]
        else:
            self.theme_cls.theme_style = "Light"
            self.mainScreen.ids.login_card.md_bg_color = self.theme_cls.bg_light
            self.mn_theme_color = [0, 0, 0, 1]

    def logout_user(self):
        def switch_back(obj):
            self.screenManager.switch_to(self.mainScreen, direction="right")

        print("Logging Out")
        self.userScreen.usr_drawer.set_state("close")
        for item in self.user_data.ui_list:
            self.userScreen.mdlist.remove_widget(item)
        Clock.schedule_once(switch_back, 0.6)

    def close_app(self):
        Clock.schedule_once(self.stop, 0.6)

    def add_new_password(self):
        self.user_data.control_content.ids.domain.text = ""
        self.user_data.control_content.ids.username.text = ""
        self.user_data.control_content.ids.user_passwd.text = ""
        self.user_data.control_dialog.title = "Add New Record:"
        self.user_data.control_dialog.open()


def run():
    PasswordManager().run()
