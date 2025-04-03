from ui_layer.ColorText import Color
from storage_layer.GameHistory_storage import GameHistory_Storage


class GameHistoryUI:
    """Class to handle game history user interface"""
    GAME_HISTORY_LIST_FORMAT = " {0:<5}{1:<10}{2:<30}{3:<20}"  # series nr, score, secret_word, result

    SCREEN_PAUSE = f"{Color.GRAY.value}\nEnter to continue...{Color.END.value}"

    def __init__(self, username: str):
        self.username = username
        self.storage = GameHistory_Storage(username)
        self.series_list = []

    def display_history_menu(self):
        """Display the history menu"""
        print(f"\n------- {self.username.capitalize()}'s HISTORY -------")
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
                case "1":
                    self._display_all_games()
                case "2":
                    self._display_game_details(input("Enter series nr: "))
                case "3":
                    self._display_statistics()
                case "b":
                    break
                case _:
                    print(f"{Color.RED.value}Invalid input{Color.END.value}")

    def _display_all_games(self):
        """Display all games series in user"s history"""
        print("\n----------- All Game Series ----------")
        print(f"Total Series: {len(self.series_list)}\n")

        print(self.GAME_HISTORY_LIST_FORMAT.format(f"Nr", "Score", "Secret Word", "Result"))

        for series_nr, games in enumerate(self.series_list, 1):
            for round_nr, round in enumerate(games["game_list"], 1):

                # print series nr for first game only
                nr = (series_nr if round_nr == 1 else "")
                print(
                    self.GAME_HISTORY_LIST_FORMAT.format(
                        nr,
                        round["score"],
                        round["secret_word"],
                        Color._color_result(round["is_victory"]),
                    )
                )
            if series_nr < len(self.series_list):
                print() # add space between series
        input(self.SCREEN_PAUSE)

    def _display_game_details(self, game_nr: int):
        """Display details for a specific game series"""
        try:
            a_series = self.series_list[int(game_nr) - 1]
        except (IndexError, ValueError):
            print(f"{Color.RED.value}Invalid game number{Color.END.value}")
            return

        print(f"\n\n------- Game Series nr.{game_nr} ------")
        for game in a_series["game_list"]:
            i = a_series["game_list"].index(game)

            print(f"\n{Color.BLUE.value}GAME: {i + 1}{Color.END.value}")

            print(f"  Secret Word: {Color.UNDERLINE.value + game["secret_word"] + Color.END.value}")
            print(f"  Result: {Color._color_result(game["is_victory"])}")
            print(f"  Score: {game["score"]}")

            print("\n  Game rounds:")

            word_length = len(game["secret_word"])
            print(f"      {"Nr":<5} {"Guess":<{word_length + 4}} {"Feedback":<{word_length}}")
            for nr, round in game["history"].items():
                feedback = Color.colorize_feedback(round["feedback"])
                print(f"      {nr:<5} {round["guess"]:<{word_length + 4}} {feedback:<{word_length}}")

        input(self.SCREEN_PAUSE)

    def _display_statistics(self):
        """Display game statistics"""
        print(f"\n{Color.BLUE.value}------- Series Statistics ------{Color.END.value}")
        print(f"Total series:    {len(self.series_list)}\n")
        print(f"Current streak:  {self.series_list[-1]["curr_streak"]}")
        print(f"Longest streak:  {max([game["longest_streak"] for game in self.series_list])}\n")
        print(f"Highest total score: {max([game["total_score"] for game in self.series_list])}")
        print(f"Lowest total score:  {min([game["total_score"] for game in self.series_list])}")

        print(f"\n{Color.BLUE.value}------- GAME STATISTICS ------{Color.END.value}")

        total_games, victory_count, defeat_count, win_percentage = (self._calculate_game_statistics())
        print(f"Total games:     {total_games}\n")
        print(f"Win percentage:  {win_percentage}%")
        print(f"Total victories: {victory_count}")
        print(f"Total defeats:   {defeat_count}\n")

        high_score, lowest_score = self._calculate_scores()
        print(f"Highest score:   {high_score}")
        print(f"Lowest score:    {lowest_score}")
        print(f"Average score:   {self._calculate_average_score(total_games)}")
        
        input(self.SCREEN_PAUSE)

    def _calculate_game_statistics(self) -> tuple[int, int, int, float]:
        """Calculate game statistics for game instances.
        Returns:
            Tuple: (total_games, victory_count, defeat_count, win_percentage)
        """
        total_games = sum([len(series["game_list"]) for series in self.series_list])
        victory_count = sum(
            [
                len([game for game in series["game_list"] if game["is_victory"]])
                for series in self.series_list
            ]
        )
        defeat_count = total_games - victory_count
        win_percentage = round((victory_count / total_games) * 100, 2)
        return total_games, victory_count, defeat_count, win_percentage

    def _calculate_average_score(self, total_games) -> float:
        """Calculate average score for all games"""
        total_score = sum(
            game["score"]
            for series in self.series_list
            for game in series["game_list"]
        )
        return round(total_score / total_games, 2)

    def _calculate_scores(self) -> tuple[int, int]:
        """Calculate high score and lowest score for all games"""
        high_score = max(
            game["score"]
            for series in self.series_list
            for game in series["game_list"]
        )
        lowest_score = min(
            game["score"]
            for series in self.series_list
            for game in series["game_list"]
        )
        return high_score, lowest_score

    def save_game_series(self, series) -> None:
        """Trigger saving game series"""
        try:
            self.storage.save_game_series(series)
            print(f"{Color.GREEN.value}Game series saved successfully!{Color.END.value}")
        except Exception as e:
            print(f"{Color.RED.value}Error saving game series: {str(e)}{Color.END.value}")