CREATE DATABASE retail_inventory;
USE retail_inventory;

-- PRODUCTS
CREATE TABLE products (
  product_id INT AUTO_INCREMENT PRIMARY KEY,
  sku VARCHAR(50) UNIQUE NOT NULL,
  name VARCHAR(200) NOT NULL,
  category VARCHAR(100),
  cost_price DECIMAL(10,2) NOT NULL DEFAULT 0.00,
  sell_price DECIMAL(10,2) NOT NULL DEFAULT 0.00,
  reorder_level INT DEFAULT 10,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- SUPPLIERS
CREATE TABLE suppliers (
  supplier_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(200) NOT NULL,
  contact_email VARCHAR(200),
  phone VARCHAR(50),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- WAREHOUSES
CREATE TABLE warehouses (
  warehouse_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  location VARCHAR(200)
);

-- PURCHASE ORDERS
CREATE TABLE purchase_orders (
  po_id INT AUTO_INCREMENT PRIMARY KEY,
  supplier_id INT,
  po_date DATE NOT NULL,
  status VARCHAR(50) DEFAULT 'RECEIVED',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

-- PURCHASE ITEMS
CREATE TABLE purchase_items (
  pi_id INT AUTO_INCREMENT PRIMARY KEY,
  po_id INT,
  product_id INT,
  warehouse_id INT,
  quantity INT NOT NULL,
  unit_cost DECIMAL(10,2) NOT NULL,
  received_date DATE,
  FOREIGN KEY (po_id) REFERENCES purchase_orders(po_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id),
  FOREIGN KEY (warehouse_id) REFERENCES warehouses(warehouse_id)
);

-- SALES ORDERS
CREATE TABLE sales_orders (
  so_id INT AUTO_INCREMENT PRIMARY KEY,
  order_date DATE NOT NULL,
  customer_name VARCHAR(200),
  status VARCHAR(50) DEFAULT 'COMPLETED'
);

-- SALES ITEMS
CREATE TABLE sales_items (
  si_id INT AUTO_INCREMENT PRIMARY KEY,
  so_id INT,
  product_id INT,
  warehouse_id INT,
  quantity INT NOT NULL,
  unit_price DECIMAL(10,2) NOT NULL,
  FOREIGN KEY (so_id) REFERENCES sales_orders(so_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id),
  FOREIGN KEY (warehouse_id) REFERENCES warehouses(warehouse_id)
);

-- STOCK MOVEMENTS (Tracks inventory in/out)
CREATE TABLE stock_movements (
  movement_id INT AUTO_INCREMENT PRIMARY KEY,
  product_id INT,
  warehouse_id INT,
  movement_type VARCHAR(50) NOT NULL, -- PURCHASE, SALE, RETURN
  reference_id INT,
  qty_change INT NOT NULL,
  movement_date DATETIME DEFAULT CURRENT_TIMESTAMP,
  note TEXT,
  FOREIGN KEY (product_id) REFERENCES products(product_id),
  FOREIGN KEY (warehouse_id) REFERENCES warehouses(warehouse_id)
);

-- Useful Views (optional)
CREATE VIEW vw_current_stock AS
SELECT 
    p.product_id,
    p.name,
    w.name AS warehouse,
    COALESCE(SUM(sm.qty_change),0) AS qty_on_hand
FROM products p
CROSS JOIN warehouses w
LEFT JOIN stock_movements sm
    ON sm.product_id = p.product_id AND sm.warehouse_id = w.warehouse_id
GROUP BY p.product_id, p.name, w.name;


-- Warehouses
INSERT INTO warehouses (name, location) VALUES
('Main Warehouse', 'Mumbai'),
('Store #1', 'Pune');

INSERT INTO warehouses (name, location) VALUES
('Store #2', 'Delhi'),
('Store #3', 'Bangalore');


-- Suppliers
INSERT INTO suppliers (name, contact_email, phone) VALUES
('Acme Supplies', 'acme@example.com', '9999000001'),
('Global Goods', 'sales@global.com', '9999000002');
INSERT INTO suppliers (name, contact_email, phone) VALUES
('Urban Traders', 'contact@urbantraders.com', '9999000003'),
('HomeStyle Ltd', 'support@homestyle.com', '9999000004');


-- Products
INSERT INTO products (sku, name, category, cost_price, sell_price, reorder_level) VALUES
('SKU001','Blue T-Shirt','Apparel', 150.00, 299.00, 20),
('SKU002','Black Jeans','Apparel', 800.00, 1299.00, 10),
('SKU003','Ceramic Mug','Home & Kitchen', 60.00, 129.00, 30);
INSERT INTO products (sku, name, category, cost_price, sell_price, reorder_level) VALUES
('SKU004','Running Shoes','Footwear', 1200.00, 2499.00, 15),
('SKU005','Leather Wallet','Accessories', 400.00, 899.00, 25),
('SKU006','Desk Lamp','Home & Kitchen', 350.00, 699.00, 10),
('SKU007','Bluetooth Earphones','Electronics', 900.00, 1899.00, 20),
('SKU008','Cotton Bedsheet','Home & Kitchen', 500.00, 999.00, 30);


-- Purchase Orders
INSERT INTO purchase_orders (supplier_id, po_date) VALUES
(1, '2025-10-01'),
(2, '2025-10-05');
INSERT INTO purchase_orders (supplier_id, po_date) VALUES
(3, '2025-10-08'),
(4, '2025-10-09'),
(1, '2025-10-12'),
(2, '2025-10-13');


-- Purchase Items
INSERT INTO purchase_items (po_id, product_id, warehouse_id, quantity, unit_cost, received_date) VALUES
(1, 1, 1, 100, 150.00, '2025-10-03'),
(1, 3, 1, 200, 60.00, '2025-10-03'),
(2, 2, 1, 50, 800.00, '2025-10-06');
INSERT INTO purchase_items (po_id, product_id, warehouse_id, quantity, unit_cost, received_date) VALUES
(3, 4, 1, 60, 1200.00, '2025-10-09'),
(3, 5, 2, 100, 400.00, '2025-10-09'),
(4, 6, 3, 80, 350.00, '2025-10-10'),
(4, 7, 3, 50, 900.00, '2025-10-10'),
(5, 8, 1, 120, 500.00, '2025-10-13'),
(6, 3, 2, 150, 60.00, '2025-10-14');


-- Sales Orders
INSERT INTO sales_orders (order_date, customer_name) VALUES
('2025-10-10','Alice'),
('2025-10-11','Bob');
INSERT INTO sales_orders (order_date, customer_name) VALUES
('2025-10-14', 'Charlie'),
('2025-10-15', 'David'),
('2025-10-16', 'Evelyn'),
('2025-10-17', 'Frank');


-- Sales Items
INSERT INTO sales_items (so_id, product_id, warehouse_id, quantity, unit_price) VALUES
(1, 1, 2, 5, 299.00),
(1, 3, 2, 2, 129.00),
(2, 2, 1, 1, 1299.00);
INSERT INTO sales_items (so_id, product_id, warehouse_id, quantity, unit_price) VALUES
(3, 4, 1, 2, 2499.00),  -- Running Shoes sold
(3, 5, 2, 3, 899.00),   -- Leather Wallets sold
(4, 7, 3, 1, 1899.00),  -- Bluetooth Earphones
(4, 6, 3, 2, 699.00),   -- Desk Lamp
(5, 1, 2, 4, 299.00),   -- Blue T-Shirt
(6, 8, 1, 2, 999.00);   -- Bedsheet


-- Stock Movements
INSERT INTO stock_movements (product_id, warehouse_id, movement_type, reference_id, qty_change, movement_date, note) VALUES
(1,1,'PURCHASE',1,100,'2025-10-03','PO#1 Received'),
(3,1,'PURCHASE',1,200,'2025-10-03','PO#1 Received'),
(2,1,'PURCHASE',2,50,'2025-10-06','PO#2 Received'),
(1,2,'SALE',1,-5,'2025-10-10','Sold to Alice'),
(3,2,'SALE',1,-2,'2025-10-10','Sold to Alice'),
(2,1,'SALE',2,-1,'2025-10-11','Sold to Bob');

INSERT INTO stock_movements (product_id, warehouse_id, movement_type, reference_id, qty_change, movement_date, note) VALUES
-- Purchases
(4,1,'PURCHASE',3,60,'2025-10-09','PO#3 Received'),
(5,2,'PURCHASE',3,100,'2025-10-09','PO#3 Received'),
(6,3,'PURCHASE',4,80,'2025-10-10','PO#4 Received'),
(7,3,'PURCHASE',4,50,'2025-10-10','PO#4 Received'),
(8,1,'PURCHASE',5,120,'2025-10-13','PO#5 Received'),
(3,2,'PURCHASE',6,150,'2025-10-14','PO#6 Received'),

-- Sales
(4,1,'SALE',3,-2,'2025-10-14','Sold to Charlie'),
(5,2,'SALE',3,-3,'2025-10-14','Sold to Charlie'),
(7,3,'SALE',4,-1,'2025-10-15','Sold to David'),
(6,3,'SALE',4,-2,'2025-10-15','Sold to David'),
(1,2,'SALE',5,-4,'2025-10-16','Sold to Evelyn'),
(8,1,'SALE',6,-2,'2025-10-17','Sold to Frank');



