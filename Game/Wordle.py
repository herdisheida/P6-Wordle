from ColorText import Color
from Game.Guess import Guess

class Wordle:
    HISTORY_FORMAT = "{0:<5}{1:<20}{2:<20}"

    def __init__(self):
        self.the_wordle: str = "HELLO"
        self.MAX_GUESS_COUNT: int = 5 # LATER customizable
        self.WORD_LENGTH: int = 5 # LATER customizable
        self.game_result: str = None

        self.user_inputs: dict[object] = {}
        self.guess_count: int = 0

    def game_play(self):
        while not self.game_result:
            guess = self.user_input()

            if not self.validate_guess(guess):
                continue
            self.guess_count += 1

            feedback = self.get_feedback(guess)
            print(feedback)

            if self.detect_victory(feedback):
                print(f"\n{Color.GREEN.value}VICTORY!{Color.RESET.value}")
                self.game_result = "Victory"
            
            if self.detect_defeat():
                print(f"\n{Color.RED.value}YOU LOSE!{Color.RESET.value}")
                self.game_result = "Defeat"
        
        self.print_game_history()
        return


    def user_input(self):
        word = input("\nGuess: ").upper()
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
            colored_feedback = f"{Color.GREEN.value}{feedback}{Color.RESET.value}"
            self.save_guess(guess, colored_feedback)
            return colored_feedback

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
    

    def save_guess(self, guessed_word: str, feedback: str):
        saved_guess = Guess(self.guess_count, guessed_word, feedback)
        self.user_inputs[self.guess_count] = saved_guess
        return

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
        correct_feedback = "C" * self.WORD_LENGTH
        if feedback == f"{Color.GREEN.value}{correct_feedback}{Color.RESET.value}":
            return True
        return False

    def detect_defeat(self):
        """ Detect loss when guesses are finished """
        if self.guess_count == self.MAX_GUESS_COUNT:
            return True
        return False


    def print_game_history(self):
        print("GAME HISTORY")

        print(self.HISTORY_FORMAT.format("nr", "Guess", "Feedback"))
        for guess_nr, guess_round in self.user_inputs.items():
            print(self.HISTORY_FORMAT.format(guess_nr, guess_round.word, guess_round.feedback))