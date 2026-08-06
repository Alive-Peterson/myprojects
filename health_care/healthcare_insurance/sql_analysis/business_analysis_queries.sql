-- 1. Monthly Claim Trend (Time Series)
SELECT 
       DATE_FORMAT(admission_date, '%Y-%m') AS claim_month, 
       COUNT(*) AS total_claims, 
       ROUND(SUM(billing_amount), 2) AS total_billing 
FROM claims 
GROUP BY claim_month 
ORDER BY claim_month;


-- 2. Insurance Provider Market Share
SELECT
    insurance_provider,
    COUNT(*) AS claims,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM claims), 2) AS market_share_pct
FROM claims
GROUP BY insurance_provider
ORDER BY claims DESC;

-- 3. Denial Rate by Insurance Provider
SELECT
      insurance_provider,
      COUNT(*) AS total_claims,
      SUM(CASE WHEN claim_status = 'Denied' THEN 1 ELSE 0 END) AS denied_claims,
      ROUND(SUM(CASE WHEN claim_status = 'Denied' THEN 1 ELSE 0 END)*100/COUNT(*),2) AS denied_rate_pct
FROM claims
GROUP BY insurance_provider
ORDER BY denied_rate_pct DESC;


-- 4. Hospitals with Above-Average Denial Rate
WITH hospital_denials AS (
      SELECT
         hospital,
		 ROUND(SUM(CASE WHEN claim_status='Denied' THEN 1 ELSE 0 END)*100/COUNT(*),2) AS denial_rate
	  FROM claims
      GROUP BY Hospital
      )
      SELECT *
      FROM hospital_denials
      WHERE denial_rate > (SELECT AVG(denial_rate) FROM hospital_denials)
      ORDER BY denial_rate DESC
      LIMIT 20;
      
      
-- 5. Average Reimbursement percentage
SELECT 
	  insurance_provider,
	  ROUND(AVG(reimbursement_amount/billing_amount*100),2) AS reimbursement_pct
FROM claims
WHERE billing_amount > 0 
GROUP BY insurance_provider 
ORDER BY reimbursement_pct DESC;


-- 6. Cost per Day by Medical Condition
SELECT 
      medical_condition, 
      ROUND(SUM(billing_amount) / SUM(length_of_stay), 2) AS cost_per_day 
FROM claims 
GROUP BY medical_condition 
ORDER BY cost_per_day DESC;


-- 7. Readmission Suspicion
SELECT 
	  patient_name, 
      COUNT(*) AS admissions, 
      MIN(admission_date) AS first_admission, 
      MAX(admission_date) AS last_admission 
FROM claims 
GROUP BY patient_name HAVING admissions >= 3 
ORDER BY admissions DESC LIMIT 20;


-- 8. Top 5 Doctors by Revenue
SELECT 
      doctor,
      COUNT(*) AS patients,
      ROUND(SUM(billing_amount),2) AS revenue_generated
FROM claims
GROUP BY doctor
ORDER BY revenue_generated DESC
LIMIT 5;

-- 9. Ranking Hospitals Within Each Insurance Provider (Window Function)

SELECT *
FROM (
    SELECT
        insurance_provider,
        hospital,
        ROUND(SUM(billing_amount), 2) AS total_billing,
        RANK() OVER (
            PARTITION BY insurance_provider
            ORDER BY SUM(billing_amount) DESC
        ) AS provider_rank
    FROM claims
    GROUP BY insurance_provider, hospital
) ranked
WHERE provider_rank <= 3;



-- 10. High-Risk Financial Claims

SELECT
    claim_id,
    hospital,
    medical_condition,
    billing_amount,
    reimbursement_amount,
    patient_payable,
    ROUND(patient_payable / billing_amount * 100, 2) AS patient_burden_pct
FROM claims
WHERE patient_payable / billing_amount > 0.5
ORDER BY patient_burden_pct DESC, billing_amount DESC
LIMIT 20;