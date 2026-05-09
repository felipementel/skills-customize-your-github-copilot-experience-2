
# 📘 Assignment: Games in Python

## 🎯 Objective

Build the classic Hangman word-guessing game using Python strings, loops, and user input. You will practice string manipulation, conditionals, random selection, and game state management.

## 📝 Tasks

### 🛠️	Word Selection and Game Setup

#### Description
Initialize the game by randomly selecting a secret word and setting up the variables needed to track game state.

#### Requirements
Completed program should:

- Randomly select a word from the predefined word list using the `random` module.
- Initialize a list to track correctly guessed letters.
- Initialize a counter for incorrect guesses.
- Set a maximum number of allowed incorrect guesses (e.g., 6).

### 🛠️	Main Game Loop

#### Description
Implement the core game loop where the player repeatedly guesses letters until they win or run out of attempts.

#### Requirements
Completed program should:

- Display the current progress of the word using `_` for unguessed letters (e.g., `_ _ t h o n`).
- Prompt the player to enter a single letter guess.
- Check if the guessed letter is in the secret word and update the game state accordingly.
- Track and display the number of incorrect guesses remaining.
- Continue looping until the word is fully guessed or the player exceeds the maximum incorrect guesses.

### 🛠️	Win and Lose Conditions

#### Description
Detect the end of the game and display the appropriate result message to the player.

#### Requirements
Completed program should:

- Display a congratulations message when the player correctly guesses all letters. Example:
  ```
  Congratulations! You guessed the word: python
  ```
- Display a game over message when the player runs out of attempts. Example:
  ```
  Game over! The word was: python
  ```
