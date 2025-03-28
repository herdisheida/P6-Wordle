from Game.WordleGame import WordleGame
from Game.GameUI import GameUI
from pathlib import Path
from ColorText import Color

from WordBank.WordBank import WordBank
from Game.GameHistory import GameHistory

class GameMenu:
    WORDBANK_FILE_PATH = Path("WordBank") / "wordbank.txt"

    def __init__(self):
        self.online = True
        self.active_game = None
        
        self.word_bank = WordBank()
        self.game_history = GameHistory() # TODO

        # self.user = User()


    def display_menu(self):
            """Display the main menu"""
            print("\n------- WORDLE ------")
            print("(1) Play")
            print("(2) See Game History")
            print("\n(q) Quit")

    def main_loop(self):
        """Main menu loop"""
        self.load_wordbank()
        while self.online:
            self.display_menu()

            user_input = input("\nEnter: ").lower()

            if user_input == "1":
                self.configure_game()
                self.start_game()

            elif user_input == "2":
                pass # TODO - See game history
            
            elif user_input == "q":
                self.online = False

            else:
                print(f"{Color.RED.value}Invalid input{Color.RESET.value}")
        


    def configure_game(self):
        """Initialize the game, set the word length and user max guesses"""
        print("\n------- Initalize Game ------")

        while not self.active_game:
            try:
                word_length = input("Choose word length: ")
                secret_word = self._get_secret_word(word_length)
            except ValueError as e:
                print(f"{Color.RED.value}{str(e)}{Color.RESET.value}")
                continue
        
            try:
                max_guess_count = input("Choose number of guesses: ")
                self.validate_guess_count(max_guess_count)
            except ValueError as e:
                print(f"{Color.RED.value}{str(e)}{Color.RESET.value}")
                continue

            self.active_game = WordleGame(secret_word, int(max_guess_count))


    def _get_secret_word(self, word_length: int):
        """Validate the user input for word length"""
        if not word_length.isdigit():
            raise ValueError("Word length needs to be an integer\n")
        secret_word = self.word_bank.get_random_word(int(word_length))        
        return secret_word.upper()
    
    def validate_guess_count(self, guess_count: int):
        """Validate the user input for guess count"""
        if not guess_count.isdigit():
            raise ValueError("Guess count needs to be an integer\n")
        guess_count = int(guess_count)
        if guess_count <= 0 or guess_count > 20:
            raise ValueError("Guess count needs to be between 1 and 20\n")
        return True

    def start_game(self):
        """Start the game"""
        print("\n------- Game Start ------")
        print(f"Playing with {self.active_game.word_length}-letter word")
        print(f"Number of guesses: {self.active_game.max_guesses}")
        print(f"Secret word: {self.active_game.secret_word}")  # EYDA For debugging
        # self.round.game_play()
        ui = GameUI(self.active_game)
        ui.game_loop()
        self.active_game = None # Reset the game




    def load_wordbank(self):
        """Create a data structure to store the words from the wordbank file"""
        with open(self.WORDBANK_FILE_PATH, mode="r", encoding="utf-8") as file:
            self.wordbank = file.readlines()

    def get_word(self, word_length):
        """Get a random word from the wordbank"""
        # TODO
        pass



# MORE REFINED SINGLE GAME - 30%
# [x] User can input or select number of letters and guesses before the game begins - 5%
    # ○ Extends the "5 letters, 5 guesses" requirement
# [x] After finishing a game the user can select to quit or start a new game - 5%
# [ ] Program stores word bank in a data structure - 5%
# [ ] Program randomly selects word from word bank - 5%
# [ ] The word bank is stored in and read from a file - 10%

# 3. CONNECTED SERIES OF GAMES - 30% (that makes 110%)
# [ ] Keep track of wins and losses throughout the run (store in classes/variables) - 5%
# [ ] Find a way to score series of games and keep track of high scores - 5%
    # ○ Total scores can for example be affected by (but not limited by):
        # ■ # of wrong guesses per word
        # ■ length of word
        # ■ # of games before loss (or total score of those games), etc.
# [ ] Scores/highscores stored so that they live between runs of the program - 5%
# [ ] Allow words to be added to the word bank (and file) through the program itself - 5%
# [ ] Allow user to see their history of games/scores - 5%
# [ ] Allow save/profile for multiple users - 5%
    # ○ Students figure out how best to accomplish this
    # ○ Don't need password login, but switching/selecting users