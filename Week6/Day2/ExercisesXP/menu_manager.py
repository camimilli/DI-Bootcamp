import db_connection as db
import menu_item as m_i

class MenuManager:

    def get_by_name(self, item_name):
        '''
        Retrieves one row from menu_items database 
        based on item_name
        '''

        query = '''SELECT item_name, item_price FROM menu_items 
                   WHERE item_name = %s'''
        
        db.cursor.execute(query, (item_name,))
        row = db.cursor.fetchone()
        if row == None:
            return None 
        else:
            item_name, item_price = row 
            return m_i.MenuItem(item_name, item_price)
        

    def all_items(self):
        '''Returns a list of all the items from the menu_items table'''

        query = '''SELECT item_name, item_price FROM menu_items'''

        db.cursor.execute(query)
        rows = list(db.cursor.fetchall())
        return rows 

