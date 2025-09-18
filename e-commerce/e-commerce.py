import mysql.connector
import getpass

def get_connection():
    db_password = getpass.getpass("Enter MySQL password : ")
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=db_password,
        database="myprojects"
    )

# register user info
def register_user():
    conn = get_connection()
    cursor = conn.cursor()
    user_name = input("Enter your user name :")
    email = input("Enter your email :")
    password = getpass.getpass("Enter your password :")
    address = input("Enter your adddress  :")
    phone = input("Enter your phone number :")

    try:
        sql = "INSERT INTO users (user_name, email, password, address, phone) VALUES (%s, %s, %s, %s, %s)"
        values = (user_name, email, password, address, phone)
        cursor.execute(sql, values)
        conn.commit()
    except mysql.connector.Error as err:
        print("Error:", err)
        conn.close()

#user login 
def login():
    conn = get_connection()
    cursor = conn.cursor()
    email = input("Enter your email :")
    password = getpass.getpass("Enter you password :")
    sql = "SELECT user_id FROM users WHERE email = %s AND password = %s"
    values = (email, password)
    cursor.execute(sql, values)
    result = cursor.fetchone()

    if result:
        user_id = result[0]
        sql = "INSERT INTO logins(user_id, status) VALUES(%s, %s)"
        values = (user_id, "success")
        cursor.execute(sql,values)
        conn.commit()
        print("Login successful!")
        return user_id
    
    else:
        sql ="INSERT INTO logins(user_id, status) VALUES(%s, %s)"
        values = ("None", "Failed")
        cursor.execute(sql, values)
        conn.commit()
        print("Inavalid email or password" \
        "\n Try registering, if you didn't")
        conn.close()

        return None
    

# view products
def view_products():
    conn = get_connection()
    cursor = conn.cursor()
    sql = """ SELECT p.product_id, p.product_name, p.price, p.stock, c.category_name
              FROM products p
              LEFT JOIN categories c ON p.category_id = c.category_id """
    cursor.execute(sql)
    rows = cursor.fetchall()
    print("----Available Products----")
    for row in rows:
        product_id, product_name, price, stock, category = row
        print(f"ID: {product_id} | {product_name} | {price} | Stock: {stock} | Category: {category}")
    conn.close()

# add products
def add_product():
    conn = get_connection()
    cursor = conn.cursor()
    product_name = input("Enter product name :")
    description = input("Enter Description :")
    price = float(input("Enter price of product :"))
    stock = int(input("Enter stock :"))
    category_id = int(input("Enter category ID :"))
    sql = "INSERT INTO products (product_name, description, price, stock, category_id) VALUES (%s, %s, %s, %s, %s)"
    values = (product_name, description, price, stock, category_id if category_id != 0 else None)
    cursor.execute(sql,values)
    conn.commit()
    conn.close()
    print("Product Added successfully")


#placing order
def place_order(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    view_products()
    product_id = int(input("Enter product ID:"))
    quantity = int(input("Enter the quantity:"))
    sql = "SELECT product_id, stock FROM products WHERE product_id = %s"
    values = (product_id,)
    cursor.execute(sql, values)
    row = cursor.fetchone()

    if not row:
        print("Invalid product")
        conn.close()
        return
    
    price, stock = row
    if quantity > stock:
        print("Not enough stock")
        conn.close()
        return
    
    total_amount = price*quantity
    
    #insert into orders
    sql = "INSERT INTO orders(user_id, total_amount, status) VALUES(%s, %s, 'Pending')" 
    values = (user_id, total_amount)
    order_id = cursor.lastrowid

    #insert into order_items
    sql = "INSERT INTO order_items(order_id, product_id, quantity, price) VALUES(%s, %s, %s, %s)"
    values = (order_id, product_id, quantity, price)

    #Updating stock
    sql = "UPDATE products SET stock= stock - %s WHERE product_id = %s"
    values = (quantity, product_id)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
    print(f"Order placed successfully, Total Amount:₹{total_amount}")

# making payment
def make_payment(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    order_id = int(input("Enter your order ID:"))
    #fetching the total amount from orders table
    sql = "SELECT total_amount FROM orders WHERE order_id = %s AND user_id = %s"
    cursor.execute(sql, (order_id, user_id))
    result = cursor.fetchone()

    if not result:
        print("Invalid order ID, please try again")
        conn.close()
        return
    
    amount = result[0]
    payment_type = ("Enter your payment type(credit card / Debit Card / UPI / Net Banking / Cash on Delivery): )")

    #inserting into payments table
    sql = "INSERT INTO payments(order_id, amount, payment_type, status) VALUES(%s, %s, %s, 'Completed')"
    values = (order_id, amount, payment_type)
    cursor.execute(sql, values)

    #update orders table that product is shipped
    sql = "UPDATE orders SET status = 'Shipped' WHERE order_id = %s"
    values = (order_id,)
    cursor.execute(sql, values)

    conn.commit()
    conn.close()
    print(f"Payment of ₹{amount} was successfull")

#viewing orders
def view_orders():
    conn = get_connection()
    cursor = conn.cursor()
    order_id = int(input("Enter your order ID to view your order:"))
    sql = "SELECT order_id, order_date, status, total_amount FROM orders WHERE order_id = %s"
    values = (order_id) 
    cursor.execute(sql,values)
    orders = cursor.fetchall()
    print("\n----Your Order----")
    for order in orders:
        print(f"order ID:{order[0]} | Order Date:{order[1]} | Status:{order[2]} | Total:₹{order[3]}")

        sql = """ SELECT p.product_name, oi.quantity, oi.price
                  FROM order_items oi
                  JOIN products ON oi.product_id = p.product_id
                  WHERE oi.order_id = %s"""
        values = (sql, (order[0],))
        cursor.execute(sql, values)
        items = cursor.fetchall()
        for item in items:
            print(f"- {item[0]} x{item[1]} @ ₹{item[2]}")
    conn.close()

#reports 
def reports():
    conn = get_connection()
    cursor = conn.cursor()
    print("\n---- Reports ----")

    print("\nTop Selling Products:")
    sql = """SELECT p.product_name, SUM(oi.quantity) as total_sold
             FROM order_items oi
             JOIN products p ON oi.product_id = p.product_id
             GROUP BY oi.product_id
             ORDER BY total_sold DESC LIMIT 5"""
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(f"{row[0]} - {row[1]} sold")
    
    print("\nOrders by Status:")
    sql = "SELECT status, COUNT(*) FROM orders GROUP BY status"
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(f"{row[0]}: {row[1]}")

    conn.close()

#main function
def main():
    user_id = None
    while True:
        print("""\n---- E-Commerce CLI ----
1. Register
2. Login
3. View Products
4. Place Order
5. Make Payment
6. View Orders
7. Admin: Add Product
8. Admin: Reports
9. Exit""")
        choice = input("Enter Your choice:")

        if choice == "1":
            register_user()
        elif choice == "2":
            login()
        elif choice == "3":
            view_products()
        elif choice == "4":
            place_order()
        elif choice == "5":
            make_payment()
        elif choice == "6":
            view_orders()
        elif choice == "7":
            add_product()
        elif choice == "8":
            reports()
        elif choice == "9":
            break
        else:
            print("Invalid Input, Try Again")

if __name__ == "__main__":
    main()