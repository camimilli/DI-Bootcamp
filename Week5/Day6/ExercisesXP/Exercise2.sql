-- Exercise 2 : DVD Rental

-- 1 

UPDATE film
SET language_id = 2 
WHERE title = 'Chamber Italian';

UPDATE film
SET language_id = 4
WHERE title IN ('Ark Ridgemont', 'Attraction Newton');

-- 2 
-- address_id is a foreign key, when we INSERT values into customer we need to select the address_id from the address table

-- 3 
-- It's an easy step as is a child table and is none of its fields its used as reference for other tables
DROP TABLE customer_review;

-- 4 
SELECT COUNT(*) FROM rental
WHERE return_date IS NULL;

-- 5 
SELECT *
FROM rental r
LEFT JOIN inventory i
ON r.inventory_id = i.inventory_id 
LEFT JOIN film f
ON i.film_id = f.film_id
WHERE r.return_date IS NULL
ORDER BY f.rental_rate DESC
LIMIT 30; 

--- 6 
-- 1 
SELECT f.title, f.description, a.first_name || ' ' || a.last_name as full_name
FROM film f 
LEFT JOIN film_actor f_ac 
ON f.film_id = f_ac.film_id
LEFT JOIN actor a
ON f_ac.actor_id = a.actor_id
WHERE f.description ILIKE '%sumo%' AND a.first_name = 'Penelope' AND a.last_name = 'Monroe';

-- 2 
SELECT * 
FROM film
WHERE description ILIKE '%documentary%' 
AND length < 60
AND rating = 'R';

-- 3
SELECT f.title, c.first_name, c.last_name, f.rental_rate, r.return_date
FROM film f 
LEFT JOIN inventory i
ON f.film_id = i.film_id 
LEFT JOIN rental r 
ON i.inventory_id = r.inventory_id 
LEFT JOIN customer c 
ON r.customer_id = c.customer_id 
WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan'
AND f.rental_rate >= 4.00 
AND r.return_date BETWEEN '2005-07-28 00:00:00' AND '2005-08-01 23:59:59';

-- 4
SELECT f.title, f.description, c.first_name || ' ' || c.last_name AS full_name, f.replacement_cost
FROM film f 
LEFT JOIN inventory i
ON f.film_id = i.film_id 
LEFT JOIN rental r 
ON i.inventory_id = r.inventory_id 
LEFT JOIN customer c 
ON r.customer_id = c.customer_id 
WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan'
AND (f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
ORDER BY f.replacement_cost DESC
LIMIT 1;