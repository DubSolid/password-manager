import sys
from functions.database_operations import Database
from utils.tcolors import tcolors
from functions.register import register
from functions.register import generate_salt
from functions.login import login

db = Database()

def print_menu():
    print('Please choose an option:')
    print('1. Register a new user')
    print('2. Log in to an existing user')
    print('3. Exit the program')


def login_menu(db):
    salt = generate_salt()

    logged_in = False
    while True:
        if not logged_in:
            print_menu()
            choice = input(tcolors.GREEN('(+) Enter an option: '))
        
            match choice:
                case '1':
                    registerd = register(db, salt)
                    if registerd:
                        continue
                case '2':
                    logged_in, username, user_id = login(db)
                    if logged_in:
                        return logged_in, username, user_id
                case'3':
                    exit_message = '(-) Exiting...'
                    seperator = '-' * len(exit_message)
                    print(f'\n{seperator}\n{tcolors.WARNING(exit_message)}\n{seperator}')
                    sys.exit(0)
                case _:
                    invalid_message = '(-) Invalid option, please try again...'
                    seperator = '-' * len(invalid_message)
                    print(f'\n{seperator}\n{tcolors.WARNING(invalid_message)}\n{seperator}')
