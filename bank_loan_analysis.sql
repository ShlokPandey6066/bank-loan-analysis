CREATE DATABASE bank_loan_analysis;
SHOW DATABASES;
USE bank_loan_analysis;

SHOW DATABASES;

select *
from loan_prediction_dataset;

SELECT COUNT(*) AS Total_Applications
FROM loan_prediction_dataset;

SELECT
loan_approved, count(*) AS total
from loan_prediction_dataset
group by loan_approved;

SELECT Employment_status,
count(*) as total_employees
from loan_prediction_dataset
group by Employment_status;

SELECT 
Employment_status, Loan_Approved, count(*) as total
from loan_prediction_dataset
group by employment_status, loan_approved
ORDER BY Loan_approved DESC;

SELECT 
ROUND(AVG(Income)) AS avg_income
from loan_prediction_dataset;

SELECT 
ROUND(AVG(credit_score)), loan_approved
from loan_prediction_dataset
group by loan_approved;

select *
from loan_prediction_dataset
where loan_approved=1;

select count(*) as high_applicant
from loan_prediction_dataset
where credit_score>350;

select count(*) as applicants
from loan_prediction_dataset
where credit_score>350 and loan_approved=1;

