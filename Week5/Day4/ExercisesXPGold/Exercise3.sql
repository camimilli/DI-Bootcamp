-- Exercise 3: Items and Customers

--- PART 1
CREATE TABLE purchases (
id SERIAL PRIMARY KEY,
quantity_purchased SMALLINT,
customer_id INT,
item_id INT,
FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
FOREIGN KEY (item_id) REFERENCES items(item_id)
);

INSERT INTO purchases (quantity_purchased, customer_id, item_id)
VALUES 
(1, (SELECT customer_id FROM customers WHERE first_name = 'Scott' AND last_name = 'Scott'), (SELECT item_id from items WHERE product = 'Fan')),
(10, (SELECT customer_id FROM customers WHERE first_name = 'Melanie' AND last_name = 'Johnson'), (SELECT item_id from items WHERE product = 'Large desk')),
(2, (SELECT customer_id FROM customers WHERE first_name = 'Greg' AND last_name = 'Jones'), (SELECT item_id from items WHERE product = 'Small Desk'));

- PART II 
--- All purchases. Is this information useful to us?
SELECT * FROM purchases;

--- All purchases, joining with the customers table.
SELECT * 
FROM purchases p 
INNER JOIN customers c
ON p.customer_id = c.customer_id;

--- Purchases of the customer with the ID equal to 5.
SELECT * 
FROM purchases
WHERE customer_id = 5;

--- Purchases for a large desk AND a small desk
SELECT p.*, i.product
FROM purchases p 
INNER JOIN items i
ON p.item_id = i.item_id
WHERE product = 'Large desk' OR product = 'Small Desk';

SELECT c.first_name, c.last_name, i.product
FROM customers c 
INNER JOIN purchases p 
	ON p.customer_id = c.customer_id
INNER JOIN items i
	ON p.item_id = i.item_id;

-- Works as didn't define contrainst when creating foreign key
INSERT INTO purchases (quantity_purchased, customer_id)
VALUES (1, (SELECT customer_id FROM customers WHERE first_name = 'Sandra' AND last_name = 'Jones'));