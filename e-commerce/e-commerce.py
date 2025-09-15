import mysql.connector
import getpass

def get_connection():
    db_password = getpass.getpass("Enter MySQL password: ")
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
    user_name = input("Enter your user name:")
    email = input("Enter your email:")
    password = getpass.getpass("Enter your password:")
    address = input("Enter your adddress:")
    phone = input("Enter your phone number:")

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
    email = input("Enter your email:")
    password = getpass.getpass("Enter you password:")
    pass


# view products
def view_products():
    conn = get_connection()
    cursor = conn.cursor()
    sql = """SELECT product_id, product_name, price, stock, category_id, category_name, date_added"""










