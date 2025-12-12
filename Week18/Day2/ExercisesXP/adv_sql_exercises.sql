-- Exercise 1: Complex Subquery Analysis

-- Task 1: Find the average age of competitors who have won at least one medal, grouped by the type of medal they won. 
-- Use a correlated subquery to achieve this.
SELECT m.id,
       m.medal_name,
       AVG(g.age) AS average_age
FROM medal m
JOIN games_competitor g
    ON EXISTS (
        SELECT 1
        FROM competitor_event ce
        WHERE ce.competitor_id = g.id
          AND ce.medal_id = m.id
    )
WHERE m.id <> 4
GROUP BY m.id, m.medal_name;

-- Task 2:  Identify the top 5 regions with the highest number of unique competitors who have participated in more than 3 different events. 
-- Use nested subqueries to filter and aggregate the data.

WITH people_over3 AS (
    SELECT g.person_id
    FROM competitor_event c
    JOIN games_competitor g 
        ON c.competitor_id = g.id
    GROUP BY g.person_id
    HAVING COUNT(DISTINCT c.event_id) > 3
)
SELECT pr.region_id,
       r.region_name,
       COUNT(DISTINCT pr.person_id) AS total_count
FROM people_over3 p
JOIN person_region pr
    ON p.person_id = pr.person_id
JOIN noc_region r
    ON pr.region_id = r.id
GROUP BY pr.region_id, r.region_name
ORDER BY total_count DESC
LIMIT 5;

-- Task 3: Create a temporary table to store the total number of medals won by each competitor and filter to show only those who have won more than 2 medals. 
--  Use subqueries to aggregate the data.

CREATE TEMP TABLE medals_count (
	id SERIAL PRIMARY KEY,
	person_id INT DEFAULT NULL,
	num_medals INT DEFAULT NULL
);

INSERT INTO medals_count(person_id, num_medals)
SELECT g.person_id, COUNT(c.medal_id)
FROM competitor_event c
JOIN games_competitor g ON c.competitor_id = g.id
WHERE c.medal_id <> 4
GROUP BY g.person_id
HAVING COUNT(c.medal_id) > 2;

SELECT * FROM medals_count
ORDER BY num_medals DESC;


-- Task 4: Use a subquery within a DELETE statement to remove records of competitors who have not won any medals from a temporary table created for analysis.
