class Wordle:

    def __init__(self):
        self.wordle_word: list[str] = ["H", "E", "L", "L", "O"]
        self.MAX_GUESS_COUNT: int = 8
        self.game_result: str = None


        self.user_inputs: dict = {} # FX: {nr: 1, word: ["W", "O", "R", "L", "D"], feedback: "-c-C-"}
        self.guess_count = 0


    def play_game(self):
        while not self.game_result:
            guess = self.user_input()
            self.validate_geuss(guess)


    def validate_geuss(self, guess):
        feedback = ""
        for char in self.wordle_word:
            if feedback


    def user_input(self):
        word = input("Enter the word to be guessed: ").upper()
        self.guess_count += 1
        return word
    

    def display_prev_guesses(self):
        """ Display previous guesses in the round """
        pass

    def display_code_with_guesses(self):
        """ Display code with each guess, -c-C- -  """
        pass

    def wrong_format(self):
        """ Lets user know if wrong format and doesn't crash"""
        pass

    def detect_defeat(self):
        """ Detect loss when guesses are finished """
        pass

    def detect_victory(self):
        """ Detect victory when a guess is correct """
        pass
