# 🎮 Tic Tac Toe – Human vs Genius Computer (Python CLI Game)

This is a Python-based terminal game of **Tic Tac Toe** where you play as `X` against a computer AI (`O`) powered by the **Minimax algorithm**. The game is fully interactive and runs in the terminal.

---

## 📌 Features

- Classic **3x3 Tic Tac Toe** board
- Play as **Player X**
- The computer plays as **Player O** and makes intelligent decisions
- Clear board rendering with cell numbers
- Win, tie, and invalid-move detection
- Playable in any terminal with Python installed

---

## 🧠 Concepts Used

- **Object-Oriented Programming (OOP)**
- **Inheritance and Polymorphism**
- **AI Decision Making** with the **Minimax algorithm**
- **Game loop** and turn alternation
- **User input validation**
- **List comprehensions**, `enumerate`, and recursion

---

## 🗂️ File Structure

• game.py - Handles game logic, board rendering, and gameplay loop 
• player.py - Contains Player, HumanPlayer, RandomComputerPlayer , and GeniusComputerPlayer classes 

---

## ▶️ How to Run

### ✅ Requirements
- Python 3.x

### 📦 Steps to run:

1. Open your terminal or VS Code terminal
2. Navigate to the folder containing both files:
   ```bash
   cd path/to/tic-tac-toe
   ```
3. Run the game.
   ```bash
   python game.py
   ```

## 🕹️ Controls

• You'll be prompted to choose a square from 0 to 8 on your turn.
• The board layout is numbered like this:
```
| 0 | 1 | 2 |
| 3 | 4 | 5 |
| 6 | 7 | 8 |
```
• Enter the number corresponding to the square where you want to place your X.

## 🧠 About the AI (GeniusComputerPlayer)

• On its first move, it picks randomly (for speed).
• After that, it uses the Minimax algorithm to determine the best move.
• It will never lose if played optimally and often wins.

## 🛠️ Customization Ideas

• Add a score counter for multiple rounds.
• Allow human vs human or computer vs computer modes.
• Implement difficulty levels (easy = random, hard = minimax).
• Add GUI using tkinter or pygame.

## 👤 Author
Alive Peterson
GitHub: @Alive-Peterson

## 🪪 License
This project is free to use, modify, and distribute. No license required.