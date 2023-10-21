DROP PROCEDURE IF EXISTS  sp_increase_salaries;
CREATE PROCEDURE sp_increase_salaries(department_name VARCHAR)
AS
$$
	BEGIN
		UPDATE employees
		SET salary = salary + 0.05 * salary
		WHERE department_id = (
			SELECT department_id
			FROM departments
			WHERE departments.name = department_name);
	END
$$
LANGUAGE plpgsql;


-- Then we call the procedure and check the result:

--CALL sp_increase_salaries('Finance');
--SELECT
--	e.first_name AS first_name,
--	e.salary
--FROM
--	employees as e
--JOIN
--	departments as d
--USING
--	(department_id)
--WHERE
--	d.name = 'Finance'
--ORDER BY
--	e.first_name,
--	e.salary;