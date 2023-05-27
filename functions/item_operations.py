import pyperclip
from functions.database_operations import Database
from functions.password_generation import generate_random_password
from functions.password_generation import get_password_length
from utils.tcolors import tcolors


db = Database()


def item_creation(db, user_id):
    item_name = input('Enter the name of the stored item: ')
    username = input('Add a username/email address: ')

    while True:
        password_input = input('Generate a password or enter one manually? (y/n): ')
        if password_input == 'y':
            password_length = get_password_length()
            password = generate_random_password(password_length)
            print(f'This is your newly created password: {tcolors.GREEN(password)}')
            break
        elif password_input == 'n':
            password = input('Enter a password: ')
            break
        else:
            print(tcolors.WARNING('(-) Incorrect entry...'))

    url= input('Enter a url to where this account is used (optional): ')
    notes = input('Notes (optional): ')

    print(tcolors.GREEN('(+) Item successfully created!'))

    db.add_item(user_id, item_name, username, password, url, notes)
    return True


def item_retrieval(db, user_id):
    items = db.retrieve_item(user_id)
    if not items:
        print(tcolors.WARNING('(-) No items matching your search found!'))
    else:
        print(tcolors.GREEN('(+) Items: '))
        for i, item in enumerate(items, start=1):
            print(f'{i}, Item Name: {item[0]}')

    while True:
            item_number_input = input(tcolors.GREEN('(+) Select which item you want to access (select with a number): '))
            if not item_number_input.isdigit():
                print(tcolors.WARNING('(-) Invalid selection!'))
                continue
            item_number = int(item_number_input)
            if item_number < 1 or item_number > len(items):
                print(tcolors.WARNING('(-) Invalid selection!'))
                continue
            else:
                selected_item = items[item_number - 1]
                print(tcolors.GREEN('(+) Selected item: '))
                print(f'\n'
                      f'Item Name: {tcolors.GREEN(selected_item[0])}\n'
                      f'Username: {tcolors.GREEN(selected_item[1])}\n'
                      f'Password: {tcolors.GREEN(selected_item[2])}\n'
                      f'URL: {tcolors.GREEN(selected_item[3])}\n'
                      f'Notes: {tcolors.GREEN(selected_item[4])}')
                pyperclip.copy(selected_item[2])
                print(tcolors.GREEN('(+) Password copied to clipboard!'))
                input(tcolors.GREEN('\n(+) Press Enter to continue...'))
                break