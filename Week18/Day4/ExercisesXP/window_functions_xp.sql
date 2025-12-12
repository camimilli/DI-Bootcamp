-- Exercise 1: Movie Rankings and Analysis

-- Task 1: Rank Movies by Popularity within Each Genre
-- Use the RANK() function to rank movies by their popularity within each genre. Display the genre name, movie title, and their rank based on popularity.
SELECT
	g.genre_name AS Genre,
	m.title AS Title,
	RANK() OVER (PARTITION BY g.genre_name ORDER BY m.popularity DESC) AS rank
FROM movie m
JOIN movie_genres mg ON m.movie_id = mg.movie_id
JOIN genre g ON mg.genre_id = g.genre_id;

-- Task 2: Identify the Top 3 Movies by Revenue within Each Production Company
-- Use the NTILE() function to divide the movies produced by each production company into quartiles based on revenue. 
-- Display the company name, movie title, revenue, and quartile.
SELECT
	pc.company_name AS production_company,
	m.title,
	m.revenue,
	NTILE(4) OVER (PARTITION BY pc.company_name ORDER BY m.revenue DESC) AS quartile
FROM movie m
JOIN movie_company mc ON m.movie_id = mc.movie_id
JOIN production_company pc ON mc.company_id = pc.company_id;

-- Task 3: Calculate the Running Total of Movie Budgets for Each Genre
-- Display the genre name, movie title, budget, and running total budget.
SELECT
	g.genre_name AS genre,
	m.title,
	m.budget,
    SUM(m.budget) OVER (
        PARTITION BY g.genre_name
        ORDER BY m.budget
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total
FROM movie m
JOIN movie_genres mg ON m.movie_id = mg.movie_id
JOIN genre g ON mg.genre_id = g.genre_id;


-- Exercise 2: Cast and Crew Performance Analysis

-- Task 1: Rank Actors by Their Appearance in Movies
-- Use the DENSE_RANK() function to rank actors based on the number of movies they have appeared in. 
-- Display the actor’s name and their rank.
SELECT 
	p.person_name AS actor,
	DENSE_RANK() OVER (ORDER BY COUNT(DISTINCT mc.movie_id) DESC) AS dense_rank
FROM movie_cast mc 
JOIN person p ON mc.person_id = p.person_id
GROUP BY p.person_id, p.person_name
ORDER BY dense_rank, actor;

-- OR

SELECT
	actor,
	DENSE_RANK() OVER (ORDER BY movie_count DESC) AS ranking
FROM
	(SELECT
		p.person_name AS actor,
		COUNT(DISTINCT m.movie_id) AS movie_count
	 FROM movie_cast m 
	 JOIN person p ON m.person_id = p.person_id
	 GROUP BY p.person_name) AS counts
ORDER BY ranking, actor;

-- Task 2: Identify the Top Director by Average Movie Rating
-- Use a CTE and the RANK() function to find the director with the highest average movie rating. Display the director’s name and their average rating.
SELECT
	director,
	RANK() OVER (ORDER BY total_avg DESC) AS ranking
FROM (SELECT
		p.person_name AS director,
		AVG(m.vote_average) AS total_avg
	  FROM movie_crew c
	  JOIN movie m ON c.movie_id = m.movie_id
	  JOIN person p ON c.person_id = p.person_id
	  WHERE job = 'Director'
	  GROUP BY p.person_id, p.person_name
	  HAVING COUNT(DISTINCT m.movie_id) > 1)
ORDER BY ranking, director;

-- Task 3: Calculate the Cumulative Revenue of Movies Acted by Each Actor
-- Use the SUM() function to calculate the cumulative revenue of movies acted by each actor. 
-- Display the actor’s name and the cumulative revenue.
SELECT
	actor,
	title,
	SUM(revenue) OVER (
		PARTITION BY actor
		ORDER BY release_date
		ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
	) AS cumulative_revenue
FROM (SELECT
		 p.person_id,
		 p.person_name AS actor,
		 m.title,
		 m.release_date,
	  	 m.revenue
	  FROM movie_cast mc
	  JOIN person p ON mc.person_id = p.person_id
	  JOIN movie m ON mc.movie_id = m.movie_id
	  ) AS revenues
ORDER BY actor, release_date;


-- Task 4: Identify the Director Whose Movies Have the Highest Total Budget
-- Use a CTE and a window function to find the director whose movies have the highest total budget. Display the director’s name and the total budget.
WITH director_budgets AS (
    SELECT
        p.person_id,
        p.person_name AS director,
        SUM(m.budget) AS total_budget
    FROM movie_crew mc
    JOIN movie m ON mc.movie_id = m.movie_id
    JOIN person p ON mc.person_id = p.person_id
    WHERE mc.job = 'Director'
    GROUP BY p.person_id, p.person_name
)
SELECT
    director,
    total_budget
FROM (
    SELECT
        director,
        total_budget,
        RANK() OVER (ORDER BY total_budget DESC) AS budget_rank
    FROM director_budgets
) AS ranked_directors
WHERE budget_rank = 1;