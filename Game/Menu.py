from Game.Wordle import Wordle
from ColorText import Color

class GameMenu:
    def __init__(self):
        self.wordle = None
        self.online = True
        
        self.get_wordbank()

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

        while not self.wordle:
            word_length = input("Choose word length: ")
            if self.validate_input(word_length, "Word length"):
                break
        
        while not self.wordle:
            max_guess_count = input("Choose number of guesses: ")
            if self.validate_input(max_guess_count, "Max guesses"):
                break

        self.wordle = Wordle("HELLO", int(max_guess_count), int(word_length)) # LATER delete the default values

    def validate_input(self, user_input, check_type):
        """Check if the user input is valid"""
        if user_input.isdigit():
            return True
        print(f"{Color.RED.value}{check_type} needs to be an integer{Color.RESET.value}\n")
        return False

    def play_game(self):
        """Start the game"""
        print(f"\nPlaying with {self.wordle.word_length}-letter word")
        print(f"Secret word: {self.wordle.wordle}")  # DELETE For debugging
        self.wordle.game_play()
        self.wordle = None # Reset the game

    def get_wordbank(self):
        pass
        # TODO



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