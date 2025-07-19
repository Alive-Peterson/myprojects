# 🎯 Hangman Game in Python

A classic word-guessing game built in Python! Try to guess the hidden word one letter at a time before you run out of tries.

---

## 📌 Overview

- A word is randomly selected from a predefined list (`word_list`).
- You have **6 tries** to guess all letters correctly.
- For each incorrect guess, the number of tries decreases.
- The game displays:
  - Letters you've already guessed
  - Your progress with the word (correct letters revealed, others hidden)
- You win by revealing the full word.
- You lose if you run out of tries before guessing the word.

---

## 🧠 Concepts Used

- **Random selection** from a word list
- **Loops and conditionals**
- **User input handling**
- **String and list operations**
- **Game loop and state tracking**

---

## 🚀 How to Run

### ✅ Requirements

- Python 3.x installed
- A separate file named `words.py` containing the `word_list`

### ▶️ Running the Game

1. Create a file called `words.py` with a list of words:
   ```python
   word_list = ["python", "hangman", "challenge", "programming", "developer"]
   ```
2. Save your main game file as hangman.py.

3. In terminal or command prompt, navigate to the folder where the files are saved.

4 Run the game using:
```bash
python hangman.py
```

## 🔁 Sample Gameplay
```less
Welcome to Hangman!
_ _ _ _ _ _

Guess a letter: a
Wrong guess! Tries left: 5
Used Letters: a
_ _ _ _ _ _

Guess a letter: p
Good guess!
Used Letters: a p
p _ _ _ _ _

...

Congratulations! You guessed the word 🎉
```
## 🧾 Code Snapshot
```python
import random
from words import word_list  

def hangman():
    word = random.choice(word_list)
    guessed_letters = []
    tries = 6

    print("Welcome to Hangman!")
    print("_ " * len(word))

    while tries > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            tries -= 1
            print(f"Wrong guess! Tries left: {tries}")

        print("\nUsed Letters:", " ".join(guessed_letters))

        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print(display_word.strip())

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word 🎉")
            break
    else:
        print(f"Game Over! The word was '{word}'.")

hangman()
```
## 🛠️ Customization Ideas

1. Add difficulty levels (more or fewer tries).

2. Track and display the hangman visual state.

3. Load a large word list from an external .txt file.

4. Add score tracking for multiple rounds.

## 👤 Author
Alive Peterson
GitHub: @Alive-Peterson

## 🪪 License
This project is open-source and free to use. No license required.