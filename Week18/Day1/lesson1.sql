-- DROP TABLE IF EXISTS employees;


-- CREATE TABLE departments (
--     department_id INT PRIMARY KEY,
--     department_name VARCHAR(50),
--     location_id INT
-- );

-- CREATE TABLE employees (
--     employee_id INT PRIMARY KEY,
--     first_name VARCHAR(50),
--     last_name VARCHAR(50),
--     department_id INT,
--     salary DECIMAL(10, 2),
--     FOREIGN KEY (department_id) REFERENCES departments(department_id)
-- );

-- CREATE TABLE locations (
--     location_id INT PRIMARY KEY,
--     city VARCHAR(50),
--     country VARCHAR(50)
-- );

-- CREATE TABLE high_salary_employees (
--     employee_id INT PRIMARY KEY,
--     first_name VARCHAR(50),
--     last_name VARCHAR(50),
--     salary DECIMAL(10, 2)
-- );

-- CREATE TABLE promotion_list (
--     employee_id INT PRIMARY KEY,
--     first_name VARCHAR(50),
--     last_name VARCHAR(50),
--     salary DECIMAL(10, 2)
-- );

-- CREATE TABLE orders (
--     order_id INT PRIMARY KEY,
--     customer_id INT,
--     order_date DATE
-- );

-- CREATE TABLE customers (
--     customer_id INT PRIMARY KEY,
--     first_name VARCHAR(50),
--     last_name VARCHAR(50)
-- );

-- CREATE TABLE products (
--     product_id INT PRIMARY KEY,
--     category_id INT,
--     price DECIMAL(10, 2)
-- );

-- CREATE TABLE categories (
--     category_id INT PRIMARY KEY,
--     category_name VARCHAR(50)
-- );

-- CREATE TABLE inventory (
--     product_id INT PRIMARY KEY,
--     stock INT
-- );

-- CREATE TABLE sales (
--     sale_id INT PRIMARY KEY,
--     department_id INT,
--     sales DECIMAL(10, 2)
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

-- INSERT INTO orders (order_id, customer_id, order_date) VALUES
-- (1, 1, '2024-01-10'),
-- (2, 1, '2024-01-15'),
-- (3, 2

-- , '2024-01-20'),
-- (4, 3, '2024-02-10'),
-- (5, 4, '2024-03-10'),
-- (6, 5, '2024-04-10');

-- INSERT INTO customers (customer_id, first_name, last_name) VALUES
-- (1, 'Alice', 'Johnson'),
-- (2, 'Bob', 'Smith'),
-- (3, 'Charlie', 'Brown'),
-- (4, 'David', 'Davis'),
-- (5, 'Eve', 'Evans');

-- INSERT INTO products (product_id, category_id, price) VALUES
-- (1, 1, 50),
-- (2, 1, 60),
-- (3, 2, 100),
-- (4, 2, 110),
-- (5, 3, 150);

-- INSERT INTO categories (category_id, category_name) VALUES
-- (1, 'Electronics'),
-- (2, 'Furniture'),
-- (3, 'Clothing');

-- INSERT INTO inventory (product_id, stock) VALUES
-- (1, 100),
-- (2, 200),
-- (3, 150),
-- (4, 50),
-- (5, 75);

-- INSERT INTO sales (sale_id, department_id, sales) VALUES
-- (1, 1, 5000),
-- (2, 2, 6000),
-- (3, 3, 7000),
-- (4, 4, 8000),
-- (5, 5, 9000);

-- INSERT INTO high_salary_employees (employee_id, first_name, last_name, salary)
-- SELECT employee_id, first_name, last_name, salary
-- FROM employees
-- WHERE salary > (SELECT AVG(salary) FROM employees); -- 78857.142857142857

-- UPDATE inventory
-- SET stock = stock + 50
-- WHERE product_id IN (SELECT product_id
--                      FROM orders
--                      WHERE order_date BETWEEN '2024-01-01' AND '2024-01-31'
--                      GROUP BY product_id
--                      HAVING COUNT(order_id) > 10);


-- UPDATE employees
-- SET salary = salary * 1.1
-- WHERE department_id = (SELECT department_id
--                        FROM departments
--                        WHERE department_name = 'IT');

-- DELETE FROM employees
-- WHERE department_id IN (SELECT department_id
--                         FROM departments
--                         WHERE location_id = (SELECT location_id
--                                              FROM locations
--                                              WHERE country = 'UK'));


-- EXERCISE 2
-- UPDATE employees
-- SET salary = salary * 1.1
-- WHERE department_id IN (
-- 	SELECT department_id
-- 	FROM departments d
-- 	WHERE (SELECT SUM(sales)
-- 		   FROM sales s 
-- 		   WHERE s.department_id = d.department_id) <
-- 			  (SELECT AVG(total_sales) FROM 
-- 				  (SELECT SUM(sales) as total_sales
-- 				   FROM sales
-- 				   GROUP BY department_id)))

-- -- EXERCISE 3
-- DELETE inventory
-- WHERE product_id IN (SELECT product_id
--                      FROM orders
--                      WHERE order_date >= CURRENT_DATE - INTERVAL'1 year'
--                      GROUP BY product_id
--                      HAVING COUNT(order_id) > 10);


SELECT employee_id, first_name, last_name, salary
FROM employees
WHERE department_id IN ( 
	SELECT department_id 
	FROM sales s
	GROUP BY department_id 
	HAVING SUM(s.sales) >
			(SELECT AVG(total_sales) FROM 
				(SELECT SUM(sales) as total_sales
				FROM sales 
				GROUP BY department_id) as q1)
)
AND salary >= (
    SELECT AVG(salary)
    FROM employees e
    WHERE e.department_id = employees.department_id
);
