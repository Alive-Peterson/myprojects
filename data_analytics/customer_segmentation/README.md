# 🛍️ Customer Segmentation Project  
## RFM Analysis | Cohort Analysis | K-Means Clustering

This project performs advanced **customer segmentation** using transactional retail data.  
It combines **RFM Analysis**, **Cohort Analysis**, and **K-Means Clustering** to identify customer behavior patterns and actionable business insights.

---

##  Project Overview

The objective of this project is to:
- Segment customers based on purchasing behavior  
- Identify high-value and at-risk customers  
- Analyze customer retention over time  
- Apply machine learning clustering for behavioral grouping  

The analysis is performed in **Python using Pandas, NumPy, Matplotlib, Seaborn, and Scikit-learn**.

---

## 🗂️ Dataset

**File:** `OnlineRetail.csv`  

This dataset contains online retail transactions with the following key columns:

| Column | Description |
|---------|-------------|
| InvoiceNo | Unique transaction ID |
| StockCode | Product code |
| Description | Product name |
| Quantity | Number of products purchased |
| InvoiceDate | Transaction date |
| UnitPrice | Price per unit |
| CustomerID | Unique customer ID |
| Country | Customer’s country |

---

## 🧹 Data Preprocessing

- Removed cancelled transactions  
- Removed negative quantities and invalid prices  
- Handled missing `CustomerID` values  
- Converted `InvoiceDate` to datetime format  
- Created `TotalPrice = Quantity × UnitPrice`  

---

## 1. RFM Analysis

RFM stands for:

- **Recency (R)** – How recently a customer made a purchase  
- **Frequency (F)** – How often a customer purchases  
- **Monetary (M)** – How much money the customer spends  

### Steps Performed:
1. Calculated Recency, Frequency, and Monetary values for each customer  
2. Used `pd.qcut()` to assign RFM scores (1–4 scale)  
3. Created combined RFM segments  
4. Categorized customers into groups like:
   - Champions  
   - Loyal Customers  
   - At Risk  
   - Lost Customers  

### Key Insight:
A small percentage of customers contribute a large share of total revenue.

---

## 2. Cohort Analysis

Cohort analysis was used to measure **customer retention over time**.

### Steps Performed:
1. Extracted customer’s first purchase month  
2. Created Cohort Groups based on first purchase month  
3. Calculated monthly retention rates  
4. Built a retention heatmap  

### Key Insight:
Retention decreases significantly after the first few months, highlighting opportunities for customer engagement strategies.

---

##  3. K-Means Clustering

To enhance segmentation, **K-Means Clustering** was applied.

### Steps Performed:
1. Scaled RFM features using StandardScaler  
2. Used the Elbow Method to determine optimal K  
3. Applied K-Means clustering  
4. Analyzed cluster characteristics  

### Result:
Customers were grouped into behavioral clusters such as:
- High-value frequent buyers  
- Medium regular customers  
- Low-frequency low-spend customers  

---

### 📊 Visualizations Included

- Distribution plots for RFM variables  
- RFM segment bar charts  
- Cohort retention heatmap  
- Elbow curve for K selection  
- Cluster comparison plots  


### ⚙️ Tools & Technologies

 Python - as Programming language 
 Pandas - for Data manipulation 
 Matplotlib & Seaborn - for Data visualization 
 Scikit-learn - for K-Means clustering 
 Jupyter Notebook - for Interactive analysis 

### 🚀 How to Run

1. Clone this repository  
2. Install required libraries:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
   ```
3. Open:
   ```bash
   jupyter notebook customer_segmentation.ipynb
   ```
4. Run all cells to reproduce analysis 

### 📁 Project Files
```bash
   customer_segmentation.ipynb   # Main analysis notebook
   OnlineRetail.csv              # Dataset
   README.md                     # Project documentation
```

### Business Value

Enables targeted marketing campaigns

Identifies high-value customers

Improves retention strategy

Supports personalized recommendation systems

### Author

Alive Peterson
GitHub: @Alive-Peterson

### License

This project is open-source and intended for educational and portfolio purposes.