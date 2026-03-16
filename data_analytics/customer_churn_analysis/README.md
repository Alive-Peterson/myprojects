# Customer Churn Analysis & Dashboard

This project analyzes **customer churn behavior in a telecom company** using Python for data analysis and **Power BI for interactive dashboards**.  
The objective is to understand **why customers leave**, identify **high-risk segments**, and provide insights that can help businesses **reduce churn and improve retention**.

---

## Project Overview

Customer churn is a critical challenge for subscription-based businesses.  
In this project, we analyze telecom customer data to:

- Identify churn patterns
- Understand financial risk due to churn
- Segment customers based on behavior
- Discover the key drivers behind customer churn

The analysis is performed in **Python (Pandas, visualization libraries)** and the results are visualized using **Power BI dashboards**.

---

## Project Structure
Customer_churn_analysis/
│
├── notebooks/
│ ├── Customer_churn.ipynb # Exploratory Data Analysis and churn insights
│ ├── dashboard_dataset_prep.ipynb # Data preparation for Power BI dashboards
│
├── data/
│ ├── Telco_customer_churn.csv # Original dataset
│ ├── churn_dashboard_data.csv # Processed dataset used for dashboards
│
├── dashboards/
│ ├── Executive_Overview.pbix
│ ├── Financial_Risk.pbix
│ ├── Customer_Segmentation.pbix
│ ├── Churn_Reasons.pbix
│
└── README.md


---

## Data Preparation

The dataset was cleaned and transformed using Python:

### Steps Performed
- Removed or handled missing values
- Converted data types (e.g., TotalCharges)
- Encoded categorical variables
- Created additional features for analysis
- Prepared aggregated datasets for Power BI dashboards

Tools used:
- **Pandas**
- **NumPy**
- **Jupyter Notebook**

---

## Exploratory Data Analysis (EDA)

The EDA notebook explores key churn patterns such as:

- Churn rate across different **contract types**
- Impact of **monthly charges and total charges**
- Relationship between **tenure and churn**
- Churn distribution across **internet services and payment methods**

Key insight:
Customers with **month-to-month contracts and higher monthly charges** show significantly higher churn rates.

---

## Power BI Dashboards

The project includes **four interactive dashboards** built in Power BI.

---

### 1. Executive Overview Dashboard

Purpose: Provide a high-level business summary.

Key Metrics:
- Total Customers
- Total Churned Customers
- Churn Rate
- Average Monthly Charges
- Customer distribution by contract type

Insights:
- Quick snapshot of overall churn health
- Identification of high-risk customer groups

---

### 2. Financial Risk Dashboard

Purpose: Analyze **revenue impact caused by customer churn**.

Key Metrics:
- Revenue lost due to churn
- Average revenue per customer
- Churned revenue by customer segment
- Monthly charge comparison

Insights:
- Helps quantify **financial losses caused by churn**
- Identifies high-value customers leaving the service

---

### 3. Customer Segmentation Dashboard

Purpose: Segment customers based on attributes such as:

- Contract type
- Tenure
- Services used
- Payment methods

Insights:
- Identifies **loyal vs high-risk customer segments**
- Helps marketing teams target retention campaigns

---

### 4. Churn Reasons / Customer Churn Drivers

Purpose: Identify the **key factors driving churn**.

Key Drivers Analyzed:
- Contract type
- Monthly charges
- Internet service type
- Customer tenure
- Payment method

Insights:
- Month-to-month contracts are strongly linked with churn
- Higher monthly charges increase churn likelihood
- Short-tenure customers churn more frequently

---

## 📈 Key Business Insights

- **Month-to-month contracts** show the highest churn rate
- Customers with **higher monthly charges** are more likely to leave
- **Short-tenure customers** are at higher churn risk
- Certain **internet service types and payment methods** correlate with higher churn

---

## ⚙️ Tools & Technologies

 Python               - Data analysis 
 Pandas               - Data manipulation 
 NumPy                - Numerical operations 
 Matplotlib / Seaborn - Data visualization 
 Jupyter Notebook     - Analysis environment 
 Power BI             - Interactive dashboards 

---

## Business Value

This project helps organizations:

- Detect customers at high risk of churn
- Understand the financial impact of churn
- Improve customer retention strategies
- Create targeted marketing campaigns

---

## Author

**Alive Peterson**

GitHub: https://github.com/Alive-Peterson

---

## 🪪 License

This project is open-source and available for educational and portfolio purposes.