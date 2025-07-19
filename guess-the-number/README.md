# 🤖 Computer Guesses Your Number!

This is a simple interactive Python program where **you think of a number**, and the **computer guesses it** using logic and your feedback.

---

## 📌 Overview

- You think of a number between `1` and `x` (in this code, 5).
- The computer makes a guess.
- You tell it whether the guess is:
  - too low (`l`)
  - too high (`h`)
  - or correct (`c`)
- The computer continues guessing until it finds your number.

---

## 🧠 Concepts Used

- **Binary search logic** (narrowing down the range based on feedback)
- **Random number generation**
- **Interactive CLI input/output**

---

## 🚀 How to Run

### ✅ Requirements
- Python 3.x installed

### ▶️ Steps to Run

1. Open your terminal or command prompt.
2. Navigate to the folder containing the `.py` file.
3. Run the script:
   ```bash
   python filename.py
  (Replace filename.py with the actual name of your Python file.)
4. Follow the instructions in the terminal.

## 🔢 Sample Gameplay

Think of a number between1 & 5 and the computer will guess it !
Is the number 3 too low (l),too high(h) and correct(c): l
Is the number 5 too low (l),too high(h) and correct(c): h
Is the number 4 too low (l),too high(h) and correct(c): c
Yay, the computer guessed your number correctly! 4

## Sample Code

import random

def guess_comp(x):
    low = 1
    high = x
    feedback = ''
    guess = None

    print(f"Think of a number between{low} & {high} and the computer will guess it !")

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f"is the number {guess} too low (l),too high(h) and correct(c):")
        
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback != 'c':
            print("Enter only h,l and c")

    print(f"Yay, the computer guessed your number correctly! {guess}")

guess_comp(5)

## 🧠 Code Explanation

- The `guess_comp(x)` function lets the computer guess the number you're thinking of between 1 and `x`.
- It uses a loop where the computer keeps narrowing the range based on your feedback.
- If you say the guess is too high (`h`), the upper limit reduces.
- If you say it's too low (`l`), the lower limit increases.
- The loop continues until you confirm the guess is correct (`c`).

## 🛠️ Customization

You can change the range by replacing 5 in guess_comp(5) with any number (e.g., guess_comp(100)).

Improve user experience by trimming input and making it case-insensitive (e.g., feedback.lower().strip()).

## 👤 Author
Alive Peterson
GitHub: @Alive-Peterson

## License
This project is open source and free to use. No license required.