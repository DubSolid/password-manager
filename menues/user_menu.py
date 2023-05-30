from utils.tcolors import tcolors
from functions.item_operations import item_creation
from functions.item_operations import item_retrieval
from functions.item_operations import item_update
from functions.item_operations import item_deletion
from functions.database_operations import Database


def user_menu(logged_in, username, user_id):
    db = Database()

    while logged_in:
        print('Logged in as ' + tcolors.GREEN (f'{username}'))
        print('Please choose an option:')
        print('1. Add a new item to your vault')
        print('2. Retrieve an item')
        print('3. Update an existing item')
        print('4. Delete an item')
        print('5. Log out of your vault')

        choice = input(tcolors.GREEN('(+) Enter an option: '))

        if not choice:
            continue

        selection_made = False

        while not selection_made:
            match choice:
                case '1':
                    item_creation(db, user_id)
                    selection_made = True
                case '2':
                    item_retrieval(db, user_id)
                    selection_made = True
                case '3':
                    item_update(db, user_id)
                    selection_made = True
                case '4':
                    item_deletion(db, user_id)
                    selection_made = True
                    pass
                case '5':
                    logout_message = '(-) Logging out...'
                    seperator = '-' * len(logout_message)
                    print(f'\n{seperator}\n{tcolors.WARNING(logout_message)}\n{seperator}')
                    return True
                case _:
                    invalid_message = '(-) Invalid option, please try again...'
                    seperator = '-' * len(invalid_message)
                    print(f'\n{seperator}\n{tcolors.WARNING(invalid_message)}\n{seperator}')


