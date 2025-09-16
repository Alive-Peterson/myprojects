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
    category_id = int(input("Enter category id :"))
    sql = "INSERT INTO products VALUES(product_name, description, price, stock, category_id) VALUES (%s, %s, %s, %s, %s)"
    values = (product_name, description, price, stock, category_id if category_id != 0 else None)
    conn.commit()
    conn.close()
    print("Product Added successfully")


#






