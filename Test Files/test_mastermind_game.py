'''
Brian Nguyen
Test File for the Mastermind Game 
CS 5001
'''

# import necessary functions from mastermind_game for testing purposes
from mastermind_game import count_bulls_and_cows, make_secret_code, read_leaderboard_data, edit_leaderboard_data


def test_count_bulls_and_cows(secret_code, player_guess, expect_result):
    '''
    Function -- test_count_bulls_and_cows
        Tests the correctness of function count_bulls_and_cows
        
    Parameters:
        secret_code (a list of strings) -- A list of 4
        different colors created randomly based on the list of 6
        different colors (blue, red, green, yellow, purple, black)
        player_guess (a list of string) -- A list of 4
        different colors created based on player's selection for
        that turn (follows mouse-click's order)
        expected_result (a tuple containing 2 integers): the expected
        number of bulls and cows by comparing player's guess for
        that round with the secret code

    Returns nothing
    '''

    actual_result = count_bulls_and_cows(secret_code, player_guess)
    print(f"Inputs for the 'count bulls and cows' test: {secret_code} and {player_guess}.")
    print(f"Expected result was: {expect_result}. Actual result was: {actual_result}.")



def test_making_secret_code():
    '''
    Function -- test_making_secret_code
        Tests the correctness of function make_secret_code

    No parameters

    Return nothing
    '''
    
    list_of_marbles = ['blue', 'red', 'green', 'yellow', 'purple', 'black']
    actual_secret_code = make_secret_code()

    # turn the list of marbles and secret codes into sets
    marbles_set = set(list_of_marbles)
    secret_code_set = set(actual_secret_code)
    # check if the length of the secret code is 4 and the code is from the set of permitted colors
    if len(actual_secret_code) == 4 and secret_code_set.issubset(marbles_set):
        print(f"The secret code: {actual_secret_code} passes the randomness test. Our secret code function is correct!")



def test_read_from_file(read_file_name, expected_score_board):
    '''
    Function -- test_read_from_file
        Tests the correctness of function read_leaderboard_data

    Parameters:
        read_file_name (string): name of the text file we want to read information from
        expected_score_board (dict): an expected dictionary with player's name(s) (string)
        as key(s) and their score(s) (integer) as value(s).

    Returns nothing
    '''

    actual_score_board = read_leaderboard_data(read_file_name)
    print(f"The 'read from file' test operates on the text file {read_file_name}.")
    print(f"Expected result was: {expected_score_board}. \nActual result was: {actual_score_board}.")
    


def test_write_to_file(player_name, total_guesses, score_board, write_file_name, expected_content):
    '''
    Function -- test_write_to_file
        Tests the correctness of function edit_leaderboard_data

    Parameters:
        player_name (string) -- name of the player
        total_guesses (integer) -- the number of guesses the player
        take to arrive at the correct answer
        score_board (dict) -- a dictionary with player's name as key and
        their score as value), the current leaderboard in the game
        write_file_name (string) -- name of the text file we want to write information to
        expected_content (string) -- the expected content we hope to get from reading the file we wrote to

    Returns nothing
    '''

    edit_leaderboard_data(player_name, total_guesses, score_board, write_file_name)

    # open the test write file to retrieve its content
    with open (write_file_name, mode = 'r') as read_file:
        actual_content = read_file.read()
        
    print(f"The 'write to file' test operates on the text file {write_file_name}.")
    print(f"Expected result was: {expected_content} \nActual result was: {actual_content}")


def main():
    test_count_bulls_and_cows(["red","blue","green","yellow"],["red","blue","green","yellow"],(4,0))
    test_count_bulls_and_cows(["red","blue","green","yellow"],["red","green","purple","yellow"],(2,1))
    test_count_bulls_and_cows(["red","blue","green","yellow"],["blue","green","yellow","red"],(0,4))
    test_count_bulls_and_cows(["red","blue","green","yellow"],["black","purple","yellow","red"],(0,2))

    print()
    print()

    test_making_secret_code()
    test_making_secret_code()
    test_making_secret_code()

    print()
    print()

    test_read_from_file('test_read_from_file.txt', {'Bach' : 2, 'Jenny' : 8})

    print()
    print()

    test_write_to_file('Frog',3, {'Sheep' : 2, 'Crocodile' : 1}, 'test_write_to_file.txt', 'Crocodile : 1\nSheep : 2\nFrog: 3')
    
if __name__ == "__main__":
    main()
