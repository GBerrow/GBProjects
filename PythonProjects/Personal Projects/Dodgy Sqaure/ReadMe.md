I haven't been able to upload this week as I have been busy working. However, in the spare time I had I definitely had fun
creating this mini-game called 'DodgySquare'. Down below you can see the functions within my code i've created.

| Function/Method     | Description                                                                                                                                                  |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `__init__`           | Initializes the `DodgySquare` game, sets up pygame, initializes variables for the game screen, colors, fonts, player, enemies, clock, and game data.      |
| `create_enemy`       | Creates a new enemy at a random position and adds it to the list of enemies.                                                                                 |
| `update_enemy_positions` | Updates the positions of enemies, simulating their movement downwards, and removes enemies that have passed the screen.                                       |
| `detect_collision`   | Detects collisions between the player and enemies.                                                                                                           |
| `show_game_over`     | Displays the "Game Over" text on the screen when the game ends.                                                                                               |
| `replay_game`        | Resets the game state to its initial state to allow the player to replay the game.                                                                            |
| `draw_character`     | Draws a rectangle representing the player or enemies on the game screen.                                                                                      |
| `start_screen`       | Displays the start screen of the game.                                                                                                                       |
| `run`                | The main game loop responsible for running the game. It handles user input, updates game state, draws game elements, and manages the game over screen.     |



