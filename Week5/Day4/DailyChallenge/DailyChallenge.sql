-- Daily Challenge : SQL Puzzle

-- QUERIES

CREATE TABLE FirstTab (
     id integer, 
     name VARCHAR(10)
);

INSERT INTO FirstTab VALUES
(5,'Pawan'),
(6,'Sharlee'),
(7,'Krish'),
(NULL,'Avtaar');

SELECT * FROM FirstTab;

CREATE TABLE SecondTab (
    id integer 
);

INSERT INTO SecondTab VALUES
(5),
(NULL);


SELECT * FROM SecondTab;


-- QUESTIONS

-- Q1 
-- OUTPUT: 0
-- EXPLANATION: The NULL value returned in the subquery makes the result of the entire list as UNKNOWN so count becomes 0 with no matches
-- QUERY: 
SELECT COUNT(*)
FROM FirstTab AS ft 
WHERE ft.id NOT IN 
(SELECT id FROM SecondTab WHERE id IS NULL);

-- Q2
-- OUTPUT: 2
-- EXPLANATION: Only ID 6 and 7 evaluate to TRUE on the WHERE condition when compared with NOT IN 5, NULL is UNKNOWN and 5 is in (5)
-- QUERY:
SELECT COUNT(*)
FROM FirstTab AS ft
WHERE ft.id NOT IN 
	(SELECT id FROM SecondTab WHERE id = 5);

-- Q3
-- OUTPUT: 0
-- EXPLANATION: As there's a NULL in the list the subquery returns the whole condition is UNKNOWN and no row is returned 
-- QUERY:
SELECT COUNT(*)
FROM FirstTab AS ft 
WHERE ft.id NOT IN 
	(SELECT id FROM SecondTab);

-- Q4
-- OUTPUT: 2 
-- EXPLANATION: Subquery returns 5, similar to Q2 - Only ID 6 and 7 evaluate to TRUE on the WHERE condition when compared with NOT IN 5, NULL is UNKNOWN and 5 is in (5)
-- QUERY:
SELECT COUNT(*)
FROM FirstTab AS ft 
WHERE ft.id NOT IN 
	(SELECT id FROM SecondTab WHERE id IS NOT NULL);
