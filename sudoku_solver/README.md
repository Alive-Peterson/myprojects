# 🧩 Sudoku Solver

A terminal-based Python program that uses **backtracking** to solve Sudoku puzzles.

---

## 📌 Overview

This project implements a **recursive backtracking algorithm** to solve standard 9x9 Sudoku boards. The puzzle is represented as a nested list of integers, where empty spaces are denoted by `-1`.

---

## 📚 Concepts Used

- **Backtracking recursion**
- **Constraint checking** for rows, columns, and 3×3 subgrids
- **Formatted board printing**
- **Modular design** using helper functions

---

## 🚀 How to Run

### ✅ Requirements

- Python 3.x

### ▶️ Run the Script

1. Clone the repository or download the file `sudoku_solver.py`.
2. Open a terminal and navigate to the project directory.
3. Run the script using:

   ```bash
   python sudoku_solver.py
   ```

## 🧠 How It Works
1. The program finds the next empty cell (a cell with -1).

2. It attempts to place a valid number (1–9) that doesn't violate Sudoku rules:

    2.1. The number must not appear in the same row.

    2.2. The number must not appear in the same column.

    2.3. The number must not appear in the same 3×3 box.

3. If a valid guess is found, it recurses deeper.

4. If the board reaches an invalid state, it backtracks and tries the next guess.


## 🔍 Sample Puzzle and Output

### ▶️ Input Puzzle

```python
example_board = [
    [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
    [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
    [-1, -1, -1,   7, 1, 9,   -1, 8, -1],
    [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
    [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
    [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],
    [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
    [6, 7, -1,   1, -1, 5,   -1, 4, -1],
    [1, -1, 9,   -1, -1, -1,   2, -1, -1]
]
```
### ✅ Solved Output

```text
+-------+-------+-------+
| 3 9 1 | 8 5 4 | 7 2 6 |
| 7 6 8 | 2 3 1 | 4 9 5 |
| 2 4 5 | 7 1 9 | 6 8 3 |
+-------+-------+-------+
| 4 5 3 | 9 6 8 | 1 7 2 |
| 2 1 6 | 4 7 3 | 9 5 8 |
| 9 8 7 | 5 2 6 | 3 1 4 |
+-------+-------+-------+
| 5 2 4 | 6 9 7 | 8 3 1 |
| 6 7 2 | 1 8 5 | 5 4 9 |
| 1 3 9 | 3 4 2 | 2 6 7 |
+-------+-------+-------+
```

## 🛠️ Customization

1. You can replace example_board in the script with your own 9×9 puzzle.

2. Use -1 to indicate empty spaces.

## 👤 Author
Alive Peterson
GitHub: @Alive-Peterson

## 🪪 License
This project is free to use and distribute. No license required.