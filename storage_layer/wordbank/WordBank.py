import random

class WordBank:
    WORD_BANK_FILE = "./storage_layer/WordBank/wordbank.txt" 

    def __init__(self):
        self.words = self._load_words()

    def _load_words(self) -> list[str]:
        """Load words from wordbank.txt file"""
        with open(self.WORD_BANK_FILE, mode="r") as file:
            return [word.strip().upper() for word in file.readlines()]

    def get_random_word(self, length: int) -> str:
        """Get a random word from the Word Bank with specific length"""
        filtered = [word for word in self.words if len(word) == int(length)]
        if not filtered:
            raise ValueError(f"No words found with length {length}")
        return random.choice(filtered).upper()
    
    def get_word_lengths(self) -> list[int]:
        """Get all word lengths from the Word Bank"""
        lengths = sorted(set([len(word) for word in self.words]))
        if 0 in lengths:
            lengths.remove(0)
        return lengths
      
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
        if word.upper() in self.words:
            raise ValueError("Word already exists in Word Bank")