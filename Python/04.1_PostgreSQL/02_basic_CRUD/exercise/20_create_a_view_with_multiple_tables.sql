# I

CREATE VIEW view_addresses

AS SELECT
	CONCAT(e.first_name, ' ', e.last_name) AS "Full Name",
	e.department_id,
	CONCAT(a.number, ' ', a.street) AS "Address"
FROM employees AS e, addresses AS a

WHERE
	 e.address_id = a.id

ORDER BY "Address";


# II

CREATE VIEW view_addresses

AS SELECT
	CONCAT(e.first_name, ' ', e.last_name) AS "Full Name",
	e.department_id,
	CONCAT(a.number, ' ', a.street) AS "Address"
FROM employees AS e

JOIN
	 addresses AS a
	 ON e.address_id = a.id

ORDER BY "Address";