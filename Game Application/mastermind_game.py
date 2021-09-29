'''
Brian Nguyen
Final Project: Mastermind (What a game!)
CS 5001 Spring 2021
'''

# import necessary Python modules and classes from other Python files
import turtle, random
from Marble import *
from Image import *
from Point import Point



# THE GAME-PLAY PART OF THE GAME

# set up CONSTANT variable

# for the leaderboard section in game
LEADERBOARD_WIDTH = 205
LEADERBOARD_LENGTH = 500
# for the control board section in game
CONTROLBOARD_WIDTH = 140
CONTROLBOARD_LENGTH = 685
# for the guess board section in game
GUESSBOARD_WIDTH = 450
GUESSBOARD_LENGTH = 500
# spacing between guess lines
GUESS_LINE_SPACING = 50
# spacing between each player's name and score in the leaderboard section
RECORD_LINE_SPACING = 30



def count_bulls_and_cows(secret_code, player_guess):
    '''
    Function -- count_bulls_and_cows
        Calculate the number of bulls and cows based on each
        player's guess and the secret code for that round
        
    Parameters:
        secret_code (a list of strings) -- A list of 4
        different colors created randomly based on the list of 6
        different colors (blue, red, green, yellow, purple, black)
        player_guess (a list of string) -- A list of 4
        different colors created based on player's selection for
        that turn (follows mouse-click's order)
        
    Returns a tuple with 2 elements containing the number of
    bulls and cows by comparing player's guess for that round
    with the secret code
    '''
    
    bulls = 0
    cows = 0

    for i in range (len(secret_code)):
        # if the color both matches and is in the correct position
        if player_guess[i] == secret_code[i]:
            bulls += 1
        # if the color only matches but not in the correct position
        elif player_guess[i] in secret_code:
            cows +=1
    return (bulls, cows)



def make_secret_code():
    '''
    Function -- make_secret_code
        Randomly generate a secret code containing 4
        different colors from a list of 6 different
        colors (blue, red, green, yellow, purple, black)

    No parameters

    Returns a list of 4 different colors (a list of strings)
    created randomly from a list of 6 different colors (blue, red,
    green, yellow, purple, black)
    '''
    
    # initialize a list of 6 different colors (a list of string)
    list_of_marbles = ['blue', 'red', 'green', 'yellow', 'purple', 'black']
    # shuffle the list to create random order
    random.shuffle(list_of_marbles)
    # create the secret code (also a list of strings) from the first 4 colors in the list above
    secret_code = list_of_marbles[0:4]
    return secret_code




def read_leaderboard_data(read_file_name):
    '''
    Function -- read_leaderboard_data
        Read the information from the leaderboard text file (if exists)
        to show that information on the leaderboard section of the game.
        If the leaderboard text file does not exist then create a new file.
        If there is an issue with the leaderboard text file (file is corrupt,
        unable to use, etc...), pop up the notification to players.

    Parameter
        read_file_name (string) -- name of the text file we want to read information from

    Returns a dictionary (a score board) with player's name(s) (string) as key(s) and
    their score(s) (integer) as value(s).
    '''
    
    try:
        with open(read_file_name, mode = 'r') as leaderboard_file:
            score_board = {}
            # retrieve information from each line of the leaderboard file and add them to score_board dictionary
            for each_line in leaderboard_file.readlines():
                a_list = each_line.split()
                player_name = a_list[0]
                total_guesses = a_list[2]
                score_board[player_name] = int(total_guesses)

            return score_board

    # when the leaderboard text file is not found (does not exist)
    except FileNotFoundError:
        # create a leaderboard text file along with an empty score_board dictionary
        with open(read_file_name, mode = 'w') as leaderboard_file:
            score_board = {}
            return score_board
    # when there are other issues with the leaderboard text file 
    except:
        # leaderboard error notification pops up
        leaderboard_error_noti = Image(Point(0,0), "leaderboard_error.gif")
        # the game quits when players click the mouse
        turtle.exitonclick()



        
