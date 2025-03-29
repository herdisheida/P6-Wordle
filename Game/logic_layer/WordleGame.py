from logic_layer.Guess import Guess
from pathlib import Path


class WordleGame:
    RESULT_FOLDER = Path("./storage_layer/results")

    def __init__(self, secret_word: str, max_guesses: int):
        self.secret_word = secret_word
        self.max_guesses = max_guesses
        self.word_length = len(secret_word)

        self.game_result = None
        self.game_history = {}
        self.guess_count = 0

    def submit_guess(self, guess: str):
        """Process a guess and return feedback"""
        valid, msg = self._validate_guess(guess)
        if not valid:
            raise ValueError(msg)

        self.guess_count += 1
        feedback = self._calculate_feedback(guess)
        self._save_guess(guess, feedback)
        
        if feedback == "C" * self.word_length:
            self.game_result = {"outcome": "Victory", "score": self._calculate_score()}
        elif self.guess_count >= self.max_guesses:
            self.game_result = {"outcome": "Defeat", "score": self._calculate_score()}
        return feedback
    
    def _validate_guess(self, guess: str):
        """Validate guess format (pure logic)"""
        if not guess.isalpha():
            return False, "Guess needs to be alphabetic"
        if len(guess) != self.word_length:
            return False, f"Guess needs {self.word_length} letters"
        return True, ""

    def _calculate_feedback(self, guess: str):
        """Generate feedback string (C/c/-)"""
        feedback = ""

        for index in range(len(self.secret_word)):
            # Correct position
            if guess[index] == self.secret_word[index]:
                feedback += "C"

            # Correct letter in wrong position
            elif guess[index] in self.secret_word:
                feedback += "c"
            
            # Incorrect letter
            else:
                feedback += "-"

        self._save_guess(guess, feedback)
        return feedback

    def _save_guess(self, guess: str, feedback: str):
        """Store guess in history"""
        self.game_history[self.guess_count] = Guess(self.guess_count, guess, feedback)

    def _calculate_score(self):
        """Calculate game score.
        The score is higher the fewer guesses the player used and the longer the wordle word is"""
        base_score = 100
        word_bonus = self.word_length * 10
        guess_penalty = (self.guess_count - 1) * 10
        return base_score + word_bonus - guess_penalty

    @property
    def is_game_over(self):
        return self.game_result is not None

    def reset(self):
        """Reset game state"""
        self.game_result = None
        self.game_history = {}
        self.guess_count = 0