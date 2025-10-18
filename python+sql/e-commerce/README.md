# 🛒 E-Commerce CLI Application

A simple **Command Line Interface (CLI)** based **E-commerce management system** built in Python with MySQL as the backend.  
It allows users to register, log in, browse products, place orders, make payments, and view reports.

---

## 📌 Features

- 👤 **User Management**
  - Register new users  
  - Secure login (with password masking)  

- 🛍 **Product Management**
  - View available products with categories and stock  
  - Admins can add new products  

- 📦 **Order Management**
  - Place orders  
  - Update stock automatically after purchase  
  - View your past orders  

- 💳 **Payment System**
  - Multiple payment types (Credit Card, Debit Card, UPI, Net Banking, COD)  
  - Updates order status after successful payment  

- 📊 **Reports (Admin)**
  - Top-selling products  
  - Orders by status  

---

## 🧠 Concepts Used

- Python functions and modular structure  
- MySQL database integration (`mysql-connector`)  
- Parameterized queries (to avoid SQL injection)  
- Joins and aggregate queries for reports  
- Exception handling  

---

## 🚀 How to Run

### ✅ Requirements
- Python 3.x  
- MySQL server running locally  
- Required Python package:
  ```bash
  pip install mysql-connector-python

## 🗄️ Database Setup

Run the following queries in MySQL to set up the database schema:

```sql
-- Users Table
CREATE TABLE users(
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    user_name VARCHAR(50) NOT NULL,
    email VARCHAR(200) NOT NULL UNIQUE,
    password VARCHAR(30) NOT NULL,
    address TEXT NOT NULL,
    phone VARCHAR(20) NOT NULL,
    registered_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Categories Table
CREATE TABLE categories(
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(30) NOT NULL UNIQUE,
    description TEXT
);

-- Products Table
CREATE TABLE products(
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    stock INT DEFAULT 0,
    category_id INT,
    date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(category_id) REFERENCES categories(category_id)
);

-- Orders Table
CREATE TABLE orders(
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status ENUM('Pending','Shipped','Delivered','Cancelled') DEFAULT 'Pending',
    total_amount DECIMAL(10,2),
    FOREIGN KEY(user_id) REFERENCES users(user_id)
);

-- Order items table
CREATE TABLE order_items(
    order_item_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY(order_id) REFERENCES orders(order_id),
    FOREIGN KEY(product_id) REFERENCES products(product_id)
);

-- Payments Table
CREATE TABLE payments(
    payment_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    payment_type ENUM('Credit Card','Debit Card','UPI','Net Banking','Cash on Delivery') NOT NULL,
    status ENUM('Pending','Completed','Failed') DEFAULT 'Pending',
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

--Shipping Table
CREATE TABLE shipping(
    shipping_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    shipping_address TEXT NOT NULL,
    courier VARCHAR(100),
    tracking_number VARCHAR(100),
    status ENUM('Processing','Shipped','In Transit','Delivered','Returned') DEFAULT 'Processing',
    shipped_on TIMESTAMP NULL,
    delivered_on TIMESTAMP NULL,
    FOREIGN KEY(order_id) REFERENCES orders(order_id)
);

-- Logins Table
CREATE TABLE logins (
    login_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NULL,
    login_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status ENUM('Success','Failure') NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
```
## ▶️ Steps

Create a MySQL database named myprojects.

Create the following tables (users, logins, products, categories, orders, order_items, payments) according to your schema.

Clone/download this project.

Run the program:
```python
python e-commerce.py
```
### 🖥️ Sample Menu
---- E-Commerce CLI ----
1. Register
2. Login
3. View Products
4. Place Order
5. Make Payment
6. View Orders
7. Admin: Add Product
8. Admin: Reports
9. Exit

## 🔢 Example Workflow
### Register & Login
```yaml
Enter your user name : JohnDoe
Enter your email : john@example.com
Enter your password :
Enter your address  : New York
Enter your phone number : 9876543210
```

### Place Order
```yaml
----Available Products----
ID: 1 | Laptop | 60000 | Stock: 5 | Category: Electronics
ID: 2 | Headphones | 2000 | Stock: 15 | Category: Accessories

Enter product ID: 2
Enter the quantity: 2
Order placed successfully, Total Amount: ₹4000
```
### Payment
```mathematica
Enter your order ID: 5
Enter your payment type (Credit Card / UPI / COD): UPI
Payment of ₹4000 was successful
```

## 🛠️ Customization

Change database credentials in get_connection() to match your setup.

Extend functionality with categories, product search, or discounts.

Add authentication/authorization for admin-specific tasks.

## 👤 Author

**Alive Peterson**  
🔗 [GitHub: @Alive-Peterson](https://github.com/Alive-Peterson)  
📧 alivepeterson2@gmail.com  