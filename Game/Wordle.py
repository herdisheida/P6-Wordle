from ColorText import Color

class Wordle:

    def __init__(self):
        self.the_wordle: str = "HELLO"
        self.MAX_GUESS_COUNT: int = 5 # LATER customizable
        self.WORD_LENGTH = 5 # LATER customizable
        self.game_result: str = None

        self.user_inputs: dict = {} # FX: {nr: 1, word: ["W", "O", "R", "L", "D"], feedback: "-c-C-"}
        self.guess_count = 0

    def game_play(self):
        while not self.game_result:
            guess = self.user_input()

            if not self.validate_guess(guess):
                continue

            self.get_feedback(guess)


            


    def validate_guess(self, guess):
        """Checks if the guess is formatted correctly"""
        if not guess.isalpha():
            print(f"{Color.RED}Guess needs to be string{Color.RESET}")
            return False

        if len(guess) != self.WORD_LENGTH:
            print(f"{Color.RED}Guess needs to have {len(self.the_wordle)} letters{Color.RESET}")
            return False
        return True
        

    def get_feedback(self, guess):
        """Checks if guess is the correct wordly word, or close to it"""
        feedback = ""
        
        for index in range(len(self.the_wordle)):

            # correct letter + correct placement
            if guess[index] == self.the_wordle[index]:
                feedback += f"{Color.GREEN}C{Color.RESET}"

            # correct letter + incorrect placement
            elif guess[index] in self.the_wordle:
                feedback += f"{Color.YELLOW}c{Color.RESET}"
            
            # letter not in THE wordle
            else:
                feedback += f"{Color.RED}-{Color.RESET}"


        print(feedback)


    def user_input(self):
        word = input("Guess: ").upper()
        self.guess_count += 1
        return word
    

    def display_prev_guesses(self):
        """ Display previous guesses in the round """
        # TODO
        pass

    def display_code_with_guesses(self):
        """ Display code with each guess, -c-C- -  """
        # TODO
        pass

    def wrong_format(self):
        """ Lets user know if wrong format and doesn't crash"""
        # TODO
        pass

    def detect_defeat(self):
        """ Detect loss when guesses are finished """
        # TODO
        pass

    def detect_victory(self):
        """ Detect victory when a guess is correct """
        # TODO
        pass
    



