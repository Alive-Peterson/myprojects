-- 1. Identifying the Most Profitable Products

SELECT
    Product_Name,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    ROUND(SUM(Net_Revenue_USD), 2) AS Total_Revenue,
    ROUND(SUM(Profit_USD), 2) AS Total_Profit,
    ROUND(AVG(Profit_Margin_Pct), 2) AS Avg_Profit_Margin
FROM fmcg_sales_cleaned
GROUP BY Product_Name
ORDER BY Total_Profit DESC
LIMIT 10;


-- 2. Identifying Products with Consistently Poor Margins

SELECT
    Product_Name,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    ROUND(AVG(Profit_Margin_Pct), 2) AS Avg_Profit_Margin,
    ROUND(SUM(Profit_USD), 2) AS Total_Profit
FROM fmcg_sales_cleaned
GROUP BY Product_Name
HAVING COUNT(DISTINCT Order_ID) >= 20
ORDER BY Avg_Profit_Margin ASC
LIMIT 10;


-- 3. Finding the Highest Individual Loss-Making Orders

SELECT
    Order_ID,
    Order_Date,
    Product_Category,
    Product_Name,
    Sales_Channel,
    Promotion_Type,
    Net_Revenue_USD,
    COGS_USD,
    Marketing_Spend_USD,
    Logistics_Cost_USD,
    Profit_USD
FROM fmcg_sales_cleaned
WHERE Profit_USD < 0
ORDER BY Profit_USD ASC
LIMIT 10;

-- 4. Comparing Profitability by Region

SELECT
    Region,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    ROUND(SUM(Net_Revenue_USD), 2) AS Total_Revenue,
    ROUND(SUM(Profit_USD), 2) AS Total_Profit,
    ROUND(
        SUM(Profit_USD) / SUM(Net_Revenue_USD) * 100,
        2
    ) AS Profit_Margin_Pct
FROM fmcg_sales_cleaned
GROUP BY Region
ORDER BY Total_Profit DESC;


-- 5. Salespeople with Lowest Profitability

SELECT
    Sales_Person,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    ROUND(SUM(Net_Revenue_USD), 2) AS Total_Revenue,
    ROUND(SUM(Profit_USD), 2) AS Total_Profit,
    ROUND(
        SUM(Profit_USD) / SUM(Net_Revenue_USD) * 100,
        2
    ) AS Profit_Margin_Pct
FROM fmcg_sales_cleaned
GROUP BY Sales_Person
ORDER BY Total_Profit ASC
LIMIT 10;

-- 6. Identifying High-Value Orders with Low/Negative Margins

SELECT
    Order_ID,
    Product_Category,
    Product_Name,
    Sales_Channel,
    Net_Revenue_USD,
    Profit_USD,
    Profit_Margin_Pct
FROM fmcg_sales_cleaned
WHERE Net_Revenue_USD >= (
    SELECT AVG(Net_Revenue_USD)
    FROM fmcg_sales_cleaned
)
AND Profit_Margin_Pct < 0
ORDER BY Net_Revenue_USD DESC;