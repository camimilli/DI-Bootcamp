-- JOINS IN SQL
-- LEFT TABLE: The one we put on FROM statement
-- RIGHT TABLE: The one we put on JOIN statement

------ INNER JOIN: SEE ONLY RELATED ROWS 
-- SELECT actors.first_name, actors.last_name, movies.movie_title
-- FROM actors 
-- INNER JOIN movies 
-- ON actors.actor_id = movies.actor_playing_id;

------ LEFT JOIN: SEE ALL THE COLUMNS FROM THE LEFT WITH THE MATCHING ROWS IF AVAILABLE FROM THE RIGHT
-- If there is no match, the right side will have null values.
-- SELECT actors.first_name, actors.last_name, movies.movie_title
-- FROM actors 
-- LEFT JOIN movies 
-- ON actors.actor_id = movies.actor_playing_id;

------ RIGHT JOIN: SEE ALL THE COLUMNS FROM THE RIGHT 
-- If there is no match, the left side will have null values.
-- SELECT actors.first_name, actors.last_name, movies.movie_title
-- FROM actors 
-- RIGHT JOIN movies 
-- ON actors.actor_id = movies.actor_playing_id;

-- INSERT INTO movies (movie_title, movie_story, actor_playing_id)
-- VALUES ('The Lord of the Rings: The Fellowship of the Ring', 'A ring with mysterious powers lands in the hands of a young hobbit, Frodo. Under the guidance of Gandalf, a wizard, he and his three friends set out on a journey and land in the Elvish kingdom.
-- ', NULL);

------ FULL JOIN: SHOWS ALL THE ROWS FROM BOTH TABLES
-- Doesn't matter which table is on the left/ride side 
-- SELECT actors.first_name, actors.last_name, movies.movie_title
-- FROM actors 
-- FULL JOIN movies 
-- ON actors.actor_id = movies.actor_playing_id;

-- EXERCISE 1 

-- CREATE TABLE countries (
-- country_id SERIAL PRIMARY KEY,
-- country_name VARCHAR(150) NOT NULL
-- );

-- INSERT INTO countries (country_name)
-- VALUES ('Argentina'),
-- ('France'),
-- ('Israel'),
-- ('United States'),
-- ('India');

----- It does the inner join on the ID so it matches the country that's on ID 1 for example
-- with the actor that's on ID 1 
-- SELECT actors.first_name, actors.last_name, countries.country_name
-- FROM actors
-- INNER JOIN countries
-- ON actors.actor_id = countries.country_id;
