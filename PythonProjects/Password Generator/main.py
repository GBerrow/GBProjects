# Password generator with improved functions:
# Extra function called 'password strength' that evaluates the overall strength of the password.
# As it is based on length and usage of uppercase letters and symbols.
# User-friendly input - Making the password customisation more easily accessible!


import string
import secrets


def contains_upper(password: str) -> bool:
    return any(char.isupper() for char in password)


def contains_symbols(password: str) -> bool:
    return any(char in string.punctuation for char in password)


def password_strength(password: str) -> str:
    length_strength = "Weak" if len(password) < 12 else "Strong"
    upper_strength = "Weak" if not contains_upper(password) else "Strong"
    symbol_strength = "Weak" if not contains_symbols(password) else "Strong"

    return f'Length: {length_strength}, Uppercase: {upper_strength}, Symbols: {symbol_strength}'


def get_user_input() -> tuple[int, bool, bool]:
    length = int(input("Enter password length: "))
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'

    return length, include_symbols, include_uppercase


def generate_password(length: int, symbols: bool, uppercase: bool) -> str:
    combination = string.ascii_lowercase + string.digits

    if symbols:
        combination += string.punctuation

    if uppercase:
        combination += string.ascii_uppercase

    combination_length = len(combination)
    new_password = ''.join(combination[secrets.randbelow(combination_length)] for _ in range(length))

    return new_password


if __name__ == '__main__':
    length, symbols, uppercase = get_user_input()

    for i in range(1, 6):
        new_pass = generate_password(length=length, symbols=symbols, uppercase=uppercase)
        specs = f'{password_strength(new_pass)}'
        print(f'{i} -> {new_pass} ({specs})')
