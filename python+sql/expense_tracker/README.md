# 💰 Expense Tracker (Python + MySQL + Matplotlib)

A Python-based **Expense Tracker** that helps you manage personal expenses by recording, summarizing, importing, and visualizing your spending data. It integrates with **MySQL** for persistent storage and uses **Matplotlib** for visualization.

---

## 📌 Features

- ➕ **Add Transactions**: Enter expenses with date, amount, category, and notes.  
- 📊 **Summary by Category**: View total spending per category.  
- 📅 **Monthly Total**: See how much you spent in the current month.  
- 📥 **Import from CSV**: Load multiple transactions from a CSV file.  
- 📈 **Visualization**:  
  - **Bar Graph**: Total expenses by category.  
  - **Pie Chart**: Percentage breakdown of categories.  

---

## 🛠 Requirements

- Python 3.x  
- MySQL server running locally  
- Libraries:  
  - `mysql-connector-python`  
  - `matplotlib`  

Install dependencies with:
```bash
pip install mysql-connector-python matplotlib
```

## 🗄️ Database Setup

Before running the program, create a database and table in MySQL:

```sql
CREATE DATABASE yourdatabasename;

USE yourdatabasename;

CREATE TABLE expense_transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    txn_date DATE,
    amount DECIMAL(10,2),
    category VARCHAR(50),
    notes VARCHAR(255)
);
```
### Update the MySQL connection details in expense_tracker.py according to your databse name, user, and password:
```python
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="yourdatabasename"
    )
```

## 🚀 How to Run

Run the script:
```python
python expense_tracker.py
```

You will see a menu like this:
```text
-----Expense Tracker-----
1. Add Transaction
2. View summary by category
3. View monthly expense
4. Import from csv
5. Visualize expenses
6. Exit
```
Choose an option by entering its number.

## 📊 Example Usage

1️⃣ Adding an Expense
```text
Enter Date (YYYY-MM-DD): 2025-09-10
Enter the amount: 250
Enter Category: Food
Enter notes(Optional): Lunch with friends
Expense added with ID 1
```
2️⃣ Viewing Summary
```python
Summary by Category:
Food: 250.00
```
3️⃣ Visualization

Select option 5 → Choose a for bar graph or b for pie chart.

📥 CSV Import Format

Your CSV file should have the following headers:
```yaml
txn_date,amount,category,notes
2025-09-01,500,Groceries,Weekly shopping
2025-09-03,200,Transport,Bus pass
```
## 👤 Author

**Alive Peterson**  
🔗 [GitHub: @Alive-Peterson](https://github.com/Alive-Peterson)  
📧 alivepeterson2@gmail.com  
