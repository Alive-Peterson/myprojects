-- EDA - Exploratory Data Analysis

SELECT *
FROM layoffs_staging;

SELECT MAX(total_laid_off), MAX(percentage_laid_off)
FROM layoffs_staging
;

SELECT *
FROM layoffs_staging
WHERE percentage_laid_off = 1
ORDER BY funds_raised_millions DESC;

SELECT company, SUM(total_laid_off)
FROM layoffs_staging
GROUP BY company
ORDER BY 2 DESC
;

SELECT MIN(`date`), MAX(`date`)
FROM layoffs_staging;

SELECT industry, SUM(total_laid_off)
FROM layoffs_staging
GROUP BY industry
ORDER BY 2 DESC
;

SELECT country, SUM(total_laid_off)
FROM layoffs_staging
GROUP BY country
ORDER BY 2 DESC;

SELECT YEAR(`date`), SUM(total_laid_off)
FROM layoffs_staging
GROUP BY YEAR(`date`)
ORDER BY 1 DESC;

SELECT stage, SUM(total_laid_off)
FROM layoffs_staging
GROUP BY stage
ORDER BY 2 DESC;

SELECT SUBSTRING(`date`,1,7) AS `Year and Month`, SUM(total_laid_off)
FROM layoffs_staging
WHERE SUBSTRING(`date`,1,7) IS NOT NULL
GROUP BY `Year and Month`
ORDER BY 2 DESC
;

WITH CTE_OFF AS
(
SELECT SUBSTRING(`date`,1,7) AS `YEAR-MONTH`, SUM(total_laid_off) AS total_lof
FROM layoffs_staging
WHERE SUBSTRING(`date`,1,7) IS NOT NULL
GROUP BY `YEAR-MONTH`
ORDER BY 2 DESC
)
SELECT `YEAR-MONTH`, total_lof, SUM(total_lof) OVER(ORDER BY `YEAR-MONTH` ) AS Rolling_total
FROM CTE_OFF;


SELECT company, YEAR(`date`) as `YEAR`, SUM(total_laid_off)
FROM layoffs_staging
WHERE YEAR(`date`) IS NOT NULL
GROUP BY company, `YEAR`
HAVING SUM(total_laid_off) IS NOT NULL
ORDER BY 1 ASC
;


WITH 
company_year (company, years, sum_of_total_laid_off) AS
(
SELECT company, YEAR(`date`), SUM(total_laid_off)
FROM layoffs_staging
GROUP BY company,  YEAR(`date`)
) 
SELECT * ,
DENSE_RANK() OVER(PARTITION BY years ORDER BY sum_of_total_laid_off DESC) AS Ranking
FROM company_year
WHERE years IS NOT NULL
ORDER BY Ranking;


WITH 
company_year (company, years, sum_of_total_laid_off) AS
(
SELECT company, YEAR(`date`), SUM(total_laid_off)
FROM layoffs_staging
GROUP BY company,  YEAR(`date`)
),
company_year_rank AS
(
SELECT * ,
DENSE_RANK() OVER(PARTITION BY years ORDER BY sum_of_total_laid_off DESC) AS Ranking
FROM company_year
WHERE years IS NOT NULL
)
SELECT *
FROM company_year_rank
WHERE Ranking <= 5
;


WITH 
funds AS
(
SELECT company, YEAR(`date`) AS years, SUM(funds_raised_millions) AS total_funds
FROM layoffs_staging
GROUP BY company, years
ORDER BY years DESC
)
SELECT *
FROM funds
WHERE total_funds >= 20000
;
