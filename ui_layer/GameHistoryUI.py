from ui_layer.ColorText import Color
from logic_layer.WordleGame import WordleGame
from pathlib import Path
import json

class GameHistory:
    RESULTS_FOLDER = Path("./storage_layer/results")

    GUESS_HISTORY_FORMAT = "   {0:<8}{1:<20}{2:<20}" # nr, guesses, feedback
    GAME_HISTORY_LIST_FORMAT = " {0:<5}{1:<10}{2:<20}{3:<20}" # nr, score, secret_word, outcome
    SCREEN_PAUSE = f"{Color.GRAY.value}\nEnter to continue...{Color.END.value}"

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
        self.series_list = self.load_history()
        if not self.series_list:
            print(f"{Color.RED.value}User ({self.username}) hasn't played any games{Color.END.value}")
            input(self.SCREEN_PAUSE)

        while self.series_list:
            self.display_history_menu()
            choice = input("\nEnter: ").lower()

            match choice:
                case "1": self.display_all_games()
                case "2": self.display_game_details(input("Enter game number: "))
                case "3": self.display_statistics()
                case "b": break
                case _: print(f"{Color.RED.value}Invalid input{Color.END.value}")


    def display_all_games(self):
        """Display all games in history"""        
        print("\n----------- ALL GAMES ----------")
        print(self.GAME_HISTORY_LIST_FORMAT.format(f"Nr", "Score", "Secret Word", "Result"))

        for series_nr, games in enumerate(self.series_list, 1):
            for round_nr, round in enumerate(games["game_list"], 1):

                # colorize outcome
                result = f"{Color.GREEN.value}Victory{Color.END.value}" if round["is_victory"] else f"{Color.RED.value}Defeat{Color.END.value}"

                # get game series nr
                nr = series_nr if round_nr == 1 else ""
                print(self.GAME_HISTORY_LIST_FORMAT.format(nr, round["score"], round["secret_word"], result))
                if nr == "":
                    print()

        input(self.SCREEN_PAUSE)

    def display_game_details(self, game_nr: int):
        """Display details for a specific game series"""
        try:
            a_series = self.series_list[int(game_nr) - 1]
        except (IndexError, ValueError):
            print(f"{Color.RED.value}Invalid game number{Color.END.value}")
            return
         
        print(f"\n\n------- GAME SERIES nr.{game_nr} ------\n")
        for game in a_series["game_list"]:
            i = a_series["game_list"].index(game)

            print(f"{Color.BLUE.value}GAME: {i + 1}{Color.END.value}")

            print(f"  Secret Word: {game['secret_word']}")
            print(f"  Result: {game['is_victory']}")   
            print(f"  Score: {game['score']}")

            print("\n  Game rounds:")
            print(self.GUESS_HISTORY_FORMAT.format("Nr", "Guess", "Feedback"))
            for nr, round in game["history"].items():
                print(self.GUESS_HISTORY_FORMAT.format(nr, round["guess"], Color.colorize_feedback(round["feedback"])))
            print()

        input(self.SCREEN_PAUSE)

    def display_statistics(self):
        """Display game statistics"""

        total_games = 0
        victory_count = 0
        for game in self.series_list:
            total_games += len(game["game_list"])
            victory_count += len([game for game in game["game_list"] if game["is_victory"]])

        print("\n------- GAME STATISTICS ------")
        print(f"Total series:    {len(self.series_list)}")
        print(f"Total games      {total_games}\n")

        print(f"Total victories: {victory_count}")
        print(f"Total defeats:   {total_games - victory_count}\n")

        print(f"Average score:   {self._calculate_average_score()}")
        print(f"High score:      {self._calculate_high_score()}\n")
        print(f"Current streak:  {self.series_list[-1]["curr_streak"]}")
        print(f"Longest streak:  {self.series_list[-1]["longest_streak"]}")

        input(self.SCREEN_PAUSE)

    def _calculate_average_score(self):
        """Calculate and return average score for all games"""
        total_score = sum([game["total_score"] for game in self.series_list])
        avg = total_score / len(self.series_list)
        return round(avg, 2)
    
    def _calculate_high_score(self):
        """Calculate and return high score from all games"""
        high_score = 0
        for game in self.series_list:
            score = max([game["score"] for game in game["game_list"]])
            if score > high_score:
                high_score = score
        return high_score
    
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