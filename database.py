import os
import mysql.connector

# Read database credentials from environment variables
# Sensitive Information
host = os.environ.get('DB_HOST')
user = os.environ.get('DB_USER')
password = os.environ.get('DB_PASSWORD')
database = os.environ.get('DB_DATABASE')

# Establish connection to MySQL database
try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    # Check if connection is successful
    if connection.is_connected():
        print("Connected to MySQL database")
    
    # Create cursor object
    cursor = connection.cursor()
    
    # Execute SQL query
    cursor.execute("SELECT * FROM your_table")
    
    # Fetch all rows
    rows = cursor.fetchall()
    
    # Print fetched rows
    for row in rows:
        print(row)

except mysql.connector.Error as e:
    print("Error connecting to MySQL database:", e)

finally:
    # Closing the database connection
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
