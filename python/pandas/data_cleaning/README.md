# 🧹 Data Cleaning in Pandas — Customer Call List

This project demonstrates a complete **data cleaning workflow using Pandas** on a raw **customer call list dataset**.  
The goal is to transform messy, inconsistent data into a clean, structured format ready for analysis or business use.

---

## 📊 Project Overview

The notebook (`Data_Cleaning_in_Pandas.ipynb`) focuses on:
- Cleaning missing and inconsistent values  
- Formatting phone numbers and names  
- Standardizing categorical fields  
- Removing duplicates  
- Exporting a clean dataset for further analysis  

---

## 🗂️ Dataset

### Input File  
**`customer_call_list.xlsx`**  
A raw dataset containing customer information such as:
- Names  
- Phone numbers  
- Email addresses  
- Call status  
- Contact preferences  

### Output File  
**`cleaned_sample.csv`**  
The cleaned and structured dataset produced after processing.

---

## 🧠 Data Cleaning Steps Performed

### 1. Data Loading & Inspection
- Loaded Excel file into Pandas  
- Checked shape, column names, and data types  
- Displayed initial rows  

### 2. Handling Missing Values
- Filled or removed null values  
- Standardized empty fields  

### 3. Removing Duplicates
- Identified duplicate records  
- Dropped duplicate rows  

### 4. Cleaning Text Fields
- Trimmed extra spaces  
- Converted names to proper case  
- Standardized categorical values (e.g., Yes/No, Call Status)  

### 5. Phone Number Formatting
- Removed non-numeric characters  
- Standardized phone numbers into a consistent format  

### 6. Column Cleanup
- Renamed columns for clarity  
- Dropped unnecessary columns  

### 7. Exporting Clean Data
- Saved the cleaned dataset as `cleaned_sample.csv`

---

## 📈 Key Outcomes

- Transformed messy customer data into a clean and consistent format  
- Standardized phone numbers and text fields  
- Removed duplicates and irrelevant records  
- Created a ready-to-use dataset for reporting or analytics  

---

## ⚙️ Tools Used

| Tool | Purpose |
|------|--------|
| Python | Data processing |
| Pandas | Data manipulation |
| Jupyter Notebook | Interactive workflow |
| Excel | Raw data source |

---

## 🚀 How to Run

1. Clone this repository  
2. Install required packages:
   ```bash
   pip install pandas openpyxl
   ```
3. Open the notebook:
   ``` bash
   Data_Cleaning_in_Pandas.ipynb
   ```
4. Run all cells to reproduce the cleaning process

## 📁 Project Files
Data_Cleaning_in_Pandas.ipynb   
customer_call_list.xlsx        
cleaned_sample.csv             
README.md                      

## 👤 Author
Alive Peterson
🔗 GitHub: @Alive-Peterson

## 🪪 License
This project is open-source and free to use for learning and portfolio purposes.