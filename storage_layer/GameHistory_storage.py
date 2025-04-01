from logic_layer.WordleGame import WordleGame
from pathlib import Path
import json

class GameHistory_Storage:
    """Class to handle game history storage and retrieval"""
    RESULTS_FOLDER = Path("./storage_layer/results")

    def __init__(self, username: str):
        # create results folder if it doesn't exist
        self.RESULTS_FOLDER.mkdir(exist_ok=True)
        # set file path for user
        self.RESULT_FILE_PATH = self.RESULTS_FOLDER / f"{username}_results.json"      
        
    def load_history(self) -> list[dict]:
        """Get game history from file,
        return empty list if file doesn't exist"""
        try:
            with open(self.RESULT_FILE_PATH, "r") as file:
                all_games = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            all_games = []
        return all_games
    
    def save_game_series(self, series: list[WordleGame]):
        """Save game series results to file"""
        game_series = self._get_game_series(series)

        # get existing user series history and add new game to it
        all_series = self.load_history()
        all_series.append(game_series)
        self._write_to_file(data=all_series)

    def _get_game_series(self, series: list[WordleGame]) -> dict:
        """Get all game series data, including new game series"""        
        # get all games in the series
        series_list = []
        for game in series.series_list:
            data = {
                "secret_word": game.secret_word,
                "is_victory": game.is_victory,
                "score": game.score,
                "history": {
                    nr: {
                        "guess": round.word,
                        "feedback": round.feedback
                    }
                    for nr, round in game.guess_history.items()
                    }
                }
            series_list.append(data)

        # create game series data
        game_series = {
            "total_score": series.total_score,
            "curr_streak": series.curr_streak,
            "longest_streak": series.longest_streak,
            "game_list": series_list
        }
        return game_series

    def _write_to_file(self, data: dict):
        """Write game data to file"""
        try:
            with open(self.RESULT_FILE_PATH, "w") as file:
                json.dump(data, file, indent=2)
        except Exception as e:
            raise IOError(f"Error writing to file: {e}")