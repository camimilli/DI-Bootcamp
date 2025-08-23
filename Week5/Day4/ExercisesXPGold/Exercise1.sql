SELECT COUNT(*), rating
FROM film
GROUP BY rating;

SELECT * FROM film
LIMIT 10;

SELECT * 
FROM film
WHERE rating IN ('G', 'PG-13') AND rental_duration < 2 AND rental_rate > 3.00
ORDER BY title ASC;

UPDATE customer
SET first_name = 'Camila', last_name = 'Milli', email='test@test.com'
WHERE customer_id = 1;

SELECT customer_id, first_name, customer.address_id, address 
FROM customer
INNER JOIN address
ON customer.address_id = address.address_id
WHERE customer_id = 1;

UPDATE address
SET address = 'Invisible Street 123'
FROM address AS A
INNER JOIN customer AS C
		ON A.address_id = C.address_id
WHERE C.customer_id = 1;
