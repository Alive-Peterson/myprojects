CREATE TABLE users(
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    user_name VARCHAR(50) NOT NULL,
    email VARCHAR(200) NOT NULL UNIQUE,
    password VARCHAR(30) NOT NULL,
    address TEXT NOT NULL,
    phone VARCHAR(20) NOT NULL,
    registered_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    
);

CREATE TABLE categories(
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(30) NOT NULL UNIQUE,
    description TEXT
);

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

CREATE TABLE orders(
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status ENUM('Pending','Shipped','Delivered','Cancelled') DEFAULT 'Pending',
    total_amount DECIMAL(10,2),
    FOREIGN KEY(user_id) REFERENCES users(user_id)
);

CREATE TABLE order_items(
    order_item_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY(order_id) REFERENCES orders(order_id),
    FOREIGN KEY(product_id) REFERENCES products(product_id)

);


CREATE TABLE payments(
    payment_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    payment_type ENUM('Credit Card','Debit Card','UPI','Net Banking','Cash on Delivery') NOT NULL,
    status ENUM('Pending','Completed','Failed') DEFAULT 'Pending',
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

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

CREATE TABLE logins (
    login_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NULL,
    login_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status ENUM('Success','Failure') NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
