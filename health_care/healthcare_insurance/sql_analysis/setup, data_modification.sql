-- Database 
CREATE DATABASE healthcare_claims;
USE healthcare_claims;

-- checking column types
DESCRIBE claims;

-- Convert date columns
ALTER TABLE claims
MODIFY COLUMN `Date of Admission` DATE,
MODIFY COLUMN `Discharge Date` DATE;

-- Convert numeric columns
ALTER TABLE claims
MODIFY COLUMN `Billing Amount` DECIMAL(12,2),
MODIFY COLUMN `Reimbursement Amount` DECIMAL(12,2),
MODIFY COLUMN `Patient Payable` DECIMAL(12,2);

-- Convert integer columns
ALTER TABLE claims
MODIFY COLUMN `Length of Stay` INT,
MODIFY COLUMN `Age` INT,
MODIFY COLUMN `Room Number` INT;

-- Rename columns
ALTER TABLE claims
RENAME COLUMN `Name` TO patient_name,
RENAME COLUMN `Blood Type` TO blood_type,
RENAME COLUMN `Medical Condition` TO medical_condition,
RENAME COLUMN `Date of Admission` TO admission_date,
RENAME COLUMN `Insurance Provider` TO insurance_provider,
RENAME COLUMN `Billing Amount` TO billing_amount,
RENAME COLUMN `Room Number` TO room_number,
RENAME COLUMN `Admission Type` TO admission_type,
RENAME COLUMN `Discharge Date` TO discharge_date,
RENAME COLUMN `Test Results` TO test_results,
RENAME COLUMN `Claim ID` TO claim_id,
RENAME COLUMN `Length of Stay` TO length_of_stay,
RENAME COLUMN `Age Group` TO age_group,
RENAME COLUMN `Cost Category` TO cost_category,
RENAME COLUMN `Claim Status` TO claim_status,
RENAME COLUMN `Reimbursement Amount` TO reimbursement_amount,
RENAME COLUMN `Patient Payable` TO patient_payable;