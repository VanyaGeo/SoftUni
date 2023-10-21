SELECT
    CONCAT(c.first_name, ' ', c.last_name) AS coach_full_name,
    CONCAT(p.first_name, ' ', p.last_name) AS player_full_name,
    t.name AS team_name,
    ps.passing,
    ps.shooting,
    ps.speed
FROM
	coaches AS c
JOIN
	players_coaches AS pc
ON
	c.id = pc.coach_id
JOIN
	players AS p
ON
	pc.player_id = p.id
JOIN
	skills_data AS ps
ON
	p.skills_data_id = ps.id
JOIN
	teams AS t
ON
	p.team_id = t.id
ORDER BY
	coach_full_name ASC,
	player_full_name DESC;