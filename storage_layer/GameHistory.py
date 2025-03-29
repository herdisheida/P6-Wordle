from ui_layer.ColorText import Color
from pathlib import Path
import json

class GameHistory:
    RESULTS_FOLDER = Path("./storage_layer/results")

    GUESS_HISTORY_FORMAT = "  {0:<8}{1:<20}{2:<20}" # nr, guesses, feedback
    GAME_HISTORY_LIST_FORMAT = " {0:<5}{1:<10}{2:<20}{3:<20}" # nr, score, secret_word, outcome
    SCREEN_PAUSE = "\nEnter to continue..."

    def __init__(self, username: str):
        self.username = username

        # create folder if it doesn't exist
        self.RESULTS_FOLDER.mkdir(exist_ok=True) # EYDA þarf þetta ?
        self.RESULT_FILE_PATH = self.RESULTS_FOLDER / f"{self.username}_results.json"      
        

    def display_history_menu(self):
        """Display the history menu"""
        print("\n------- GAME HISTORY -------")
        print(f"User: {self.username}\n")

        print("(1) See all games")
        print("(2) See game details")
        print("(3) See game statistics")

        print("\n(B) Back")

    def history_menu(self):
        """History menu loop"""
        self.games = self.load_history()

        while self.games:
            self.display_history_menu()
            choice = input("\nEnter: ").lower()

            match choice:
                case "1": self.display_all_games()
                case "2": self.display_game_details(input("Enter game number: "))
                case "3": self.display_statistics()
                case "b": break
                case _: print(f"{Color.RED.value}Invalid input{Color.END.value}")

        if not self.games:
            print(f"{Color.RED.value}User ({self.username}) hasn't played any games{Color.END.value}")
            input(self.SCREEN_PAUSE)

    def display_all_games(self):
        """Display all games in history"""        
        print("\n----------- ALL GAMES ----------")
        print(self.GAME_HISTORY_LIST_FORMAT.format(f"Nr", "Score", "Secret Word", "Outcome"))

        for series_nr, game in enumerate(self.games, 1):
            for round_nr, round in enumerate(game, 1):
                # colorize outcome
                outcome = round["result"]["outcome"]
                color = Color.GREEN.value if outcome == "Victory" else Color.RED.value
                colored_outcome = f"{color}{outcome}{Color.END.value}"

                # get game series nr
                nr = series_nr if round_nr == 1 else ""
                print(self.GAME_HISTORY_LIST_FORMAT.format(nr, round["result"]["score"], round["secret_word"], colored_outcome))
                if nr == "":
                    print()

        input(self.SCREEN_PAUSE)

    def display_game_details(self, game_nr: int):
        """Display details for a specific game"""
        try:
            game_series = self.games[int(game_nr) - 1]
        except (IndexError, ValueError):
            print(f"{Color.RED.value}Invalid game number{Color.END.value}")
            return
         
        print(f"\n------- GAME SERIES {game_nr} ------")
        for count in range(len(game_series)):
            game = game_series[count]
            print(f"{Color.BLUE.value}GAME: {count}{Color.END.value}")

            print(f" Secret Word: {game['secret_word']}")
            print(f" Result: {game['result']['outcome']}")   
            print(f" Score: {game['result']['score']}")

            print("\n Game rounds:")
            print(self.GUESS_HISTORY_FORMAT.format("Nr", "Guess", "Feedback"))
            for nr, round in game["history"].items():
                print(self.GUESS_HISTORY_FORMAT.format(nr, round["guess"], Color.colorize_feedback(round["feedback"])))
                print()

            # input("\nEnter for next game...\n")
        input(self.SCREEN_PAUSE)

    def display_statistics(self):
        """Display game statistics"""
        print("\n------- GAME STATISTICS ------")
        print(f"Total games: {len(self.games)}")
        print(f"Total victories: {len([game for game in self.games if game['result']['outcome'] == 'Victory'])}")
        print(f"Total defeats: {len([game for game in self.games if game['result']['outcome'] == 'Defeat'])}")
        print(f"Average score: {self._calculate_average_score()}")
        print(f"High score: {self._calculate_high_score()}")

        input(self.SCREEN_PAUSE)

    def _calculate_average_score(self):
        """Calculate and return average score for all games"""
        total_score = sum([game["result"]["score"] for game in self.games])
        avg = total_score / len(self.games)
        return round(avg, 2)
    
    def _calculate_high_score(self):
        """Calculate and return high score from all games"""
        return max([game["result"]["score"] for game in self.games])
    
    def load_history(self):
        """Load game history from file"""
        try:
            with open(self.RESULT_FILE_PATH, "r") as file:
                all_games = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            all_games = []
        return all_games

    # def save_game(self, secret_word: str, game_result: dict, game_history: dict): # EYDA OLD CODE
    #     """Save game results to file"""
    #     data = {
    #         "secret_word": secret_word,
    #         "result": game_result,
    #         "history": {
    #             nr: {
    #                 "guess": round.word,
    #                 "feedback": round.feedback
    #             }
    #             for nr, round in game_history.items()
    #         }
    #     }
        
    #     # get existing data and add new game to it
    #     all_games = self.load_history()
    #     all_games.append(data)
    #     with open(self.RESULT_FILE_PATH, "w") as file:
    #         json.dump(all_games, file, indent=2)
    
    def save_game(self, game_series: list):
    #     """Save game results to file"""
        game_series_list = []
        for game in game_series:

            data = {
                "secret_word": game["secret_word"],
                "result": game["game_result"],
                "history": {
                    nr: {
                        "guess": round.word,
                        "feedback": round.feedback
                    }
                    for nr, round in game["game_round_history"].items()
                }
            }
            game_series_list.append(data)

        # get existing data and add new game to it
        all_games = self.load_history()
        all_games.append(game_series_list)
        with open(self.RESULT_FILE_PATH, "w") as file:
            json.dump(all_games, file, indent=2)