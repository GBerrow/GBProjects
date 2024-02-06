# Rock paper scissors...But with 2 improvements from the regular game!
# Score Tracking - Keep track of the user's and AI's scores and display them after each round.
# Extended Moves - Introduce additional moves to make the game more exciting.
# you can also choose from additional moves (lizard and spock) to add more variety to the gameplay. Have fun!


import random

class RPS:
    def __init__(self):
        print('Welcome to RPS 9000!')

        # Moves for display
        self.moves = {
            'rock': '🪨', 'paper': '📜', 'scissors': '✂️',
            'lizard': '🦎', 'spock': '🖖'
        }
        self.valid_moves = list(self.moves.keys())

        # Scores
        self.user_score = 0
        self.ai_score = 0

    def play_game(self):
        # Get the user input and lower() it
        user_move = input('Rock, paper, scissors, lizard, or spock? >> ').lower()

        # Give the user an option to exit
        if user_move == 'exit':
            print('Thanks for playing!')
            self.display_scores()
            return False

        # Check that the user made a valid move, else try again
        if user_move not in self.valid_moves:
            print('Invalid move...')
            return True

        # The AI's move
        ai_move = random.choice(self.valid_moves)

        self.display_moves(user_move, ai_move)
        self.check_move(user_move, ai_move)
        self.display_scores()
        return True

    def display_moves(self, user_move, ai_move):
        # Display everything nicely
        print('----')
        print(f'You: {self.moves[user_move]}')
        print(f'AI: {self.moves[ai_move]}')
        print('----')

    def check_move(self, user_move, ai_move):
        # The game logic
        if user_move == ai_move:
            print('It is a tie!')
        elif (
            (user_move, ai_move) in [('rock', 'scissors'), ('scissors', 'paper'),
                                     ('paper', 'rock'), ('rock', 'lizard'),
                                     ('lizard', 'spock'), ('spock', 'scissors'),
                                     ('scissors', 'lizard'), ('lizard', 'paper'),
                                     ('paper', 'spock'), ('spock', 'rock')]
        ):
            print('You win!')
            self.user_score += 1
        else:
            print('AI wins...')
            self.ai_score += 1

    def display_scores(self):
        print(f'Scores: You - {self.user_score}, AI - {self.ai_score}')

if __name__ == '__main__':
    rps = RPS()

    while rps.play_game():
        pass


if __name__ == '__main__':
    rps = RPS()

    while True:
        rps.play_game()