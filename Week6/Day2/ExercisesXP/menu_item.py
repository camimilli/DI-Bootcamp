import db_connection as db
import psycopg2

class MenuItem:

    def __init__(self, item_name, item_price):
        self.item_name = item_name
        self.item_price = item_price 

    def __str__(self):
        return f"Name: {self.item_name} || Price: {self.item_price}"

    def save(self):
        '''Inserts a new item in the table menu_items'''

        connection = db.get_db_connection()
        if connection:
            try:
                with connection.cursor() as cursor:
                    query = '''INSERT INTO menu_items (item_name, item_price)
                               VALUES (%s, %s)''' 

                    cursor.execute(query, (self.item_name, self.item_price))
                    connection.commit()
            except psycopg2.Error as e:
                print("Database Error: {e}")
            finally:
                connection.close()
        
        

    def delete(self):
        '''Deletes an item from the table Menu_Items'''

        connection = db.get_db_connection()
        if connection:
            try:
                with connection.cursor() as cursor:
                    query = '''DELETE FROM menu_items WHERE item_name = %s''' 
                    cursor.execute(query, (self.item_name,)) # comma and () create a single element tuple
                    connection.commit()
            except psycopg2.Error as e:
                print("Database error: {e}")
            finally:
                connection.close()
        

    def update(self, new_name=None, new_price=None):
        '''Updates an item in the table Menu_Items'''

        # No values provided for either argument  
        if new_name == None and new_price == None:
            print("You haven't provided any values to update your item, please enter item name, price, or both")
        
        else:
            connection = db.get_db_connection()
            if connection:
                with connection.cursor() as cursor:
                    try:
                        if new_name != None and new_price == None:
                            query = '''UPDATE menu_items
                                        SET item_name = %s
                                        WHERE item_name = %s''' 
                            
                            cursor.execute(query, (new_name, self.item_name))
                            
                            # Update attribute name 
                            self.item_name = new_name
                            
                        # Update item_price only 
                        elif new_price != None and new_name == None:
                            query = '''UPDATE menu_items
                                        SET item_price = %s
                                        WHERE item_name = %s'''
                            
                            cursor.execute(query, (new_price, self.item_name))

                            # Update attribute price 
                            self.item_price = new_price

                        else:
                            query = '''UPDATE menu_items
                                        SET item_name = %s, item_price = %s
                                        WHERE item_name = %s'''
                            
                            cursor.execute(query, (new_name, new_price, self.item_name))
                            
                            # Update attributes name and price
                            self.item_name = new_name
                            self.item_price = new_price
                    
                        connection.commit()
                    
                    except psycopg2.Error as e:
                        print(f"Database error: {e}")
                    finally:
                        connection.close()

        
    