-- Data Cleaning in MySQL

-- 1.Remove duplicates
-- 2.Handle NULLs/ Blank Values
-- 3.Fix data types	- fixing or converting data types
-- 4.Clean text	- removing unnecesary spaces, making proper capitalization for text
-- 5.Standardize formats - Time and Date format
-- 6.Drop Noise - Remove any unnecessary rows or columns
-- (optional)
-- 7.Logical checks - Verify that related columns make sense together like total sales or profit
-- 8.Fix outliers - Detect and remove unrealistic or invalid values (like negative amounts).


-- Creating a staging table 
CREATE TABLE layoffs_staging AS
SELECT * FROM layoffs;

-- alternate way to create a staging table
CREATE TABLE layoffs_staging
LIKE layoffs;

INSERT INTO layoffs_staging 
SELECT*
FROM layoffs;


SELECT *
FROM layoffs_staging;

-- removing duplicates
SELECT *
FROM (
  SELECT *,
    ROW_NUMBER() OVER(
      PARTITION BY company, location, industry, total_laid_off,
                   percentage_laid_off, `date`, stage, country, funds_raised_millions
    ) AS row_num
  FROM layoffs_staging
) AS temp
WHERE row_num > 1;



WITH duplicate_cte AS
(
SELECT *,
ROW_NUMBER() OVER(PARTITION BY company, location, industry, total_laid_off, percentage_laid_off, `date`, stage, country, funds_raised_millions) AS row_num
FROM layoffs_staging
)
DELETE
FROM duplicate_cte
WHERE row_num >1;

-- CTE can't directly delete the rows so we use unique row_id in CTE and we address "FROM layoffs_staging" not from duplicate_cte. 
-- The PARTITION BY defines which columns determine a duplicate group.
-- ORDER BY row_id decides which row becomes row_num = 1 (the one you keep). Because row_id is unique and monotonic, ordering is deterministic.
-- You delete only rows with specific row_id values — no accidental deletion of the remaining row.
-- you shouldn’t remove ORDER BY row_id inside the ROW_NUMBER() function — because without it, 
-- MySQL won’t know which duplicate row to keep and sometimes it may even throw an error depending on the version.


ALTER TABLE layoffs_staging
ADD COLUMN row_id INT AUTO_INCREMENT PRIMARY KEY;

WITH duplicate_cte AS (
  SELECT *,
         ROW_NUMBER() OVER (
           PARTITION BY company, location, industry, total_laid_off,
                        percentage_laid_off, `date`, stage, country, funds_raised_millions
           ORDER BY row_id
         ) AS row_num
  FROM layoffs_staging
)
DELETE FROM layoffs_staging
WHERE row_id IN (
  SELECT row_id FROM duplicate_cte WHERE row_num > 1
);

ALTER TABLE layoffs_staging
DROP COLUMN row_id;


-- Standardize data
SELECT company, TRIM(company)
FROM layoffs_staging
ORDER BY 1;

UPDATE layoffs_staging
SET company = TRIM(company);

SELECT distinct(industry)
FROM layoffs_staging
ORDER BY 1;

SELECT *
FROM layoffs_staging
WHERE industry LIKE 'Crypto%';


UPDATE layoffs_staging
SET industry = 'Crypto'
WHERE industry LIKE 'Crypto%';


SELECT DISTINCT country
FROM layoffs_staging
ORDER BY 1
;

SELECT DISTINCT country, TRIM(TRAILING '.' FROM country)
FROM layoffs_staging
ORDER BY 1
;

UPDATE layoffs_staging
SET country = TRIM(TRAILING '.' FROM country)
WHERE country LIKE 'United States%';

-- date format

SELECT `date`
FROM layoffs_staging;

UPDATE layoffs_staging
SET `date` = STR_TO_DATE(`date`,'%m/%d/%Y');

ALTER TABLE layoffs_staging
MODIFY COLUMN `date` DATE;

-- Dealing with NULL and Blank Values

UPDATE layoffs_staging
SET industry = NULL 
WHERE industry = '';

SELECT t1.industry,t2.industry
FROM layoffs_staging t1
JOIN layoffs_staging t2
    ON t1.company = t2.company
WHERE t1.industry IS NULL 
AND t2.industry IS NOT NULL;

UPDATE layoffs_staging t1
JOIN layoffs_staging t2
    ON t1.company = t2.company
SET t1.industry = t2.industry
WHERE t1.industry IS NULL
AND t2.industry IS NOT NULL; 

SELECT *
FROM layoffs_staging
WHERE total_laid_off IS NULL
AND percentage_laid_off IS NULL;

DELETE
FROM layoffs_staging
WHERE total_laid_off IS NULL
AND percentage_laid_off IS NULL;
