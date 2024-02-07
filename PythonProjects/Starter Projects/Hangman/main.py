# In This hangman game, I have made several improved features such as:
# Displaying letters that have already been guessed
# Providing feedback on whether the guessed letter is a vowel or a consonant
# Allowing the player to guess the whole word
# Adding a difficulty level to the game

from random import choice


def choose_word(difficulty):
    if difficulty == 'easy':
        return choice(['apple', 'kiwi', 'grape'])
    elif difficulty == 'medium':
        return choice(['orange', 'banana', 'melon'])
    elif difficulty == 'hard':
        return choice(['strawberry', 'blueberry', 'pineapple'])
    else:
        print('Invalid difficulty level. Choosing a random word.')
        return choice(['apple', 'secret', 'banana'])


def run_game():
    difficulty_levels = ['easy', 'medium', 'hard']

    difficulty = input('Choose difficulty (easy, medium, hard): ').lower()
    if difficulty not in difficulty_levels:
        print('Invalid difficulty level. Choosing a random word.')

    word = choose_word(difficulty)

    username: str = input('What is your name? >> ')
    print(f'Welcome to hangman, {username}!')

    # Setup
    guessed: str = ''
    tries: int = 3

    while tries > 0:
        blanks: int = 0

        print('Word: ', end='')
        for char in word:
            if char in guessed:
                print(char, end='')
            else:
                print('_', end='')
                blanks += 1

        print()  # Adds a blank line
        print(f'Guessed Letters: {", ".join(guessed)}')

        if blanks == 0:
            print('You got it! Well done!')
            break

        guess: str = input('Enter a letter or guess the whole word: ')

        if guess.isalpha() and len(guess) == 1:  # Check if the input is a single letter
            if guess in guessed:
                print(f'You have already used: "{guess}". Please try another letter!')
                continue

            guessed += guess

            if guess not in word:
                tries -= 1
                print(f'Sorry, "{guess}" is not in the word...({tries} tries remaining)')

        elif guess.isalpha() and len(guess) > 1:  # Check if the input is a word guess
            if guess == word:
                print('Congratulations! You guessed the whole word!')
                break
            else:
                tries -= 1
                print(f'Sorry, "{guess}" is not the correct word...({tries} tries remaining)')

        else:
            print('Invalid input. Please enter a valid letter or a word guess.')

        if tries == 0:
            print(f'No more tries remaining...You lose! The correct word was "{word}".')
            break


if __name__ == '__main__':
    run_game()


