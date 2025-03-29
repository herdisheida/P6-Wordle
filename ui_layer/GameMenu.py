from ui_layer.GameUI import GameUI
from ui_layer.ColorText import Color
from logic_layer.WordleGame import WordleGame
from logic_layer.GameSeries import GameSeries
from storage_layer.wordbank.WordBank import WordBank
from ui_layer.GameHistoryUI import GameHistory

class GameMenu:
    def __init__(self):
        self.online = True
        self.username = None
        self.game_history = None

        self.word_bank = WordBank()

    def run(self):
        """Run the game menu"""
        self._login()
        print(f"\n{Color.BLUE.value}Goodbye {self.username}!{Color.END.value}")

    def _login(self):
        """Handle user login flow"""
        while self.online:
            print("\n------- LOGIN -------")
            print(f" {Color.BLUE.value}Welcome to Wordle!{Color.END.value}") # LATER UI weird
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
            print("(3) Add Word to Word Bank\n")
            print("(L)ogout")
            print("(Q)uit")

    def _main_menu(self):
        """Main menu loop"""
        while self.online:
            self._display_main_menu()
            choice = input("\nEnter: ").lower()

            match choice:
                case "1": self._start_new_series()
                case "2": self.game_history.history_menu()
                case "3": self._add_word_to_wordbank()
                case "l": return # return to login
                case "q": self.online = False
                case _: self._display_error("Invalid input")

    def _start_new_series(self):
        """Start a ew game series"
        and configure game settings"""
        print(f"\n{Color.BLUE.value}------- Game Start ------{Color.END.value}")

        # initialize game series
        word_length = int(self._get_valid_input("Enter word length: ", self._get_valid_word_length))
        max_guess_count = int(self._get_valid_input("Enter number of guess attempts: ", self._get_valid_attempts))
        series = GameSeries(word_length, max_guess_count)

        while True: # TODO breya while true
            print(f"\n{Color.BLUE.value} -- New Game -- {Color.END.value}")
        
            try:
                # configure game
                secret_word = self.word_bank.get_random_word(word_length)

                # secret_word = "HELLO" # EYDA debug

                # start game
                active_game = WordleGame(secret_word, max_guess_count)
                GameUI(active_game, series, self.game_history).run() # FIX vtk hvort ég ætli að hafa game_history sem argument
                series.add_game(active_game)

                if not self._continue_playing():
                    break

            except ValueError as e:
                self._display_error(str(e))
        
        self.game_history.save_game_series(series)
            

    def _continue_playing(self):
        """Check if user wants to keep playing"""
        play_again = None
        while not play_again:
            choice = input("\nDo you want to continue playing? (Y/N): ").lower()

            if choice == "y":
                return True
            elif choice == "n":
                return False
            else:
                print(f"{Color.RED.value}Invalid input.{Color.END.value}")
                continue


    def _add_word_to_wordbank(self):
        """Add a word to the word bank"""
        new_word = input("Enter a new word: ").upper()
        try:
            self.word_bank.add_word(new_word)
            print(f"{Color.GREEN.value}Word added successfully!{Color.END.value}")
        except ValueError as e:
            self._display_error(str(e))

    def _get_valid_attempts(self, num: str) -> int:
        """Validate the user input for guess count"""
        if not num.isdigit():
            raise ValueError("Num needs to be an integer\n")
        if int(num) < 1:
            raise ValueError("Num must be greater than 0\n")
        if int(num) > 20:
            raise ValueError("Num too high (max 20)\n")
        return int(num)
    
    def _get_valid_word_length(self, word_length: str) -> int:
        if not word_length.isdigit():
            raise ValueError("Word length needs to be an integer")
        min_length, max_length = self.word_bank.get_max_min_word_length()
        if int(word_length) < min_length or int(word_length) > max_length:
            raise ValueError(f"No word found with {word_length}-letters \nWord length must be between {min_length} and {max_length}\n")
        return int(word_length)

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
# [x] After finishing a game the user can select to quit or start a new game - 5%
        # TODO i can only let them play again, not continue the game...
# [x] Program stores word bank in a data structure - 5%
# [x] Program randomly selects word from word bank - 5%
# [x] The word bank is stored in and read from a file - 10%

# 3. CONNECTED SERIES OF GAMES - 30% (that makes 110%)
# [x] Keep track of wins and losses throughout the run (store in classes/variables) - 5%
        # TODO i only have that in a file
# [x] Find a way to score series of games and keep track of high scores - 5%
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
        # [x] scores ( scoring series of games --- breyta kerfinu ugghhh)
        # [ ] games played

    # FIX :
        # [x] user see history games/scores -- lookar öðruvísi í series of games
        # [x] let user choose to continue playing game:
            # [x] if played 1's = single game instance, else = series of connected games

# TODO
    # [x] the feedback is not good enough
    # [x] when lette is correct stop showing that letter as yellow in other places


# IDEAS
    # [x] make class for SeriesOfGames, save stuff their...?