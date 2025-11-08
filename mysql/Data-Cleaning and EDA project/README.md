# 🧹 Data Cleaning and Exploratory Data Analysis (EDA) on Layoffs Dataset using MySQL
## 📘 Project Overview

This project involves cleaning, preprocessing, and analyzing a real-world layoffs dataset using MySQL.
It showcases SQL-based data cleaning best practices and exploratory data analysis (EDA) to extract meaningful business insights about layoffs across industries, companies, and time periods.

## 🧾 Dataset Information

File: layoffs.csv

Source: Kaggle / Public Layoffs Dataset

Contents:


company	                Name of the company
location	            City/Region of operation
industry	            Industry sector
total_laid_off	        Number of employees laid off
percentage_laid_off	    Layoff percentage
date	                Date of the event
stage	                Funding stage or company maturity
country	                Country where layoffs occurred
funds_raised_millions	Total funds raised by the company


## 🧠 Objectives

Clean the raw dataset to handle missing, duplicate, and inconsistent data.

Standardize data formats (especially dates and text fields).

Perform EDA to identify layoff patterns by company, country, industry, and year.

Extract insights using SQL aggregation and ranking functions.

## 🧰 Tools & Technologies

Database: MySQL

Language: SQL

Data Source: CSV (imported into MySQL Workbench)

Techniques Used: Window Functions, CTEs, Data Cleaning Queries, Aggregations

## 🧼 Data Cleaning Steps (from Data_cleaning.sql)

Create a staging table to preserve raw data (layoffs_staging).

Remove duplicates using ROW_NUMBER() with PARTITION BY.

Trim and standardize text (TRIM(), LIKE, and proper capitalization).

Fix inconsistent values (e.g., Crypto% → Crypto, remove trailing dots in country).

Convert data types (converted date string to DATE type).

Handle NULL and blank values — filled industries by self-join and deleted invalid rows.

Dropped unnecessary columns once cleaning was done.


## 📈 Insights & Key Findings

Tech sector (especially startups) experienced the highest layoffs.

United States led layoffs by volume.

Layoffs peaked between 2022–2023, coinciding with global market corrections.

Companies with higher funding still conducted large layoffs, showing funding ≠ stability.

Rolling totals reveal consistent quarterly layoff increases before stabilization.

## 🧩 Files Included

1. Data_cleaning.sql	- SQL scripts for full data cleaning process
2. EDA.sql	            - SQL queries for exploration and insights
3. layoffs.csv	        - Raw dataset used for analysis


## 🧑‍💻 How to Use

Import layoffs.csv into MySQL.

Run the Data_cleaning.sql script step by step.

Then execute queries in EDA.sql to perform the analysis.

Optionally, visualize the results in Tableau or Power BI.

## 🧩 Author

Developed by **Alive Peterson**<br>
🔗 GitHub: [Alive-Peterson](https://github.com/Alive-Peterson)<br>
📧 Email: [alivepeterson2@gmail.com](mailto:alivepeterson2@gmail.com)