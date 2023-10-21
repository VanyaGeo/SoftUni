# I

SELECT title
FROM books
WHERE SUBSTRING(title, 1, 3) = 'The'
ORDER BY id;

# II

SELECT title
FROM books
WHERE title LIKE 'The%'
ORDER BY id;