def edit_leaderboard_data(player_name, total_guesses, score_board, write_file_name):
    '''
    Function -- edit_leaderboard_data
        write to the leaderboard text file the
        lastest data of the game (player's name and
        their score)

    Parameters:
        player_name (string) -- name of the player
        total_guesses (integer) -- the number of guesses the player
        take to arrive at the correct answer
        score_board (dict) -- a dictionary with player's name as key and
        their score as value), the current leaderboard in the game
        write_file_name (string) -- name of the text file we want to write information from the leaderboard to

    Returns nothing
    '''
    try:
        with open(write_file_name, mode = 'w') as leaderboard_file:
            # if the leaderboard is empty, add the player's name along with their score to it
            if score_board == {}:
                score_board[player_name] = total_guesses
            else:
                # if an old player achieves new best guess (lower number of guesses), replace their old score with it 
                if player_name in score_board.keys() and score_board[player_name] > total_guesses:
                    score_board[player_name] = total_guesses
                # add new player's name and their score to the leaderboard until there are 10 players (limit to 10) 
                if player_name not in score_board.keys() and len(score_board.keys()) < 10:
                    score_board[player_name] = total_guesses
            # sort the leaderboard so that players with lower number of guesses stay on top of others 
            sorted_score_board = sorted(score_board.items(), key=lambda x:x[1], reverse = False)
            # write the information on the leaderboard to the leaderboard text file
            for each_element in sorted_score_board:
                leaderboard_file.write(each_element[0] + " : " + str(each_element[1]) + "\n")
    except OSError:
        # file error notification pops up
        file_error_noti = Image(Point(0,0), "file_error.gif")
        # the game quits when players click the mouse
        turtle.exitonclick()
            


# THE DESIGN PART OF THE GAME

# initialize global variables my_turtle and screen
my_turtle = turtle.Turtle()
screen = turtle.Screen()


def ask_player_name():
    '''
    Function -- ask_player_name
        Create a dialog box using turtle module to ask for
        player's name when the game starts

    No parameters

    Returns player's name (string)
    '''
    
    player_name = turtle.textinput("Mastermind Game", "Please enter your name:")
    return player_name



def design_game_outlook():
    '''
    Function -- design_game_outlook
        Draw the overall design of the game, with the
        leaderboard, control board (where players make
        their choices in the game, without colored
        marbles and option buttons) and guess board
        (without empty marbles and empty pegs) sections

    No parameters

    Returns nothing
    '''

    # set up my_turtle object's attributes
    my_turtle.speed(0)
    my_turtle.up()
    my_turtle.ht()
    my_turtle.pensize(5)
    
    # draw leaderboard
    my_turtle.goto(130,330)
    my_turtle.down()
    my_turtle.fd(LEADERBOARD_WIDTH)
    my_turtle.rt(90)
    my_turtle.fd(LEADERBOARD_LENGTH)
    my_turtle.rt(90)
    my_turtle.fd(LEADERBOARD_WIDTH)
    my_turtle.rt(90)
    my_turtle.fd(LEADERBOARD_LENGTH)
    my_turtle.up()
    my_turtle.goto(235, 290)
    my_turtle.write("Leaderboard", align = "center", font = ("Arial", 20, "bold"))

    # draw control board
    my_turtle.goto(-350, -180)
    my_turtle.down()
    my_turtle.rt(90)
    my_turtle.fd(CONTROLBOARD_LENGTH)
    my_turtle.rt(90)
    my_turtle.fd(CONTROLBOARD_WIDTH)
    my_turtle.rt(90)
    my_turtle.fd(CONTROLBOARD_LENGTH)
    my_turtle.rt(90)
    my_turtle.fd(CONTROLBOARD_WIDTH)
    

    # draw the guess board
    my_turtle.up()
    my_turtle.goto(-350,330)
    my_turtle.down()
    my_turtle.rt(90)
    my_turtle.fd(GUESSBOARD_WIDTH)
    my_turtle.rt(90)
    my_turtle.fd(GUESSBOARD_LENGTH)
    my_turtle.rt(90)
    my_turtle.fd(GUESSBOARD_WIDTH)
    my_turtle.rt(90)
    my_turtle.fd(GUESSBOARD_LENGTH)

    

