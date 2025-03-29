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
        self.username = None
        self.game_history = None

        self.word_bank = WordBank()

    def run(self):
        """Run the game menu"""
        self._login()
        print(f"\n{Color.BLUE.value}Goodbye!{Color.END.value}")

    def _login(self):
        """Handle user login flow"""
        print("\n------- LOGIN -------")
        print(f" {Color.BLUE.value}Welcome to Wordle!{Color.END.value}") # LATER UI weird

        while self.online:
            choice = input("\n(L)ogin | (Q)uit: ").lower()
            match choice:
                case "l": self._handle_login()
                case "q": self.online = False
                case _: self._display_error("Invalid input")

    def _handle_login(self) -> str:
        """Authenticate user and initalize game history"""
        self.username = self._get_valid_input("Enter username: ", self._validate_username)
        self.game_history = GameHistory(self.username)
        self._main_menu()
    
    def _display_main_menu(self):
            """Display the main menu"""
            print(f"\n{Color.BLUE.value}------- {self.username.capitalize()}'s WORDLE -------{Color.END.value}")
            print("(1) New Game")
            print("(2) See Game History")
            print("(3) Add Word to Word Bank")

            print("(L) Logout")
            print("(Q) Quit")

    def _main_menu(self):
        """Main menu loop"""
        while self.online:
            self._display_main_menu()
            choice = input("\nEnter: ").lower()

            match choice:
                case "1": self._start_new_game()
                case "2": self.game_history.history_menu()
                case "3": self._add_word_to_wordbank()
                case "l": return # return to login
                case "q": self.online = False
                case _: self._display_error("Invalid input")

    def _start_new_game(self):
        """Configure and start a new game"""

        try:
            # configure game
            word_length = self._get_valid_input("Enter word length: ", self._get_valid_num)
            max_guess_count = self._get_valid_input("Enter number of guess attempts: ", self._get_valid_num)
            secret_word = self.word_bank.get_random_word(word_length)

            # start game
            print(f"\n{Color.BLUE.value}------- Game Start ------{Color.END.value}")
            print(f"Secret word: {Color.BLUE.value}{Color.UNDERLINE.value}{secret_word}{Color.END.value}") # EYDA DEBUG
            self.active_game = WordleGame(secret_word, int(max_guess_count))
            GameUI(self.active_game, self.game_history).run()

        except ValueError as e:
            self._display_error(str(e))
        finally:
            self.active_game = None

    def _add_word_to_wordbank(self):
        """Add a word to the word bank"""
        new_word = input("Enter a new word: ").upper()
        try:
            self.word_bank.add_word(new_word)
            print(f"{Color.GREEN.value}Word added successfully!{Color.END.value}")
        except ValueError as e:
            self._display_error(str(e))

    def _get_valid_num(self, num: int):
        """Validate the user input for guess count"""
        if not num.isdigit():
            raise ValueError("Num needs to be an integer")
        if int(num) < 1:
            raise ValueError("Num must be greater than 0")
        if int(num) > 20:
            raise ValueError("Num too high (max 20)")
        return int(num)

    def _get_valid_input(self, prompt: str, validation_func: callable) -> str:
        """Get valid input from user"""
        not_valid_input = True
        while not_valid_input:
            user_input = input(prompt)
            try:
                if validation_func(user_input):
                    not_valid_input = False
            except ValueError as e:
                self._display_error(str(e))
        return user_input

    def _validate_username(self, username: str) -> bool:
        """Validate the username"""
        if not username:
            raise ValueError("Username cannot be empty")
        if len(username) > 20:
            raise ValueError("Username too long (max 20 characters)")
        return True

    def _display_error(self, message):
        """ Display error message in red """
        print(f"{Color.RED.value}{message}{Color.END.value}")





# 1. BASIC GAME - 50%
# [x] Display previous guesses in the round - 10%
# [x] Display code with each guess, -c-C- - 10%
# [x] Lets user know if wrong format and doesn't crash - 5%
# [x] Handles uppercase and lowercase without complaint - 5%
# [x] Detect loss when guesses are finished - 10%
# [x] Detect victory when a guess is correct - 10%

# 2. MORE REFINED SINGLE GAME - 30%
# [x] User can input or select number of letters and guesses before the game begins - 5%
    # ○ Extends the "5 letters, 5 guesses" requirement
# [ ] After finishing a game the user can select to quit or start a new game - 5%
        # TODO i can only let them play again, not continue the game...
# [x] Program stores word bank in a data structure - 5%
# [x] Program randomly selects word from word bank - 5%
# [x] The word bank is stored in and read from a file - 10%

# 3. CONNECTED SERIES OF GAMES - 30% (that makes 110%)
# [ ] Keep track of wins and losses throughout the run (store in classes/variables) - 5%
        # TODO i only have that in a file
# [ ] Find a way to score series of games and keep track of high scores - 5%
    # ○ Total scores can for example be affected by (but not limited by):
        # ■ # of wrong guesses per word
        # ■ length of word
        # ■ # of games before loss (or total score of those games), etc.
# [ ] Scores/highscores stored so that they live between runs of the program - 5%
# [x] Allow words to be added to the word bank (and file) through the program itself - 5%
# [x] Allow user to see their history of games/scores - 5%
# [x] Allow save/profile for multiple users - 5%
    # ○ Students figure out how best to accomplish this
    # ○ Don't need password login, but switching/selecting users




# TODO 'connected' series of games (not singular instance)
    # add calass variables:
        # wins
        # losses
        # scores ( scoring series of games --- breyta kerfinu ugghhh)
        # high score
        # games played

    # FIX :
        # user see history games/scores -- lookar öðruvísi í series of games
        # let user choose to continue playing game:
            # if played 1's = single game instance, else = series of connected games


# IDEAS
    # make class for SeriesOfGames, save stuff their...?