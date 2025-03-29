from ui_layer.ColorText import Color
from logic_layer.WordleGame import WordleGame
from logic_layer.GameSeries import GameSeries
from storage_layer.GameHistory import GameHistory


class GameUI:
    def __init__(self, game: WordleGame, series: GameSeries, history: GameHistory):
        self.games = game
        self.game_seris = series
        self.history = history

    def run(self):
        """Run the game UI"""
        self.game_loop()

    def game_loop(self):
        """Handle user guess flow"""
        while not self.games.is_game_over:
            guess = self._get_guess()
            try:
                feedback = self.games.submit_guess(guess)
                self._display_feedback(feedback)
            except ValueError as e:
                print(f"{Color.RED.value}{str(e)}{Color.END.value}")
                continue
            
        self._display_result()
        # self._save_game_series() # EYDA
        self.games.reset_game()


    def _get_guess(self):
        """Get and validate user input"""
        return input("\nGuess: ").upper()

    def _display_feedback(self, feedback: str):
        """Show colored feedback"""
        print("Hint:  " + Color.colorize_feedback(feedback))

    def _display_result(self):
        """Show win/loss message"""
        self._print_history()
        
        if self.games.is_victory:
            print(f"\n{Color.GREEN.value}{Color.BOLD.value}VICTORY!{Color.END.value}")
            print(f"Score: {Color.BLUE.value}{self.games.game_result['score']}{Color.END.value}")
        else:
            print(f"\n{Color.RED.value}{Color.BOLD.value}GAME OVER!{Color.END.value}")
            print(f"Word was: {Color.BLUE.value}{Color.UNDERLINE.value}{self.games.secret_word}{Color.END.value}")
        
        input(self.history.SCREEN_PAUSE)


    def _print_history(self):
        """Show guess history for game round"""
        print("\n---------- GAME HISTORY ----------")
        print(self.history.GUESS_HISTORY_FORMAT.format("Nr", "Guess", "Feedback"))
        for nr, round in self.games.guess_history.items():
            feedback = Color.colorize_feedback(round.feedback)
            print(self.history.GUESS_HISTORY_FORMAT.format(nr, round.word, feedback))

    def _save_game(self): # EYDA old save game
        """Trigger saving game"""
        self.history.save_game_series(
            secret_word = self.games.secret_word,
            game_result = self.games.game_result,
            game_history = self.games.guess_history
        )

    def _save_game_series(self): # FIX
        """Trigger saving game"""
        self.history.save_game_series(self.games.game_series)