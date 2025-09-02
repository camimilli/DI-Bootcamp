import psycopg2 
import db_connection as db
import menu_item as m_i

class MenuManager:

    @staticmethod 
    def get_by_name(item_name):
        '''
        Retrieves one row from menu_items database 
        based on item_name
        '''
        connection = db.get_db_connection()
        if connection:
            try:
                with connection.cursor() as cursor:
                    query = '''SELECT item_name, item_price FROM menu_items WHERE item_name = %s'''
                    cursor.execute(query, (item_name,))
                    row = cursor.fetchone()

                if row:
                    item_name, item_price = row 
                    return m_i.MenuItem(item_name, item_price)
                else:
                    return None 
            except psycopg2.Error as e:
                print(f'Database error: {e}')
                return None
            finally:
                connection.close()
        
        return None
            
        
    @classmethod
    def all_items(cls):
        '''Returns a list of all the items from the menu_items table'''

        connection = db.get_db_connection()
        if connection:
            try:
                with connection.cursor() as cursor:
                    query = '''SELECT item_name, item_price FROM menu_items'''
                    cursor.execute(query)
                    rows = list(cursor.fetchall())
                    list_item_objects = []
                    for row in rows:
                        item_name, item_price = row 
                        list_item_objects.append(m_i.MenuItem(item_name, item_price))
                    return list_item_objects 
            
            except psycopg2.Error as e:
                print(f"Database error: {e}")
                return []
            
            finally:
                connection.close()

        return []
