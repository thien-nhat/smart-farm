import db_connector



class DataRepository:


    def create_data(self, data):
        self.connection = db_connector.create_connection()
        cursor = self.connection.cursor()
        cursor.execute(''' INSERT INTO data(temperature, humidity, soilMoisture) VALUES(%s,%s,%s)''', (data['temp'], data['humi'], data['soilMoisture']))
        self.connection.commit()
        cursor.close()
        self.connection.close()

    def get_all_data(self):
        self.connection = db_connector.create_connection()
        cursor = self.connection.cursor()
        cursor.execute(''' SELECT * FROM data ORDER BY ts DESC ''')
        data = cursor.fetchall()
        cursor.close()
        self.connection.close()
        return data
    def get_latest_data(self):
        self.connection = db_connector.create_connection()
        cursor = self.connection.cursor()
        query = "SELECT * FROM data ORDER BY ts DESC LIMIT 1"
        cursor.execute(query)
        result = cursor.fetchone()
        self.connection.close()
        return result
    def get_daily_average(self):
        self.connection = db_connector.create_connection()
        cursor = self.connection.cursor()
        query = """
        SELECT AVG(temperature) as temperature, AVG(humidity) as humidity, AVG(soilMoisture) as soilMoisture,  DATE(ts) as date
        FROM data
        GROUP BY DATE(ts)
        """
        cursor.execute(query)
        result = cursor.fetchall()
        self.connection.close()
        return result
    def get_data(self, id):
        self.connection = db_connector.create_connection()
        cursor = self.connection.cursor()
        cursor.execute(''' SELECT * FROM data WHERE id = %s''', (id,))
        data = cursor.fetchone()
        cursor.close()
        self.connection.close()
        return data

    def update_data(self, id, data):
        self.connection = db_connector.create_connection()
        cursor = self.connection.cursor()
        cursor.execute(''' UPDATE data SET temp = %s, humi = %s, soilMoisture = %s WHERE id = %s''', (data['temp'], data['humi'], data['soilMoisture'], id))
        self.connection.commit()
        cursor.close()
        self.connection.close()

    def delete_data(self, id):
        self.connection = db_connector.create_connection()
        cursor = self.connection.cursor()
        cursor.execute(''' DELETE FROM data WHERE id = %s''', (id,))
        self.connection.commit()
        cursor.close()
        self.connection.close()

    # def authenticate_user(self, email, password):
    #     cursor = self.connection.cursor()
    #     cursor.execute(''' SELECT * FROM users WHERE email = %s AND password = %s''', (email, password))
    #     user = cursor.fetchone()
    #     cursor.close()
    #     return user

    