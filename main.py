import psycopg2
from config import config

def connect():
    connection = None
    
    try:
        # Assuming 'config' is a dictionary containing the connection parameters
        params = config()
        print('Connecting to PostgreSQL...')
        
        # Debugging print to check type of 'params'
        print(f'Type of params: {type(params)}')
        connection = psycopg2.connect(**params)
        
        cursor = connection.cursor()
        print('PostgreSQL database version:')
        cursor.execute('SELECT version()')
        db_version = cursor.fetchone()
        print(db_version)
        cursor.close()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if connection is not None:
            connection.close()
            print("Database connection terminated")
            
            
if __name__=="__main__":
    connect()