from Game.Guess import Guess
from pathlib import Path
import json


class WordleGame:
    RESULT_FOLDER = Path("results")

    def __init__(self, secret_word: str, max_guesses: int = 5):
        self.secret_word = secret_word
        self.max_guesses = max_guesses
        self.word_length = len(secret_word)

        self.game_result = None
        self.game_history = {}
        self.guess_count = 0

    def validate_guess(self, guess: str):
        """Validate guess format (pure logic)"""
        if not guess.isalpha():
            return False, "Guess needs to be alphabetic"
        if len(guess) != self.word_length:
            return False, f"Guess needs {self.word_length} letters"
        return True, ""

    def submit_guess(self, guess: str):
        """Process a guess and return feedback"""
        valid, msg = self.validate_guess(guess)
        if not valid:
            raise ValueError(msg)

        self.guess_count += 1
        feedback = self._calculate_feedback(guess)
        self._save_guess(guess, feedback)
        
        if feedback == "C" * self.word_length:
            self.game_result = {"result": "Victory", "score": self._calculate_score()}
        elif self.guess_count >= self.max_guesses:
            self.game_result = {"result": "Defeat", "score": self._calculate_score()}
            
        return feedback

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
        return (self.max_guesses - self.guess_count) * self.word_length

    def _save_results(self):
        """Save game results to file"""
        username = input("Enter username: ") # LATER add this username in the menu section
        file_path = self.RESULT_FOLDER / f"{username}_results.json"

        data = {
            "secret_word": self.secret_word,
            "result": self.game_result,
            "history": {
                nr: {
                    "guess": round.word,
                    "feedback": round.feedback
                }
                for nr, round in self.game_history.items()
            }
        }

        self.RESULT_FOLDER.mkdir(exist_ok=True)
        
        # get existing data and append new game to it
        try:
            with open(file_path, "r") as f:
                all_games = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            all_games = []
            
        all_games.append(data)
        
        with open(file_path, "w") as f:
            json.dump(all_games, f, indent=2)

    @property
    def is_game_over(self):
        return self.game_result is not None

    def reset(self):
        """Reset game state"""
        self.game_result = None
        self.game_history = {}
        self.guess_count = 0