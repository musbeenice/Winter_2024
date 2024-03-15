CREATE OR REPLACE VIEW author_w_min_books_total AS
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
-- or
CREATE OR REPLACE VIEW author_sum_amount AS
SELECT author_id, SUM(amount) as sum_amount
FROM author
INNER JOIN book USING (author_id)
GROUP BY author_id

CREATE OR REPLACE VIEW min_sum_amount AS
SELECT MIN(sum_amount)
FROM author_sum_amount

SELECT author_name
FROM author
LEFT JOIN author_sum_amount
USING (author_id)
WHERE sum_amount = 
	(SELECT *
	FROM min_sum_amount
	 );
