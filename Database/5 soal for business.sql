-- How many book have been loans more than once?
SELECT COUNT(book_id)
FROM books
WHERE book_id IN(
	SELECT book_id
	FROM loans
	GROUP BY book_id
	HAVING COUNT(loan_id)>1);


-- Show the user name and book ID that have been loans more than once 
SELECT u.user_name, l.book_id
FROM users u
JOIN loans l ON u.user_id = l.user_id
WHERE l.book_id IN(
	SELECT l.book_id
	FROM loans l
	GROUP BY l.book_id
	HAVING COUNT(loan_id)>1)
ORDER BY l.book_id;


-- What are the top 5 most borrowed books?
SELECT l.book_id, b.title, COUNT(*) AS borrow_count
FROM loans l
JOIN books b ON l.book_id = b.book_id
GROUP BY l.book_id, b.title
ORDER BY borrow_count DESC
LIMIT 5;


-- How many users have borrowed at least one book from each category?
SELECT u.user_id, COUNT(DISTINCT b.category_id) AS num_categories_borrowed
FROM users u
JOIN loans l ON u.user_id = l.user_id
JOIN books b ON l.book_id = b.book_id
GROUP BY u.user_id
HAVING COUNT(DISTINCT b.category_id) = (SELECT COUNT(*) FROM categories);


-- What is the average time between book returns for users who have borrowed from multiple categories?
SELECT u.user_id, AVG(l2.return_date - l1.return_date) AS avg_return_interval
FROM users u
JOIN loans l1 ON u.user_id = l1.user_id
JOIN loans l2 ON u.user_id = l2.user_id AND l2.return_date > l1.return_date
JOIN books b1 ON l1.book_id = b1.book_id
JOIN books b2 ON l2.book_id = b2.book_id
WHERE b1.category_id <> b2.category_id
GROUP BY u.user_id;