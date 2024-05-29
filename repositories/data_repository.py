# from flask_mysqldb import MySQL
import mysql.connector


class DataRepository:
    def __init__(self):
        self.connection = mysql.connector.connect(host='sql12.freesqldatabase.com', user='sql12710166', password='HLGccp9xiC', database='sql12710166')

    def create_data(self, data):
        cursor = self.connection.cursor()
        cursor.execute(''' INSERT INTO data(temp, humi, soilMoisture) VALUES(%s,%s,%s)''', (data['temp'], data['humi'], data['soilMoisture']))
        self.connection.commit()
        cursor.close()

    def get_all_data(self):
        cursor = self.connection.cursor()
        cursor.execute(''' SELECT * FROM data ''')
        data = cursor.fetchall()
        cursor.close()
        return data

    def get_data(self, id):
        cursor = self.connection.cursor()
        cursor.execute(''' SELECT * FROM data WHERE id = %s''', (id,))
        data = cursor.fetchone()
        cursor.close()
        return data

    def update_data(self, id, data):
        cursor = self.connection.cursor()
        cursor.execute(''' UPDATE data SET temp = %s, humi = %s, soilMoisture = %s WHERE id = %s''', (data['temp'], data['humi'], data['soilMoisture'], id))
        self.connection.commit()
        cursor.close()

    def delete_data(self, id):
        cursor = self.connection.cursor()
        cursor.execute(''' DELETE FROM data WHERE id = %s''', (id,))
        self.connection.commit()
        cursor.close()

    # def authenticate_user(self, email, password):
    #     cursor = self.connection.cursor()
    #     cursor.execute(''' SELECT * FROM users WHERE email = %s AND password = %s''', (email, password))
    #     user = cursor.fetchone()
    #     cursor.close()
    #     return user

    