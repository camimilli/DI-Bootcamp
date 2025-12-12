-- Exercise 1: Complex Subquery Analysis

-- Task 1: Find the average age of competitors who have won at least one medal, grouped by the type of medal they won. 
-- Use a correlated subquery to achieve this.
SELECT m.id, m.medal_name, AVG(g.age) AS average_age
FROM medal m 
JOIN games_competitor g
ON EXISTS (
	SELECT 1
	FROM competitor_event c
	WHERE c.competitor_id = g.id
		AND c.medal_id = m.id
)
GROUP BY m.id, m.medal_name;


-- Task 2: Identify the top 5 regions with the highest number of unique competitors who have participated in more than 3 different events. 
-- Use nested subqueries to filter and aggregate the data.
SELECT r.region_name, COUNT(DISTINCT pr.person_id) 
FROM noc_region r
JOIN person_region pr ON r.id = pr.region_id
WHERE pr.person_id IN (SELECT g.person_id
						FROM games_competitor g
						JOIN competitor_event c ON g.id = c.competitor_id
						GROUP BY g.person_id
						HAVING count(DISTINCT c.event_id) > 3
						ORDER BY g.person_id)
GROUP BY r.region_name
ORDER BY count DESC
LIMIT 5;


-- Exercise 2: Advanced Data Manipulation and Optimization

-- Task 1: Update the heights of competitors based on the average height of competitors from the same region. 
-- Use a correlated subquery within the UPDATE statement.

-- UPDATE person p
-- SET height = (SELECT AVG(p1.height)
-- 			  FROM person p1
-- 			  JOIN person_region pr ON p1.id = pr.person_id
-- 			  WHERE pr.region_id = (SELECT pr1.region_id
-- 			  						FROM person_region pr1
-- 									WHERE pr1.person_id = p.id
-- 									LIMIT 1));









