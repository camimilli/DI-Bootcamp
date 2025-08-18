-- CREATE TABLE students (
-- student_id SERIAL PRIMARY KEY,
-- last_name VARCHAR(150) NOT NULL,
-- first_name VARCHAR(50) NOT NULL,
-- birth_date DATE NOT NULL
-- );

-- INSERT INTO students (first_name, last_name, birth_date)
-- VALUES
-- 	('Marc', 'Benichou', '1998-11-02'),
-- 	('Yoan', 'Cohen', '2010-12-03'),
-- 	('Lea', 'Benichou', '1987-07-27'),
-- 	('Amelia', 'Dux', '1996-04-07'),
-- 	('David', 'Grez', '2003-06-14'),
-- 	('Omer', 'Simpson', '1980-10-03');

-- INSERT INTO students(first_name, last_name, birth_date)
-- VALUES ('Camila', 'Millicovsky', '1995/03/27');

-- SELECT * FROM students;

-- SELECT first_name, last_name
-- FROM students;

-- SELECT first_name, last_name FROM students
-- WHERE student_id = 2;

-- SELECT first_name, last_name FROM students
-- WHERE last_name = 'Benichou' AND first_name = 'Marc';

-- SELECT first_name, last_name FROM students
-- WHERE last_name = 'Benichou' OR first_name = 'Marc';

-- SELECT first_name, last_name FROM students
-- WHERE first_name ILIKE '%a%'

-- SELECT first_name, last_name FROM students
-- WHERE first_name ILIKE 'a%'

-- SELECT first_name, last_name FROM students
-- WHERE first_name ILIKE '%a'

-- SELECT first_name, last_name FROM students
-- WHERE first_name ILIKE '%a_'

-- SELECT first_name, last_name FROM students
-- WHERE student_id = 1 AND student_id = 3

-- SELECT * FROM students
-- WHERE birth_date >= '2000/01/01'

-- SELECT student_id, first_name, last_name, birth_date 
-- FROM students
-- WHERE student_id BETWEEN 1 AND 4
-- ORDER BY first_name ASC;

-- SELECT student_id, first_name, last_name, birth_date
-- FROM students
-- ORDER BY birth_date desc
-- LIMIT 1

SELECT student_id, first_name, last_name, birth_date
FROM students
LIMIT 3
OFFSET 2 
