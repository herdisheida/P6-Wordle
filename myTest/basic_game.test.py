# Add the parent directory to Python's path
import sys
import os

# Get the absolute path of the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

# Now import from the `Game` folder
from Game.Wordle import Wordle


import unittest


class TestWordleGame(unittest.TestCase):

    def setUp(self):
        self.wordle = Wordle()
        self.wordle.wordle = "HELLO"  # Set a fixed word for testing
        self.wordle.max_attempts = 3  # Reduce guesses for quicker tests

    def test_display_previous_guesses(self):
        self.wordle.guess_count = 1
        self.wordle.save_guess("HOUSE", "-c---")
        self.wordle.guess_count = 2
        self.wordle.save_guess("HELLO", "CCCCC")
        history = self.wordle.game_history
        self.assertEqual(len(history), 2)
        self.assertEqual(history[1].word, "HOUSE")
        self.assertEqual(history[2].feedback, "CCCCC")

    def test_feedback_display(self):
        feedback = self.wordle.get_feedback("HOLLY")
        self.assertEqual(feedback, "CcCC-")

    def test_invalid_format(self):
        self.assertFalse(self.wordle.validate_guess("12345"))  # Non-alphabetic
        self.assertFalse(self.wordle.validate_guess("HEL"))    # Incorrect length
        self.assertTrue(self.wordle.validate_guess("HELLO"))   # Valid guess

    def test_case_insensitivity(self):
        self.assertTrue(self.wordle.validate_guess("hello"))  # Lowercase input
        feedback = self.wordle.get_feedback("hello")
        self.assertEqual(feedback, "CCCCC")

    def test_detect_loss(self):
        self.wordle.guess_count = 3
        self.assertTrue(self.wordle.detect_defeat())

    def test_detect_victory(self):
        feedback = self.wordle.get_feedback("HELLO")
        self.assertTrue(self.wordle.detect_victory(feedback))

if __name__ == "__main__":
    unittest.main()
