import json

from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
from kivymd.toast import toast
from kivymd.uix.button import MDFlatButton
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelTwoLine
from kivymd.uix.list import MDList, IconLeftWidget, IconRightWidget, OneLineAvatarIconListItem
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.filemanager import MDFileManager
from kivy.utils import platform
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import MDScrollView

from uix.uix_design import *


class DataItem:

    def password_controls(self, site, userid):
        self.control_dialog.title = "Edit Record:"
        self.control_content.ids.domain.text = site
        self.control_content.ids.username.text = userid
        self.control_content.ids.user_passwd.text = self.passwd_db[site][userid]
        self.control_dialog.open()

    def show_passwd(self, obj):
        if self.control_content.ids.user_passwd.password:
            self.control_content.ids.user_passwd.password = False
            self.show_pass_button.text = "Hide"
        else:
            self.control_content.ids.user_passwd.password = True
            self.show_pass_button.text = "Show"

    def save_data(self, obj):
        self.control_dialog.dismiss()
        pass

    def gen_password(self, obj):
        self.control_dialog.dismiss()
        pass

    def check_password(self, obj):
        self.control_dialog.dismiss()
        pass

    def delete_record(self, site, usr):
        toast("Password Deleted")
        pass

    def prepare_content(self, site):

        acc_list = MDList()

        for userid in self.passwd_db[site].keys():
            item = OneLineAvatarIconListItem(text=userid)
            icon = IconLeftWidget(icon="lock", _no_ripple_effect=True)
            del_icon = IconRightWidget(icon="delete-forever", _no_ripple_effect=True)

            item.add_widget(icon)
            item.add_widget(del_icon)

            item.on_release = lambda usr=userid: self.password_controls(site, usr)
            del_icon.on_release = lambda usr=userid: self.delete_record(site, usr)

            acc_list.add_widget(item)
        return acc_list

    def __init__(self, username):  # CHANGE THIS

        self.show_pass_button = MDFlatButton(text="Show", on_release=self.show_passwd)
        self.control_content = self.control_content = Builder.load_string(control_content)
        self.control_dialog = MDDialog(title="Edit Record:",
                                       buttons=[
                                           MDFlatButton(text="Save", size_hint=(0.8, 0.8), on_release=self.save_data),
                                           MDFlatButton(text="Discard",
                                                        on_release=lambda obj: self.control_dialog.dismiss()),
                                           MDFlatButton(text="Judge", on_release=self.check_password),
                                           MDFlatButton(text="Generate", on_release=self.gen_password),
                                           self.show_pass_button,
                                       ], type="custom",
                                       content_cls=self.control_content, radius=[24, 24, 24, 24])
        jsn = json.load(open('uix/data.json'))
        self.passwd_db = jsn['password_db'][username]

        # self.parse_data_list = dict()
        self.ui_list = list()

        exp_head = [ky for ky in self.passwd_db.keys()]

        for site in exp_head:
            accounts = self.passwd_db[site].keys()
            count = len(accounts)

            site_panel_cls = MDExpansionPanelTwoLine(text=str(site), secondary_text=str(count))
            site_panel = MDExpansionPanel(icon="web", panel_cls=site_panel_cls,
                                          content=self.prepare_content(site))
            self.ui_list.append(site_panel)


class UtilityDialog:

    def __init__(self):
        self.file_mode = None
        self.selected_path = ""
        self.path = "/"
        if platform == "win":
            self.path = "C:"
        self.file_manager = MDFileManager(exit_manager=self.on_close_manager, select_path=self.on_select_manager, )
        self.generate_dialog_content_inp = Builder.load_string(gen_pass_dialog_inp)
        self.generate_dialog_content_btn = Builder.load_string(gen_pass_dialog_btn)
        self.judge_dialog_content_inp = Builder.load_string(judge_pass_dialog_inp)
        self.judge_dialog_content_btn = Builder.load_string(judge_pass_dialog_btn)

        self.generate_dialog_content_btn.on_release = self.get_strong_password
        self.judge_dialog_content_btn.on_release = self.get_judge_results

        self.file_inp = Builder.load_string(filename_inp)
        self.file_btn = Builder.load_string(select_file)

        self.generate_dialog = MDDialog(title="Generate Password", size_hint=(0.5, None),
                                        buttons=[self.generate_dialog_content_btn],
                                        type="custom", content_cls=self.generate_dialog_content_inp)
        self.judge_dialog = MDDialog(title="Judge Password", size_hint=(0.5, None),
                                     buttons=[self.judge_dialog_content_btn],
                                     type="custom", content_cls=self.judge_dialog_content_inp)
        self.file_dialog = MDDialog(title="File Name :", size_hint=(0.5, None),
                                    buttons=[self.file_btn],
                                    type="custom", content_cls=self.file_inp)

        self.result_dialog = MDDialog(text="Results", radius=[20, 20, 20, 20])

    def generate_password(self):
        self.generate_dialog.open()

    def judge_password(self):
        self.judge_dialog.open()

    def get_strong_password(self):
        self.result_dialog.text = "New Strong Password Generated of length " + self.generate_dialog_content_inp.text
        Clipboard.copy(self.result_dialog.text)
        self.result_dialog.open()
        self.generate_dialog.dismiss()

    def get_judge_results(self):
        self.result_dialog.text = "Success Password " + self.judge_dialog_content_inp.text + " is Safe"
        self.result_dialog.open()
        self.judge_dialog.dismiss()

    def export_to_chosen(self):
        try:
            self.file_dialog.dismiss()

            seperator = "/"
            if platform == "win":
                seperator = "\\"
            file_handler = open(self.selected_path + seperator + self.file_inp.text, "w")
            file_handler.write("Super Man is Exported")
        except OSError:
            toast("Export Failed! Invalid File")

    def on_close_manager(self, *args):
        self.file_manager.close()
        if len(self.selected_path) != 0:
            try:
                if self.file_mode == "export":
                    self.file_dialog.open()
                elif self.file_mode == "import":
                    file_handler = open(self.selected_path)
                    print(file_handler.read())
            except OSError:
                print("Permission Denied")
        else:
            toast("File Not Selected")

    def on_select_manager(self, path):
        self.selected_path = path
        self.on_close_manager()
        toast(path)

    def export_file(self):
        self.file_mode = "export"
        self.file_manager.search = 'dirs'
        self.file_manager.show(self.path)

    def import_file(self):
        self.file_mode = "import"
        self.file_manager.search = 'all'
        self.file_manager.show(self.path)


class UserScreen(MDScreen):

    def show(self, obj):
        print("backing off")

    def create_user_drawer(self):
        self.usr_drawer = Builder.load_string(nav_drawer)
        self.usr_nav_menu = Builder.load_string(usr_nav_menu)
        self.usr_drawer.add_widget(self.usr_nav_menu)
        self.usr_drawer.anchor = "left"

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)

        self.usr_nav_menu = None
        self.usr_drawer = None
        self.tool_bar = Builder.load_string(usr_toolbar)

        # Box Layout
        self.scr_box_layout = MDBoxLayout(orientation="vertical")
        self.scr_box_layout.add_widget(self.tool_bar)
        self.scroll_view = MDScrollView()
        self.mdlist = MDList()
        self.scroll_view.add_widget(self.mdlist)
        self.scr_box_layout.add_widget(self.scroll_view)

        self.add_widget(self.scr_box_layout)
        self.create_user_drawer()

    def show_user_drawer(self):
        self.usr_drawer.set_state("open")
