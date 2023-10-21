CREATE OR REPLACE FUNCTION fn_get_volunteers_count_from_department(
	IN searched_volunteers_department VARCHAR(30),
	OUT count_of_volunteers INT)
RETURNS INT
AS
$$
	BEGIN
		SELECT
			count(*)
		FROM
			volunteers AS v
		JOIN
			volunteers_departments AS vd
		ON
			v.department_id = vd.id
		WHERE
			vd.department_name = searched_volunteers_department
		INTO count_of_volunteers;
	END;
$$
LANGUAGE plpgsql;