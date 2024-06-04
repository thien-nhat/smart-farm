# from flask_mysqldb import MySQL
# import mysql.connector
import db_connector


class UserRepository:

        
    def create_user(self, user_data):
        self.connection = db_connector.create_connection()
        cursor = self.connection.cursor()
        cursor.execute(''' INSERT INTO users(name, email, password) VALUES(%s,%s,%s)''', (user_data['name'], user_data['email'], user_data['password']))
        self.connection.commit()
        cursor.close()
        self.connection.close()
    def get_user(self, user_id):
        self.connection = db_connector.create_connection()
        cursor = self.connection.cursor()
        cursor.execute(''' SELECT * FROM users WHERE id = %s''', (user_id,))
        user = cursor.fetchone()
        cursor.close()
        self.connection.close()
        return user

    def update_user(self, user_id, user_data):
        self.connection = db_connector.create_connection()
        cursor = self.connection.cursor()
        cursor.execute(''' UPDATE users SET name = %s, email = %s, password = %s WHERE id = %s''', (user_data['name'], user_data['email'], user_data['password'], user_id))
        self.connection.commit()
        cursor.close()
        self.connection.close()

    def delete_user(self, user_id):
        self.connection = db_connector.create_connection()
        cursor = self.connection.cursor()
        cursor.execute(''' DELETE FROM users WHERE id = %s''', (user_id,))
        self.connection.commit()
        cursor.close()
        self.connection.close()

    def authenticate_user(self, username, password):
        self.connection = db_connector.create_connection()
        cursor = self.connection.cursor()
        cursor.execute(''' SELECT * FROM users WHERE username = %s AND password = %s''', (username, password))
        user = cursor.fetchone()
        cursor.close()
        self.connection.close()
        return user

    