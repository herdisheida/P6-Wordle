from ColorText import Color
from pathlib import Path
import json

class GameHistory:
    RESULTS_FOLDER = Path("results")
    GAME_REPLAY_FORMAT = " {0:<5}{1:<20}{2:<20}" # nr, guesses, feedback
    GAME_HISTORY_LIST_FORMAT = " {0:<5}{1:<20}{2:<20}{3:<10}" # nr, secret_word, outcome, score


    def __init__(self):
        self.games = self.load_history()

    def display_history_menu(self):
        """Display the history menu"""
        print("\n------- GAME HISTORY ------")
        print("(1) See all games")
        print("(2) See game details")
        print("(3) See game statistics")
        print("\n(b) Back")

    def menu_loop(self):
        """History menu loop"""
        while self.games:
            self.display_history_menu()

            user_input = input("\nEnter: ").lower()

            if user_input == "1":
                self.display_all_games() # TODO all games -- list of games, scores, etc
            elif user_input == "2":
                pass # TODO game details -- guess history, feedback, etc
            elif user_input == "3":
                pass # TODO game statistics -- high score, average score, etc
            elif user_input == "b":
                break
            else:
                print(f"{Color.RED.value}Invalid input{Color.RESET.value}")

        if not self.games:
            print(f"{Color.RED.value}User hasn't played any games{Color.RESET.value}")

    def display_all_games(self):
        """Display all games in history"""        
        print("\n------- ALL GAMES ------")
        print(self.GAME_HISTORY_LIST_FORMAT.format("Nr", "Secret Word", "Outcome", "Score"))
        for nr, game in enumerate(self.games, 1):
            print(self.GAME_HISTORY_LIST_FORMAT.format(nr, game["secret_word"], game["result"]["outcome"], game["result"]["score"]))

    def load_history(self):
        """Load game history from file"""
        username = input("Enter username: ") # LATER add this username in the menu section

        # create folder if it doesn't exist
        self.RESULTS_FOLDER.mkdir(exist_ok=True)
        file_path = self.RESULTS_FOLDER / f"{username}_results.json"

        try:
            with open(file_path, "r") as f:
                all_games = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            all_games = []
        return all_games

    def save_game(self, username: str, secret_word: str, game_result: dict, game_history: dict):
        """Save game results to file"""
        username = input("Enter username: ") # LATER add this username in the menu section
        file_path = self.RESULTS_FOLDER / f"{username}_results.json"

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
        
        # get existing data and add new game to it
        all_games = self.load_history()
        all_games.append(data)
        with open(file_path, "w") as f:
            json.dump(all_games, f, indent=2)
    