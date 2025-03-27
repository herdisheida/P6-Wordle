from ColorText import Color
from Game.Guess import Guess

class Wordle:
    HISTORY_FORMAT = "{0:<5}{1:<20}{2:<20}"

    def __init__(self):
        self.the_wordle: str = "HELLO"
        self.MAX_GUESS_COUNT: int = 5 # LATER customizable
        self.WORD_LENGTH: int = 5 # LATER customizable
        self.game_result: str = None

        self.game_history: dict[object] = {}
        self.guess_count: int = 0

    def game_play(self):
        """Main game loop"""
        while not self.game_result:
            guess = self.user_input()

            if not self.validate_guess(guess):
                continue
            self.guess_count += 1

            feedback = self.get_feedback(guess)
            print(self.highlight_feedback(feedback))

            if self.detect_victory(feedback):
                print(f"\n{Color.GREEN.value}VICTORY!{Color.RESET.value}")
                self.game_result = "Victory"
            
            if self.detect_defeat():
                print(f"\n{Color.RED.value}YOU LOSE!{Color.RESET.value}")
                self.game_result = "Defeat"
        
        self.print_game_history()
        return


    def user_input(self):
        """Get user input for guess"""
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
        """Get feedback for user's guess"""
        if guess == self.the_wordle:
            feedback = "C" * self.WORD_LENGTH
            self.save_guess(guess, feedback)
            return self.highlight_feedback(feedback)

        feedback = ""
        for index in range(len(self.the_wordle)):

            # correct letter + correct placement
            if guess[index] == self.the_wordle[index]:
                feedback += "C"

            # correct letter + incorrect placement
            elif guess[index] in self.the_wordle:
                feedback += "c"
            
            # letter not in THE wordle
            else:
                feedback += "-"

        self.save_guess(guess, feedback)
        return feedback
    
    def highlight_feedback(self, feedback: str):
        """Highlight the correct letters in the feedback for better readability,
         'C' is highlighted in green
         'c' is highlighted in yellow
         '-' is highlighted in red
         """
        colored_feedback = ""
        for char in feedback:
            if char == "C":
                colored_feedback += f"{Color.GREEN.value}{char}{Color.RESET.value}"
            elif char == "c":
                colored_feedback += f"{Color.YELLOW.value}{char}{Color.RESET.value}"
            elif char == "-":
                colored_feedback += f"{Color.RED.value}{char}{Color.RESET.value}"
        return colored_feedback


    def save_guess(self, guessed_word: str, feedback: str):
        """Save the guess and feedback to history"""
        saved_guess = Guess(self.guess_count, guessed_word, feedback)
        self.game_history[self.guess_count] = saved_guess
        return


    def detect_victory(self, feedback: str):
        """ Detect victory when a guess is correct """
        correct_feedback = "C" * self.WORD_LENGTH
        if feedback == correct_feedback:
            return True
        return False

    def detect_defeat(self):
        """ Detect loss when guesses are finished """
        if self.guess_count == self.MAX_GUESS_COUNT:
            return True
        return False


    def print_game_history(self):
        """Print the game history,
         including the guesses and feedback"""
        print("\nGAME HISTORY")
        print(self.HISTORY_FORMAT.format("nr", "Guess", "Feedback"))
        for guess_nr, guess_round in self.game_history.items():
            colored_feedback = self.highlight_feedback(guess_round.feedback)
            print(self.HISTORY_FORMAT.format(guess_nr, guess_round.word, colored_feedback))
        return