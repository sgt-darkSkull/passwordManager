import os
from styling import color
import password_checker
import password_generator
import user


def main():
    while True:

        os.system('clear')
        print(color.BOLD + color.GREEN + color.UNDERLINE + 'Password Manager'.center(30) + color.END)
        print('')
        print('1. Login')
        print('2. Sign Up')
        print('3. Generate a strong password')
        print('4. Check my password if secure')
        print('5. Exit')

        ch = input().lower()

        if ch == '1' or ch == 'login':
            user.user_login()

        elif ch == '2' or ch == 'sign':
            user.user_signup()

        elif ch == '3' or ch == 'generate':

            password_generator.main()

        elif ch == '4' or ch == 'check':
            password_checker.main()

        elif ch == '5' or ch == 'exit':
            return

        else:
            print('Invalid Choice!')

        print('Want to Exit Program (Y/N) : ', end='')
        en = input().lower()

        if en == 'y':
            return
        else:
            pass


if __name__ == '__main__':

    if not os.path.exists('database.sqlite'):
        print('Looks like you are running this program first time...')
        print('We are creating setting up your files..')
        print('Please wait a few seconds..😄')
        os.system('sleep 10s')

    main()
