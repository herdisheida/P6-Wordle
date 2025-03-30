from ui_layer.ColorText import Color
from storage_layer.GameHistory_storage import GameHistory_Storage

class GameHistoryUI:
    """Class to handle game history user interface"""
    GUESS_HISTORY_FORMAT = "   {0:<8}{1:<15}{2:<15}" # guess nr, guesses, feedback
    GAME_HISTORY_LIST_FORMAT = " {0:<5}{1:<10}{2:<20}{3:<20}" # series nr, score, secret_word, result
    SCREEN_PAUSE = f"{Color.GRAY.value}\nEnter to continue...{Color.END.value}"

    def __init__(self, username: str):
        self.username = username
        self.storage = GameHistory_Storage(username)

    def display_history_menu(self):
        """Display the history menu"""
        print(f"\n------- {self.username}'s HISTORY -------")
        print("(1) See all games")
        print("(2) See game details")
        print("(3) See game statistics")
        print("\n(B) Back")

    def history_menu(self):
        """History menu loop"""
        self.series_list = self.storage.load_history()
        if not self.series_list:
            print(f"{Color.RED.value}User ({self.username}) hasn't played any games{Color.END.value}")
            input(self.SCREEN_PAUSE)

        while self.series_list:
            self.display_history_menu()
            choice = input("\nEnter: ").lower()

            match choice:
                case "1": self._display_all_games()
                case "2": self._display_game_details(input("Enter series nr: "))
                case "3": self._display_statistics()
                case "b": break
                case _: print(f"{Color.RED.value}Invalid input{Color.END.value}")


    def _display_all_games(self):
        """Display all games series in user's history"""        
        print("\n----------- ALL GAMES SERIES ----------")
        print(f"Total Series: {len(self.series_list)}\n")

        print(self.GAME_HISTORY_LIST_FORMAT.format(f"Nr", "Score", "Secret Word", "Result"))

        for series_nr, games in enumerate(self.series_list, 1):
            for round_nr, round in enumerate(games["game_list"], 1):
    
                nr = series_nr if round_nr == 1 else "" # print series nr for first game only
                print(self.GAME_HISTORY_LIST_FORMAT.format(nr, round["score"], round["secret_word"], Color._color_result(round["is_victory"])))


            # show one game series at a time
            if series_nr < len(self.series_list):
                choice = input(f"\n{Color.GRAY.value}(B) back | Enter for next...{Color.END.value}\n").lower()
                if choice == "b":
                    return

        input(self.SCREEN_PAUSE)

    def _display_game_details(self, game_nr: int):
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
            print(f"  Result:  {Color._color_result(game['is_victory'])}")   
            print(f"  Score: {game['score']}")

            print("\n  Game rounds:")
            print(self.GUESS_HISTORY_FORMAT.format("Nr", "Guess", "Feedback"))
            for nr, round in game["history"].items():
                print(self.GUESS_HISTORY_FORMAT.format(nr, round["guess"], Color.colorize_feedback(round["feedback"])))
            print()

        input(self.SCREEN_PAUSE)


    def _display_statistics(self):
        """Display game statistics"""
        print(f"\n{Color.BLUE.value}------- SERIES STATISTICS ------{Color.END.value}")
        print(f"Total series:    {len(self.series_list)}")
        print(f"Current streak:  {self.series_list[-1]["curr_streak"]}")
        print(f"Longest streak:  {self.series_list[-1]["longest_streak"]}")

        total_games, victory_count, defeat_count, win_percentage = self._calculate_game_statistics()

        print(f"\n{Color.BLUE.value}------- GAME STATISTICS ------{Color.END.value}")
        print(f"Total games      {total_games}\n")

        print(f"Win percentage:  {win_percentage}%")
        print(f"Total victories: {victory_count}")
        print(f"Total defeats:   {defeat_count}\n")

        print(f"High score:      {self._calculate_high_score()}")
        print(f"Average score:   {self._calculate_average_score(total_games)}")

        input(self.SCREEN_PAUSE)

    def _calculate_game_statistics(self) -> list:
        """Calculate and return game statistics,
        returning total games, victories, defeats and win percentage"""
        total_games = 0
        victory_count = 0
        for game in self.series_list:
            total_games += len(game["game_list"])
            victory_count += len([game for game in game["game_list"] if game["is_victory"]])
        defeat_count = total_games - victory_count
        win_percentage = round((victory_count / total_games) * 100, 2)
        return total_games, victory_count, defeat_count, win_percentage

    def _calculate_average_score(self, total_games):
        """Calculate and return average score for all games"""
        score_sum = 0
        for game in self.series_list:
            score_sum += sum([game["score"] for game in game["game_list"]])
        avg = score_sum / total_games
        return round(avg, 2)
    
    def _calculate_high_score(self):
        """Calculate and return high score from all games"""
        high_score = 0
        for game in self.series_list:
            score = max([game["score"] for game in game["game_list"]])
            if score > high_score:
                high_score = score
        return high_score
    
    def save_game_series(self, series):
        """Trigger saving game series"""
        self.storage.save_game_series(series)
        print(f"{Color.GREEN.value}Game series saved successfully!{Color.END.value}")
