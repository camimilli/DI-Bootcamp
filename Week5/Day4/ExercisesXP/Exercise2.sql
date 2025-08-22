SELECT * FROM customer;

SELECT (first_name, last_name) AS full_name
FROM customer; 

SELECT DISTINCT create_date
FROM customer;

SELECT * FROM customer 
ORDER BY first_name DESC;

SELECT film_id, title, description, release_year, rental_rate
FROM film 
ORDER BY rental_rate;

SELECT address, phone
FROM address
WHERE district = 'Texas'

SELECT *
FROM film
WHERE film_id = 15 or film_id = 150;

SELECT film_id, title, description, length, rental_rate
FROM film
WHERE title = 'Tarzan';

SELECT film_id, title, description, length, rental_rate
FROM film
WHERE title ILIKE 'ta%';

SELECT *
FROM film
ORDER BY replacement_cost
LIMIT 10;

WITH RankFilms AS (
	SELECT *,
		ROW_NUMBER() OVER(ORDER BY replacement_cost ASC) AS low_price_rank
	FROM film
	)
SELECT *
FROM RankFilms
WHERE low_price_rank BETWEEN 11 AND 20;


SELECT first_name, last_name, amount, payment_date 
FROM customer 
INNER JOIN payment
ON customer.customer_id = payment.customer_id
ORDER BY customer.customer_id;

SELECT city, country
FROM city 
LEFT JOIN country
ON city.country_id = country.country_id;

SELECT customer.customer_id, (customer.first_name, customer.last_name) AS full_name, amount, payment_date, payment.staff_id
FROM customer
INNER JOIN payment 
ON customer.customer_id = payment.customer_id 
INNER JOIN staff
ON payment.staff_id = staff.staff_id
ORDER BY staff.staff_id;

