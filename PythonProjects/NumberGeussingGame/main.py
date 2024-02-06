# This is the simple Number Guessing Game, but I have added humorous messages as well as a hint system.
# So it looks more visually pleasing to the eye!


from random import randint

lower_num, higher_num = 1, 20
random_number: int = randint(lower_num, higher_num)
print(f'Guess the number in the range from {lower_num} to {higher_num}.')

max_guesses = 5
guess_count = 0

def provide_hint(user_guess, random_number):
    if user_guess < random_number:
        return 'Hint: Try going higher!'
    elif user_guess > random_number:
        return 'Hint: Aim a little lower!'
    else:
        return 'Hint: You guessed it correctly!'

while guess_count < max_guesses:
    try:
        user_guess: int = int(input('Guess: '))
    except ValueError as e:
        print('Please enter a valid number.')
        continue

    guess_count += 1

    if user_guess == random_number:
        print('You guessed it correctly! You must have a secret alliance with the numbers. Well played!')
        break
    else:
        print(provide_hint(user_guess, random_number))

if guess_count != max_guesses and user_guess != random_number:
    print(f'Sorry, you have reached the maximum number of guesses. The correct number was {random_number}.'
          f' The number is now taking a coffee break. Better luck next time!')
