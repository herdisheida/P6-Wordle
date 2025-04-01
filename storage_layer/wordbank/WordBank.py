from pathlib import Path
import random


class WordBank:
    WORD_BANK_FILE = Path("./storage_layer/WordBank/wordbank.txt")

    def __init__(self):
        # create word bank file if it doesn't exist
        self.WORD_BANK_FILE.touch(exist_ok=True)
        self.words = self._load_words()

    def _load_words(self) -> list[str]:
        """Load words from wordbank.txt file"""
        try:
            with open(self.WORD_BANK_FILE, mode="r") as file:
                return [word.strip().upper() for word in file.readlines()]
        except FileNotFoundError:
            raise FileNotFoundError(f"Word Bank file not found: {self.WORD_BANK_FILE}")
        except Exception as e:
            raise Exception(f"Error loading Word Bank: {e}")

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
        try:
            with open(self.WORD_BANK_FILE, mode="a") as file:
                file.write(f"\n{word.upper()}")
                self.words.append(word.upper())
        except Exception as e:
            print(f"Error writing to Word Bank file: {e}")

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
