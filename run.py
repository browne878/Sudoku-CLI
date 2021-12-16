import os

from classes.board import Board
from classes.game import Game


def new_game():
    """
    Begin a new game.
    """

    current_game = Game()

    current_game.welcome()
    current_game.instructions()
    difficulty = current_game.select_difficulty()

    current_board = Board(difficulty)
    current_board.populate_board()

    while True:

        # Source
        # https://stackoverflow.com/questions/2084508/clear-terminal-in-python
        os.system('cls' if os.name == 'nt' else 'clear')

        current_game.print_header(current_game.correct_guesses,
                                  current_game.incorrect_guesses)

        for row in current_board.board:
            print(row)

        location = current_game.request_box()
        guess = current_game.request_guess()

        if current_board.edit_board(int(location[0]), int(location[1]), guess):
            print('Correct!')
            input('Press enter to continue: ')
            current_game.correct_guesses += 1
        else:
            print('Incorrect!')
            input('Press enter to continue: ')
            current_game.incorrect_guesses += 1

        if current_board.check_complete():
            print('congratulations!')
            print('')
            print('Would you like to play again?')
            print('Press Y for Yes.')
            print('Press N for No.')

            while True:
                play_again = input()

                if play_again.upper() == 'Y':
                    return True
                elif play_again.upper() == 'N':
                    return False

        if ((current_game.correct_guesses +
                current_game.incorrect_guesses) > 79 and
                (current_game.correct_guesses +
                    current_game.incorrect_guesses) % 10 == 0):
            print('Are you cheating?')
            print('It is not as fun when you cheat ;)')
            input('Press enter to continue cheating! ')


while True:
    if not new_game():
        break
