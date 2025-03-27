class Guess:
    def __init__(self, nr, word, feedback):
        self.nr = nr
        self.word = word
        self.feedback = feedback
        
    def __str__(self):
        return f"{self.nr}: {self.word} {self.feedback}"