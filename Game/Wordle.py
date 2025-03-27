from ColorText import Color
from Guess import Guess

class Wordle:

    def __init__(self):
        self.the_wordle: str = "HELLO"
        self.MAX_GUESS_COUNT: int = 5 # LATER customizable
        self.WORD_LENGTH: int = 5 # LATER customizable
        self.game_result: str = None

        self.user_inputs: dict = {} # FX: {nr: 1, word: ["W", "O", "R", "L", "D"], feedback: "-c-C-"}
        self.guess_count: int = 0

    def game_play(self):
        while not self.game_result:
            guess = self.user_input()

            if not self.validate_guess(guess: str):
                continue

            feedback = self.get_feedback(guess)
            print(feedback)

            if self.detect_victory(feedback):
                break
            
            if self.detect_defeat():
                break


    def user_input(self):
        word = input("\nGuess: ").upper()
        self.guess_count += 1
        return word

    def validate_guess(self, guess: str):
        """Checks if the guess is formatted correctly"""
        if not guess.isalpha():
            print(f"{Color.RED.value}Guess needs to be string{Color.RESET.value}")
            return False

        if len(guess) != self.WORD_LENGTH:
            print(f"{Color.RED.value}Guess needs to have {len(self.the_wordle)} letters{Color.RESET.value}")
            return False
        return True
        

    def get_feedback(self, guess: str):
        """Checks if guess is the correct wordly word, or close to it"""
        if guess == self.the_wordle:
            feedback = "C" * self.WORD_LENGTH
            return f"{Color.GREEN.value}{feedback}{Color.RESET.value}"

        feedback = ""
        for index in range(len(self.the_wordle)):

            # correct letter + correct placement
            if guess[index] == self.the_wordle[index]:
                feedback += f"{Color.GREEN.value}C{Color.RESET.value}"

            # correct letter + incorrect placement
            elif guess[index] in self.the_wordle:
                feedback += f"{Color.YELLOW.value}c{Color.RESET.value}"
            
            # letter not in THE wordle
            else:
                feedback += f"{Color.RED.value}-{Color.RESET.value}"

        self.save_guess(guess, feedback)
        return feedback
    

    def save_guess(self, guess:str, feedback: str):
        pass

    def display_prev_guesses(self):
        """ Display previous guesses in the round """
        # TODO
        pass

    def display_code_with_guesses(self):
        """ Display code with each guess, -c-C- -  """
        # TODO
        pass

    def wrong_format(self):
        """ Lets user know if wrong format and doesn't crash"""
        # TODO
        pass


    def detect_victory(self, feedback: str):
        """ Detect victory when a guess is correct """
        if feedback == "C" * self.WORD_LENGTH:
            return True
        return False

    def detect_defeat(self):
        """ Detect loss when guesses are finished """
        if self.guess_count == self.MAX_GUESS_COUNT:
            return True
        return False


