import hashlib
import getpass
from utils.tcolors import tcolors
from functions.database_operations import Database


db = Database()


def login(db):
    username = input('Enter your username: ')

    max_attempts = 3
    user_id = None
    for attempt in range(max_attempts):
        password = getpass.getpass('Enter your password: ')

        result = db.login_user(username)

        if result:
            user_id = result[0]
            stored_password = result[1]
            salt = result[2]
            hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)

            if hashed_password == stored_password:
                logged_in = True
                print(tcolors.GREEN('(+) Login successful!')) 
                break  

            else:
                logged_in = False
                print(tcolors.WARNING('(-) Wrong password, try again...'))

        else:
            logged_in = False
            print(tcolors.WARNING('(-) User not found!'))

    else:
        logged_in = False
        error_message = '(-) Maximum number of attempts reached!'
        seperator = '-' * len(error_message)
        print(f'\n{seperator}\n{tcolors.WARNING(error_message)}\n{seperator}')

    return logged_in, username, user_id