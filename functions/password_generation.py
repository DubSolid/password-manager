import random
import string


def generate_random_password(length=12):
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    all_characters = uppercase_letters + lowercase_letters + digits + symbols
    password = [random.choice(all_characters) for _ in range(length)]

    random.shuffle(password)
    return ''.join(password)


def get_password_length():
    while True:
        try:
            password_length = int(input("Enter the desired password length (minimum 10): "))
            if password_length < 10:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive number.")
    return password_length
