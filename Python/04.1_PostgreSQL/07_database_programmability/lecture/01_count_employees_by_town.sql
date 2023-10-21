DROP FUNCTION IF EXISTS  fn_count_employees_by_town;
CREATE FUNCTION fn_count_employees_by_town(town_name VARCHAR)
RETURNS INT AS
$$
	DECLARE
		count_employees INT;
	BEGIN
		SELECT COUNT(*)
		FROM employees
		JOIN addresses ON addresses.address_id = employees.address_id
		JOIN towns ON towns.town_id = addresses.town_id
		WHERE towns.name = town_name
		INTO count_employees;
		RETURN count_employees;
	END
$$
LANGUAGE plpgsql;

--II

CREATE OR REPLACE FUNCTION fn_count_employees_by_town(town_name VARCHAR)
RETURNS INT AS
$$
	DECLARE
	BEGIN
	    RETURN(
            SELECT COUNT(*)
            FROM employees AS e
            JOIN addresses AS a
            USING (address_id)
            JOIN towns AS t
            USING (town_id)
            WHERE t.name = town_name;
	END
$$
LANGUAGE plpgsql;


--III

CREATE FUNCTION fn_count_employees_by_town(
    IN town_name VARCHAR,
    OUT count_employees INT)
 AS
$$
	BEGIN
		SELECT COUNT(*)
		FROM employees
		JOIN addresses ON addresses.address_id = employees.address_id
		JOIN towns ON towns.town_id = addresses.town_id
		WHERE towns.name = town_name
		INTO count_employees;
	END
$$
LANGUAGE plpgsql;