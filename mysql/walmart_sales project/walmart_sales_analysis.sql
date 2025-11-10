-- Data Analysis

SELECT *
FROM walmart_staging;

SELECT MIN(date), MAX(date) 
FROM walmart_staging;

-- Total sales across all stores

SELECT ROUND(SUM(Weekly_Sales), 2) AS total_sales
FROM walmart_staging;

-- Average weekly sales per store
SELECT Store, 
       ROUND(AVG(Weekly_Sales), 2) AS avg_weekly_sales
FROM walmart_staging
GROUP BY Store
ORDER BY Store ASC;

-- Highest sales and Lowest sales
SELECT * 
FROM walmart_staging
WHERE Weekly_Sales = (SELECT MAX(Weekly_Sales) FROM walmart_staging)
   OR Weekly_Sales = (SELECT MIN(Weekly_Sales) FROM walmart_staging);

-- Holiday vs Non-Holiday Sales Comparison
SELECT Holiday_Flag,
       ROUND(AVG(Weekly_Sales),2) AS avg_sales
FROM walmart_staging
GROUP BY Holiday_Flag;

-- Average sales by stores
SELECT Store,
       ROUND(AVG(Weekly_Sales),2) AS avg_sales
FROM walmart_staging
WHERE Holiday_Flag = 1
GROUP BY Store
ORDER BY avg_sales DESC
LIMIT 5;


-- Monthly Sales Trend

SELECT DATE_FORMAT(date, '%Y-%m') AS `Month`,
       ROUND(SUM(Weekly_Sales),2) AS total_sales
FROM walmart_staging
GROUP BY `Month`
ORDER BY `Month`;


-- Effect of Temperature on Sales
SELECT 
    CASE 
        WHEN Temperature < 40 THEN 'Cold'
        WHEN Temperature BETWEEN 40 AND 70 THEN 'Moderate'
        ELSE 'Hot'
    END AS temp_category,
    ROUND(AVG(Weekly_Sales),2) AS avg_sales
FROM walmart_staging
GROUP BY temp_category;

-- Effect of Fuel Price on Sales

SELECT 
      CASE
          WHEN Fuel_Price < 2.6 THEN 'low fuel price'
          WHEN Fuel_Price BETWEEN 2.6 AND 3.0 THEN 'Medium Fuel Price'
          ELSE 'High Fuel Price'
	  END AS fuel_group,
      ROUND(AVG(Weekly_Sales),2) AS avg_sales
FROM walmart_staging
GROUP BY fuel_group;

-- Impact of Unemployment Rate

SELECT
ROUND(Unemployment,1) AS unemployment_rate,
ROUND(AVG(Weekly_Sales),2) AS avg_sales
FROM walmart_staging
GROUP BY unemployment_rate
ORDER BY unemployment_rate DESC;


-- Yearly Sales Summary
SELECT YEAR(`Date`) AS `Year`,
ROUND(AVG(Weekly_Sales), 2) AS avg_sales,
ROUND(SUM(Weekly_Sales), 2) AS total_sales
FROM walmart_staging
GROUP BY `Year`
ORDER BY `Year`;

-- Creating a View for stores weekly sales in terms of avg, max, total sales
CREATE VIEW store_summary AS
SELECT Store,
       ROUND(SUM(Weekly_Sales),2) AS total_sales,
       ROUND(AVG(Weekly_Sales),2) AS avg_sales,
       ROUND(MAX(Weekly_Sales),2) AS max_weekly_sales
FROM walmart_staging
GROUP BY Store;

SELECT *
FROM store_summary;

SELECT DISTINCT YEAR(`Date`)
FROM walmart_staging;

-- Top 5 stores throughout years by total of weekly sales

WITH total_sales(store, years, sum_weekly_sales) AS
(
SELECT Store, YEAR(`Date`), SUM(Weekly_Sales)
FROM walmart_staging
GROUP BY Store, YEAR(`Date`)
),
store_rank AS
(
SELECT*,
DENSE_RANK() OVER(PARTITION BY years ORDER BY sum_weekly_sales DESC) AS store_ranking
FROM total_sales
)
SELECT *
FROM store_rank
WHERE store_ranking <=5;

