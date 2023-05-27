from .tcolors import tcolors

# Define a function to print a banner with a logo in green text
def banner():
    print(tcolors.GREEN('''
     _____  _______ _______ _______     _______ _______ _______ _______      _    _ _______ _     _        _______
    |_____] |_____| |______ |______ ___ |______ |_____| |______ |______       \  /  |_____| |     | |         |   
    |       |     | ______| ______|     ______| |     | |       |______        \/   |     | |_____| |_____    |                                                                                                                                   
    '''))


# Define a function to print a welcome message for the password vault in red text
def display_welcome():
    print(tcolors.GREEN('Welcome to Pass-Safe Vault!'))


# Define a function to print a welcome message for when the user logs into the password vault in red text
def welcomed_to_vault():
        seperator = '-' * 22
        print('\n')
        print(seperator)
        print(tcolors.GREEN('Welcome to your vault!'))
        print(seperator)


# Define a function to print the banner and the welcome message for the password vault
def print_banner():
     banner()
     display_welcome()
