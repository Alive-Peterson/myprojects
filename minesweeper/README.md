# 💣 Minesweeper – Terminal Edition

This is a Python terminal-based implementation of the classic **Minesweeper** game. You dig squares on a grid, trying to avoid hidden bombs. If you uncover all non-bomb squares, you win. Hit a bomb, and it's game over!

---

## 📌 Overview

- The board is randomly generated with bombs placed across it.
- Each square shows the number of bombs in the surrounding 8 cells.
- You can dig by entering the row and column number.
- The game ends when you either:
  - Uncover a bomb (you lose), or
  - Successfully dig all non-bomb cells (you win!).

---

## 🧠 Concepts Used

- Object-Oriented Programming (classes, methods, and encapsulation)
- 2D grid generation
- Recursion for safe zone auto-digging
- Input validation and error handling
- Custom string formatting for clean terminal display

---

## 🚀 How to Run

### ✅ Requirements

- Python 3.x

### ▶️ Steps to Run

1. Open your terminal or command prompt.
2. Navigate to the folder containing `minesweeper.py`.
3. Run the script:
   ```bash
   python minesweeper.py
   ```
4. Follow the on-screen prompts to play.

## 🔢 Sample Gameplay

```markdown
   0  1  2  3  4  5  6  7  8  9  
----------------------------------
0 |  |  |  |  |  |  |  |  |  |  |
1 |  |  |  |  |  |  |  |  |  |  |
2 |  |  |  |  |  |  |  |  |  |  |
3 |  |  |  |  |  |  |  |  |  |  |
4 |  |  |  |  |  |  |  |  |  |  |
5 |  |  |  |  |  |  |  |  |  |  |
6 |  |  |  |  |  |  |  |  |  |  |
7 |  |  |  |  |  |  |  |  |  |  |
8 |  |  |  |  |  |  |  |  |  |  |
9 |  |  |  |  |  |  |  |  |  |  |
----------------------------------
Choose a location to dig? (Input as row,col format):0,0
   0  1  2  3  4  5  6  7  8  9  
----------------------------------
0 |0 |0 |0 |1 |  |  |  |  |  |  |
1 |0 |0 |0 |1 |  |  |  |  |  |  |
2 |0 |0 |0 |1 |2 |3 |  |  |  |  |
3 |0 |0 |0 |0 |0 |1 |  |  |  |  |
4 |0 |1 |1 |1 |0 |1 |  |  |  |  |
5 |0 |2 |  |2 |0 |1 |2 |  |  |  |
6 |0 |2 |  |2 |0 |0 |1 |  |  |  |
7 |0 |1 |1 |1 |0 |0 |2 |  |  |  |
8 |0 |0 |0 |0 |0 |0 |1 |  |  |  |
9 |0 |0 |0 |0 |0 |0 |1 |  |  |  |
----------------------------------
Choose a location to dig? (Input as row,col format):
```

## 🛠️ Customization

• To change board size or number of bombs, edit:
```python
play(dim_size=10, num_bombs=10)
```
in the last line of the script.

• Difficulty ideas:

Easy: dim_size=8, num_bombs=8

Medium: dim_size=10, num_bombs=15

Hard: dim_size=15, num_bombs=40

## 🧾 Code Structure

Board class handles:

   Grid generation

   Bomb placement

   Value assignment

   Digging logic

   Board display

play() function:

   Main game loop

   Handles player input

   Ends game on win/loss

## 👤 Author
Alive Peterson
GitHub: @Alive-Peterson

## 🪪 License
This project is free to use. No license required.