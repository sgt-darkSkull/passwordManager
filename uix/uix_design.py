root = """
MDNavigationLayout:
"""

main_screen = """
MDScreen:
    id: main_screen
    name: "MainScreen"
    
    MDLabel:
        text: "Deadlock\\nPassword Manager"
        # text: "Password Manager"
        halign: "center"
        pos_hint: {"center_y": 0.8}
        font_style: "H1"
        font_name:"uix/fonts/PermanentMarker"
        # font_name:"uix/fonts/RubikDirt"
        font_size: "45dp"
    
    MDCard:
        id: login_card
        size_hint: 0.7, 0.4
        pos_hint: {"center_x": 0.5, "center_y": 0.4 }
        style: "elevated"
        radius: "24dp"
        md_bg_color: app.theme_cls.bg_dark
        MDRelativeLayout:
            id: main_form
            MDLabel:
                text: "Login"
                font_style: "H5"
                halign: "center"
                pos_hint: {"center_x" : 0.5, "center_y" : 0.9} 
    MDIconButton:   
        id: settings_button
        icon: "cog"
        pos_hint: {"center_x": 0.9 , "center_y": 0.05}
"""

userInputField = """
MDTextField:
    id: usernameField
    write_tab: False
    hint_text: "Enter Username"
    size_hint: 0.8, None
    halign: "center"
    pos_hint: {"center_x" : 0.5, "center_y" : 0.7}
"""

signup_cnt = """
MDBoxLayout:
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "120dp"
    MDTextField:
        id: full_name
        write_tab: False
        hint_text: "Enter Full Name"
        size_hint: 0.8, None
        halign: "center"
        pos_hint: {"center_x": 0.5}
    MDTextField:
        id: confirm_password
        write_tab: False
        hint_text: "Confirm Password"
        size_hint: 0.8, None
        halign: "center"
        pos_hint: {"center_x": 0.5}
        password: True
    
"""

passwdInputField = """
MDTextField:
    id: passwordField
    write_tab: False
    hint_text: "Enter Password"
    size_hint: 0.8, None
    halign: "center"
    pos_hint: {"center_x" : 0.5, "center_y" : 0.5}
    password: True
"""

loginButton = """
MDFillRoundFlatButton:
    text: "Log In"
    size_hint_x: 0.8
    pos_hint: {"center_x" : 0.5, "center_y" : 0.3}
"""

singupButton = """
MDFillRoundFlatButton:
    text: "Sign Up"
    size_hint_x: 0.8
    pos_hint: {"center_x" : 0.5, "center_y" : 0.1}
"""

confirmButton = """
MDFillRoundFlatButton:
    text: "Sign Up"
    size_hint_x: 0.8
    pos_hint: {"center_x" : 0.5, "center_y" : 0.4}
"""

nav_drawer = """
MDNavigationDrawer:
    id: nav_drawer
    mg_bg_color: app.theme_cls.bg_light
    anchor: "right"
    padding: 30, 56, 12, 16
    type: "modal"
"""

nav_menu = """
MDNavigationDrawerMenu:
    MDNavigationDrawerHeader:
        id: drw_head
        spacing: "4dp"
        padding: "12dp", 0, 0, "56dp"
        title: "Account Login"
        text: "user@mail.com"  
    
    MDNavigationDrawerItem:
        id: drw_theme
        icon: "theme-light-dark"
        text: "Change Theme"
        text_color: 76/255,175/255,80/255,1
        selected_color: 76/255,175/255,80/255,1
        on_release: app.change_theme()
    
    MDNavigationDrawerItem:
        id: drw_genPass
        icon: "form-textbox-password"
        text: "Generate Password"
        text_color: 76/255,175/255,80/255,1
        selected_color: 76/255,175/255,80/255,1
        on_release: app.util_dialogs.generate_password()
    MDNavigationDrawerItem:
        id: drw_chkPass
        icon: "check-decagram"
        text: "Judge Password"
        text_color: 76/255,175/255,80/255,1
        selected_color: 76/255,175/255,80/255,1
        on_release: app.util_dialogs.judge_password()
    MDNavigationDrawerItem:
        id: drw_export
        icon: "file-export"
        text: "Export Passwords"
        text_color: 76/255,175/255,80/255,1
        selected_color: 76/255,175/255,80/255,1
        on_release: app.util_dialogs.export_file()
    MDNavigationDrawerItem:
        id: drw_import
        icon: "file-import"
        text: "Import Passwords"
        text_color: 76/255,175/255,80/255,1
        selected_color: 76/255,175/255,80/255,1
        on_release: app.util_dialogs.import_file()
    MDNavigationDrawerItem:
        id: drw_exit
        icon: "exit-to-app"
        text: "Exit"
        text_color: 76/255,175/255,80/255,1
        selected_color: 76/255,175/255,80/255,1
        on_release: app.close_app()
"""

