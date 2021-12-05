class Game:
    """
    Creates an instance of the game
    """

    def __init__(self):
        self.correct_guesses = 0
        self.incorrect_guesses = 0
        self.boards_completed = 0

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
