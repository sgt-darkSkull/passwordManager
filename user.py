import os
import sql_query as sql
from styling import color
import password_checker
import password_generator



class Login:

    def __init__(self):
        self.username = ''
        self.password = ''
        self.is_login = False
        self.website = ''
        self.account = ''

        try:
            os.system('clear')
            print(color.BOLD + color.RED + 'User Login'.center(30) + color.END)
            print('')
            self.username = input('Enter Username : ')
            self.password = input('Enter Password : ')

            auth = sql.get_user_Password(self.username)

            if auth == self.password:
                self.is_login = True
            else:
                self.is_login = False

        except:
            print('An Error Occurred!')
            return

    def get_Website(self, arr):
        for n, web in enumerate(arr):
            print(f'{n + 1}. {web}')

        self.website = input('Select Website : ')

    def get_Account(self, arr):
        for n, acc in enumerate(arr):
            print(f'{n + 1}. {acc}')

        self.account = input('Select Account :')

    def add_password(self):
        os.system('clear')
        print(color.BOLD + color.RED + 'Add Password'.center(30) + color.END)
        print('')
        url = input('Website/Url : ')
        identifier = input('Account/Username/Identifier : ')
        password = input('Password : ')
        sql.add_password(url, identifier, password, self.username)

    def delete_password(self):
        os.system('clear')
        print(color.BOLD + color.RED + 'Delete Passwrod'.center(30) + color.END)
        print('')
        ## print(all website)

        web = input('Select Website : ')
        # print all accounts for the website
        acc = input('Select Account :')
        # print confirmation message
        # print success message
        return

    def modify_password(self):
        os.system('clear')
        print(color.BOLD + color.RED + 'Modify Password'.center(30) + color.END)
        print('')
        # print(all website)
        web = input('Select Website : ')
        # print all accounts for the website
        acc = input('Select Account :')

        if input('Want to generate Password (Y/N): ').lower() == 'y':
            password_generator.main()

        new_pass = input('New Password : ')

        # execute SQL query
        # print confirmation message
        # print success message
        return

    def show_password(self):
        os.system('clear')
        print(color.BOLD + color.RED + 'Show Password'.center(30) + color.END)
        print('')

        websites = sql.all_websites(self.username)
        self.get_Website(websites)

        accounts = sql.all_accounts(self.username, self.website)
        self.get_Account(accounts)

        sql.show_password(self.username, self.website, self.account)

        return

    def main(self):

        while True:
            os.system('clear')
            print(color.BOLD + color.RED + self.username.center(30) + color.END)
            print('')
            print('1. Add Password')
            print('2. Delete a Password')
            print('3. Modify a Password')
            print('4. Show Password')
            print('5. Generate a strong password')
            print('6. Check my password if secure')
            print('7. Log out')

            ch = input().lower()

            if ch == '1' or ch == 'add':
                self.add_password()
            elif ch == '2' or ch == 'delete':
                self.delete_password()
            elif ch == '3' or ch == 'modify':
                self.modify_password()
            elif ch == '4' or ch == 'show':
                self.show_password()
            elif ch == '5' or ch == 'generate':
                password_generator.main()
            elif ch == '6' or ch == 'check':
                password_checker.main()
            elif ch == '7' or ch == 'exit':
                return
            else:
                print('Invalid Choice!')

            en = input('Want to Log Out? (Y/N) : ').lower()

            if en == 'y':
                return
            else:
                pass


def user_login():
    user = Login()

    if user.is_login:
        user.main()
    else:
        print('Login Failure, Wrong password or username..')
        return


def user_signup():
    try:
        os.system('clear')
        print(color.BOLD + color.RED + 'User Sign Up'.center(30) + color.END)
        print('')
        username = input('Enter Username : ')
        password = input('Enter Password : ')
        if password == input('Confirm Password : '):
            sql.sign_up(username, password)
        else:
            print('Wrong Password...\nSign up failure!')
            return
    except:
        print('An Error Occurred!')
        return