usr_nav_menu = """
MDNavigationDrawerMenu:
    MDNavigationDrawerHeader:
        id: drw_head
        spacing: "4dp"
        padding: "12dp", 0, 0, "56dp"
        title: "Account Login"
        text: "user@mail.com"  
    
    MDNavigationDrawerItem:
        id: drw_theme
        icon: "theme-light-dark"
        text: "Change Theme"
        text_color: 76/255,175/255,80/255,1
        selected_color: 76/255,175/255,80/255,1
        on_release: app.change_theme()
    
    MDNavigationDrawerItem:
        id: drw_genPass
        icon: "form-textbox-password"
        text: "Generate Password"
        text_color: 76/255,175/255,80/255,1
        selected_color: 76/255,175/255,80/255,1
        on_release: app.util_dialogs.generate_password()
    MDNavigationDrawerItem:
        id: drw_chkPass
        icon: "check-decagram"
        text: "Judge Password"
        text_color: 76/255,175/255,80/255,1
        selected_color: 76/255,175/255,80/255,1
        on_release: app.util_dialogs.judge_password()
    MDNavigationDrawerItem:
        id: drw_export
        icon: "file-export"
        text: "Export Passwords"
        text_color: 76/255,175/255,80/255,1
        selected_color: 76/255,175/255,80/255,1
        on_release: app.util_dialogs.export_file()
    MDNavigationDrawerItem:
        id: drw_import
        icon: "file-import"
        text: "Import Passwords"
        text_color: 76/255,175/255,80/255,1
        selected_color: 76/255,175/255,80/255,1
        on_release: app.util_dialogs.import_file()
    MDNavigationDrawerItem:
        id: drw_logout
        icon: "exit-to-app"
        text: "Log Out"
        text_color: 76/255,175/255,80/255,1
        selected_color: 76/255,175/255,80/255,1
        on_release: app.logout_user()
"""

gen_pass_dialog_inp = """
MDTextField:
    id: gen_pass_inp
    write_tab: False
    hint_text: "Enter Password Length"
    size_hint: 0.8, None
    halign: "center"
    pos_hint: {"center_x" : 0.5, "center_y" : 0.5}
"""

gen_pass_dialog_btn = """
MDFillRoundFlatButton:
    text: "Generate"
    size_hint_x: 0.8
    pos_hint: {"center_x" : 0.5, "center_y" : 0.4}
"""

judge_pass_dialog_inp = """
MDTextField:
    id: judge_pass_inp
    write_tab: False
    hint_text: "Enter Password"
    size_hint: 0.8, None
    halign: "center"
    pos_hint: {"center_x" : 0.5, "center_y" : 0.5}
"""
judge_pass_dialog_btn = """
MDFillRoundFlatButton:
    text: "Judge"
    size_hint_x: 0.8
    pos_hint: {"center_x" : 0.5, "center_y" : 0.4}
"""

filename_inp = """
MDTextField:
    id: judge_pass_inp
    write_tab: False
    hint_text: ""
    size_hint: 0.8, None
    halign: "center"
    pos_hint: {"center_x" : 0.5, "center_y" : 0.5}
"""

select_file = """
MDFillRoundFlatButton:
    text: "Select"
    size_hint_x: 0.8
    pos_hint: {"center_x" : 0.5, "center_y" : 0.4}
    on_release: app.util_dialogs.export_to_chosen()
"""

usr_toolbar = """
MDTopAppBar:
    title: "Account Login"
    elevation: 15
    
    left_action_items: [["menu", lambda obj: app.userScreen.show_user_drawer()]]
    right_action_items: [["lock-open-plus", lambda obj: app.add_new_password()]]
"""

password_edit_dialog_content = """
MDBoxLayout:
    orientation: "vertical"
    spacing: "10dp"
    size_hint_y: None
    height: "140dp"
    MDTextField:
        id: edit_domain_name
        write_tab: False
        hint_text: "Domain Name:"
        size_hint: 0.8, None
        halign: "center"
        pos_hint: {"center_x": 0.5}
    MDTextField:
        id: edit_username
        write_tab: False
        hint_text: "Username:"
        size_hint: 0.8, None
        halign: "center"
        pos_hint: {"center_x": 0.5}
        password: True 
    MDTextField:
        id: edit_password
        write_tab: False
        hint_text: "Password:"
        size_hint: 0.8, None
        halign: "center"
        pos_hint: {"center_x": 0.5}
        password: True 
    MDWidget:
"""

control_content = """
MDBoxLayout:
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "200dp"
    MDTextField:
        id: domain
        hint_text: "Domain Name"
        size_hint: 0.8, None
        halign: "center"
        pos_hint: {"center_x": 0.5}
        icon_left: "key-variant"
    MDTextField:
        id: username
        hint_text: "Username:"
        size_hint: 0.8, None
        halign: "center"
        pos_hint: {"center_x": 0.5}
        icon_left: "key-variant"
    MDTextField:
        id: user_passwd
        size_hint: 0.8, None
        halign: "center"
        pos_hint: {"center_x": 0.5}
        hint_text: "Password"
        password: True
        icon_left: "key-variant"
"""
