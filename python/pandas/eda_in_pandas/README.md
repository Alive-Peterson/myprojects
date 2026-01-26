# 🌍 Exploratory Data Analysis (EDA) in Pandas — World Population

This project performs **Exploratory Data Analysis (EDA)** on a global **world population dataset** using **Python and Pandas**.  
The goal is to understand population trends, distributions, and country-level comparisons through structured analysis and visual exploration.

---

## 📊 Project Overview

The notebook (`EDA_in_pandas.ipynb`) explores world population data to:
- Analyze population growth across countries and years  
- Identify the most and least populated countries  
- Compare regional population patterns  
- Understand overall population distribution  

---

## 🗂️ Dataset

**File:** `world_population.csv`  

**Key Columns:**
- `Country/Territory` – Country name  
- `Continent` – Continent name  
- `2022 Population`, `2020 Population`, `2015 Population`, etc.  
- `World Population Percentage`  
- `Area (km²)`  
- `Density (per km²)`  

---

## 🧠 EDA Steps Performed

### 1. Data Loading & Inspection
- Loaded CSV file into Pandas  
- Checked shape, column names, and data types  
- Viewed sample rows  

### 2. Data Cleaning
- Handled missing values (if any)  
- Standardized column names  
- Removed or corrected inconsistent entries  

### 3. Descriptive Statistics
- Calculated mean, median, min, max, and standard deviation  
- Analyzed population distributions  

### 4. Country-Level Analysis
- Top 10 most populated countries  
- Least populated countries  
- Population density comparisons  

### 5. Trend Analysis
- Compared population across multiple years  
- Observed growth patterns  

### 6. Visualization
- Bar charts for population by country  
- Line plots for population growth  
- Distribution plots for density and population  

---

## 📈 Key Insights

- Countries like **China** and **India** dominate global population share  
- Population growth varies significantly across continents  
- High population density is concentrated in a few small countries  
- Steady population growth observed in developing regions  

---

## ⚙️ Tools Used

| Tool | Purpose |
|------|--------|
| Python | Data analysis |
| Pandas | Data manipulation |
| Matplotlib / Seaborn | Data visualization |
| Jupyter Notebook | Interactive analysis |

---

## 🚀 How to Run

1. Clone this repository  
2. Install required packages:
   ```bash
   pip install pandas matplotlib seaborn
   ```
3. Open the notebook:
```bash
   EDA_in_pandas.ipynb
```
4. Run all cells to reproduce the analysis

## 📁 Project Files
 EDA_in_pandas.ipynb     
 world_population.csv  
 README.md              

## 👤 Author
Alive Peterson
🔗 GitHub: @Alive-Peterson

## 🪪 License
This project is open-source and free to use for learning and portfolio purposes.