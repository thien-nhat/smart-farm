
import db_connector 


# Need to replace all information
class FarmRepository:

    def create_farm(self, farm):
        self.connection = db_connector.create_connection()
        cursor = self.connection.cursor()
        cursor.execute(''' INSERT INTO farms(temp, humi, soilMoisture) VALUES(%s,%s,%s)''', (farm['temp'], farm['humi'], farm['soilMoisture']))
        self.connection.commit()
        cursor.close()
        self.connection.close()

    def get_all_farm(self):
        self.connection = db_connector.create_connection()
        cursor = self.connection.cursor()
        cursor.execute(''' SELECT * FROM farms ''')
        farm = cursor.fetchall()
        cursor.close()
        self.connection.close()
        return farm

    def get_farm(self, id):
        self.connection = db_connector.create_connection()
        cursor = self.connection.cursor()
        cursor.execute(''' SELECT * FROM farms WHERE id = %s''', (id,))
        farm = cursor.fetchone()
        cursor.close()
        self.connection.close()
        return farm

    def update_farm(self, id, farm):
        self.connection = db_connector.create_connection()
        cursor = self.connection.cursor()
        cursor.execute(''' UPDATE farms SET temp = %s, humi = %s, soilMoisture = %s WHERE id = %s''', (farm['temp'], farm['humi'], farm['soilMoisture'], id))
        self.connection.commit()
        cursor.close()
        self.connection.close()

    def delete_farm(self, id):
        self.connection = db_connector.create_connection()
        cursor = self.connection.cursor()
        cursor.execute(''' DELETE FROM farms WHERE id = %s''', (id,))
        self.connection.commit()
        cursor.close()
        self.connection.close()


    