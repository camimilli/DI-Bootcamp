-- Exercise 1: Bonus Public Database (Continuation Of XP)

-- 1 
SELECT first_name || ' ' || last_name as full_name
FROM customers
ORDER BY full_name ASC
OFFSET (SELECT COUNT(*) FROM customers)-2;

-- 2
DELETE FROM purchases 
WHERE customer_id = (SELECT customer_id FROM customers WHERE first_name = 'Scott');

-- 3 
-- Customer's table didn't change as we only deleted a record in purchase 
SELECT * FROM customers
WHERE first_name = 'Scott';

-- 4 
-- Need to use a RIGHT JOIN to show all records from customer tables 
SELECT id, quantity_purchased, p.customer_id, item_id
FROM purchases p
RIGHT JOIN customers c 
ON p.customer_id = c.customer_id;

-- 5
-- Used an INNER JOIN
SELECT * 
FROM purchases p 
INNER JOIN customers c 
ON p.customer_id = c.customer_id;








