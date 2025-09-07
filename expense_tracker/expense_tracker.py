import mysql.connector
import csv
import matplotlib

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",          
        password="llawlietnate",
        database="projects"
    )

# for adding new expense
def add_expense():
    date=input("Enter Date (DD-MM-YYYY):")
    amount=float(input("Enter the amount:"))
    category=input("Enter Category:")
    notes=input("Enter notes(Optional):")

    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO expense_transactions (txn_date, amount, category, notes) VALUES (%s, %s, %s, %s)"
    values = (date, amount, category, notes)
    cursor.execute(sql, values)
    conn.commit()
    print(f"✅ Expense added with ID {cursor.lastrowid}")
    conn.close()

# for viewing summary by category 
def view_summary_by_category():
    conn = get_connection
    cursor = conn.cursor()
    sql = "SELECT category, SUM(amount) FROM expense_transactions GROUP BY category"
    cursor.execute(sql)
    rows=cursor.fetchall

    print("\n Summary by Category:")
    for category, total in rows:
        print(f"{category}:{total}")
    conn.close()

#for viewing monthly total
def view_monthly_total():
    conn = get_connection
    cursor = conn.cursor()
    sql = """ SELECT SUM(amount)
              FROM expense_transactions
              WHERE MONTH(txn_date) = MONTH(CURDATE())
              AND YEAR(txn_date) = YEAR(CURDATE()) """
    cursor.execute(sql)
    total = cursor.fetchone()[0]
    print("\n Monthly Total:", total if total else 0)
    conn.close()