import db_connection as db

class MenuItem:

    def __init__(self, item_name, item_price):
        self.item_name = item_name
        self.item_price = item_price 

    def __str__(self):
        return f"Name: {self.item_name} || Price: {self.item_price}"

    def save(self):
        '''Inserts a new item in the table menu_items'''
        query = '''INSERT INTO menu_items (item_name, item_price)
                    VALUES (%s, %s)''' 

        db.cursor.execute(query, (self.item_name, self.item_price))
        db.connection.commit()
        
        # check where i close the cursor and the connection and open in classes 

    def delete(self):
        '''Deletes an item from the table Menu_Items'''
        query = '''DELETE FROM menu_items WHERE item_name = %s'''
        
        db.cursor.execute(query, (self.item_name,)) # comma and () create a single element tuple
        db.connection.commit()
        

    def update(self, new_name=None, new_price=None):
        '''Updates an item in the table Menu_Items'''

        # User didn't enter values for name and item 
        if new_name == None and new_price == None:
            print("You haven't provided any values to update your item, please enter item name, price, or both")
        
        else:
            # Update item_name only 
            if new_name != None and new_price == None:
                query = '''UPDATE menu_items
                            SET item_name = %s
                            WHERE item_name = %s''' 
                
                db.cursor.execute(query, (new_name, self.item_name))
                
                # Update attribute name 
                self.item_name = new_name
                
            # Update item_price only 
            elif new_price != None and new_name == None:
                query = '''UPDATE menu_items
                            SET item_price = %s
                            WHERE item_name = %s'''
                
                db.cursor.execute(query, (new_price, self.item_name))

                # Update attribute price 
                self.item_price = new_price

            else:
                query = '''UPDATE menu_items
                            SET item_name = %s, item_price = %s
                            WHERE item_name = %s'''
                
                db.cursor.execute(query, (new_name, new_price, self.item_name))
                
                # Update attributes name and price
                self.item_name = new_name
                self.item_price = new_price
           
            db.connection.commit()

        
    