def draw_marble():
    '''
    Function -- draw_marble
        Draw the line of 6 colored marbles (in the control
        board section) which players can click on to make
        selection
        
    No parameters

    Returns a list of 6 marble objects
    '''

    # create 6 marble objects (using the imported Marble class) representing 6 different colors 
    blue_marble = Marble(Point(-280,-240), "blue")    
    red_marble = Marble(Point(-240,-240), "red") 
    green_marble = Marble(Point(-200,-240), "green")   
    yellow_marble = Marble(Point(-160,-240), "yellow")    
    purple_marble = Marble(Point(-120,-240), "purple")
    black_marble = Marble(Point(-80,-240), "black")

    # put all marble objects into a list called list_of_marbles
    list_of_marbles = [blue_marble, red_marble, green_marble, \
                       yellow_marble, purple_marble, black_marble]

    # draw all 6 marbles objects using the draw() method in the imported Marble class
    for each_marble in list_of_marbles:
        each_marble.draw()

    return list_of_marbles



def draw_each_guess():
    '''
    Function -- draw_each_guess
        Draw 10 lines of guesses in the guess board section
        (with 4 empty marbles and 4 empty pegs) representing
        the maximum number of guesses each player can have
        when playing the game

    No parameters

    Returns a nested list of guesses (a list of 10 lists with
    each list, containing 4 empty marble objects and 4 empty
    peg objects, represent a guess)
    '''

    # set up the coordinates for the first empty marble object on the drawing canvas
    x = -270
    y = 290
    list_of_guesses = []

    # draw 10 lines of guesses (representing the maximum number of guesses each player can have)
    for i in range(10):
        # each guess first contains 4 empty marbles, then 4 empty pegs
        each_guess = []
        first_marble = Marble(Point(x,y),"")
        first_marble.draw_empty()
        each_guess.append(first_marble)
        second_marble = Marble(Point(x + 40,y), "")
        second_marble.draw_empty()
        each_guess.append(second_marble)
        third_marble = Marble(Point(x + 80,y), "")
        third_marble.draw_empty()
        each_guess.append(third_marble)
        fourth_marble = Marble(Point(x + 120,y), "")
        fourth_marble.draw_empty()
        each_guess.append(fourth_marble)
        
        first_peg = Marble(Point(x + 250,y + 20), "", size = 5)
        first_peg.draw_empty()
        each_guess.append(first_peg)
        second_peg = Marble(Point(x + 270,y + 20), "", size = 5)
        second_peg.draw_empty()
        each_guess.append(second_peg)
        third_peg = Marble(Point(x + 250,y), "", size = 5)
        third_peg.draw_empty()
        each_guess.append(third_peg)
        fourth_peg = Marble(Point(x + 270,y), "", size = 5)
        fourth_peg.draw_empty()
        each_guess.append(fourth_peg)

        # append each guess (10 guesses in total) to the big list list_of_guesses
        list_of_guesses.append(each_guess)

        # set up the right distance between each line of guess
        y -= GUESS_LINE_SPACING
        
    return list_of_guesses



def turn_indicator():
    '''
    Function -- turn_indicator
        Create a guess marker to show which line of guess the player is at

    No parameters

    Returns a turtle object (indicator)
    '''

    # initialize and set up attributes for the turtle object named indicator
    indicator = turtle.Turtle()
    indicator.turtlesize(2,2,3)
    indicator.color("orange")
    indicator.up()
    indicator.speed(0)
    # indicator moves to the first line of guess in the game
    indicator.goto(-305,305)
    return indicator


