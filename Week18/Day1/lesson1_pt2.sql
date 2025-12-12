-- DROP TABLE IF EXISTS departments;
-- CREATE TABLE departments (
--     department_id INT PRIMARY KEY,
--     department_name VARCHAR(50),
--     location_id INT
-- );

-- DROP TABLE IF EXISTS employees;
-- CREATE TABLE employees (
--     employee_id INT PRIMARY KEY,
--     first_name VARCHAR(50),
--     last_name VARCHAR(50),
--     department_id INT,
--     salary DECIMAL(10, 2),
--     FOREIGN KEY (department_id) REFERENCES departments(department_id)
-- );

-- DROP TABLE IF EXISTS locations;
-- CREATE TABLE locations (
--     location_id INT PRIMARY KEY,
--     city VARCHAR(50),
--     country VARCHAR(50)
-- );

-- INSERT INTO departments (department_id, department_name, location_id) VALUES
-- (1, 'HR', 100),
-- (2, 'Finance', 200),
-- (3, 'IT', 300),
-- (4, 'Marketing', 400),
-- (5, 'Sales', 500);

-- INSERT INTO employees (employee_id, first_name, last_name, department_id, salary) VALUES
-- (1, 'John', 'Doe', 1, 60000),
-- (2, 'Jane', 'Smith', 2, 80000),
-- (3, 'Jim', 'Brown', 3, 90000),
-- (4, 'Jake', 'White', 4, 70000),
-- (5, 'Jill', 'Green', 5, 75000),
-- (6, 'Jack', 'Black', 3, 95000),
-- (7, 'Jerry', 'Gray', 2, 82000);

-- INSERT INTO locations (location_id, city, country) VALUES
-- (100, 'New York', 'USA'),
-- (200, 'London', 'UK'),
-- (300, 'San Francisco', 'USA'),
-- (400, 'Berlin', 'Germany'),
-- (500, 'Paris', 'France');

-- SELECT e.first_name, e.last_name, e.salary, e.department_id
-- FROM employees e
-- WHERE e.department_id IN (
--     SELECT department_id
--     FROM employees
--     GROUP BY department_id
--     HAVING AVG(salary) > 70000
-- );

-- SELECT first_name, last_name
-- FROM employees e
-- WHERE EXISTS (
--     SELECT 1
--     FROM departments d
--     JOIN locations l ON d.location_id = l.location_id
--     WHERE e.department_id = d.department_id
--     AND l.city = 'London'
-- );

-- SELECT d.department_name, e.first_name, e.last_name, e.salary
-- FROM (
--     SELECT department_id, MAX(salary) AS max_salary
--     FROM employees
--     GROUP BY department_id
-- ) m
-- JOIN employees e ON e.department_id = m.department_id AND e.salary = m.max_salary
-- JOIN departments d ON e.department_id = d.department_id;


-- SELECT first_name, last_name, department_id, salary
-- FROM employees 
-- WHERE salary IN (SELECT MAX(salary)
-- 				FROM employees
-- 				GROUP BY department_id)
-- ORDER BY department_id ASC


-- SELECT e.first_name, e.last_name, l.city
-- FROM employees e
-- JOIN departments d ON e.department_id = d.department_id
-- JOIN locations l ON d.location_id = l.location_id
-- WHERE l.city IN ('London', 'New York')


SELECT e.first_name, e.last_name, e.salary, l.country
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN locations l ON d.location_id = l.location_id
WHERE l.country = 'USA'
AND e.salary > (SELECT AVG(salary)
				FROM employees
				WHERE department_id = e.department_id)

