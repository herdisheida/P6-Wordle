class GameSeries:
    def __init__(self, word_length: int, max_guesses: int):
        self.word_length = word_length
        self.max_guesses = max_guesses

        self.game_series = [] # list of WordleGame objects
        self.total_score = 0
        self.curr_sreak = 0

    def add_game(self, game: dict):
        """Add a game to the series"""
        self.game_series.append(game)
        self.total_score += game["score"]

        if game["outcome"] == "Victory":
            self.curr_streak += 1
        else:
            self.curr_streak = 0

    @property
    def longest_streak(self):
        """Get the longest winning streak"""
        return max([game["streak"] for game in self.game_series], default=0)