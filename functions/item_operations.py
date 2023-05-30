import pyperclip
from functions.database_operations import Database
from functions.password_generation import generate_random_password
from functions.password_generation import get_password_length
from utils.tcolors import tcolors


def item_creation(db: Database, user_id):
    item_name = input('Enter the name of the stored item: ')
    username = input('Add a username/email address: ')

    while True:
        print(tcolors.GREEN('(+) You have two options. Either getting a generated password, or the ability to enter one manually.'))
        password_input = input('Generate a password (y/n): ')
        if password_input == 'y':
            password_length = get_password_length()
            password = generate_random_password(password_length)
            print(f'This is your newly created password: {tcolors.GREEN(password)}')
            break
        elif password_input == 'n':
            password = input('Enter a password manually: ').strip()
            break
        else:
            print(tcolors.WARNING('(-) Incorrect entry...'))

    url= input('Enter a url to where this account is used (optional): ')
    notes = input('Notes (optional): ')

    print(tcolors.GREEN('(+) Item successfully created!'))

    db.add_item(user_id, item_name, username, password, url, notes)
    return True


def item_retrieval(db: Database, user_id):
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


def item_update(db: Database, user_id):
    items = db.retrieve_item(user_id)

    if not items:
        print(tcolors.WARNING('(-) No items matching your search found!'))
    else:
        print(tcolors.GREEN('(+) Items: '))
        for i, item in enumerate(items, start=1):
            print(f'{i}, Item Name: {item[0]}')

    while True:
        item_number_input = input(tcolors.GREEN('(+) Select which item you want to update (select with a number): '))
        if not item_number_input.isdigit():
            print(tcolors.WARNING('(-) Invalid selection!'))
            continue
        item_number = int(item_number_input)
        if item_number < 1 or item_number > len(items):
            print(tcolors.WARNING('(-) Invalid selection!'))
            continue
        else:
            selected_item = items[item_number - 1]
            new_item_name = input('Enter a new item name: ')
            new_username = input('Enter a new username/email: ')

            while True:
                password_input = input('Generate a new password or enter one manually? (y/n): ')
                if password_input.lower() == 'y':
                    password_length = get_password_length()
                    new_password = generate_random_password(password_length)
                    print(f'This is your newly created password: {tcolors.GREEN(new_password)}')
                    break
                elif password_input.lower() == 'n':
                    new_password = input('Enter a new password: ')
                    break
                else:
                    print(tcolors.WARNING('(-) Incorrect entry...'))

            new_url = input('Enter a new url: ')
            new_notes = input('Enter new notes: ')

            db.update_item(selected_item[0], user_id, new_item_name, new_username, new_password, new_url, new_notes)
            break


def item_deletion(db: Database, user_id):
    items = db.retrieve_item(user_id)
    item_ids = {}
    
    if not items:
        print(tcolors.WARNING('(-) No items matching your search found!'))
        return

    else:
        print(tcolors.GREEN('(+) Items: '))
        for i, item in enumerate(items, start=1):
            print(f'{i}, Item Name: {item[1]}')
            item_ids[i] = item[0]

    while True:
        item_number_input = input(tcolors.GREEN('(+) Select which item you want to delete (select with a number): '))
        
        if not item_number_input.isdigit():
            print(tcolors.WARNING('(-) Invalid selection!'))
            continue
        
        item_number = int(item_number_input)
        
        if item_number < 1 or item_number > len(items):
            print(tcolors.WARNING('(-) Invalid selection!'))
            continue

        deletion_confirmation = input(tcolors.WARNING(f'Are you sure you want to delete item number "{item_number}"? (y/n): '))
        
        if deletion_confirmation.lower() == 'y':
            db.delete_item(item_ids[item_number], user_id)
            print(tcolors.GREEN('(+) Item successfully deleted!'))
            break