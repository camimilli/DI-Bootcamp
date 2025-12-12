-- SET search_path TO olympics

-- Exercise 1: Detailed Medal Analysis
-- Task 1: Identify competitors who have won at least one medal in events spanning both Summer and Winter Olympics.
-- Create a temporary table to store these competitors and their medal counts for each season, and then display the contents of this table.
CREATE TEMP TABLE temp_medal_seasons AS
SELECT 
    gc.person_id,
    SUM(CASE WHEN ga.season = 'Summer' THEN 1 ELSE 0 END) AS summer_medals,
    SUM(CASE WHEN ga.season = 'Winter' THEN 1 ELSE 0 END) AS winter_medals
FROM competitor_event ce
JOIN games_competitor gc ON ce.competitor_id = gc.id
JOIN games ga ON gc.games_id = ga.id
WHERE ce.medal_id <> 4       -- only medal-winning events
GROUP BY gc.person_id
HAVING 
    SUM(CASE WHEN ga.season = 'Summer' THEN 1 ELSE 0 END) > 0
    AND
    SUM(CASE WHEN ga.season = 'Winter' THEN 1 ELSE 0 END) > 0;

-- Check
SELECT * FROM temp_medal_seasons


-- Task 2: Create a temporary table to store competitors who have won medals in exactly two different sports, and then use a subquery to identify 
-- the top 3 competitors with the highest total number of medals across all sports. Display the contents of this table.
DROP TABLE IF EXISTS two_sport_winners;

CREATE TEMP TABLE two_sport_winners AS
SELECT gc.person_id
FROM games_competitor gc
JOIN competitor_event ce ON ce.competitor_id = gc.id
JOIN event e ON ce.event_id = e.id
WHERE ce.medal_id <> 4
GROUP BY gc.person_id
HAVING COUNT(DISTINCT e.sport_id) = 2;

SELECT *
FROM (
    SELECT 
        t.person_id,
        COUNT(ce.medal_id) AS total_medals
    FROM two_sport_winners t
    JOIN games_competitor gc ON gc.person_id = t.person_id
    JOIN competitor_event ce ON ce.competitor_id = gc.id
    WHERE ce.medal_id <> 4
    GROUP BY t.person_id
    ORDER BY total_medals DESC
    LIMIT 3
) AS top_three;


-- Exercise 2: Region and Competitor Performance
-- Task 1: Retrieve the regions that have competitors who have won the highest number of medals in a single Olympic event.
-- Use a subquery to determine the event with the highest number of medals for each competitor, and then display the top 5 regions with the highest total medals.
SELECT r.region_name, SUM(t.medal_count) AS total_medals
FROM (SELECT
			gc.person_id,
			ce.event_id,
			COUNT(ce.medal_id) AS medal_count,
			ROW_NUMBER() OVER (PARTITION BY gc.person_id ORDER BY COUNT(*) DESC) AS row_num
	   FROM games_competitor gc
	   JOIN competitor_event ce ON gc.id = ce.competitor_id
	   WHERE ce.medal_id <> 4
	   GROUP BY gc.person_id, ce.event_id
	   ORDER  BY gc.person_id) AS t
JOIN person_region pr ON t.person_id = pr.person_id
JOIN noc_region r ON pr.region_id = r.id
WHERE row_num = 1
GROUP BY r.region_name
ORDER BY total_medals DESC
LIMIT 5;


-- Task 2: Create a temporary table to store competitors who have participated in more than three Olympic Games but have not won any medals. 
-- Retrieve and display the contents of this table, including their full names and the number of games they participated in.


DROP TABLE IF EXISTS no_wins;

CREATE TEMP TABLE no_wins AS
SELECT gc.person_id
FROM games_competitor gc
WHERE NOT EXISTS (
    SELECT 1
    FROM games_competitor gc2
    JOIN competitor_event ce 
      ON ce.competitor_id = gc2.id
    WHERE gc2.person_id = gc.person_id
      AND ce.medal_id IN (1, 2, 3)
)
GROUP BY gc.person_id
HAVING COUNT(DISTINCT gc.games_id) > 3;

SELECT 
    n.person_id, 
    p.full_name, 
    COUNT(DISTINCT gc.games_id) AS appearances
FROM no_wins n
JOIN person p ON n.person_id = p.id
JOIN games_competitor gc ON n.person_id = gc.person_id
GROUP BY n.person_id, p.full_name
ORDER BY appearances DESC;