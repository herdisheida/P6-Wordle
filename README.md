# WORDLE
*Herdís Heiða Jing Guðjohnsen*

## Prerequisites
- Python 3.4+ (for `pathlib`)  


## Game Tutorial
### Info
Wordle is a daily word-guessing game where the goal is to deduce the hidden word using logic and process of elimination. Players set their own rules; choosing X attempts to guess a Y-letter word and recieve feedback after each try.

### Game Score
The Score for each game is calculated based on the wordle length, user's guess attempts and the results (Victory/Defeat) of the game. The Total Score for a Game Series is the sum of all Scores in a Game Series is the total Score,

### User Customization
* Word length (MAX 20)
* Guess attempts (MAX 20)
* Wordbank words

### Feedback Symbols  
* 🟩 C = Correct letter & position  
* 🟨 c = Correct letter, wrong position  
* 🟥 - = Letter not in the word  


## Usage
### Run program
Go to the directory of the Wordle program and run it with the start.py file.
```bash
cd <your-wordle-game-folder>
python3 start.py
```
Or run it in VS Code by running the start.py file.

### Users
You can signup and login by typing your username at the start of the programm, no password needed :D.
If you want to try an existing account, use username: 'test'