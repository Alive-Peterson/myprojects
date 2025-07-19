# 🎮 Guess the Number – User & Computer Versions

This is a simple interactive Python project with **two guessing games**:
- **🤖 Computer Guesses Your Number**
- **🧍 You Guess the Computer's Number**

---

## 📌 Overview

### 🤖 Computer Guesses Your Number
- You think of a number between `1` and `x`.
- The computer makes a guess.
- You tell it whether the guess is:
  - too low (`l`)
  - too high (`h`)
  - or correct (`c`)
- The computer keeps guessing until it finds your number.

### 🧍 You Guess the Computer's Number
- The computer randomly selects a number between `1` and `x`.
- You keep guessing until you find the number.
- The computer gives you hints whether your guess is too low or too high.

---

## 🧠 Concepts Used

- **Binary search logic** (for computer guesses)
- **Random number generation**
- **Conditional statements**
- **Looping and user input**
- **Interactive CLI interface**

---

## 🚀 How to Run

### ✅ Requirements
- Python 3.x installed

### ▶️ Steps to Run

1. Open your terminal or command prompt.
2. Navigate to the folder containing the `.py` files.
3. Run the script of your choice:

   - For **computer guesses** version:
     ```bash
     python guess_comp.py
     ```
   - For **user guesses** version:
     ```bash
     python guess_user.py
     ```

4. Follow the instructions shown in the terminal.

---

## 🔢 Sample Gameplay

### 🤖 Computer Guesses
Think of a number between1 & 5 and the computer will guess it !
Is the number 3 too low (l),too high(h) and correct(c): l
Is the number 5 too low (l),too high(h) and correct(c): h
Is the number 4 too low (l),too high(h) and correct(c): c
Yay, the computer guessed your number correctly! 4

### 🧍 You Guess
Enter a num between 1 and 4: 1
Sorry, the number is too low
Enter a num between 1 and 4: 4
Sorry, the number is too high
Enter a num between 1 and 4: 3
Yay! you guessed it correct


---

## 🧾 Sample Code

### 🤖 `guess_comp.py`
```python
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

### 🧍 guess_user.py

import random

def guess_num(x):
    random_num = random.randint(1, x)
    guess = 0
    while guess != random_num:
        guess = int(input(f"Enter a num between 1 and {x}: "))
        if guess < random_num:
            print("Sorry, the number is too low")
        elif guess > random_num:
            print("Sorry, the number is too high")

    print("Yay! you guessed it correct")

guess_num(4)

## 🧠 Code Explanation:

guess_comp(x)
i.The computer uses binary search logic to guess your number.
ii.It narrows down the range based on your feedback until it gets the correct number.

guess_num(x)
i.You try to guess a number the computer randomly generated.
ii.The game helps you by giving hints like "too low" or "too high".

## 🛠️ Customization

i. Change the range: Replace 5 or 4 with any number like 100 for a bigger challenge.
ii. Add difficulty levels.
iii. Track number of attempts.
iv. Make inputs more user-friendly:
       feedback = input(...).strip().lower()

## 👤 Author
Alive Peterson
GitHub: @Alive-Peterson

## 🪪 License
This project is open-source and free to use. No license required.
