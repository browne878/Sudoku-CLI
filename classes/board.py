import copy
import json
import random


class Board:
    """
    Creates an instance of Board
    """

    def __init__(self, difficulty):
        self.board = ["¦===================================¦",
                      "¦ _ | _ | _ ¦ _ | _ | _ ¦ _ | _ | _ ¦",
                      "¦ _ | _ | _ ¦ _ | _ | _ ¦ _ | _ | _ ¦",
                      "¦ _ | _ | _ ¦ _ | _ | _ ¦ _ | _ | _ ¦",
                      "¦===========¦===========¦===========¦",
                      "¦ _ | _ | _ ¦ _ | _ | _ ¦ _ | _ | _ ¦",
                      "¦ _ | _ | _ ¦ _ | _ | _ ¦ _ | _ | _ ¦",
                      "¦ _ | _ | _ ¦ _ | _ | _ ¦ _ | _ | _ ¦",
                      "¦===========¦===========¦===========¦",
                      "¦ _ | _ | _ ¦ _ | _ | _ ¦ _ | _ | _ ¦",
                      "¦ _ | _ | _ ¦ _ | _ | _ ¦ _ | _ | _ ¦",
                      "¦ _ | _ | _ ¦ _ | _ | _ ¦ _ | _ | _ ¦",
                      "¦===================================¦"]
        self.board_solution = []
        self.column_index = [2, 6, 10, 14, 18, 22, 26, 30, 34]
        self.difficulty = difficulty

    def __validate_guess(self, temp_board, row, column, num):
        """
        Checks if user input is the correct num.
        Checks if position is free to place a num.
        """

        temp_board_solution = copy.copy(self.board_solution)

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
