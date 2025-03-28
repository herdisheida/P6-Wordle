class Guess:
    """A class to represent a guess in the game"""
    def __init__(self, nr: int, word: str, feedback: str):
        self.nr = nr
        self.word = word
        self.feedback = feedback
        
    def __str__(self):
        return f"{self.nr}: {self.word} {self.feedback}"