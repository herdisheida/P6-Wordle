from logic_layer.WordleGame import WordleGame
from pathlib import Path
import json

class GameHistory_Storage:
    """Class to handle game history storage and retrieval"""
    RESULTS_FOLDER = Path("./storage_layer/results")

    def __init__(self, username: str):
        # create folder if it doesn't exist
        self.RESULTS_FOLDER.mkdir(exist_ok=True) # EYDA þarf þetta ?
        self.RESULT_FILE_PATH = self.RESULTS_FOLDER / f"{username}_results.json"      
        
    
    def load_history(self):
        """Load game history from file"""
        try:
            with open(self.RESULT_FILE_PATH, "r") as file:
                all_games = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            all_games = []
        return all_games
    
    def save_game_series(self, series: list[WordleGame]):
        """Save game series results to file"""
        series_list = []
        
        # get all games in the series
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

        # get existing user series history and add new game to it
        all_series = self.load_history()
        all_series.append(game_series)

        # save to file
        with open(self.RESULT_FILE_PATH, "w") as file:
            json.dump(all_series, file, indent=2)