import psycopg2
# from psycopg2 import OperationalError
import config as c 

def get_db_connection():
    '''Establishes and returns a new database connection.'''

    try:
        connection = psycopg2.connect (
            database = c.DATABASE,
            user = c.USER,
            password = c.PASSWORD,
            host = c.HOST,
            port = c.PORT
        )
        return connection 
    except psycopg2.OperationalError as e:
        print(f"The error '{e}' occurred")
        return None 


    