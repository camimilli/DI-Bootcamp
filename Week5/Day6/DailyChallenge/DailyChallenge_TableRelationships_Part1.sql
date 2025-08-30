-- Daily Challenge: Tables Relationships 

-- Part 1 
-- 1 
CREATE TABLE customer (
	customer_id SERIAL PRIMARY KEY,
	first_name VARCHAR(50),
	last_name VARCHAR(100) NOT NULL
);

CREATE TABLE customer_profile (
	id SERIAL PRIMARY KEY,
	isLoggedIn BOOLEAN DEFAULT false,
	customer_id INTEGER UNIQUE REFERENCES customer(customer_id)
);

-- 2 
INSERT INTO customer (first_name, last_name)
VALUES ('John', 'Doe'),
	   ('Jerome', 'Lalu'),
	   ('Lea', 'Rive');

-- 3 
INSERT INTO customer_profile(isLoggedIn, customer_id)
VALUES (TRUE, (SELECT customer_id FROM customer WHERE first_name = 'John' AND last_name = 'Doe')),
	   (FALSE, (SELECT customer_id FROM customer WHERE first_name = 'Jerome' AND last_name = 'Lalu'));

-- 4
SELECT c.first_name
FROM customer c
INNER JOIN customer_profile c_prof
ON c.customer_id = c_prof.customer_id 
WHERE c_prof.isloggedin = true;

SELECT c.first_name, c_prof.isloggedin
FROM customer c 
LEFT JOIN customer_profile c_prof
ON c.customer_id = c_prof.customer_id;

SELECT COUNT(*) as not_loggedin
FROM customer_profile
WHERE isloggedin = FALSE; 