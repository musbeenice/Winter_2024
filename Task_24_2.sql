CREATE VIEW author_w_min_books_total AS
SELECT author_name
FROM author
INNER JOIN book USING (author_id)
GROUP BY author_id
HAVING SUM(amount) = 
(
	SELECT MIN(books_total) AS min_books_total
	FROM
	(
		SELECT author_id, SUM(amount) AS books_total
		FROM author INNER JOIN book USING (author_id)
		GROUP BY author_id
	) AS min_amounts
);
