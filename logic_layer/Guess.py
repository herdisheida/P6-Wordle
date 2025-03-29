class Guess:
    """A class to represent a single guess in the game"""
    def __init__(self, nr: int, word: str, feedback: str):
        self.nr = nr
        self.word = word
        self.feedback = feedback