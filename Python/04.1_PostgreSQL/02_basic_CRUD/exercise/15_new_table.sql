CREATE TABLE company_chart
AS SELECT
	CONCAT(first_namE, ' ', last_name) AS "Full Name",
	job_title AS "Job Title",
	department_id AS "Department ID",
	manager_id AS "Manager ID"
FROM employees;
