# 🛒 Walmart Sales Analysis — SQL + Power BI Dashboard

This project combines SQL-based data analysis and Power BI visualization to explore Walmart’s sales performance across multiple stores and time periods. The aim is to uncover trends, compare store-level performance, and understand the influence of external factors such as temperature, fuel price, holidays, and unemployment rate on weekly sales.

## 📁 Project Components

walmart_sales_analysis.sql – SQL queries for data analysis, aggregation, and trend exploration.

walmart_sales_dashboard.pbix – Interactive Power BI dashboard that visualizes insights derived from SQL outputs.

Dataset – Walmart weekly sales dataset containing information such as store numbers, weekly sales, temperature, fuel prices, CPI, and unemployment rates.

## 🧾 Dataset Description
**Column**	       **Description**

Store	          - Store ID number
Date	          - Week ending date
Weekly_Sales	  - Total sales for that week
Holiday_Flag	  - 1 if the week includes a major holiday, else 0
Temperature	      - Average temperature for the week
Fuel_Price	      - Cost of fuel in the area
CPI	              - Consumer Price Index
Unemployment	  - Unemployment rate of the region

## 🧠 SQL Analysis Performed
1. Basic Analysis

Fetched minimum and maximum dates to determine the analysis range.

Calculated total, average, and maximum weekly sales across all stores.

Identified top-performing stores and lowest weekly sales.

2. Sales Trend Analysis

Analyzed monthly sales patterns to observe seasonal fluctuations.

Calculated yearly sales summaries (2010–2012).

3. Holiday Impact

Compared average sales between holiday and non-holiday weeks.

Found that holidays tend to slightly increase sales performance.

4. External Factors

Temperature: Grouped into Cold, Moderate, and Hot to check its influence on sales.

Fuel Price: Classified as Low, Medium, or High to study sales impact.

Unemployment: Examined correlation between sales and unemployment rate.

5. Store-Level Analysis

Created a SQL View (store_summary) summarizing each store’s total, average, and max weekly sales.

Generated Top 5 Stores per year using CTEs and DENSE_RANK() for ranking.

## 📊 Power BI Dashboard Highlights

The SQL insights were visualized in Power BI, providing a clear, interactive overview:

Key Metrics

🧾 Total Sales: 6.74 Billion

🏬 Store Count: 45

💰 Average Sales: 1.05 Million

📈 Highest Weekly Sale: 3.82 Million

Dashboard Visuals

Top 5 Stores by Total Sales (per year) – Ranked store performance.

Sales Trend Over Time – Monthly sales progression (2010–2012).

Holiday vs Non-Holiday Sales – Donut chart comparison.

Average Sales by Temperature/Fuel Price/CPI – Bubble chart showing environmental effects.

Interactive Year Filter – Filter all visuals by year.

## ⚙️ Tools Used

MySQL – Data cleaning, aggregation, and analysis

Power BI – Interactive data visualization

Excel/CSV – Data source preprocessing

### 🚀 Steps to Reproduce

Run the SQL scripts (walmart_sales_analysis.sql) in MySQL Workbench or any SQL client.

Export key tables or query results as .csv files.

Load them into Power BI.

Build visuals using DAX measures and filters (as shown in walmart_sales_dashboard.pbix).

### 📚 Insights Gained

Sales are highest during mid-year months (June–August).

Non-holiday weeks dominate total sales but holiday weeks show higher per-week averages.

Stores 20, 4, 14, 13, and 2 are consistently top performers.

Sales remain stable despite changes in fuel prices and CPI, showing consistent demand.

Moderate temperatures (40°F–70°F) correlate with higher sales.

## 👤 Author

**Alive Peterson**<br>
🔗 GitHub: [Alive-Peterson](https://github.com/Alive-Peterson)<br>
📧 Email: [alivepeterson2@gmail.com](mailto:alivepeterson2@gmail.com)<br>