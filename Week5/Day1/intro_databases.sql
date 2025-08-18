-- HOW TO CREATE A TABLE 

-- CREATE TABLE actors (
-- actor_id SERIAL PRIMARY KEY,
-- first_name VARCHAR(50) NOT NULL,
-- last_name VARCHAR(150) NOT NULL,
-- date_of_birth DATE NOT NULL, 
-- number_oscars SMALLINT NOT NULL
-- )

---------------------------------------------------------------

-- HOW TO INSERT DATA INTO A TABLE

-- SYNTAX FOR INSERTING DATE DATA -> dd/mm/yyy or mm/dd/yyyy it depends on system
-- ****BEST WAY TO INSERT DATA**** -> yyyy/mm/dd 
-- POSTGRESQL STORES DATE DATA -> yyyy/mm/dd (USED TO QUERY DATA)
-- We can change the format that we see date on tables and how we input 

-- INSERT INTO actors (first_name, last_name, date_of_birth, number_oscars)
-- VALUES ('Matt', 'Damon', '06/05/1961', 2);

-- INSERT INTO actors (first_name, last_name, date_of_birth, number_oscars)
-- VALUES ('Leonardo', 'DiCaprio', '11/11/1974', 1);

-- INSERT INTO actors (first_name, last_name, date_of_birth, number_oscars)
-- VALUES ('Meryl', 'Streep', '06/22/1949', 3);

-- INSERT INTO actors (first_name, last_name, date_of_birth, number_oscars)
-- VALUES ('Tom', 'Hanks', '09/07/1956', 2);

-- INSERT INTO actors (first_name, last_name, date_of_birth, number_oscars)
-- VALUES ('Matt', 'O''Leary', '06/07/1987', 3);

-- INSERT INTO actors (first_name, last_name, date_of_birth, number_oscars)
-- VALUES ('Cate', 'Blanchett', '05/14/1969', 2),
-- 	('Daniel Day', 'Lewis', '04/29/1957', 3),
-- 	('Denzel', 'Washington', '12/28/1954', 2);

---------------------------------------------------------------

-- TYPES OF SELECT QUERIES
-- SELECT * FROM actors 

-- SELECT last_name, number_oscars FROM actors

---------------------------------------------------------------

-- WHERE: CONDITION 
-- SELECT last_name, number_oscars 
-- FROM actors
-- WHERE number_oscars > 2 

-- SELECT first_name, last_name, number_oscars
-- FROM actors
-- WHERE first_name = 'Matt' AND last_name = 'Damon'

---------------------------------------------------------------

-- LIKE: case sensitive 
-- ILIKE: not case sensitive

-- SELECT * FROM actors 
-- WHERE last_name LIKE '%mon%' -- actors that have mon at any point in their last_name in lowercase

-- SELECT * FROM actors 
-- WHERE last_name ILIKE '%MON%' -- actors that have mon at any point in their last_name in lower/upper case 

---------------------------------------------------------------

-- LIMIT - limits the results displayed 
-- OFFSET - skips values 

-- SELECT * FROM actors 
-- LIMIT 3;

-- SELECT * FROM actors
-- OFFSET 2; -- jumps two (shows 3 and higher)

---------------------------------------------------------------

-- ORDER BY - Used to sort the results in ascending or descending order based on the specified criteria - ASC/DESC 
-- ASC is default 

-- SELECT * FROM actors
-- WHERE date_of_birth > '01-01-1960' 
-- ORDER BY first_name ASC

-- SELECT * FROM actors
-- ORDER BY number_oscars DESC;

---------------------------------------------------------------
-- EXERCISE 1 

-- SELECT * FROM actors
-- WHERE first_name ILIKE '%e%' and number_oscars >= 3
-- ORDER BY last_name DESC
-- LIMIT 4 

---------------------------------------------------------------
-- UPDATE RECORDS - SET + WHERE 
-- When updating the record updated goes to the end of the table, can be avoided.

-- UPDATE actors 
-- SET date_of_birth = '08/10/1970'
-- WHERE
-- last_name = 'Damon';

-- RETURNING - get data back from a row that has just been modified

-- UPDATE actors
-- SET date_of_birth = '09/01/1950',
--     number_oscars = 12
-- WHERE
--     first_name = 'Meryl'
-- RETURNING 
--     first_name, 
--     date_of_birth;

---------------------------------------------------------------
-- DELETE RECORDS - Deletes all rows / specified rows from the table 
-- Also supports RETURNING
-- Can't reset SERIAL or BIGSERIAL columns (Use TRUNCATE)

-- DELETE FROM actors
-- WHERE first_name = 'Meryl' AND last_name = 'Streep'; 
-- good to practice to be as specific as possible to make sure we don't delete something by mistake

-- DELETING A TABLE
-- DELETE FROM table; 

---------------------------------------------------------------
-- TRUNCATE A TABLE - removes all rows from a table and resets data, faster than DELETE 
-- can't be rolled back (DELETE action can)
-- Resets SERIAL or BIGSERIAL columns 

-- deletes the data but keeps the table 
-- TRUNCATE TABLE actors 

-- Adding a new actor will add it with ID from the last ID we had, if we had 8 rows and we truncate and insert 
-- a new value, it will have actor_id of 9, to restart I need to RESTART IDENTITY 
-- INSERT INTO actors (first_name, last_name, date_of_birth, number_oscars)
-- VALUES ('Matt', 'O''Leary', '06/07/1987', 3);

-- TRUNCATE AND RESTART IDENTITY (RESTARTS ID NUMBERS FROM 0)
-- TRUNCATE TABLE actors RESTART IDENTITY;

-- Adding new value that will have ID 1 as we restarted 
-- INSERT INTO actors (first_name, last_name, date_of_birth, number_oscars)
-- VALUES ('Matt', 'O''Leary', '06/07/1987', 3);

-- SELECT * FROM actors;

---------------------------------------------------------------
-- ALTER A Table - Changes the table structure, we can:
-- Add a new column
-- Remove an existing column
-- Rename an existing column
-- Rename a table
-- Change the data type of a column

-- SYNTAX
-- ALTER TABLE table_name action 

---------------------------------------------------------------

-- EXERCISE 2 

-- Update the first name of Matt Damon to Maty

-- UPDATE actors 
-- SET first_name = 'Maty'
-- WHERE
-- last_name = 'Damon';

-- UPDATE actors
-- SET number_oscars = 4
-- WHERE
-- last_name = 'Streep';

-- ALTER TABLE actors RENAME COLUMN date_of_birth TO birthdate;

-- DELETE FROM actors
-- WHERE first_name = 'Leonardo' AND last_name = 'DiCaprio';

-- INSERT INTO actors (first_name, last_name, birthdate, number_oscars)
-- VALUES ('Leonardo', 'DiCaprio', '11/11/1974', 1);


-- SELECT * FROM ACTORS