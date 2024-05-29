import mysql.connector

def create_connection():
    connection = mysql.connector.connect(host='sql12.freesqldatabase.com', user='sql12710166', password='HLGccp9xiC', database='sql12710166')
    if connection.is_connected():
        print("Connected to MySQL database")
    else:
        print("Connection failed")
    return connection