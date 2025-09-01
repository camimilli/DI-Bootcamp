-- Daily Challenge: Items And Orders 

CREATE TABLE items (
	item_id SERIAL PRIMARY KEY, 
	item_name VARCHAR(100) NOT NULL,
	price SMALLINT NOT NULL
);

CREATE TABLE product_orders (
	order_id SERIAL PRIMARY KEY,
	item_id INT NOT NULL,
	quantity SMALLINT NOT NULL, 
	FOREIGN KEY (item_id) REFERENCES items (item_id) 
);

INSERT INTO items (item_name, price)
VALUES
	('Macbook Pro', 15000),
	('iPhone 11', 2500),
	('Apple Watch Gen 2', 3000),
	('iPad Pro', 7000),
	('iPencil Gen 2', 1500);

INSERT INTO product_orders (item_id, quantity)
VALUES 
	((SELECT item_id FROM items WHERE item_name = 'Macbook Pro'), 1),
	((SELECT item_id FROM items WHERE item_name = 'iPad Pro'), 2);


SELECT p_o.order_id, i.price * p_o.quantity as total_price
FROM product_orders p_o 
INNER JOIN items i 
ON p_o.item_id = i.item_id;


-- Bonus
CREATE TABLE users (
	user_id SERIAL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(100) NOT NULL
);

INSERT INTO users (first_name, last_name)
VALUES
	('John', 'Doe'),
	('Valeria', 'Mazza'),
	('Micaela', 'Lonmann')

ALTER TABLE product_orders 
ADD user_id INT;

ALTER TABLE product_orders
ADD FOREIGN KEY (user_id) REFERENCES users (user_id);

UPDATE product_orders
SET user_id = (SELECT user_id FROM users WHERE first_name = 'Valeria')
WHERE order_id = 1;

UPDATE product_orders
SET user_id = (SELECT user_id FROM users WHERE first_name = 'Micaela')
WHERE order_id = 2;

SELECT * FROM product_orders;



