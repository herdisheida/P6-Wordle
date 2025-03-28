from Game.WordleGame import WordleGame
from Game.GameUI import GameUI
from pathlib import Path
from utilities.ColorText import Color

from WordBank.WordBank import WordBank
from Game.GameHistory import GameHistory

class GameMenu:
    WORDBANK_FILE_PATH = Path("WordBank") / "wordbank.txt"

    def __init__(self):
        self.online = True
        self.active_game = None
        
        self.word_bank = WordBank()

        # self.username = input("Enter username: ") # EYDA
        # self.game_history = GameHistory(self.username)
        self.username = None
        self.game_history = None

    def _display_main_menu(self):
            """Display the main menu"""
            print(f"\n------- {self.username.capitalize()}'s WORDLE -------")
            print("(1) Play")
            print("(2) See Game History")
            print()
            print("(3) Logout")
            print("(q) Quit")

    def _display_error(self, message):
        """ Display error message in red """
        print(f"{Color.RED.value}{message}{Color.END.value}")

    def login_loop(self):
        """Login menu"""
        self.username = None
        self.game_history = None

        print("\n------- LOGIN -------")
        print("Welcome to Wordle!")

        while self.online:
            login_input = input("\nEnter (y) to login or (q) to quit: ").lower()

            if login_input == "y":
                self._fetch_username()
                # Start and create game history
                self.game_history = GameHistory(self.username)
                self.main_loop()

            elif login_input == "q":
                self.online = False
            else:
                self._display_error("Invalid input")

    def _fetch_username(self) -> str:
        """Get username from user"""
        while not self.username:
            username = input("Enter username: ")
            if not username:
                self._display_error("Username cannot be empty")
                continue
            self.username = username

    def main_loop(self):
        """Main menu loop"""
        while self.online:

            self._display_main_menu()

            user_input = input("\nEnter: ").lower()

            if user_input == "1":
                self.configure_game()
                self.start_game()
            elif user_input == "2":
                self.game_history.menu_loop()
            
            elif user_input == "3":
                return self.login_loop()
            elif user_input == "q":
                self.online = False
            else:
                self._display_error("Invalid input")

    def configure_game(self):
        """Initialize the game, set the word length and user max guesses"""
        print("\n------- Initalize Game ------")

        while not self.active_game:
            try:
                word_length = input("Choose word length: ")
                secret_word = self._get_secret_word(word_length)
            except ValueError as e:
                self._display_error(str(e))
                continue
        
            try:
                max_guess_count = input("Choose number of guess attempts: ")
                self._validate_guess_count(max_guess_count)
            except ValueError as e:
                self._display_error(str(e))
                continue

            self.active_game = WordleGame(secret_word, int(max_guess_count))


    def _get_secret_word(self, word_length: int):
        """Validate the user input for word length"""
        if not word_length.isdigit():
            raise ValueError("Word length needs to be an integer\n")
        secret_word = self.word_bank.get_random_word(int(word_length))
        print(f"Secret word: {secret_word}") # EYDA DEBUG
        return secret_word.upper()
    
    def _validate_guess_count(self, guess_count: int):
        """Validate the user input for guess count"""
        if not guess_count.isdigit():
            raise ValueError("Guess count needs to be an integer\n")
        guess_count = int(guess_count)
        if guess_count <= 0 or guess_count > 20:
            raise ValueError("Guess count needs to be between 1 and 20 (including 1 and 20)\n")
        return True

    def start_game(self):
        """Start the game"""
        print("\n------- Game Start ------")
        print(f"Playing with {self.active_game.word_length}-letter word")
        print(f"Number of guesses: {self.active_game.max_guesses}")
        ui = GameUI(self.active_game, self.game_history)
        ui.game_loop()
        self.active_game = None # Reset the game



# MORE REFINED SINGLE GAME - 30%
# [x] User can input or select number of letters and guesses before the game begins - 5%
    # ○ Extends the "5 letters, 5 guesses" requirement
# [x] After finishing a game the user can select to quit or start a new game - 5%
# [x] Program stores word bank in a data structure - 5%
# [x] Program randomly selects word from word bank - 5%
# [x] The word bank is stored in and read from a file - 10%

# 3. CONNECTED SERIES OF GAMES - 30% (that makes 110%)
# [ ] Keep track of wins and losses throughout the run (store in classes/variables) - 5%
# [ ] Find a way to score series of games and keep track of high scores - 5%
    # ○ Total scores can for example be affected by (but not limited by):
        # ■ # of wrong guesses per word
        # ■ length of word
        # ■ # of games before loss (or total score of those games), etc.
# [ ] Scores/highscores stored so that they live between runs of the program - 5%
# [ ] Allow words to be added to the word bank (and file) through the program itself - 5%
# [x] Allow user to see their history of games/scores - 5%
# [x] Allow save/profile for multiple users - 5%
    # ○ Students figure out how best to accomplish this
    # ○ Don't need password login, but switching/selecting users