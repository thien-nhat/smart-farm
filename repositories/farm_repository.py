# from flask_mysqldb import MySQL
import mysql.connector

# Need to replace all information
class FarmRepository:
    def __init__(self):
        self.connection = mysql.connector.connect(host='localhost', user='nhatthien', password='12345', farmbase='do_an')

    def create_farm(self, farm):
        cursor = self.connection.cursor()
        cursor.execute(''' INSERT INTO farm(temp, humi, soilMoisture) VALUES(%s,%s,%s)''', (farm['temp'], farm['humi'], farm['soilMoisture']))
        self.connection.commit()
        cursor.close()

    def get_all_farm(self):
        cursor = self.connection.cursor()
        cursor.execute(''' SELECT * FROM farm ''')
        farm = cursor.fetchone()
        cursor.close()
        return farm

    def get_farm(self, id):
        cursor = self.connection.cursor()
        cursor.execute(''' SELECT * FROM farm WHERE id = %s''', (id,))
        farm = cursor.fetchone()
        cursor.close()
        return farm

    def update_farm(self, id, farm):
        cursor = self.connection.cursor()
        cursor.execute(''' UPDATE farm SET temp = %s, humi = %s, soilMoisture = %s WHERE id = %s''', (farm['temp'], farm['humi'], farm['soilMoisture'], id))
        self.connection.commit()
        cursor.close()

    def delete_farm(self, id):
        cursor = self.connection.cursor()
        cursor.execute(''' DELETE FROM farm WHERE id = %s''', (id,))
        self.connection.commit()
        cursor.close()


    