def play_game():
    '''
    Function -- play_game
        This function starts the game when it is called.
        It is where all the actions (draw the game design for example)
        in the game happens

    No parameters

    Returns nothing
    '''

    # call game functions above
    player_name = ask_player_name()
    design_game_outlook()
    marbles_line = draw_marble()
    list_of_guesses = draw_each_guess()
    indicator = turn_indicator()
    secret_code = make_secret_code()
    
    score_board = read_leaderboard_data('leaderboard.txt')
    # using turtle to show the retrieving information in the leaderboard section of the game
    my_turtle.up()
    my_turtle.goto(180, 250)
    # x coordinate of the first player's name showed on the leaderboard
    x = my_turtle.xcor()
    # y coordinate of the first player's name showed on the leaderboard
    y = my_turtle.ycor()
    for each_player_name in score_board:
        my_turtle.goto(x, y)
        my_turtle.write(each_player_name + " : " + str(score_board[each_player_name]), align = "left", font = ("Arial", 15, "normal"))
        y -= RECORD_LINE_SPACING


    # create option buttons (check, X and quit) for the game at suitable positions using the imported Image class
    check_button = Image(Point(20,-240), "checkbutton.gif")
    x_button = Image(Point(90,-240), "xbutton.gif")
    quit_button = Image(Point(230,-250), "quit.gif")

    # initialize necessary empty lists to store player's current guess and current peg's suggestion
    current_guess = []
    current_pegs_color = []

    # initialize a pointer to indicate which empty marbles (or pegs) we want to modify 
    Pointer = [0,0]

    def click_mouse(x,y):
        '''
        Function -- click_mouse
            Serves to operate all mouse click actions of the player during the game

        No parameters

        Returns nothing
        '''

        # if player clicks on the quit button, quit noti pops up and player clicks to exit the game
        if quit_button.clicked(x,y):
            quit_msg = Image(Point(0,0), "quitmsg.gif")
            turtle.exitonclick()
        else:
            # to indicate which 4 marbles combination player selects for their current guess
            for each_marble in marbles_line:
                # if a marble is clicked, that marble turns blank and the correspond empty marble takes its color
                if each_marble.clicked_in_region(x,y):
                    # limit player to 10 turns and 4 colored marbles selected for each turn
                    if Pointer[1] < 4 and Pointer[0] < 10:
                        color = each_marble.get_color()
                        each_marble.draw_empty()
                        list_of_guesses[Pointer[0]][Pointer[1]].set_color(color)
                        list_of_guesses[Pointer[0]][Pointer[1]].draw()
                        current_guess.append(color)
                        Pointer[1] += 1

            # if player clicks on the X button, restart their current guess
            if x_button.clicked(x,y):
                for each in list_of_guesses[Pointer[0]][0:4]:
                    each.draw_empty()
                for each_marble in marbles_line:
                    each_marble.draw()
                for i in range (len(current_guess)):
                    current_guess.pop()
                Pointer[1] = 0

            # if player clicks on the check button, compare their current guess with the secret code
            if check_button.clicked(x,y):
                pegs_hints = count_bulls_and_cows(secret_code, current_guess)
                # if the marble appears in secret code and at right position, add 'black' to the list current_pegs_color
                for i in range(pegs_hints[0]):
                    current_pegs_color.append('black')
                # if the marble only appears in secret code, add 'red' to the list current_pegs_color
                for i in range(pegs_hints[1]):
                    current_pegs_color.append('red')
                # shuffle the current_pegs_color list so their appearing order is random
                random.shuffle(current_pegs_color)

                # color the pegs according to their color and appearing order
                for each_color in current_pegs_color:
                    list_of_guesses[Pointer[0]][Pointer[1]].set_color(each_color)
                    list_of_guesses[Pointer[0]][Pointer[1]].draw()
                    if Pointer[1] < 7:
                        Pointer[1] += 1

                # move on to next guess when done
                Pointer[0] += 1

                # if player used up all 10 guesses and still hasn't figured out the secret code
                if Pointer[0] > 9:
                    # Lose notification pops up
                    loser_noti = Image(Point(0,0), "Lose.gif")
                    # announce the secret code
                    turtle.textinput("The secret code was", secret_code)
                    turtle.exitonclick()
                # if player guessed the secret code
                elif pegs_hints[0] == 4:
                    # Win notification pops up
                    winner_noti = Image(Point(0,0), "winner.gif")
                    # player's name and their score are added to leaderboard
                    edit_leaderboard_data(player_name, Pointer[0], score_board, 'leaderboard.txt')
                    turtle.exitonclick()
                # if the player still has more guesses to go and hasn't figured out the secret code, game continues
                else:
                    for each_marble in marbles_line:
                        each_marble.draw()
                        
                    for i in range (len(current_guess)):
                        current_guess.pop()
                        
                    for i in range (len(current_pegs_color)):
                        current_pegs_color.pop()

                    # pointer now points to the first element (empty marble) of the next guess
                    Pointer[1] = 0
                    y = indicator.ycor()
                    x = indicator.xcor()
                    # the indicator moves to the next guess
                    indicator.goto(x, y - GUESS_LINE_SPACING)

    # call click_mouse function by using mouse click on screen
    screen.onclick(click_mouse)



def main():
    # set the title for the turtle drawing canvas
    screen.title("Mastermind Game")
    # let's play the game 
    play_game()
    
if __name__ == "__main__":
    main()
