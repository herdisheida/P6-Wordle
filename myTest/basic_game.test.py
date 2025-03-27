# Add the parent directory to Python's path
import sys
import os

# Get the absolute path of the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

# Now import from the `Game` folder
from Game.WordleGame import WordleGame
from Game.GameUI import GameUI


import unittest


class TestWordleGame(unittest.TestCase):

    def setUp(self):
        self.wordle_game = WordleGame("HELLO", max_guesses=3)
        self.game_ui = GameUI(self.wordle_game)

    def test_display_previous_guesses(self):
        self.wordle_game.guess_count = 1
        self.wordle_game._save_guess("HOUSE", "-c---")
        self.wordle_game.guess_count = 2
        self.wordle_game._save_guess("HELLO", "CCCCC")
        history = self.wordle_game.game_history
        self.assertEqual(len(history), 2)
        self.assertEqual(history[1].word, "HOUSE")
        self.assertEqual(history[2].feedback, "CCCCC")

    def test_feedback_display(self):
        feedback = self.wordle_game.submit_guess("HOLLY")
        self.assertEqual(feedback, "CcCC-")

    def test_invalid_format(self):
        valid, msg = self.wordle_game.validate_guess("12345")  # Non-alphabetic
        self.assertFalse(valid)
        self.assertEqual(msg, "Guess needs to be alphabetic")

        valid, msg = self.wordle_game.validate_guess("HEL")  # Incorrect length
        self.assertFalse(valid)
        self.assertEqual(msg, "Guess needs 5 letters")

        valid, msg = self.wordle_game.validate_guess("HELLO")  # Valid guess
        self.assertTrue(valid)
        self.assertEqual(msg, "")

    def test_case_insensitivity(self):
        feedback = self.wordle_game.submit_guess("hello")  # Lowercase input
        self.assertEqual(feedback, "CCCCC")

    def test_detect_loss(self):
        self.wordle_game.guess_count = 3
        self.wordle_game.submit_guess("WRONG")
        self.wordle_game.submit_guess("WORLD")
        self.wordle_game.submit_guess("NOOOO")

        self.assertTrue(self.wordle_game.is_game_over)
        self.assertEqual(self.wordle_game.game_result["result"], "Defeat")

    def test_detect_victory(self):
        feedback = self.wordle_game.submit_guess("HELLO")
        self.assertTrue(self.wordle_game.is_game_over)
        self.assertEqual(self.wordle_game.game_result["result"], "Victory")

    def test_game_ui_feedback_display(self):
        feedback = "C-c-C-"
        colored_feedback = self.game_ui._colorize_feedback(feedback)
        self.assertIn("\033[32mC\033[0m", colored_feedback)  # Green for 'C'
        self.assertIn("\033[33mc\033[0m", colored_feedback)  # Yellow for 'c'
        self.assertIn("\033[31m-\033[0m", colored_feedback)  # Red for '-'

if __name__ == "__main__":
    unittest.main()
