from logic_layer.Guess import Guess


class WordleGame:
    def __init__(self, secret_word: str, max_guesses: int):
        self.secret_word = secret_word
        self.max_guesses = max_guesses
        self.word_length = len(secret_word)

        self.game_result = None  # outcome, score
        self.outcome = None
        self.score = 0

        self.game_round_history = {} # guesses & feedbacks for each round in a single game instance
        self.guess_count = 0

        self.game_series = None

    def submit_guess(self, guess: str) -> str:
        """Process a guess and return feedback"""
        valid, msg = self._validate_guess(guess)
        if not valid:
            raise ValueError(msg)

        self.guess_count += 1
        feedback = self._calculate_feedback(guess)
        self._save_guess(guess, feedback)
        
        if feedback == "C" * self.word_length:
            self.outcome = "Victory"
            self.score = self._calculate_score("Victory")
            # self.game_result = {"outcome": "Victory", "score": self._calculate_score("Victory")} # EYDA setti kóða í variable
            self._save_game()
        elif self.guess_count >= self.max_guesses:
            self.outcome = "Defeat"
            self.score = self._calculate_score("Defeat")
            # self.game_result = {"outcome": "Defeat", "score": self._calculate_score("Defeat")} # EYDA setti kóða í class variable
            self._save_game()
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

    def _calculate_score(self, outcome: str) -> int:
        """Calculate game score.
        The score is higher the fewer guesses the player used and the longer the wordle word is"""
        if outcome == "Defeat":
            return -5 * self.guess_count
        word_bonus = 2 * self.word_length
        if self.max_guesses == self.guess_count:
            return 50 + word_bonus
        guess_penalty = (self.max_guesses - self.guess_count + 1) * 5
        return word_bonus - guess_penalty

    def _save_game(self):
        """Store game in game series variable"""
        self.game_series = {
                "secret_word": self.secret_word,
                "game_result": self.game_result,
                "game_round_history": self.game_round_history
                }

    @property
    def is_game_over(self) -> bool:
        return self.outcome is not None

    def reset_game(self):
        """Reset game state"""
        self.game_result = None
        self.game_round_history = {}
        self.guess_count = 0
        self.game_series = None