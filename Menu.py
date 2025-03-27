from Wordle import Wordle

class GameMenu:
    def __init__(self):
        self.wordle = Wordle()


    def main_menu(self):
        print("------- Wordle ------")
        print("Start Game")

        user_input = input("(y) Yes or (n) No : ")

        if user_input.lower() == "y":
            self.wordle.play_game()
        

    def get_word_from_wordbank(self):
        pass
        