-- Task 1: Calculate the Average Budget Growth Rate for Each Production Company
-- Calculate the average budget growth rate for each production company across all movies they have produced. 
-- Use window functions to determine the budget growth rate and then calculate the average growth rate.
WITH running_totals AS (
    SELECT
        pc.company_name,
        m.release_date,
        m.budget,
        SUM(m.budget) OVER (
            PARTITION BY pc.company_name 
            ORDER BY m.release_date
        ) AS total_budget
    FROM movie m
    JOIN movie_company mc ON m.movie_id = mc.movie_id
    JOIN production_company pc ON mc.company_id = pc.company_id
    WHERE m.budget <> 0
),
growth AS (
	SELECT
		company_name,
		total_budget,
		(total_budget - LAG(total_budget) OVER (
			PARTITION BY company_name 
			ORDER BY release_date
		)) * 100.0 / NULLIF(LAG(total_budget) OVER (
			PARTITION BY company_name 
			ORDER BY release_date
		), 0) AS growth_rate
	FROM running_totals
)
SELECT
	company_name,
	ROUND(AVG(growth_rate),2) AS avg_growth_rate
FROM growth
GROUP BY company_name
HAVING AVG(growth_rate) IS NOT NULL
ORDER BY company_name;


-- Task 2: Determine the Most Consistently High-Rated Actor
-- Identify the actor who has appeared in the most movies that are rated above the average rating of all movies. 
-- Use window functions and CTEs to calculate the average rating and filter the actors based on this criterion.
WITH above_avg AS(
	SELECT movie_id
	FROM movie
	WHERE vote_average > (SELECT AVG(vote_average) FROM movie)
)
SELECT p.person_name, COUNT(DISTINCT a.movie_id) AS appearances
FROM above_avg a 
JOIN movie_cast mc ON a.movie_id = mc.movie_id
JOIN person p ON mc.person_id = p.person_id
GROUP BY p.person_name
ORDER BY appearances DESC
LIMIT 1;

-- Task 3: Calculate the Rolling Average Revenue for Each Genre
-- Calculate the rolling average revenue for movies within each genre, considering only the last three movies released in the genre. 
-- Use window functions with the ROWS frame specification to achieve this.
SELECT
    g.genre_name,
    m.title,
    m.release_date,
    m.revenue,
    AVG(m.revenue) OVER (
        PARTITION BY g.genre_name
        ORDER BY m.release_date
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS rolling_avg_revenue
FROM movie m
JOIN movie_genres mg ON m.movie_id = mg.movie_id
JOIN genre g ON mg.genre_id = g.genre_id
WHERE m.revenue <> 0 AND m.revenue IS NOT NULL
ORDER BY g.genre_name, m.release_date;

-- Task 4: Identify the Highest-Grossing Movie Series
-- Identify the movie series (based on shared keywords) with the highest total revenue. 
-- Use window functions and CTEs to group movies by their series and calculate the total revenue.

WITH movie_keywords AS (
    -- Get all movies with their keywords
    SELECT 
        m.movie_id,
        m.title,
        m.revenue,
        k.keyword_name
    FROM movie m
    JOIN movie_keywords mk ON m.movie_id = mk.movie_id
    JOIN keyword k ON mk.keyword_id = k.keyword_id
    WHERE m.revenue <> 0
),
series_revenue AS (
    -- Calculate total revenue for each keyword/series
    SELECT 
        keyword_name AS series_name,
        SUM(revenue) AS total_revenue,
        COUNT(DISTINCT movie_id) AS movie_count,
        -- Use window function to rank series by revenue
        RANK() OVER (ORDER BY SUM(revenue) DESC) AS revenue_rank
    FROM movie_keywords
    GROUP BY keyword_name
)
SELECT 
    series_name,
    total_revenue,
    movie_count,
    revenue_rank
FROM series_revenue
WHERE revenue_rank = 1;

