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

        for row in current_board.board:
            print(row)

        location = current_game.request_box()
        guess = current_game.request_guess()

        if current_board.edit_board(int(location[0]), int(location[1]), guess):
            print('Correct!')
        else:
            print('Incorrect!')

        if current_board.check_complete():
            print('congratulations')


while True:
    new_game()
