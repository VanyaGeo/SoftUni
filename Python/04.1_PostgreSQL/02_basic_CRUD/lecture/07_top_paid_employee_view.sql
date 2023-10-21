CREATE VIEW top_paid_employee_info AS
SELECT *
FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees);

SELECT * FROM top_paid_employee_info;