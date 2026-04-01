# 🧠 Customer Lifetime Value (CLV) Prediction & Revenue Optimization

## 📌 Project Overview

This project builds an end-to-end **Customer Lifetime Value (CLV) prediction system** using machine learning and transforms insights into actionable business strategies.

The goal is to identify high-value customers, optimize marketing spend, and improve overall profitability through data-driven decision-making.

---

## 🎯 Objectives

* Predict customer lifetime value using historical transaction data
* Segment customers based on predicted value
* Analyze customer behavior (purchase frequency, spending patterns)
* Design targeted retention and marketing strategies
* Evaluate ROI of marketing efforts

---

## 📊 Dataset

* **Source:** Online Retail Dataset (UCI)
* Contains transactional data including:

  * Customer ID
  * Invoice details
  * Purchase quantity and price
  * Transaction dates

---

## ⚙️ Tech Stack

* **Languages:** Python
* **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
* **Visualization:** Tableau
* **Version Control:** Git

---

## 🧹 Data Processing

* Removed missing Customer IDs
* Filtered out returns and invalid transactions
* Converted date fields to datetime format
* Created `TotalPrice` feature

---

## 🧠 Feature Engineering

* RFM Features:

  * Recency
  * Frequency
  * Monetary Value
* Advanced Features:

  * Average Order Value
  * Purchase Frequency Rate
  * Customer Lifespan
  * Average Days Between Purchases

---

## 🤖 Model Building

* Implemented:

  * Linear Regression (baseline)
  * Random Forest Regressor (final model)
* Evaluation Metrics:

  * RMSE
  * R² Score
* Extracted feature importance to identify key drivers of CLV

---

## 📈 Key Insights

* Customer value is highly **right-skewed**, with a small segment contributing most revenue
* High CLV customers purchase frequently and spend significantly more
* Low CLV customers generate **negative ROI**
* Medium CLV customers present strong growth opportunities

---

## 🧩 Customer Segmentation

Customers were segmented into:

* High Value
* Medium Value
* Low Value

---

## 💡 Business Strategy

* **High CLV:** Retain through loyalty programs and exclusive offers
* **Medium CLV:** Upsell and increase engagement
* **Low CLV:** Minimize marketing spend and automate campaigns

---

## 💰 ROI Analysis

* High-value customers generate significant profit (~₹936 per user)
* Medium-value customers provide moderate returns
* Low-value customers result in losses (~₹55 per user)

👉 Recommendation: Reallocate marketing budget towards high and medium-value customers to maximize ROI.

---

## 📊 Dashboard

Built an interactive Tableau dashboard:

**Customer Lifetime Value & Revenue Optimization Dashboard**

### Key Components:

* KPI metrics (Total Customers, Avg CLV, Revenue, Profit)
* CLV distribution
* Segment-wise revenue & profit analysis
* Frequency vs CLV and Monetary vs CLV relationships
* Interactive filters

---

## 📂 Project Structure

```
customer_lifetime_value/
│
├── data/
├── notebooks/
├── dashboard/
├── README.md
```

---

## 🚀 Key Outcomes

* Developed a complete ML pipeline from raw data to business insights
* Identified high-value customer segments driving revenue
* Provided actionable strategies to improve marketing efficiency
* Demonstrated strong analytical and business problem-solving skills

---

## 📌 Future Improvements

* Use time-based split to predict **future CLV**
* Hyperparameter tuning for improved model performance
* Deploy model using Flask/FastAPI
* Integrate real-time data pipelines

---

## 👤 Author

GitHub: Alive-Peterson

---
