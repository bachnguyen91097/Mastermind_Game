# Mastermind Game

This one-player version Mastermind game is built mostly using functions
procedures approach with the help from 3 classes: Marble, Point and Image

The design part of the game includes the dialog box asking for player's name (
using the ask_player_name() function), the score board, the play area with
color marbles and option buttons, the guess board with empty marbles/pegs lines
(all 3 using the design_game_outlook() function) and a small orange indicator
representing player's turn (using the turn_indicator() function). The color
marbles are built using the draw_marble() function, Marble and Point class.
The empty marbles/pegs guess lines are built using the draw_each_guess() function,
Marble and Point class. The options buttons along with game notifications are
created using the Image and Point class.

The game-play part is designed so that all functions can handle game rules
correctly in the back. The make_secret_code() function is used to generate
a secret code at the start of every game. The count_bulls_and_cows() function is
used to compare players' guesses with the secret code, which later reveals the
result through pegs' colors. The read_leaderboard_data() function reads players'
data (names and scores) from the existing text file (the file should be created
if not existed) so that data can be displayed in the score board section of the
game. The edit_leaderboard_data() function writes new/updated data after every
game to the existing text file.

The program makes use of nested function for the click_mouse() function so that
the use of many global variables can be avoided, functions are more organized and
the testing process can run without the whole game being played (although turtle
object and canvas will still appear as we use them as global variables).


