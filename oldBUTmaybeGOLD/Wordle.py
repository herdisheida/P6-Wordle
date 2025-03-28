from utilities.ColorText import Color
from Game.Guess import Guess
from pathlib import Path
import json
from Game.User import User

class WordleGame():
    HISTORY_FORMAT = " {0:<5}{1:<20}{2:<20}"
    RESULT_FOLDER = Path("results")

    def __init__(self, wordle: str, max_guess_count: int = 5):
        self.secret_word: str = wordle.upper()
        self.max_guesses: int = max_guess_count
        self.word_length: int = len(wordle)
        
        self.game_result: dict = None
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
                print(f"\n{Color.GREEN.value}VICTORY!{Color.END.value}")
                score = (self.max_guesses - self.guess_count) ^ 2
                print(f"Score: {Color.BLUE.value}{score}{Color.END.value}")
                self.game_result = {"result": "Victory", "score": score}
            
            elif self.detect_defeat():
                print(f"\n{Color.RED.value}YOU LOSE!{Color.END.value}")
                print(f"Score: {Color.BLUE.value}0{Color.END.value}")
                print(f"The word was: {Color.BLUE.value}{self.secret_word}{Color.END.value}")
                self.game_result = {"result": "DEFEAT", "score": 0}
        
        self.print_game_history()
        self.save_game_result()
        self.reset_game()
        return


    def user_input(self):
        """Get user input for guess"""
        word = input("\nGuess: ").upper()
        return word

    def validate_guess(self, guess: str):
        """Checks if the guess is formatted correctly"""
        if not guess.isalpha():
            print(f"{Color.RED.value}Guess needs to be string{Color.END.value}")
            return False
        if len(guess) != self.word_length:
            print(f"{Color.RED.value}Guess needs to have {len(self.secret_word)} letters{Color.END.value}")
            return False
        return True


    def get_feedback(self, guess: str):
        """Get feedback for user's guess"""
        if guess.upper() == self.secret_word:
            feedback = "C" * self.word_length
            self.save_guess(guess, feedback)
            return feedback

        feedback = ""
        for index in range(len(self.secret_word)):

            # correct letter + correct placement
            if guess[index] == self.secret_word[index]:
                feedback += "C"

            # correct letter + incorrect placement
            elif guess[index] in self.secret_word:
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
                colored_feedback += f"{Color.GREEN.value}{char}{Color.END.value}"
            elif char == "c":
                colored_feedback += f"{Color.YELLOW.value}{char}{Color.END.value}"
            elif char == "-":
                colored_feedback += f"{Color.RED.value}{char}{Color.END.value}"
        return colored_feedback


    def save_guess(self, guessed_word: str, feedback: str):
        """Save the guess and feedback to history"""
        self.game_history[self.guess_count] = Guess(self.guess_count, guessed_word, feedback)
        return


    def detect_victory(self, feedback: str):
        """ Detect victory when a guess is correct """
        correct_feedback = "C" * self.word_length
        if feedback == correct_feedback:
            return True
        return False

    def detect_defeat(self):
        """ Detect loss when guesses are finished """
        if self.guess_count == self.max_guesses:
            return True
        return False

    def print_game_history(self):
        """Print the game history,
         including the guesses and feedback"""
        print("\n---------- GAME HISTORY ----------")
        print(self.HISTORY_FORMAT.format("nr", "Guesses", "Feedbacks"))
        for guess_nr, guess_round in self.game_history.items():
            colored_feedback = self.highlight_feedback(guess_round.feedback)
            print(self.HISTORY_FORMAT.format(guess_nr, guess_round.word, colored_feedback))
        return

    def save_game_result(self):
        """Save the game result to a file"""
        # username
        username = input("Enter your username: ") # LATER add this username in the menu section
        # username = self.get_user()
        filename = f"{username}_results.txt"
        file_path = self.RESULT_FOLDER / filename

        game = {
            "wordle": self.secret_word,
            "result": self.game_result["result"],
            "score": self.game_result["score"],
            "game_data": {
                guess_nr:  {
                    "word": guess_round.word,
                    "feedback": guess_round.feedback
                    } for guess_nr, guess_round in self.game_history.items()
                }
            }

        # create the results folder if it doesn't exist
        Path(self.RESULT_FOLDER).mkdir(parents=True, exist_ok=True)
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                all_games = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            all_games = []
        
        # add new game to existing games
        all_games.append(game)
        
        # update the user's result file
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(all_games, file, indent=4)
        
        return game

    def reset_game(self):
        """Reset the game for a new round"""
        self.game_result = None
        self.game_history = {}
        self.guess_count = 0
        return
