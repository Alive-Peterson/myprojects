-- Basic SQL Queries
-- 1. Current stock (on-hand quantity)
SELECT 
    p.sku,
    p.name,
    w.name AS warehouse,
    COALESCE(SUM(sm.qty_change), 0) AS qty_on_hand
FROM products p
CROSS JOIN warehouses w
LEFT JOIN stock_movements sm
    ON sm.product_id = p.product_id AND sm.warehouse_id = w.warehouse_id
GROUP BY p.sku, p.name, w.name
ORDER BY p.sku;

-- 2. Top-selling products
SELECT 
    p.sku,
    p.name,
    SUM(-sm.qty_change) AS qty_sold
FROM stock_movements sm
JOIN products p ON p.product_id = sm.product_id
WHERE sm.movement_type = 'SALE'
GROUP BY p.sku, p.name
ORDER BY qty_sold DESC;

-- 3. Products below reorder level
SELECT 
    p.sku,
    p.name,
    p.reorder_level,
    COALESCE(SUM(sm.qty_change),0) AS qty_on_hand
FROM products p
LEFT JOIN stock_movements sm ON p.product_id = sm.product_id
GROUP BY p.sku, p.name, p.reorder_level
HAVING qty_on_hand < p.reorder_level;

-- 4. Inventory value (based on cost price)
SELECT 
    p.sku,
    p.name,
    COALESCE(SUM(sm.qty_change),0) AS qty_on_hand,
    p.cost_price,
    (COALESCE(SUM(sm.qty_change),0) * p.cost_price) AS inventory_value
FROM products p
LEFT JOIN stock_movements sm ON p.product_id = sm.product_id
GROUP BY p.sku, p.name, p.cost_price
ORDER BY inventory_value DESC;

-- Analytical / Intermediate Queries
-- 1. Monthly stock received per product
SELECT 
    p.name,
    DATE_FORMAT(sm.movement_date, '%Y-%m') AS month,
    SUM(CASE WHEN sm.qty_change > 0 THEN sm.qty_change ELSE 0 END) AS total_received
FROM stock_movements sm
JOIN products p ON sm.product_id = p.product_id
WHERE sm.movement_type = 'PURCHASE'
GROUP BY p.name, DATE_FORMAT(sm.movement_date, '%Y-%m')
ORDER BY month;

-- 2. Supplier with fastest delivery time
SELECT 
    s.name AS supplier,
    AVG(DATEDIFF(pi.received_date, po.po_date)) AS avg_lead_days
FROM purchase_orders po
JOIN purchase_items pi ON po.po_id = pi.po_id
JOIN suppliers s ON po.supplier_id = s.supplier_id
GROUP BY s.name
ORDER BY avg_lead_days ASC;

-- 3. Profit analysis per product
SELECT 
    p.name,
    SUM(si.quantity * si.unit_price) AS total_revenue,
    SUM(si.quantity * p.cost_price) AS total_cost,
    (SUM(si.quantity * si.unit_price) - SUM(si.quantity * p.cost_price)) AS total_profit,
    ROUND(((SUM(si.quantity * si.unit_price) - SUM(si.quantity * p.cost_price)) / 
           SUM(si.quantity * si.unit_price)) * 100, 2) AS profit_margin_pct
FROM sales_items si
JOIN products p ON si.product_id = p.product_id
GROUP BY p.name
ORDER BY total_profit DESC;

-- Optional query for view table
SELECT * FROM vw_current_stock;
