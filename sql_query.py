import sqlite3
import os


def check_for_database():
    return os.path.exists('database.sqlite')


def createDatabase():
    conn = sqlite3.connect('database.sqlite')
    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE "Users"
                (Name text PRIMARY KEY, Password text NOT NULL)''')

    conn.commit()
    conn.close()


def sign_up(username: str, password: str):
    if check_for_database():
        conn = sqlite3.connect('database.sqlite')
        c = conn.cursor()

        # Create table
        command_create = 'CREATE TABLE IF NOT EXISTS ' + username + '( Website text NOT NULL, Account text NOT NULL, Password text NOT NULL, PRIMARY KEY ( Website, Account) )'
        c.execute(command_create)

        ## hashing remaining
        command_insert = 'INSERT INTO Users VALUES ( "' + username + '", "' + password + '" )'
        c.execute(command_insert)

        conn.commit()
        conn.close()
    else:
        print('Database is not connected.\nRestart the program.')


def add_password(website, identifier, password, table):
    if check_for_database():
        conn = sqlite3.connect('database.sqlite')
        c = conn.cursor()

        command_insert = 'INSERT INTO ' + table + ' VALUES ( "' + website + '", "' + identifier + '", "' + password + '" )'
        c.execute(command_insert)

        conn.commit()
        conn.close()
    else:
        print('Database is not connected.\nRestart the program.')


def get_user_Password(user):
    if check_for_database():
        conn = sqlite3.connect('database.sqlite')
        c = conn.cursor()

        command_selectPassword = 'SELECT Password FROM Users WHERE Name = "' + user + '";'

        passwd = str(*list(*c.execute(command_selectPassword)))
        conn.commit()
        conn.close()

        return passwd
    else:
        print('Database is not connected.\nRestart the program.')


def all_websites(user):
    if check_for_database():
        conn = sqlite3.connect('database.sqlite')
        c = conn.cursor()

        command_website = 'SELECT DISTINCT Website FROM "' + user + '"'
        tup = c.execute(command_website)

        websites = [list(row)[0] for row in tup]
        conn.commit()
        conn.close()

        return websites

    else:
        print('Database is not connected.\nRestart the program.')


def all_accounts(user, website):
    if check_for_database():
        conn = sqlite3.connect('database.sqlite')
        c = conn.cursor()

        command_account = 'SELECT Account FROM "' + user + f'" WHERE Website LIKE "%{website}%"'
        tup = c.execute(command_account)

        accounts = [list(row)[0] for row in tup]
        conn.commit()
        conn.close()

        return accounts

    else:
        print('Database is not connected.\nRestart the program.')


def show_password(user, web, account):
    if check_for_database():
        conn = sqlite3.connect('database.sqlite')
        c = conn.cursor()

        command_password = f'SELECT * FROM "{user}" ' \
                           f'WHERE Website LIKE "%{web}%" ' \
                           f'AND Account LIKE "%{account}%" ;'

        tup = c.execute(command_password)

        for row in tup:
            print(*list(row), sep=' : ')

        conn.commit()
        conn.close()
    else:
        print('Database is not connected.\nRestart the program.')


def delete(user, website, account):
    if check_for_database():
        conn = sqlite3.connect('database.sqlite')
        c = conn.cursor()

        command_delete = f'DELETE FROM "{user}" ' \
                         f'WHERE Website LIKE "%{website}%" ' \
                         f'AND Account LIKE "%{account}%" ;'

        c.execute(command_delete)

        conn.commit()
        conn.close()

    else:
        print('Database is not connected.\nRestart the program.')


def modify(user, website, account, password):
    if check_for_database():
        conn = sqlite3.connect('database.sqlite')
        c = conn.cursor()

        command_modify = f'UPDATE "{user}" ' \
                         f'SET Password = "{password}" ' \
                         f'WHERE Account = "{account}" ' \
                         f'AND Website = "{website}" ;'

        c.execute(command_modify)

        conn.commit()
        conn.close()

    else:
        print('Database is not connected.\nRestart the program.')
