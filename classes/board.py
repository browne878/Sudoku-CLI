import copy
import json
import random


class Board:
    """
    Creates an instance of Board
    """

    def __init__(self, difficulty):
        self.board = ["               1   2   3   4   5   6   7   8   9  ",
                      "             ¦===================================¦",
                      "         1   ¦ _ | _ | _ ¦ _ | _ | _ ¦ _ | _ | _ ¦",
                      "         2   ¦ _ | _ | _ ¦ _ | _ | _ ¦ _ | _ | _ ¦",
                      "         3   ¦ _ | _ | _ ¦ _ | _ | _ ¦ _ | _ | _ ¦",
                      "             ¦===========¦===========¦===========¦",
                      "         4   ¦ _ | _ | _ ¦ _ | _ | _ ¦ _ | _ | _ ¦",
                      "         5   ¦ _ | _ | _ ¦ _ | _ | _ ¦ _ | _ | _ ¦",
                      "         6   ¦ _ | _ | _ ¦ _ | _ | _ ¦ _ | _ | _ ¦",
                      "             ¦===========¦===========¦===========¦",
                      "         7   ¦ _ | _ | _ ¦ _ | _ | _ ¦ _ | _ | _ ¦",
                      "         8   ¦ _ | _ | _ ¦ _ | _ | _ ¦ _ | _ | _ ¦",
                      "         9   ¦ _ | _ | _ ¦ _ | _ | _ ¦ _ | _ | _ ¦",
                      "             ¦===================================¦"]
        self.board_solution = []
        self.column_index = [15, 19, 23, 27, 31, 35, 39, 43, 47]
        self.difficulty = difficulty

    def __validate_guess(self, temp_board, row, column, num):
        """
        Checks if user input is the correct num.
        Checks if position is free to place a num.
        """

        temp_board_solution = copy.copy(self.board_solution)

        del temp_board_solution[0]
        del temp_board_solution[0]
        del temp_board_solution[3]
        del temp_board_solution[6]
        del temp_board_solution[-1]

        current_num = temp_board[row - 1][self.column_index[column - 1]]

        if current_num != '_':
            return False

        correct_num = temp_board_solution[
            row - 1][self.column_index[column - 1]]

        if correct_num != num:
            return False

        return True

    def populate_board(self):
        """
        Populates the sudoku board and solution with a template from JSON
        """

        with open('./assets/boards/boards.json') as json_board:
            boards = json.load(json_board)

            if self.difficulty == 'random':
                difficulties = [
                    'easy', 'normal', 'medium', 'hard', 'very_hard'
                ]

                self.difficulty = random.choice(difficulties)

            board_count = len(boards[self.difficulty + '_boards'])
            rand_board_index = random.randint(0, (board_count - 1))

            self.board = boards[
                self.difficulty + '_boards'][rand_board_index]['template']

            self.board_solution = boards[
                self.difficulty + '_boards'][rand_board_index]['solution']

    def edit_board(self, row, column, num):
        """
        Edit's the number at the provided row and column
        Returns False if incorrect num or there is already a number at index
        """
        temp_board = copy.copy(self.board)
        del temp_board[0]
        del temp_board[0]
        del temp_board[3]
        del temp_board[6]
        del temp_board[-1]

        if not (self.__validate_guess(temp_board, row, column, num)):
            return False

        index = self.board.index(temp_board[row - 1])

        temp_board[row - 1] = (
                temp_board[row - 1][:self.column_index[column - 1]] +
                num + temp_board[row - 1][self.column_index[column - 1] + 1:])

        self.board[index] = temp_board[row - 1]

        return True

    def check_complete(self):
        """
        Compares Game board and complete versions to see
        if the game is complete.
        """

        if self.board == self.board_solution:
            return True
        else:
            return False
