# from Game.Wordle import Wordle
from Game.WordleGame import WordleGame
from Game.GameUI import GameUI
from ColorText import Color
from pathlib import Path

class GameMenu:
    WORDBANK_FILE_PATH = Path("WordBank") / "wordbank.txt"

    def __init__(self):
        self.round = None
        self.online = True
        
        self.load_wordbank()

        # self.user = User()

    def main_menu(self):

        while self.online:
            self.print_menu()

            user_input = input("\nEnter: ").lower()

            if user_input == "1":
                self.configure_game()
                self.play_game()

            elif user_input == "2":
                pass # TODO - See game history
            
            elif user_input == "q":
                self.online = False

            else:
                print(f"{Color.RED.value}Invalid input{Color.RESET.value}")
        
    def print_menu(self):
            print("\n------- WORDLE ------")
            print("(1) Play")
            print("(2) See Game History")
            print("\n(q) Quit")


    def configure_game(self):
        """Initialize the game, set the word length and user max guesses"""
        print("\n------- Initalize Game ------")

        while not self.round:
            word_length = input("Choose word length: ")
            if self.validate_word_length(word_length):
                break
        
        while not self.round:
            max_guess_count = input("Choose number of guesses: ")
            if self.validate_guess_count(max_guess_count):
                break

        self.round = WordleGame("HELLO", int(max_guess_count)) # LATER delete the default values


    def validate_word_length(self, user_input):
        """Validate the user input for word length"""
        if not user_input.isdigit():
            print(f"{Color.RED.value}Word length needs to be an integer{Color.RESET.value}\n")
            return False
        
        # LATER check the longest and shortest word in the wordbank
        shortest_word = 5
        longest_word = 10
        if shortest_word <= int(user_input) <= longest_word:
            return True
        print(f"{Color.RED.value}Word length needs to be between 5 and 10{Color.RESET.value}\n")
        return False
    
    def validate_guess_count(self, user_input):
        """Validate the user input for guess count"""
        if not user_input.isdigit():
            print(f"{Color.RED.value}Guess count needs to be an integer{Color.RESET.value}\n")
            return False
        if 1 <= int(user_input) <= 10:
            return True
        print(f"{Color.RED.value}Guess count needs to be between 1 and 10{Color.RESET.value}\n")
        return False


    def play_game(self):
        """Start the game"""
        print("\n------- Game Start ------")
        print(f"\nPlaying with {self.round.word_length}-letter word")
        print(f"Number of guesses: {self.round.max_guesses}")
        print(f"Secret word: {self.round.secret_word}")  # EYDA For debugging
        # self.round.game_play()
        ui = GameUI(self.round)
        ui.game_loop()
        self.round = None # Reset the game

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
# [ ] After finishing a game the user can select to quit or start a new game - 5%
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