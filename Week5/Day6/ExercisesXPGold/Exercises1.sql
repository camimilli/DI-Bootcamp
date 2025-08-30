-- 1
-- Gets a list of films that haven't been returned 
SELECT f.title AS films_to_be_returned
FROM film f 
LEFT JOIN inventory i
ON f.film_id = i.film_id 
LEFT JOIN rental r 
ON i.inventory_id = r.rental_id 
WHERE r.return_date IS NULL;


-- 2 
-- Get a list of all customers who have not returned their rentals. Make sure to group your results.
-- The count is on rentals as I want to know how many per customer 
-- group by customer 
SELECT c.first_name || ' ' || c.last_name as customer_details,
COUNT(*) as movies_to_return
FROM rental r 
LEFT JOIN customer c
ON r.customer_id = c.customer_id 
WHERE r.return_date IS NULL
GROUP BY customer_details
ORDER BY movies_to_return DESC;


-- 3 
-- Using film_list view 
SELECT * FROM public.film_list
WHERE category = 'Action' AND actors ILIKE '%Joe Swank%';

-- Using subquery 
-- SELECT title
-- FROM film 
-- WHERE film_id IN 
-- (SELECT film_id FROM film_actor WHERE actor_id IN 
-- (SELECT actor_id FROM actor WHERE first_name = 'Joe' AND last_name = 'Swank')) 
-- AND film_id IN (SELECT film_id FROM film_category WHERE category_id IN 
-- (SELECT category_id FROM category WHERE name = 'Action'));

-- Using JOIN
SELECT f.title
FROM film f
LEFT JOIN film_category f_cat
ON f.film_id = f_cat.film_id 
LEFT JOIN category c 
ON f_cat.category_id = c.category_id
LEFT JOIN film_actor f_act
ON f.film_id = f_act.film_id 
LEFT JOIN actor a
ON f_act.actor_id = a.actor_id 
WHERE a.first_name = 'Joe' AND a.last_name = 'Swank' 
AND c.name = 'Action';










