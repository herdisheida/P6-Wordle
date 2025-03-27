from Wordle import Wordle

class GameMenu:
    def __init__(self):
        self.wordle = Wordle()


    def main_menu(self):
        print("------- Wordle ------")
        print("Start Game")

        user_input = input("(y) Yes or (n) No : ")

        if user_input.lower() == "y":
            self.wordle.game_play()
        

    def get_wordbank(self):
        pass
        # TODO



# MORE REFINED SINGLE GAME - 30%
# TODO User can input or select number of letters and guesses before the game begins - 5%
    # ○ Extends the "5 letters, 5 guesses" requirement
# TODO After finishing a game the user can select to quit or start a new game - 5%
# TODO Program stores word bank in a data structure - 5%
# TODO Program randomly selects word from word bank - 5%
# TODO The word bank is stored in and read from a file - 10%

# 3. CONNECTED SERIES OF GAMES - 30% (that makes 110%)
# TODO Keep track of wins and losses throughout the run (store in classes/variables) - 5%
# TODO Find a way to score series of games and keep track of high scores - 5%
    # ○ Total scores can for example be affected by (but not limited by):
        # ■ # of wrong guesses per word
        # ■ length of word
        # ■ # of games before loss (or total score of those games), etc.
# TODO Scores/highscores stored so that they live between runs of the program - 5%
# TODO Allow words to be added to the word bank (and file) through the program itself - 5%
# TODO Allow user to see their history of games/scores - 5%
# TODO Allow save/profile for multiple users - 5%
    # ○ Students figure out how best to accomplish this
    # ○ Don't need password login, but switching/selecting users