# 🏪 Retail Inventory Management System (MySQL)

## 📘 Overview

This project is a **Retail Inventory Management System** built using **MySQL**.
It helps track **products, suppliers, warehouses, purchases, sales, stock levels, and profits** efficiently.
The system is designed to support small to medium retail businesses in maintaining accurate inventory data and generating insights through analytical SQL queries.

---

## 🧱 Database Structure

The system includes the following tables:

products - Stores product details like SKU, name, category, cost & selling prices. 
suppliers - Contains supplier information including contact details.                
warehouses - Tracks storage locations and warehouse names.                           
purchase_orders - Records orders placed to suppliers.
purchase_items - Holds individual products from each purchase order.
sales_orders - Manages customer orders and dates.                                      
sales_items - Contains individual products sold in each order.
stock_movements - Logs every stock movement (purchase, sale, return).      
vw_current_stock - Displays the current stock available in each warehouse.                 |


## 📊 Example Analytical Queries

Some of the key insights generated from this project include:

1. **Current Stock Levels**

   ```sql
   SELECT p.sku, p.name, w.name AS warehouse, COALESCE(SUM(sm.qty_change), 0) AS qty_on_hand
   FROM products p
   CROSS JOIN warehouses w
   LEFT JOIN stock_movements sm
       ON sm.product_id = p.product_id AND sm.warehouse_id = w.warehouse_id
   GROUP BY p.sku, p.name, w.name;
   ```

2. **Top-Selling Products**

   ```sql
   SELECT p.sku, p.name, SUM(-sm.qty_change) AS qty_sold
   FROM stock_movements sm
   JOIN products p ON p.product_id = sm.product_id
   WHERE sm.movement_type = 'SALE'
   GROUP BY p.sku, p.name
   ORDER BY qty_sold DESC;
   ```

3. **Products Below Reorder Level**

   ```sql
   SELECT p.name, p.reorder_level, COALESCE(SUM(sm.qty_change),0) AS qty_on_hand
   FROM products p
   LEFT JOIN stock_movements sm ON p.product_id = sm.product_id
   GROUP BY p.name, p.reorder_level
   HAVING qty_on_hand < p.reorder_level;
   ```

4. **Profit Analysis per Product**

   ```sql
   SELECT 
       p.name,
       SUM(si.quantity * si.unit_price) AS total_revenue,
       SUM(si.quantity * p.cost_price) AS total_cost,
       (SUM(si.quantity * si.unit_price) - SUM(si.quantity * p.cost_price)) AS total_profit
   FROM sales_items si
   JOIN products p ON si.product_id = p.product_id
   GROUP BY p.name;
   ```

---

## ⚙️ How to Use

1. Open MySQL Workbench or any SQL client.
2. Run `Tables_and_Data-insertion.sql` to create tables and insert sample data.
3. Execute `Queries.sql` to explore reports and analytics such as:

   * Current stock levels
   * Top-selling products
   * Monthly purchase quantities
   * Supplier lead times
   * Profit margins per product

---

## 📈 Key Features

* Tracks **purchases, sales, and inventory movements** automatically.
* Monitors **reorder levels** and **low-stock alerts**.
* Calculates **profit margins** and **inventory valuation**.
* Provides **analytical reports** on stock, suppliers, and sales performance.

---

## 🧩 Tech Stack

* **Database:** MySQL
* **Language:** SQL
* **Tools:** MySQL Workbench / DBeaver
* **Dataset:** Custom sample data for retail products, warehouses, and transactions

---

## 📄 Author

**Alive Peterson**
🔗 GitHub: [Alive-Peterson](https://github.com/Alive-Peterson)  <br>
📧 alivepeterson2@gmail.com  

---

## 💡 Future Improvements

* Add **user roles** (admin, manager, warehouse staff).
* Build **Python or Power BI dashboard** for live visual analytics.
* Include **trigger-based stock updates** for automatic movement logging.
