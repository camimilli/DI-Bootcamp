SELECT d.department_name, e.first_name, e.last_name, e.salary
FROM (
    SELECT department_id, MAX(salary) AS max_salary
    FROM employees
    GROUP BY department_id
) m
JOIN employees e ON e.department_id = m.department_id AND e.salary = m.max_salary
JOIN departments d ON e.department_id = d.department_id;

--- Same Query but Better

WITH max_salary as (
    SELECT department_id, MAX(salary) AS max_salary
    FROM employees
    GROUP BY department_id
)
SELECT d.department_name, e.first_name, e.last_name, e.salary
FROM max_salary m
JOIN employees e ON e.department_id = m.department_id AND e.salary = m.max_salary
JOIN departments d ON e.department_id = d.department_id;

-- Create the original products table
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,       -- Auto-incrementing product ID
    product_name VARCHAR(100) NOT NULL, -- Product name (cannot be null)
    price DECIMAL(10, 2) NOT NULL       -- Product price (cannot be null)
);
-- Insert sample data into the products table
INSERT INTO products (product_name, price)
VALUES
    ('Laptop', 1200.00),
    ('Smartphone', 800.00),
    ('Tablet', 400.00),
    ('Headphones', 150.00),
    ('Smartwatch', 250.00);
-- Verify the data in the products table
SELECT * FROM products;
-- Step 1: Create a temporary table
CREATE TEMP TABLE temp_products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    original_price DECIMAL(10, 2),
    increased_price DECIMAL(10, 2)
);
-- Step 2: Insert data into the temporary table
INSERT INTO temp_products (product_name, original_price, increased_price)
SELECT
    product_name,
    price AS original_price,
    price * 1.10 AS increased_price -- Increase price by 10%
FROM
    products;
-- Step 3: Query the temporary table
SELECT * FROM temp_products;

-- Create the customers table with sample data
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,        -- Unique customer ID
    first_name VARCHAR(50) NOT NULL,      -- Customer first name
    last_name VARCHAR(50) NOT NULL,       -- Customer last name
    total_spent DECIMAL(10, 2),           -- Total amount spent by the customer
    last_purchase_date DATE               -- Date of the customer's last purchase
);
-- Insert sample data into the customers table
INSERT INTO customers (first_name, last_name, total_spent, last_purchase_date)
VALUES
    ('Alice', 'Brown', 1500.50, '2024-11-15'),
    ('Bob', 'Smith', 800.00, '2024-12-01'),
    ('Charlie', 'Johnson', 2500.00, '2024-11-20'),
    ('Diana', 'White', 600.00, '2024-10-30'),
    ('Eve', 'Black', 3000.00, '2024-12-10');
-- Verify the data
SELECT * FROM customers;
-- Create a local temporary table for staging and transforming customer data
CREATE TEMP TABLE temp_customers (
    customer_id SERIAL PRIMARY KEY,        -- Unique customer ID
    full_name VARCHAR(100),                -- Concatenated full name
    total_spent DECIMAL(10, 2),            -- Total amount spent
    last_purchase_date DATE,               -- Date of last purchase
    customer_value_category VARCHAR(50)    -- Categorized customer value
);
-- Populate the temporary table with transformed data
INSERT INTO temp_customers (full_name, total_spent, last_purchase_date, customer_value_category)
WITH temp_customers AS (SELECT
    CONCAT(first_name, ' ', last_name) AS full_name,  -- Concatenate first and last name
    total_spent,
    last_purchase_date,
    CASE
        WHEN total_spent >= 2000 THEN 'High-Value'
        WHEN total_spent >= 1000 THEN 'Medium-Value'
        ELSE 'Low-Value'
    END AS customer_value_category
FROM
    customers)
-- Verify the data in the temporary table
SELECT * FROM temp_customers;















