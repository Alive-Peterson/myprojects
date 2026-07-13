-- 1. Highest Average bed Utilization
SELECT service, ROUND(AVG(bed_utilization_pct),2) AS avg_bed_utilization
FROM services
GROUP BY service
ORDER BY avg_bed_utilization DESC;

-- 2. Highest Refusal Rate
SELECT service, ROUND(AVG(refusal_rate_pct),2) AS avg_refusal_rate
FROM services
GROUP BY service
ORDER BY avg_refusal_rate DESC;

-- 3. Highest Demand Pressure
SELECT service, ROUND(AVG(demand_pressure),2) AS avg_demand_pressure
FROM services
GROUP BY service
ORDER BY avg_demand_pressure DESC;

-- 4. Rank services by operational efficiency
SELECT service,
    ROUND(AVG(admission_rate_pct),2) AS avg_admission_rate,
    DENSE_RANK() OVER(ORDER BY AVG(admission_rate_pct) DESC) AS efficiency_rank
FROM services
GROUP BY service;

-- 5. Highest Patient Demand
SELECT week, SUM(patients_request) AS total_requests
FROM services
GROUP BY week
ORDER BY total_requests DESC
LIMIT 5;

-- 6. Running Total of Patient Requests
SELECT week,
    SUM(patients_request) AS weekly_requests,
    SUM(SUM(patients_request)) OVER (ORDER BY week) AS running_total_requests
FROM services
GROUP BY week
ORDER BY week;

-- 7. 4-Week Moving Average of Admissions
SELECT week,
    SUM(patients_admitted) AS weekly_admissions,
    ROUND(
        AVG(SUM(patients_admitted)) OVER (
            ORDER BY week
            ROWS BETWEEN 3 PRECEDING AND CURRENT ROW),2) AS moving_avg_admissions
FROM services
GROUP BY week
ORDER BY week;

-- 8. longest average patient stay
SELECT service,
    ROUND(AVG(length_of_stay),2) AS avg_length_of_stay
FROM patients
GROUP BY service
ORDER BY avg_length_of_stay DESC;

-- 9. longest average hospital stay
SELECT age_group,
    ROUND(AVG(length_of_stay),2) AS avg_length_of_stay
FROM patients
GROUP BY age_group
ORDER BY avg_length_of_stay DESC;

-- 10. Monthly Admission Trend
SELECT admission_month,
    COUNT(*) AS total_admissions
FROM patients
GROUP BY admission_month
ORDER BY STR_TO_DATE(admission_month,'%M');

-- 11. Staff Attendance Rate by Service
SELECT service,
    ROUND(AVG(present) * 100,2) AS attendance_rate
FROM staff_schedule
GROUP BY service
ORDER BY attendance_rate DESC;

-- 12. Impact of Hospital Events
SELECT
    event,
    ROUND(AVG(patients_request),2) AS avg_requests,
    ROUND(AVG(patients_admitted),2) AS avg_admissions,
    ROUND(AVG(patients_refused),2) AS avg_refusals,
    ROUND(AVG(patient_satisfaction),2) AS avg_patient_satisfaction,
    ROUND(AVG(staff_morale),2) AS avg_staff_morale
FROM services
GROUP BY event
ORDER BY avg_requests DESC;

-- 13. Services Operating Above Average Bed Utilization (CTE)
WITH avg_utilization AS (
    SELECT AVG(bed_utilization_pct) AS hospital_avg
    FROM services
)

SELECT
    s.service,
    ROUND(AVG(s.bed_utilization_pct),2) AS service_utilization
FROM services s
CROSS JOIN avg_utilization a
GROUP BY s.service, a.hospital_avg
HAVING AVG(s.bed_utilization_pct) > a.hospital_avg
ORDER BY service_utilization DESC;