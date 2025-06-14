from ui_layer.ColorText import Color
from logic_layer.WordleGame import WordleGame
from logic_layer.GameSeries import GameSeries
from ui_layer.GameHistoryUI import GameHistoryUI


class GameUI:
    def __init__(self, game: WordleGame, series: GameSeries, history: GameHistoryUI):
        self.game = game
        self.game_series = series
        self.history = history

    def run(self):
        """Run the game UI"""
        self.game_loop()

    def game_loop(self):
        """Handle user guess flow"""
        while not self.game.is_game_over:
            guess = self._get_guess()
            try:
                feedback = self.game.submit_guess(guess)
                self._display_feedback(feedback)
            except ValueError as e:
                print(f"{Color.RED.value}{str(e)}{Color.END.value}")
                continue
            
        self.game_series.add_game(self.game)
        self.game_series.calculate_longest_streak()
        self._display_result()

    def _get_guess(self):
        """Get and validate user input"""
        return input("\nGuess: ").upper()

    def _display_feedback(self, feedback: str):
        """Show colored feedback"""
        print("Hint:  " + Color.colorize_feedback(feedback))

    def _display_result(self):
        """Show win/loss message"""
        self._print_history()
        
        if self.game.is_victory:
            print(f"\n{Color.GREEN.value}{Color.BOLD.value}VICTORY!{Color.END.value}")
        else:
            print(f"\n{Color.RED.value}{Color.BOLD.value}GAME OVER!{Color.END.value}")
            print(f"Word was: {Color.BLUE.value}{Color.UNDERLINE.value}{self.game.secret_word}{Color.END.value}")
        print(f"Score: {Color.BLUE.value}{self.game.score}{Color.END.value}")


    def _print_history(self):
        """Show guess history for game round"""
        word_length = self.game.word_length

        print("\n---------- GAME HISTORY ----------")
        print(f"{'Nr':<5} {'Guess':<{word_length + 4}} {'Feedback':<{word_length}}")

        for nr, round in self.game.guess_history.items():
            feedback = Color.colorize_feedback(round.feedback)
            print(f"{nr:<5} {round.word:<{word_length + 4}} {feedback:<{word_length}}")