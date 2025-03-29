from utilities.ColorText import Color
from pathlib import Path
import json

class GameHistory:
    RESULTS_FOLDER = Path("results")
    GUESS_HISTORY_FORMAT = " {0:<5}{1:<20}{2:<20}" # nr, guesses, feedback
    GAME_HISTORY_LIST_FORMAT = " {0:<5}{1:<10}{2:<20}{3:<20}" # nr, score, secret_word, outcome

    SCREEN_PAUSE = "\nEnter to continue..."

    def __init__(self, username: str):
        self.username = username

        # create folder if it doesn't exist
        self.RESULTS_FOLDER.mkdir(exist_ok=True)
        self.RESULT_PATH = self.RESULTS_FOLDER / f"{self.username}_results.json"      
        

    def display_history_menu(self):
        """Display the history menu"""
        # load game history
        print("\n------- GAME HISTORY -------")
        print(f"User: {self.username}\n")

        print("(1) See all games")
        print("(2) See game details")
        print("(3) See game statistics")

        print("\n(B) Back")

    def menu_loop(self):
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

        # if no games are found
        if not self.games:
            print(f"{Color.RED.value}User ({self.username}) hasn't played any games{Color.END.value}")
            input(self.SCREEN_PAUSE)

    def display_all_games(self):
        """Display all games in history"""        
        print("\n----------- ALL GAMES ----------")
        print(self.GAME_HISTORY_LIST_FORMAT.format(f"Nr", "Score", "Secret Word", "Outcome"))
        for nr, game in enumerate(self.games, 1):
            # colorize outcome
            outcome = game["result"]["outcome"]
            color = Color.GREEN.value if outcome == "Victory" else Color.RED.value
            colored_outcome = f"{color}{outcome}{Color.END.value}"

            print(self.GAME_HISTORY_LIST_FORMAT.format(nr, game["result"]["score"], game["secret_word"], colored_outcome))
        input(self.SCREEN_PAUSE)

    def display_game_details(self, game_nr: int):
        """Display details for a specific game"""
        try:
            game_nr = int(game_nr) - 1
            game = self.games[game_nr]
        except (IndexError, ValueError):
            print(f"{Color.RED.value}Invalid game number{Color.END.value}")
            return
        
        print("\n------- GAME DETAILS ------")
        print(f"Secret Word: {game['secret_word']}")
        print(f"Result: {game['result']['outcome']}")   
        print(f"Score: {game['result']['score']}")

        print("\nGame rounds:")
        print(self.GUESS_HISTORY_FORMAT.format("Nr", "Guess", "Feedback"))
        for nr, round in game["history"].items():
            print(self.GUESS_HISTORY_FORMAT.format(nr, round["guess"], Color._colorize_feedback(round["feedback"])))

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
            with open(self.RESULT_PATH, "r") as file:
                all_games = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            all_games = []
        return all_games

    def save_game(self, secret_word: str, game_result: dict, game_history: dict):
        """Save game results to file"""
        data = {
            "secret_word": secret_word,
            "result": game_result,
            "history": {
                nr: {
                    "guess": round.word,
                    "feedback": round.feedback
                }
                for nr, round in game_history.items()
            }
        }
        
        # get existing data and add new game to it
        all_games = self.load_history()
        all_games.append(data)
        with open(self.RESULT_PATH, "w") as file:
            json.dump(all_games, file, indent=2)
    