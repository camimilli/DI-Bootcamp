-- Exercise 2: Students Table

-- UPDATE
--- 1 
-- UPDATE students
-- SET birth_date = '1998/02/11'
-- WHERE last_name = 'Benichou';

--- 2 
-- UPDATE students
-- SET last_name = 'Guez'
-- WHERE first_name = 'David' AND last_name = 'Grez';

-- DELETE
-- DELETE FROM students
-- WHERE first_name = 'Lea' AND last_name = 'Benichou';

-- COUNT
--- 1 
-- SELECT COUNT(*) student_count
-- FROM students;

--- 2 
-- SELECT COUNT(*) student_count
-- FROM students
-- WHERE birth_date > '2000/01/01';

-- INSERT/ALTER
--- 1 
-- ALTER TABLE students ADD COLUMN math_grade SMALLINT;

-- --- 2 - 4 
-- UPDATE students
-- SET math_grade = 80
-- WHERE student_id = 1;

-- UPDATE students 
-- SET math_grade = 90
-- WHERE student_id = 2 OR student_id = 4;

-- UPDATE students
-- SET math_grade = 40
-- WHERE student_id = 6;

-- SELECT * FROM students;

--- 5 
-- SELECT COUNT(*) grade_bigger_83
-- FROM students
-- WHERE math_grade > 83;

--- 6 
-- INSERT INTO students (first_name, last_name, birth_date, math_grade)
-- VALUES ('Omer', 'Simpson', '1980-10-03', 70);

--- 7 
-- SELECT first_name, last_name, COUNT(math_grade) total_grade
-- FROM students
-- GROUP BY first_name, last_name;

-- SUM
-- SELECT SUM(math_grade) sum_grades
-- FROM students;





