import getpass
import secrets
import hashlib
from utils.tcolors import tcolors
from functions.database_operations import Database

db = Database()

def generate_salt():
    salt = secrets.token_bytes(16)
    return salt


def pw_hashing(stored_password, salt):
    hashed_password = hashlib.pbkdf2_hmac('sha256', stored_password.encode(), salt, 100000)
    return hashed_password


def register(db, salt):
    while True:
        username = input('Enter your desired username: ')
        if username:
            db.cursor.execute('SELECT username FROM users WHERE username = ?', (username,))
            result = db.cursor.fetchone()

        if result:
            print(tcolors.WARNING('(-) Username taken, please provide a different username.'))
        else:
            break

    while True:
        password = getpass.getpass('Enter your desired master-password: ')
        pass_validation = getpass.getpass('Please repeat your desired master-password: ')

        if password == pass_validation:
            stored_password = password

            salt = generate_salt()
            hashed_password = pw_hashing(stored_password, salt)

            success_message = '(+) Account created succesfully!'
            seperator = '-' * len(success_message)
            print(f'\n{seperator}\n{tcolors.GREEN(success_message)}\n{seperator}')

            db.insert_user(username, hashed_password, salt)
            break

        else:
            print(tcolors.WARNING('(-) Passwords does not match, try again...'))
