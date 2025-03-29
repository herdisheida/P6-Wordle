import random

class WordBank:
    WORD_BANK_FILE = "./storage_layer/WordBank/wordbank.txt" 

    def __init__(self):
        self.words = self._load_words()

    def _load_words(self) -> list[str]:
        """Load words from wordbank.txt file"""
        with open(self.WORD_BANK_FILE, mode="r") as file:
            return [word.strip() for word in file.readlines()]

    def get_random_word(self, length: int) -> str:
        """Get a random word from the Word Bank with specific length"""
        filtered = [word for word in self.words if len(word) == int(length)]
        return random.choice(filtered).upper()
    
    def get_max_min_word_length(self) -> tuple[int, int]:
        """Get the max and min word length from the Word Bank"""
        min_length = min(len(word) for word in self.words)
        max_length = max(len(word) for word in self.words)
        return min_length, max_length
    
    def add_word(self, word: str):
        """Add a word to the Word Bank"""
        self._validate_word(word)
        with open(self.WORD_BANK_FILE, mode="a") as file:
            file.write(f"\n{word.upper()}")
        self.words.append(word.upper())

    def _validate_word(self, word: str):
        """Validate word for Word Bank"""
        if not word.isalpha():
            raise ValueError("Word needs to be alphabetic")
        if len(word) < 2:
            raise ValueError("Word too short (min 2 letters)")
        if len(word) > 20:
            raise ValueError("Word too long (max 20 letters)")
        if word in self.words:
            raise ValueError("Word already exists in Word Bank")