-- 1. Overall Mortality Rate

SELECT
    COUNT(*) AS total_patients,
    SUM(mortality_label) AS total_deaths,
    ROUND(SUM(mortality_label) * 100.0 / COUNT(*), 2) AS mortality_rate
FROM icu_mortality;


-- 2. Mortality by age group

SELECT
    CASE
        WHEN age BETWEEN 18 AND 29 THEN '18-29'
        WHEN age BETWEEN 30 AND 39 THEN '30-39'
        WHEN age BETWEEN 40 AND 49 THEN '40-49'
        WHEN age BETWEEN 50 AND 59 THEN '50-59'
        WHEN age BETWEEN 60 AND 69 THEN '60-69'
        ELSE '70+'
    END AS age_group,

    COUNT(*) AS patients,
    ROUND(AVG(mortality_label)*100,2) AS mortality_rate
FROM icu_mortality
GROUP BY age_group
ORDER BY age_group;


-- 3. Mortality by Ventilation Status

SELECT
    ventilation_required,
    COUNT(*) AS patients,
    ROUND(AVG(mortality_label)*100,2) AS mortality_rate
FROM icu_mortality
GROUP BY ventilation_required;


-- 4. Mortality by Sepsis

SELECT
    sepsis_flag,
    COUNT(*) AS patients,
    ROUND(AVG(mortality_label)*100,2) AS mortality_rate
FROM icu_mortality
GROUP BY sepsis_flag;


-- 5. Mortality by APACHE Score Bucket

SELECT
    CASE
        WHEN apache_score <= 10 THEN '0-10'
        WHEN apache_score <= 20 THEN '11-20'
        WHEN apache_score <= 30 THEN '21-30'
        ELSE '31-40'
    END AS apache_bucket,

    COUNT(*) AS patients,
    ROUND(AVG(mortality_label) * 100, 2) AS mortality_rate

FROM icu_mortality

GROUP BY
    CASE
        WHEN apache_score <= 10 THEN '0-10'
        WHEN apache_score <= 20 THEN '11-20'
        WHEN apache_score <= 30 THEN '21-30'
        ELSE '31-40'
    END

ORDER BY apache_bucket;

-- 7. Top Risk Profile

SELECT
    ventilation_required,
    sepsis_flag,
    COUNT(*) AS patients,
    ROUND(AVG(mortality_label)*100,2) AS mortality_rate
FROM icu_mortality
GROUP BY ventilation_required, sepsis_flag
ORDER BY mortality_rate DESC;


-- 8. Average clinical metrics by outcome

SELECT
    mortality_label,

    ROUND(AVG(apache_score),2) AS avg_apache,
    ROUND(AVG(sofa_score),2) AS avg_sofa,
    ROUND(AVG(lactate_mean),2) AS avg_lactate,
    ROUND(AVG(length_of_stay_days),2) AS avg_los

FROM icu_mortality
GROUP BY mortality_label;
