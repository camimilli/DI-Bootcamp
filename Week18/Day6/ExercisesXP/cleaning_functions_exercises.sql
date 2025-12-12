-- Exercise 1: Building a Comprehensive Dataset for Employee Analysis

-- 1. Create a temporary table that join all tables and create a new one using LEFT JOIN.
DROP TABLE IF EXISTS emp_dataset;
CREATE TEMP TABLE emp_dataset AS(
	SELECT *
	FROM salaries s
	LEFT JOIN employees e ON s.employee_id = e.employee_code_emp
	LEFT JOIN functions f ON s.func_code = f.function_code
	LEFT JOIN companies c ON s.comp_name = c.company_name
);
SELECT * FROM emp_dataset;

-- 2. Create an unique identifier code between the columns ‘employee_id’ and ‘date’ and call it ‘id’.
-- 3. Convert the column ‘date’ to DATE type because it was previously configured as TIMESTAMP.
-- 4. Transform this new table into a dataset “df_employee” for analysis.
CREATE TABLE df_employee AS(
	SELECT
		employee_id || '_' || DATE(date) AS id,
		DATE(date) AS month_year,
		employee_id,
		employee_name,
		gen_m_f AS gender,
		age,
		salary,
		function_group, 
		company_name, 
		company_city, 
		company_state, 
		company_type, 
		const_site_category
	FROM emp_dataset
);


-- Exercise 2: Cleaning Data for Consistency and Quality
-- 1. Run the following SQLite request and observe your new table:
SELECT * FROM df_employee;

-- 2. Remove all unwanted spaces from all text columns using TRIM
UPDATE df_employee
SET
id = TRIM(id),
employee_name = TRIM(employee_name),
gender = TRIM(gender),
salary = TRIM(salary),
company_name = TRIM(company_name),
company_city = TRIM(company_city),
company_state = TRIM(company_state),
company_type = TRIM(company_type),
const_site_category = TRIM(const_site_category);

-- 3. Check for NULL values and empty values
SELECT *
FROM df_employee
WHERE id IS NULL
OR month_year IS NULL
OR employee_id IS NULL
OR employee_id IS NULL
OR employee_name IS NULL
OR gender IS NULL
OR age IS NULL
OR salary = ''
OR function_group IS NULL
OR company_name IS NULL
OR company_city IS NULL
OR company_state IS NULL
OR company_type IS NULL
OR const_site_category = '';

-- 4. Delete rows of the detected missing values.
DELETE FROM df_employee
WHERE id IS NULL
OR month_year IS NULL
OR employee_id IS NULL
OR employee_id IS NULL
OR employee_name IS NULL
OR gender IS NULL
OR age IS NULL
OR salary = ''
OR function_group IS NULL
OR company_name IS NULL
OR company_city IS NULL
OR company_state IS NULL
OR company_type IS NULL
OR const_site_category = '';

-- Exercise 3 : Calculating Current Employee Counts by Company
-- How many employees do the companies have today? Group them by company
SELECT
	company_name,
	COUNT(DISTINCT employee_id) AS employee_count
FROM df_employee
GROUP BY company_name
ORDER BY employee_count DESC;



-- Exercise 4 : Analyzing Employee Distribution by City and Over Time
-- What is the total number of employees each city? Add a percentage column
SELECT
	company_city,
	COUNT(DISTINCT employee_id) AS employee_count,
	ROUND(COUNT(DISTINCT employee_id) / SUM(COUNT(DISTINCT employee_id)) OVER (), 4) AS proportion
FROM df_employee
GROUP BY company_city
ORDER BY proportion DESC;

-- What is the total number of employees each month?
SELECT month_year, COUNT(DISTINCT employee_id) AS employee_count 
FROM df_employee
GROUP BY month_year
ORDER BY month_year ASC;


-- What is the average number of employees each month?
SELECT (COUNT(employee_id) / COUNT(DISTINCT month_year)) AS avg_employees_per_month
FROM df_employee;

















