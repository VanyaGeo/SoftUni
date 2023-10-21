SELECT
	magic_wand_creator,
	MIN(magic_wand_size) AS minimum_wand_size
FROM
	wizard_deposits
GROUP BY
	magic_wand_creator
ORDER BY
	"Minimum Wand Size" ASC
LIMIT 5;