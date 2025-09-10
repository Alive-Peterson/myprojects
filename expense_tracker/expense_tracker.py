import mysql.connector
import csv
import matplotlib as plt

def get_connection():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",          
        password = "llawlietnate",
        database = "myprojects"
    )

# for adding new expense
def add_expense():
    date = input("Enter Date (YYYY-MM-DD):")
    amount = float(input("Enter the amount:"))
    category = input("Enter Category:")
    notes = input("Enter notes(Optional):")

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

#import from csv
def import_from_csv():
    filepath = input("Enter csv file path:")
    try:
        with open(filepath, mode='r') as file:
            reader = csv.DictReader(file)
            data = [(row["txn_date"], float(row["amount"]), row["category"], row["notes"]) for row in reader]

        conn = get_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO expense_transactions (txn_date, amount, category, notes) VALUES (%s, %s, %s, %s)"
        cursor.executemany(sql,data)
        conn.commit()
        print(f"Imported {cursor.rowcount} from csv file")
        conn.close()

    except Exception as e:
        print("Error importing csv:", e)

#visualization(bargraph and pie chart using matplotlib)
def visualize_expense():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT category, SUM(amount FROM expense_transactions GROUP BY category)")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("No Data to Visualize")
        return

    categories = [row[0] for row in rows]
    totals = [float(row[1] for row in rows)]

    #bar graph
    plt.figure(figure=(10,5))
    plt.bar(categories, totals, colour="skyblue")
    plt.title("Expenses by category(BarGraph):")
    plt.xlabe("Category")
    plt.ylabel("TotalAmount")
    plt.show()

    #pie chart
    plt.figure(figure=(8,8))
    plt.pie(totals, labels=categories, autopct="%1.1f%%", startangle=140)
    plt.title("Expenses by Category (Pie Chart)")
    plt.show()

# main function

def menu():
    while True:
        print("\n-----Expense Tracker-----")
        print("1. Add Transaction")
        print("2. View summary by category")
        print("3. View monthly expense")
        print("4. Import from csv")
        print("5. Visualize expenses")
        print("6. Exit")

        choice = input("Enter your choice:")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_summary_by_category()
        elif choice == "3":
            view_monthly_total()
        elif choice == "4":
            import_from_csv()
        elif choice == "5":
            visualize_expense()
        elif choice == "6":
            break

        else:
            print("Invalid Input, Try Again")

if __name__ == "__main__":
    print("Connected to MySQL")
    menu()
            
