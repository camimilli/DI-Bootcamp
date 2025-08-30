-- Daily Challenge: Tables Relationships 

-- Part 1 
-- 1 
CREATE TABLE customer (
	customer_id SERIAL PRIMARY KEY,
	first_name VARCHAR(50),
	last_name VARCHAR(100) NOT NULL
);

CREATE TABLE customer_profile (
	id SERIAL PRIMARY KEY,
	isLoggedIn BOOLEAN DEFAULT false,
	customer_id INTEGER UNIQUE REFERENCES customer(customer_id)
);

-- 2 
INSERT INTO customer (first_name, last_name)
VALUES ('John', 'Doe'),
	   ('Jerome', 'Lalu'),
	   ('Lea', 'Rive');

-- 3 
INSERT INTO customer_profile(isLoggedIn, customer_id)
VALUES (TRUE, (SELECT customer_id FROM customer WHERE first_name = 'John' AND last_name = 'Doe')),
	   (FALSE, (SELECT customer_id FROM customer WHERE first_name = 'Jerome' AND last_name = 'Lalu'));

-- 4
SELECT c.first_name
FROM customer c
INNER JOIN customer_profile c_prof
ON c.customer_id = c_prof.customer_id 
WHERE c_prof.isloggedin = true;

SELECT c.first_name, c_prof.isloggedin
FROM customer c 
LEFT JOIN customer_profile c_prof
ON c.customer_id = c_prof.customer_id;

SELECT COUNT(*) as not_loggedin
FROM customer_profile
WHERE isloggedin = FALSE; 


-- Part 2 
-- 1 
CREATE TABLE book (
	book_id SERIAL PRIMARY KEY,
	title VARCHAR(150) NOT NULL,
	author VARCHAR(150) NOT NULL
);

-- 2 
INSERT INTO book (title, author)
VALUES 
('Alice In Wonderland', 'Lewis Carroll'),
('Harry Potter', 'J.K Rowling'),
('To kill a mockingbird', 'Harper Lee');

-- 3 
CREATE TABLE student (
	student_id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL UNIQUE,
	age SMALLINT CHECK (age < 16)
);

-- 4 
INSERT INTO student (name, age)
VALUES
('John', 12),
('Lera', 11),
('Patrick', 10),
('Bob', 14);

-- 5
DROP TABLE IF EXISTS library;
CREATE TABLE library (
	book_fk_id INTEGER,
	student_fk_id INTEGER,
	borrowed_date DATE,

	FOREIGN KEY (book_fk_id) REFERENCES book (book_id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (student_fk_id) REFERENCES student (student_id) ON DELETE CASCADE ON UPDATE CASCADE,

	PRIMARY KEY (book_fk_id, student_fk_id)
);

-- 6 
INSERT INTO library (book_fk_id, student_fk_id, borrowed_date)
VALUES

((SELECT book_id FROM book WHERE title = 'Alice In Wonderland'), 
 (SELECT student_id FROM student WHERE name = 'John'),
  '2022-02-15'),
  
((SELECT book_id FROM book WHERE title = 'To kill a mockingbird'), 
 (SELECT student_id FROM student WHERE name = 'Bob'),
  '2021-03-03'),

((SELECT book_id FROM book WHERE title = 'Alice In Wonderland'), 
 (SELECT student_id FROM student WHERE name = 'Lera'),
  '2021-05-23'),

((SELECT book_id FROM book WHERE title = 'Harry Potter'), 
 (SELECT student_id FROM student WHERE name = 'Bob'),
  '2021-08-12');

-- 7 
SELECT * FROM library;

SELECT s.name as student_name, b.title as borrowed_book
FROM library l
INNER JOIN student s 
ON l.student_fk_id = s.student_id 
INNER JOIN book b 
ON l.book_fk_id = b.book_id;

SELECT ROUND(AVG(s.age)) as average_student_age
FROM library l 
INNER JOIN student s 
ON l.student_fk_id = s.student_id 
INNER JOIN book b
ON l.book_fk_id = b.book_id 
WHERE b.title = 'Alice In Wonderland';

-- The row that refers to the student we deleted will be deleted as well from the junction table
DELETE FROM student
WHERE name = 'Lera';







