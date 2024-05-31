import db_connector

# Need to replace all information
class PumpRepository:
        
    def create_pump(self, pump):
        self.connection = db_connector.create_connection()
        cursor = self.connection.cursor()
        cursor.execute(''' INSERT INTO pump(pump_name, farm_id, status, temp, humi, soilMoisture) VALUES(%s,%s,%s,%s,%s,%s)''', 
                        (pump['pump_name'], pump['farm_id'], pump['status'], pump['temp'], pump['humi'], pump['soilMoisture']))
        self.connection.commit()
        cursor.close()
        self.connection.close()

    def get_all_pump(self):
        self.connection = db_connector.create_connection()
        cursor = self.connection.cursor()
        cursor.execute(''' SELECT * FROM pump ''')
        pump = cursor.fetchall()
        cursor.close()
        self.connection.close()
        return pump

    def get_pump(self, id):
        self.connection = db_connector.create_connection()
        cursor = self.connection.cursor()
        cursor.execute(''' SELECT * FROM pump WHERE id = %s''', (id,))
        pump = cursor.fetchone()
        cursor.close()
        self.connection.close()
        return pump

    def update_pump(self, id, pump):
        self.connection = db_connector.create_connection()
        cursor = self.connection.cursor()
        cursor.execute(''' UPDATE pump SET temp = %s, humi = %s, soilMoisture = %s WHERE id = %s''', (pump['temp'], pump['humi'], pump['soilMoisture'], id))
        self.connection.commit()
        cursor.close()
        self.connection.close()

    def delete_pump(self, id):
        self.connection = db_connector.create_connection()
        cursor = self.connection.cursor()
        cursor.execute(''' DELETE FROM pump WHERE id = %s''', (id,))
        self.connection.commit()
        cursor.close()
        self.connection.close()


    