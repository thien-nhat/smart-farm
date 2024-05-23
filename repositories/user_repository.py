# from flask_mysqldb import MySQL
import mysql.connector


class UserRepository:
    def __init__(self):
        self.connection = mysql.connector.connect(host='localhost', user='nhatthien', password='12345', database='do_an')

    def create_user(self, user_data):
        cursor = self.connection.cursor()
        cursor.execute(''' INSERT INTO users(name, email, password) VALUES(%s,%s,%s)''', (user_data['name'], user_data['email'], user_data['password']))
        self.connection.commit()
        cursor.close()
    def get_user(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute(''' SELECT * FROM users WHERE id = %s''', (user_id,))
        user = cursor.fetchone()
        cursor.close()
        return user

    def update_user(self, user_id, user_data):
        cursor = self.connection.cursor()
        cursor.execute(''' UPDATE users SET name = %s, email = %s, password = %s WHERE id = %s''', (user_data['name'], user_data['email'], user_data['password'], user_id))
        self.connection.commit()
        cursor.close()

    def delete_user(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute(''' DELETE FROM users WHERE id = %s''', (user_id,))
        self.connection.commit()
        cursor.close()

    def authenticate_user(self, email, password):
        cursor = self.connection.cursor()
        cursor.execute(''' SELECT * FROM users WHERE email = %s AND password = %s''', (email, password))
        user = cursor.fetchone()
        cursor.close()
        return user

    