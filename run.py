import os
from classes.game import Game
from classes.board import Board


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

        os.system('cls' if os.name == 'nt' else 'clear')

        current_game.print_header(current_game.correct_guesses,
                                  current_game.incorrect_guesses)

        for row in current_board.board:
            print(row)

        location = current_game.request_box()
        guess = current_game.request_guess()

        if current_board.edit_board(int(location[0]), int(location[1]), guess):
            print('Correct!')
            current_game.correct_guesses += 1
        else:
            print('Incorrect!')
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


while True:
    if not new_game():
        break
