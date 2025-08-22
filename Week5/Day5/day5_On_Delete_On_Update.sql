--- PARENT TABLE
-- CREATE TABLE colors (
-- color_id SERIAL PRIMARY KEY,
-- name VARCHAR(50)
-- ); 

-- INSERT INTO colors (name)
-- VALUES ('blue'), ('yellow'), ('pink');

-- SELECT * FROM colors;

-- OPTIONS ON WHAT HAPPENS IF I DELETE A ROW ON THE PARENT TABLE:
-- OPTION 1 - RESTRICT
----- ON DELETE RESTRICT: It is not possible to delete a record if it is related to another table
----- ON UPDATE RESTRICT: Same as delete but is update (if I'm trying to change the value)

---- CHILD TABLE
-- CREATE TABLE cars_rstrict (
-- car_id SERIAL PRIMARY KEY,
-- car_name VARCHAR(100),
-- car_color INTEGER REFERENCES colors (color_id) ON DELETE RESTRICT ON UPDATE RESTRICT
-- );


-- INSERT INTO cars_rstrict (car_name, car_color) VALUES ('Toyota', 1), ('Ford', 2), ('Honda', 3);

-- SELECT * FROM cars_rstrict;

-- TRY TO DELETE COLOR BLUE FROM PARENT TABLE 
-- DELETE FROM colors WHERE name = 'blue';
-- GIVES AN ERROR: 
--ERROR:  update or delete on table "colors" violates foreign key constraint "cars_rstrict_car_color_fkey" on table "cars_rstrict"
--Key (color_id)=(1) is still referenced from table "cars_rstrict". 


-- OPTION 2 - CASCADE (MOST USED, BEST FOR UPDATE) 
----- ON DELETE CASCADE: Deletes the record and the reference on the child will be deleted as well from the child table
----- ON UPDATE CASCADE: Same as delete but is update (if I'm trying to change the value)

-- CREATE TABLE cars_cascade (
-- car_id SERIAL PRIMARY KEY,
-- car_name VARCHAR(100),
-- car_color INTEGER REFERENCES colors (color_id) ON DELETE CASCADE ON UPDATE CASCADE
-- );

-- INSERT INTO cars_cascade (car_name, car_color) VALUES ('Toyota', 1), ('Ford', 2), ('Honda', 3);

-- DELETE FROM colors WHERE name = 'blue'; -- Removes Toyota that has blue as reference 
-- UPDATE colors SET color_id = 10 WHERE color_id = 2; -- Changes the reference from 2 to 10 in the child's parent

-- SELECT * FROM cars_cascade;






