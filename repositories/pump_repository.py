# from flask_mysqldb import MySQL
import mysql.connector

# Need to replace all information
class pumpRepository:
    def __init__(self):
        self.connection = mysql.connector.connect(host='localhost', user='nhatthien', password='12345', pumpbase='do_an')

    def create_pump(self, pump):
        cursor = self.connection.cursor()
        cursor.execute(''' INSERT INTO pump(temp, humi, soilMoisture) VALUES(%s,%s,%s)''', (pump['temp'], pump['humi'], pump['soilMoisture']))
        self.connection.commit()
        cursor.close()

    def get_all_pump(self):
        cursor = self.connection.cursor()
        cursor.execute(''' SELECT * FROM pump ''')
        pump = cursor.fetchone()
        cursor.close()
        return pump

    def get_pump(self, id):
        cursor = self.connection.cursor()
        cursor.execute(''' SELECT * FROM pump WHERE id = %s''', (id,))
        pump = cursor.fetchone()
        cursor.close()
        return pump

    def update_pump(self, id, pump):
        cursor = self.connection.cursor()
        cursor.execute(''' UPDATE pump SET temp = %s, humi = %s, soilMoisture = %s WHERE id = %s''', (pump['temp'], pump['humi'], pump['soilMoisture'], id))
        self.connection.commit()
        cursor.close()

    def delete_pump(self, id):
        cursor = self.connection.cursor()
        cursor.execute(''' DELETE FROM pump WHERE id = %s''', (id,))
        self.connection.commit()
        cursor.close()


    