-- Task 1: Find the average age of competitors who have won at least one medal, grouped by the type of medal they won.
-- Use a correlated subquery to achieve this.
SELECT 
	m.medal_name AS medal,
	AVG(gc.age) AS average_age
FROM competitor_event ce
JOIN medal m ON ce.medal_id = m.id
JOIN games_competitor gc ON ce.competitor_id = gc.id
JOIN person p ON gc.person_id = p.id
WHERE ce.medal_id <> 4
AND EXISTS (
    SELECT 1
    FROM competitor_event ce2
    JOIN games_competitor gc2 ON ce2.competitor_id = gc2.id
    WHERE gc2.person_id = p.id
      AND ce2.medal_id <> 4
)
GROUP BY m.medal_name;

-- SELECT DISTINCT p.id, p.full_name
-- FROM person p
-- WHERE NOT EXISTS (
--     SELECT 1
--     FROM games_competitor gc
--     JOIN competitor_event ce ON gc.id = ce.competitor_id
--     WHERE gc.person_id = p.id
--       AND ce.medal_id = 4
-- );

-- Task 2: Task 2: Identify the top 5 regions with the highest number of unique competitors who have participated in more than 3 different events. 
-- Use nested subqueries to filter and aggregate the data.
WITH competitors AS (
	SELECT gc.person_id
	FROM competitor_event ce
	JOIN games_competitor gc ON ce.competitor_id = gc.id
	GROUP BY gc.person_id
	HAVING COUNT(DISTINCT ce.event_id) > 3
	)
SELECT 
	r.region_name,
	COUNT(DISTINCT c.person_id) AS num_athletes
FROM competitors c
JOIN person_region pr ON c.person_id = pr.person_id
JOIN noc_region r ON pr.region_id = r.id
GROUP BY r.region_name
ORDER BY num_athletes DESC
LIMIT 5;