# 🧠 Word Guessing Game (with Hint & Attempt Tracker)

A simple and engaging Python terminal game where you guess a hidden word using hints, with limited attempts and multiple round support.

---

## 📌 Overview

- The player is given a **hint** to guess a predefined secret word.
- You have **3 chances** to guess it correctly.
- After each guess, you're informed how many attempts remain.
- Win by guessing the word before you run out of tries.
- Lose if all attempts are used up — but you can play again in a new round.

---

## 🧠 Concepts Used

- **Loops** (`while`)
- **Conditionals**
- **Input/output formatting**
- **Boolean flags**
- **Game replay mechanics**
- **String comparison and tracking user attempts**

---

## 🚀 How to Run

### ✅ Requirements
- Python 3.x installed on your system

### ▶️ Steps to Run

1. Save the code to a file named `word_guess_game.py`.
2. Open a terminal or command prompt.
3. Navigate to the folder where the script is saved.
4. Run the game using:
   ```bash
   python word_guess_game.py

## 🔁 Sample Gameplay
```yaml
Game Round: 1
Hint: It's a word that means nothing or zero.
Remaining attempts: 3
Enter a Guess: zero
Remaining attempts: 2
Enter a Guess: void
Remaining attempts: 1
Enter a Guess: empty
Out of guesses, YOU LOSE !!!

Do you want to play again? (yes/no): yes

Game Round: 2
Hint: It's a word that means nothing or zero.
Remaining attempts: 3
Enter a Guess: None
You Win!

Do you want to play again? (yes/no): no
Thanks for playing!
```

## 🧾 Code Snapshot
```python
game_round_count = 1

while True:
    print(f"\nGame Round: {game_round_count}")

    secret_word = "None"
    hint = "Hint: It's a word that means nothing or zero."

    guess = ""
    guess_count = 0
    guess_limit = 3
    out_of_guesses = False

    print(hint)  # Show the hint once per round

    while guess != secret_word and not out_of_guesses:
        if guess_count < guess_limit:
            remaining_attempts = guess_limit - guess_count
            print(f"Remaining attempts: {remaining_attempts}")
            guess = input("Enter a Guess: ")
            guess_count += 1
        else:
            out_of_guesses = True

    if out_of_guesses:
        print("Out of guesses, YOU LOSE !!!")
    else:
        print("You Win!")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break

    game_round_count += 1
```
## 🛠️ Customization Ideas

a. Change the secret_word or randomly choose from a list.

b. Add multiple hints or word categories.

c. Allow players to choose difficulty (more or fewer guesses).

d. Add a score tracker across rounds.

e. Improve input handling (e.g., case-insensitive guesses).

## 👤 Author

Alive Peterson

GitHub: @Alive-Peterson

## 🪪 License
This project is open-source and free to use. No license required.