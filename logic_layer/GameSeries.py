class GameSeries:
    def __init__(self, word_length: int, max_guesses: int):
        self.word_length = word_length
        self.max_guesses = max_guesses

        self.series_list = [] # list of WordleGame objects
        self.total_score = 0
        self.curr_streak = 0
        self.longest_streak = self.curr_streak

    def add_game(self, game: dict):
        """Add a game to the series"""
        self.series_list.append(game)
        self.total_score += game.score

        if game.is_victory:
            self.curr_streak += 1
        else:
            self.curr_streak = 0

    def calculate_longest_streak(self) -> int:
        """Calculate the longest streak from the series"""
        if self.curr_streak > self.longest_streak:
            self.longest_streak = self.curr_streak