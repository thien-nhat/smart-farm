import mysql.connector

def create_connection():
    connection = mysql.connector.connect(host='sql12.freesqldatabase.com', user='sql12711906', password='r3ue1hrjUW', database='sql12711906')
    if connection.is_connected():
        print("Connected to MySQL database")
    else:
        print("Connection failed")
    return connection