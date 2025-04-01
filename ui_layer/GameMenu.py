from ui_layer.GameUI import GameUI
from ui_layer.ColorText import Color
from logic_layer.WordleGame import WordleGame
from logic_layer.GameSeries import GameSeries
from storage_layer.wordbank.WordBank import WordBank
from ui_layer.GameHistoryUI import GameHistoryUI


class GameMenu:
    def __init__(self):
        self.online = True
        self.username = None
        self.game_history = None

        self.word_bank = WordBank()

    def run(self):
        """Run the game menu"""
        self._login()
        print(f"\n{Color.BLUE.value}Goodbye {self.username.capitalize()}!{Color.END.value}")

    def _login(self):
        """Handle user login flow"""
        while self.online:
            print("\n------- LOGIN -------")
            print(f" {Color.BLUE.value}Welcome to Wordle!{Color.END.value}")
            choice = input("\n(S) Signup | (L)ogin | (Q)uit\n").lower()
            match choice:
                case "l" | "s":
                    self._handle_login()
                case "q":
                    self.online = False
                case _:
                    self._display_error("Invalid input")

    def _handle_login(self) -> str:
        """Authenticate user and initalize game history"""
        self.username = self._get_valid_input("Enter username: ", self._validate_username)
        self.game_history = GameHistoryUI(self.username)
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
                case "1":
                    self._start_new_series()
                case "2":
                    self.game_history.history_menu()
                case "3":
                    self._add_word_to_wordbank()
                case "l":
                    return  # return to login
                case "q":
                    self.online = False
                case _:
                    self._display_error("Invalid input")

    def _start_new_series(self):
        """Start a ew game series"
        and configure game settings"""
        print(f"\n{Color.BLUE.value}------- Game Start ------{Color.END.value}")

        # initialize game series
        word_length = int(self._get_valid_input("Enter word length: ", self._get_valid_word_length))
        max_guess_count = int(self._get_valid_input("Enter number of guess attempts: ", self._get_valid_attempts))
        series = GameSeries(word_length, max_guess_count)

        while self.online:
            print(f"\n{Color.BLUE.value} -- New Game -- {Color.END.value}")

            try:
                # configure game
                secret_word = self.word_bank.get_random_word(word_length)

                # start game
                active_game = WordleGame(secret_word, max_guess_count)
                GameUI(active_game, series, self.game_history).run()

                if not self._continue_playing():
                    break
            except ValueError as e:
                self._display_error(str(e))

        self._display_series_result(series)
        self.game_history.save_game_series(series)

    def _continue_playing(self):
        """Check if user wants to keep playing"""
        play_again = None
        while not play_again:
            choice = input("\nDo you want to continue playing? (Y/N): ").lower()

            match choice:
                case "y":
                    return True
                case "n":
                    return False
                case _:
                    print(f"{Color.RED.value}Invalid input.{Color.END.value}")

    def _display_series_result(self, series: GameSeries):
        """Display game series result,
        including longest streak and total score
        """
        print(f"\n{Color.BLUE.value}------- Game Series Result -------{Color.END.value}")
        print(f"Total games played: {len(series.game_list)}")
        print(f"Total score: {series.total_score}")
        input(self.game_history.SCREEN_PAUSE)

    def _add_word_to_wordbank(self):
        """Add a word to the word bank"""
        new_word = input("Enter a new word: ").upper()
        try:
            self.word_bank.add_word(new_word)
            print(f"{Color.GREEN.value}{new_word} was added successfully!{Color.END.value}")
        except ValueError as e:
            self._display_error(str(e))

    def _get_valid_attempts(self, num: str) -> int:
        """Validate the user input for guess count"""
        if not num.isdigit():
            raise ValueError("Num needs to be a positive integer")
        if int(num) < 1:
            raise ValueError("Num must be greater than 0")
        if int(num) > 20:
            raise ValueError("Num too high (max 20)")
        return int(num)

    def _get_valid_word_length(self, word_length: str) -> int:
        if not word_length.isdigit():
            raise ValueError("Word length needs to be a positive integer")
        letter_lengths = self.word_bank.get_word_lengths()
        if int(word_length) not in letter_lengths:
            raise ValueError(f"No word found with {word_length}-letters \nWord length available: {str(letter_lengths)}\n")
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
        """Display error message in red"""
        print(f"{Color.RED.value}{message}{Color.END.value}")
