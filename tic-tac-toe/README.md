# 🎮 Terminal Tic-Tac-Toe Game (Human vs Computer)

This is a Python-based **Tic-Tac-Toe** game played in the terminal where a human player competes against a computer that picks moves at random.

---

## 📌 Overview

- A 3x3 grid game between Player `X` (human) and Player `O` (computer).
- Human plays interactively via terminal.
- The computer picks valid moves randomly.
- The game checks for wins in rows, columns, and diagonals.
- Includes win detection, tie detection, and alternating turns.

---

## 🧠 Concepts Used

- **Object-Oriented Programming (OOP)**  
  - `TicTacToe` class for managing the board and gameplay
  - `Player`, `HumanPlayer`, and `RandomComputerPlayer` classes for players
- **Inheritance and Polymorphism**
- **Basic AI (Random computer moves)**
- **Error handling and input validation**
- **List manipulation and board state tracking**

---

## 🚀 How to Run

### ✅ Requirements

- Python 3.x installed

### ▶️ Steps

1. Clone or download the repository.
2. Make sure `game.py` and `player.py` are in the same folder.
3. Open terminal in the project directory.
4. Run the game with:
   ```bash
   python game.py
   ```

## 🕹️ Gameplay Instructions

• You'll be prompted to input a number from 0-8 for your move.
• The board is numbered like this:
```text
| 0 | 1 | 2 |
| 3 | 4 | 5 |
| 6 | 7 | 8 |
```
• Example flow:
```text
x's turn. Input move (0-8): 0
x make a move to square 0
| x |   |   |
|   |   |   |
|   |   |   |

o make a move to square 4
...
```

• The game ends when:
   a. One player has 3 in a row (→ win)
   b. The board is full with no winner (→ tie)

## 🧾 File Structure

game.py    - 	Contains the core game logic and board setup
player.py  -    Defines the Human and RandomComputer players

## 🔁 Customization Ideas

Replace RandomComputerPlayer with a smarter AI (like Minimax).

Add support for 2 human players.

Track and display player score over multiple rounds.