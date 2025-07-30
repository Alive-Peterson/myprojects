# 📘 Binary Search vs Naive Search in Python

This Python script demonstrates and compares the performance of two search algorithms: **Naive (Linear) Search** and **Binary Search**. It uses randomly generated data to show how binary search is significantly faster on sorted lists.

---

## 🔍 Algorithms Implemented

- **Naive Search (Linear Search):**  
  Scans each element one by one until it finds the target.

- **Binary Search:**  
  Uses a divide-and-conquer approach on sorted data for much faster lookups.

---

## 🚀 How It Works

1. Generates a large set of unique random integers.
2. Sorts the list for binary search.
3. Times how long it takes each algorithm to search for **every item** in the list.
4. Prints the average time per search for both algorithms.

---

## 🛠️ How to Run

1. Make sure you have Python installed.  
2. Run the script from the terminal:
    ```bash
    python binary_search.py
    ```

## 📈 Sample Output
```sql
Naive Search Time: 0.0001887599229812622 seconds
Binary Search Time: 1.9651412963867187e-06 seconds
```
## 📚 Concepts Demonstrated

• Search algorithm comparison
• Recursion
• Timing code with time.time()
• List generation and sorting
• Performance benchmarking

## ✅ Requirements
Python 3.x (no external libraries needed)

## 👤 Author
Alive Peterson
GitHub: @Alive-Peterson

## 🪪 License
This project is free to use, modify, and distribute. No license required.