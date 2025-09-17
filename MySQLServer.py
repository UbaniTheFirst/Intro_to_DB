import mysql.connector
from mysql.connector import Error

def create_database():
    """Create the alx_book_store database if it doesn't exist."""
    connection = None
    try:
        # Connect to MySQL server - UPDATE THESE CREDENTIALS
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Your MySQL username
            password='!Netbeans007SQL'  # Replace with your actual MySQL password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            print("Database 'alx_book_store' created successfully!")
            
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        
    finally:
        # Close the database connection
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
