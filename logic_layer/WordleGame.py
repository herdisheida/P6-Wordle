from logic_layer.Guess import Guess
from pathlib import Path


class WordleGame:
    def __init__(self, secret_word: str, max_guesses: int):
        self.secret_word = secret_word
        self.max_guesses = max_guesses
        self.word_length = len(secret_word)

        self.game_result = None  # outcome, score
        self.game_round_history = {} # guesses, feedback
        self.guess_count = 0

        self.game_series = []
        # self.is_game_over = None

    def submit_guess(self, guess: str) -> str:
        """Process a guess and return feedback"""
        valid, msg = self._validate_guess(guess)
        if not valid:
            raise ValueError(msg)

        self.guess_count += 1
        feedback = self._calculate_feedback(guess)
        self._save_guess(guess, feedback)
        
        if feedback == "C" * self.word_length:
            self.game_result = {"outcome": "Victory", "score": self._calculate_score()}
            self._add_game_to_series()
        elif self.guess_count >= self.max_guesses:
            self.game_result = {"outcome": "Defeat", "score": self._calculate_score()}
            self._add_game_to_series()
        return feedback
    
    def _validate_guess(self, guess: str) -> tuple[bool, str]:
        """Validate guess format (pure logic)"""
        if not guess.isalpha():
            return False, "Guess needs to be alphabetic"
        if len(guess) != self.word_length:
            return False, f"Guess needs {self.word_length} letters"
        return True, ""

    def _calculate_feedback(self, guess: str) -> str:
        """Generate feedback string (C/c/-)"""
        secret_word = list(self.secret_word)
        guess_letters = list(guess)
        feedback = []

        # check correct letters in correct position
        for i in range(len(secret_word)):
            # Correct position
            if guess[i] == secret_word[i]:
                feedback.append("C")

                # mark as matched
                secret_word[i] = None
                guess_letters[i] = None
            else:
                feedback.append("-")

        # check correct letters in incorrect
        for i in range(len(secret_word)):
            curr_char = guess_letters[i]
            # skip letters in correct position
            if curr_char is None:
                continue
            if guess[i] in secret_word:
                feedback[i] = "c"
                secret_word[secret_word.index(curr_char)] = None

        self._save_guess(guess, feedback)
        return "".join(feedback)

    def _save_guess(self, guess: str, feedback: str):
        """Store guess in history"""
        self.game_round_history[self.guess_count] = Guess(self.guess_count, guess, feedback)

    def _calculate_score(self) -> int:
        """Calculate game score.
        The score is higher the fewer guesses the player used and the longer the wordle word is"""
        base_score = 100
        word_bonus = self.word_length * 10
        guess_penalty = (self.guess_count - 1) * 10
        return base_score + word_bonus - guess_penalty

    def _add_game_to_series(self):
        self.game_series.append({
                "secret_word": self.secret_word,
                "game_result": self.game_result,
                "game_round_history": self.game_round_history
                })

    @property
    def is_game_over(self) -> bool:
        return self.game_result is not None

    def reset(self):
        """Reset game state"""
        self.game_result = None
        self.game_round_history = {}
        self.guess_count = 0