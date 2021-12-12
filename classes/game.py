class Game:
    """
    Creates an instance of the game
    """

    def __init__(self):
        self.correct_guesses = 0
        self.incorrect_guesses = 0
        self.boards_completed = 0
        self.game_header = []

    def __validate_input(self, input):
        input_int = None

        try:
            input_int = int(input)
        except ValueError:
            print('You did not enter a number. Please try again!')
            return False

        if input_int is not None:
            if input_int < 1 or input_int > 9:
                print('You did not enter a number 1-9. Please try again!')
                return False

        return True

    def welcome(self):
        """
        Displays a welcome message to the user when a new instance
        of a game is created
        """

        welcome = [
            '============================================',
            '          Welcome to Sudoku CLI             ',
            '============================================'
            '',
            'This game takes the usual sudoku game and',
            'makes it playable in a terminal.',
            '',
            'We hope you enjoy the game!'
        ]

        for line in welcome:
            print(line)

    def instructions(self):
        """
        Checks if user would like to see the instructions.
        If yes, prints them to the console.
        """

        print('Would you like to read the instructions?')
        show_instructions = ''

        while True:
            show_instructions = input('Press Y for Yes and N for No: ')

            if show_instructions.capitalize() == 'Y':
                break
            elif show_instructions.capitalize() == 'N':
                return
            else:
                print('Invalid Input, Please try again!')

        instructions = [
            '- Each of the 9 boxes can only have one of each number (1-9)',
            '- Each line can only have one of each number (1-9)',
            '- Only correct answers will be accepted'
        ]

        for line in instructions:
            print(line)

    def select_difficulty(self):
        """
        Gets the required difficulty from the user and returns it
        """

        request_string = [
            'Please select one of the following difficulties.',
            '0 - Random',
            '1 - Easy',
            '2 - Normal',
            '3 - Medium',
            '4 - Hard',
            '5 - Very Hard'
        ]

        difficulty_message = 'Invalid Difficulty. Please try again!'

        while difficulty_message == 'Invalid Difficulty. Please try again!':
            for line in request_string:
                print(line)

            difficulty = input('Please select the difficulty: ')

            switch = {
                '0': 'random',
                '1': 'easy',
                '2': 'normal',
                '3': 'medium',
                '4': 'hard',
                '5': 'very_hard'
            }

            difficulty_message = switch.get(difficulty, difficulty_message)

        return difficulty_message

    def request_box(self):
        """
        Requests box for guess and validates user input.
        Returns user input as array [row, column]
        """

        row_input = ''
        column_input = ''

        while True:
            print('Please select the row of the box!')
            row_input = input('Row between 1 and 9: ')

            if not self.__validate_input(row_input):
                continue

            break

        while True:
            print('Please select the column of the box!')
            column_input = input('Column between 1 and 9: ')

            if not self.__validate_input(column_input):
                continue

            break

        return [row_input, column_input]

    def request_guess(self):
        """
        Requests and validates the users guess
        Returns validated guess as a string
        """

        while True:

            print('Please select a number between 1 and 9')
            guess = input('What number belongs in the selected square: ')

            if not self.__validate_input(guess):
                continue

            return guess

    def print_header(self, correct_guesses, incorrect_guesses):
        """
        Formats and prints the game header with score variables.
        """

        self.game_header = [
            '========================= SUDOKU CLI =========================',
            f'Correct Guesses = {correct_guesses}                       ' +
            f'Incorrect Guesses = {incorrect_guesses}',
            f'                       Total Guesses = '
            f'{correct_guesses + incorrect_guesses}'
        ]

        for line in self.game_header:
            print(line)
