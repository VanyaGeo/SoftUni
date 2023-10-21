select
	a.town_id,
	t.name as town_name,
	a.address_text
from
	addresses as a
join
	towns as t
on
    t.town_id = a.town_id
where
	t.name = 'San Francisco' or t.name = 'Sofia' or t.name = 'Carnation'
order by
	town_id,
	address_id;


-- II

--SELECT
--	a.town_id,
--	t.name AS town_name,
--	a.address_text
--FROM
--	addresses AS a
--JOIN
--	towns AS t
--USING (town_id)
--WHERE
--	t.name IN ('San Francisco', 'Sofia', 'Carnation')
--ORDER BY
--	town_id,
--	address_id