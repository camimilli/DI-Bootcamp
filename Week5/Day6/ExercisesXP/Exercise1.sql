-- Exercises XP 
-- Exercise 1: DVD Rental

-- 1 
SELECT name FROM language;

-- 2 
SELECT f.title, f.description, l.name 
FROM film f
LEFT JOIN language l
ON f.language_id = l.language_id;

-- 3 
SELECT f.title, f.description, l.name
FROM language l
LEFT JOIN film f
ON l.language_id = f.language_id;

-- 4 
CREATE TABLE new_film (
film_id SERIAL PRIMARY KEY, 
film_name VARCHAR(100) NOT NULL
);

INSERT INTO new_film (film_name)
VALUES ('The Naked Gun'),('Weapons'),('Starwars 10');

-- 5 
DROP TABLE IF EXISTS customer_review;

CREATE TABLE customer_review (
review_id SERIAL PRIMARY KEY,
film_id INTEGER NOT NULL REFERENCES new_film (film_id) ON DELETE CASCADE,
language_id INTEGER REFERENCES language (language_id),
title VARCHAR(200),
score SMALLINT CHECK (score BETWEEN 1 AND 10),
review_text TEXT,
last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
);


-- 6
INSERT INTO customer_review (film_id, language_id, title, score, review_text)
VALUES ((SELECT film_id FROM new_film WHERE film_name = 'The Naked Gun'), 
		(SELECT language_id FROM language WHERE name = 'English'), 'A Classic of Unapologetic Absurdity',
		9, 'This is pure, unadulterated slapstick comedy that holds up surprisingly well. Leslie Nielsen''s deadpan delivery as Lt. Frank Drebin is masterful, and the film''s relentless barrage of sight gags and wordplay keeps you laughing from start to finish. It''s a reminder of a time when comedy wasn''t afraid to be completely ridiculous.'),
		((SELECT film_id FROM new_film WHERE film_name = 'Weapons'), (SELECT language_id FROM language WHERE name = 'French'), 'Un film d''action captivant et plein de rebondissements', 8, '"Weapons" est une masterclass de cinéma d''action. L''intrigue est complexe et intelligente, et les scènes de combat sont parfaitement chorégraphiées. La performance de l''acteur principal est incroyable, et le film vous tient en haleine du début à la fin. Un incontournable pour les amateurs du genre.'),
		((SELECT film_id FROM new_film WHERE film_name = 'Starwars 10'), (SELECT language_id FROM language WHERE name = 'English'), ' The Next Generation of the Galaxy', 7, ' While "Star Wars 10" brings a fresh perspective to the saga, it struggles to find its footing amidst the overwhelming legacy. The new characters are compelling, and the visual effects are breathtaking, but the plot feels a bit rushed. It''s a promising new chapter, but not the epic conclusion fans might have hoped for.');

-- 7 
-- The record from customer_review that has the film ID we remove will be deleted as well. 
DELETE FROM new_film 
WHERE film_name = 'Starwars 10';

SELECT * FROM customer_review;