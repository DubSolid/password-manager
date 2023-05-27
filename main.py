import sys
from utils.tcolors import tcolors
from utils.welcomes import print_banner
from menues.login_menu import login_menu
from menues.user_menu import user_menu
from functions.database_operations import Database


def main():
    db = Database()
    db.create_tables()
    try:
        while True:
            print_banner()
            logged_in, username, user_id = login_menu(db)
            if not logged_in and username is None:
                break
            if logged_in:
                logged_in = user_menu(logged_in, username, user_id)
            if logged_in is None:
                break
    except KeyboardInterrupt:
        interrupt_message = '(-) Exiting the program due to user interruption...'
        seperator = '-' * len(interrupt_message)
        print(f'\n{seperator}\n{tcolors.WARNING(interrupt_message)}\n{seperator}')
        sys.exit(0)
    db.conn.close()

if __name__ == "__main__":
    main()