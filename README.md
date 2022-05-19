# Password Manager

## Upcoming 
GUI Password Manager

## Application Structure

```text
Password Manager
    package: ui
        module: ui_manager
        module: MainInterface
        module: Login
            class: Login_Ui
            function: login_control
        module: Signup
            class: Signup_Ui
            function: signup_control
        module: Check_Generate
            class: Check_Generate_Ui
            function: check_generate_control
        module: components
    package: api
        module: Login
        module: Signup
        module: Check_Password
        module: Generate_Password
        module: security
        module: dbaccess
```