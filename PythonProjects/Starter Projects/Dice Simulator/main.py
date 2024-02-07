# I have added a unique feature to this dice simulator game,
# By adding the ability to simulate different types of dice and not just six-sided ones.
# Users can specify both the number of dice (amount) and the number of sides on each die (sides).
# This makes the game more versatile and allows for different types of dice simulations.

import random


def roll_dice(amount: int = 2, sides: int = 6) -> list[int]:
    if amount <= 0 or sides <= 0:
        raise ValueError

    rolls: list[int] = []
    total_sum: int = 0

    for i in range(amount):
        random_roll: int = random.randint(1, sides)
        rolls.append(random_roll)
        total_sum += random_roll

    return rolls, total_sum


def main():
    while True:
        try:
            user_input_amount: str = input('How many dice would you like to roll? (Type "exit" to end): ')
            if user_input_amount.lower() == 'exit':
                print('Thanks for playing!')
                break

            user_input_sides: str = input('How many sides does each die have? ')

            rolls, total_sum = roll_dice(int(user_input_amount), int(user_input_sides))
            print(f'Rolls: {rolls}, Total sum: {total_sum}')
        except ValueError:
            print('(Please enter valid numbers)')


if __name__ == '__main__':
    main()

