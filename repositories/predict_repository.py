# import mysql.connector
# from db_connector import connection
import db_connector


class PredictRepository:
    # def __init__(self):
    #     self.connection = connection.create_connection()
        
    def create_predict(self, disease_history_data):
        self.connection = db_connector.create_connection()
        query = "INSERT INTO diseasehistory (farm_id, disease_type,  image_path) VALUES (%s, %s, %s)"
        
        values = (disease_history_data['farm_id'], disease_history_data['disease_type'], disease_history_data['image_path'])
        cursor = self.connection.cursor()
        cursor.execute(query, values)
        self.connection.commit()
        cursor.close()
        self.connection.close()

    def get_all_predict(self):
        # Your code to get all disease history records goes here
        self.connection = db_connector.create_connection()
        cursor = self.connection.cursor()
        cursor.execute(''' SELECT * FROM diseasehistory ''')
        disease_history = cursor.fetchall()
        cursor.close()
        self.connection.close()
        return disease_history

    def get_predict(self, id):
        # Your code to get a specific disease history record by id goes here
        self.connection = db_connector.create_connection()
        cursor = self.connection.cursor()
        cursor.execute(''' SELECT * FROM diseasehistory WHERE id = %s''', (id,))
        disease_history = cursor.fetchone()
        cursor.close()
        self.connection.close()
        return disease_history