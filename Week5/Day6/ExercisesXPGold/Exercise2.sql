-- Exercise 2 - Happy Halloween 

-- 1 
-- How many stores there are, and in which city and country they are located.
SELECT s.store_id, ci.city, cou.country 
FROM store s 
LEFT JOIN address a
ON s.address_id = a.address_id 
LEFT JOIN city ci
ON a.city_id = ci.city_id 
LEFT JOIN country cou
ON ci.country_id = cou.country_id; 


-- 2 
-- How many hours of viewing time there are in total in each store – in other words, the sum of the length of every inventory item in each store.
SELECT 
	i.store_id, 
	SUM(f.length) / 60 AS hours_of_viewing_time 
FROM 
	film f
INNER JOIN 
	inventory i ON f.film_id = i.film_id
GROUP BY
	i.store_id;


-- 3 
-- Make sure to exclude any inventory items which are not yet returned. (Yes, even in the time of zombies there are people who do not return their DVDs)
SELECT i.inventory_id
FROM inventory i
INNER JOIN rental r 
ON i.inventory_id = r.inventory_id
WHERE r.return_date IS NULL;


-- 4 
-- A list of all customers in the cities where the stores are located.

SELECT c.first_name || ' ' || c.last_name as customer_full_name
FROM customer c 
INNER JOIN address a 
ON c.address_id = a.address_id 
WHERE a.city_id IN 
(SELECT ci.city_id
FROM store s 
LEFT JOIN address a
ON s.address_id = a.address_id 
LEFT JOIN city ci
ON a.city_id = ci.city_id 
LEFT JOIN country cou
ON ci.country_id = cou.country_id);






-- SELECT ci.city_id, ci.city
-- FROM store s 
-- LEFT JOIN address a
-- ON s.address_id = a.address_id 
-- LEFT JOIN city ci
-- ON a.city_id = ci.city_id 
-- LEFT JOIN country cou
-- ON ci.country_id = cou.country_id;









-- 5 
-- A list of all customers in the countries where the stores are located.

-- 6
-- Some people will be frightened by watching scary movies while zombies walk the streets. 
-- Create a ‘safe list’ of all movies which do not include the ‘Horror’ category, or contain the words ‘beast’, 
-- ‘monster’, ‘ghost’, ‘dead’, ‘zombie’, or ‘undead’ in their titles or descriptions… 
-- Get the sum of their viewing time (length).
-- Hint : use the CHECK contraint

-- 7 
-- For both the ‘general’ and the ‘safe’ lists above, also calculate the time in hours and days(not just minutes).
