-- 1. Core KPI Queries

-- Total Patients
SELECT COUNT(*) AS total_patients
FROM er_data;

-- Average Wait Time
SELECT AVG(`Patient Waittime`) as avg_wait_time
FROM er_data;

-- Average of Satisfaction Score
SELECT AVG(`Patient Satisfaction Score`) as avg_satisfaction_score
FROM er_data;

-- Admission Status Count
SELECT `Patient Admission Flag`, COUNT(*) AS total_patients
FROM er_data
GROUP BY `Patient Admission Flag`;


-- 2. Business Analysis Queries

-- Most busy department

SELECT `Department Referral`, COUNT(*) AS total_patients
FROM er_data
GROUP BY `Department Referral`
ORDER BY total_patients DESC;

-- Gender distribution
SELECT `Patient Gender`, COUNT(*) AS total
FROM er_data
GROUP BY `Patient Gender`
;
-- Age Group Analysis
SELECT `Patient Age Group`, COUNT(*) AS total
FROM er_data
GROUP BY `Patient Age Group`
ORDER BY total DESC;

-- Wait Category Analysis
SELECT `Wait Category`, COUNT(*) AS total_patients
FROM er_data
GROUP BY `Wait Category`;


-- 3.Time based analysis

-- Peak Days
SELECT DAYNAME(`Patient Admission Date`) AS day_name,
COUNT(*) AS total_visits
FROM er_data
GROUP BY day_name
ORDER BY total_visits DESC
;

-- Monthly Trends
SELECT MONTHNAME(`Patient Admission Date`) AS month_name, COUNT(*) AS total_patients
FROM er_data
GROUP BY month_name
ORDER BY total_patients DESC
;

-- 4. Satisfaction Insights

SELECT `Wait Category`, AVG(`Patient Satisfaction Score`) AS avg_satisfaction
FROM er_data
GROUP BY `Wait Category`
;
