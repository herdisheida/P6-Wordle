from Game.WordleGame import WordleGame
from Game.GameHistory import GameHistory
from ColorText import Color


class GameUI:

    def __init__(self, game: WordleGame, history: GameHistory):
        self.game = game
        self.history = history



    def game_loop(self):
        """Main game loop"""
        while not self.game.is_game_over:
            guess = self._get_guess()
            try:
                feedback = self.game.submit_guess(guess)
                self._display_feedback(feedback)
            except ValueError as e:
                print(f"{Color.RED.value}{str(e)}{Color.RESET.value}")

        self._display_result()
        self.save_game()
        self.game.reset()

    def _get_guess(self):
        """Get and validate user input"""
        return input("\nGuess: ").upper()

    def _display_feedback(self, feedback: str):
        """Show colored feedback"""
        print("Feedback: " + self._colorize_feedback(feedback))

    def _display_result(self):
        """Show win/loss message"""
        if self.game.game_result["outcome"] == "Victory":
            print(f"\n{Color.GREEN.value}VICTORY! Score: {self.game.game_result['score']}{Color.RESET.value}")
        else:
            print(f"\n{Color.RED.value}GAME OVER! Word was: {self.game.secret_word}{Color.RESET.value}")
        self._print_history()

    def _print_history(self):
        """Show guess history for game round"""
        print("\n---------- GAME HISTORY ----------")
        print(self.history.GAME_HISTORY_FORMAT.format("Nr", "Guess", "Feedback"))
        for nr, round in self.game.game_history.items():
            feedback = self._colorize_feedback(round.feedback)
            print(self.GAME_HISTORY_FORMAT.format(nr, round.word, feedback))

    def _colorize_feedback(self, feedback: str):
        """Colorize feedback string"""
        colored = ""
        for char in feedback:
            if char == "C":
                colored += f"{Color.GREEN.value}{char}{Color.RESET.value}"
            elif char == "c":
                colored += f"{Color.YELLOW.value}{char}{Color.RESET.value}"
            elif char == "-":
                colored += f"{Color.RED.value}{char}{Color.RESET.value}"
        return colored

    def save_game(self):
        """Save game results to file"""
        username = input("Enter username: ")
        self.history.save_game(
            username = username,
            secret_word = self.game.secret_word,
            game_result = self.game.game_result,
            game_history = self.game.game_history
        )