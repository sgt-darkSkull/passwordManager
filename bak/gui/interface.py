# from kivy.app import App
# from kivy.core.text import LabelBase
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.relativelayout import RelativeLayout
# from kivy.uix.screenmanager import Screen, ScreenManager
# from kivy.config import Config
# from gui.components import *
#
# LabelBase.register(name='Macondo', fn_regular='assets/Macondo.ttf')
# LabelBase.register(name='Kalam', fn_regular='assets/Kalam-Regular.ttf')
#
# Config.set('graphics', 'width', '480')
# Config.set('graphics', 'height', '720')
# Config.write()
#
#
# class PScreenManager(ScreenManager):
#     pass
#
#
# class MainScreen(Screen):
#     pass
#
#
# class MainLayout(GridLayout):
#     pass
#
#
# class MainInterface(RelativeLayout):
#     pass
#
#
# class LoginScreen(Screen):
#     pass
#
#
# class LoginLayout(GridLayout):
#
#     def validate_login_request(self):
#         username = self.ids["username"].text
#         passwd = self.ids["passwd"].text
#
#         if username == "user1" and passwd == "user1":
#             self.ids["login_label"].text = "Access Granted"
#
#
# class Interface(App):
#     def build(self):
#         self.title = "Password Manager"
#         return MainInterface()
#
#
#
# <MainInterface>:
#     PScreenManager:
#
# <PScreenManager>:
# 	id: "s_manager"
#     MainScreen:
#     #LoginScreen:
#
#
# <MainScreen>:
# 	name: "main_screen"
# 	MainLayout:
#
#
# <MainLayout>:
# 	cols: 1
# 	rows: 2
# 	padding: (dp(20), 0, dp(20), dp(20))
# 	Label:
# 		text: "Password Manager"
# 		font_name: "Kalam"
# 		font_size: dp(30)
# 	GridLayout:
# 		rows: 3
# 		padding: dp(40)
# 		spacing: dp(20)
# 		KvRoundButtonUi:
# 			button_color: .6, .2, .2
# 			button_label_text: "Login"
# 			on_release:
# 				app.root.children[0].current = "login_screen"
# 				root.parent.manager.transition.direction = "left"
# 		KvRoundButtonUi:
# 			button_color: .6, .2, .2
# 			button_label_text: "Signup"
# 		KvRoundButtonUi:
# 			button_color: .6, .2, .2
# 			button_label_text: "Check/Generate Password"
#
# <LoginScreen>:
# 	name: "login_screen"
# 	BoxLayout:
# 		orientation: "vertical"
# 		KvPreviousButtonUi:
# 			on_release:
# 				app.root.children[0].current = "main_screen"
# 				root.manager.transition.direction = "right"
# 		LoginLayout:
#
#
# <LoginLayout>:
# 	cols: 1
# 	rows: 2
# 	padding: (dp(20), 0, dp(20), dp(20))
# 	Label:
# 		id: login_label
# 		text: "Login Screen"
# 		font_name: "Macondo"
# 		font_size: dp(30)
# 	GridLayout:
# 		cols: 1
# 		rows: 3
# 		padding: dp(40)
# 		spacing: dp(30)
# 		GridLayout:
# 			cols: 2
# 			padding: dp(10)
# 			Label:
# 				text: "USERNAME: "
# 			KvTextFieldUi:
# 				id: username
# 		GridLayout:
# 			cols: 2
# 			padding: dp(10)
# 			Label:
# 				text: "PASSWORD"
# 			KvTextFieldUi:
# 				id: passwd
# 				password: True
# 				#password_mask: "*"
# 		GridLayout:
# 			cols: 1
# 			KvRoundButtonUi:
# 				id: "login_button"
# 				button_color: .6, .2, .2
# 				button_label_text: "Login"
# 				on_press: root.validate_login_request()
