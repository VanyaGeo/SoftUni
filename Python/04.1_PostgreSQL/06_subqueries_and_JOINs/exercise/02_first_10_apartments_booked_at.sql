-- I

SELECT
    a.name,
    a.country,
    DATE(b.booked_at)
FROM
    apartments AS a
LEFT JOIN
    bookings AS b
USING
    (booking_id)
LIMIT 10;


-- II

--SELECT
--	a.name,
--	a.country,
--	b.booked_at::date
--FROM
--	apartments AS a
--LEFT JOIN
--	bookings AS b
--ON a.booking_id = b.booking_id
--LIMIT 10;


