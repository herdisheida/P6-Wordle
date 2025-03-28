from pathlib import Path
import random

class WordBank:
    WORD_BANK_FILE = Path("WordBank") / "wordbank.txt"

    def __init__(self):
        self.words = self._load_words()

    def _load_words(self) -> list[str]:
        """Load words from file"""
        with open(self.WORD_BANK_FILE, mode="r") as file:
            return [word.strip() for word in file.readlines()]

    def get_random_word(self, length: int) -> str:
        """Get a random word from the word bank with specified length"""
        filtered = [word for word in self.words if len(word) == length]

        if not filtered:
            raise ValueError("No word found with that length\n")
        return random.choice(filtered)
    
    def add_word(self, word: str):
        """ Add a word to the word bank"""
        with open(self.WORD_BANK_FILE, mode="a") as file:
            file.write(f"{word}\n")
        self.words.append(word)
        # TODO word check... maybe þurfum við?