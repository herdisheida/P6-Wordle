# WORDLE
*Herdís Heiða Jing Guðjohnsen*

## Prerequisites
- Python 3.4+ (for `pathlib`)  


## Tutorial
Wordle is a daily word-guessing game where the goal is to deduce the hidden word using logic and process of elimination. Players set their own rules; choosing X attempts to guess a Y-letter word and recieve feedback after each try.

### User Customization
The user can customize:
* Word length (MAX 20)
* Guess attempts (MAX 20)
* Wordbank words
* Amount of games in connected series (MAX 5)

## Feedback Symbols  
* 🟩 C = Correct letter & position  
* 🟨 c = Correct letter, wrong position  
* 🟥 - = Letter not in the word  


## Usage
Go to the Game folder and run the program in start.py file
```bash
cd Game
python3 start.py
```