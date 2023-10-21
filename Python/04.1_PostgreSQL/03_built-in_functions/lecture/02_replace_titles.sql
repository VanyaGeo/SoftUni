SELECT REPLACE(title, 'The', '***')
FROM books
WHERE title like 'The%'
ORDER BY id;