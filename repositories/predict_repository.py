# import mysql.connector
from db_connector import connection


class PredictRepository:
    def __init__(self):
        self.connection = connection
        
    def create_predict(self, disease_history_data):
        query = "INSERT INTO diseasehistory (farm_id, disease_type,  image_path) VALUES (%s, %s, %s)"
        
        values = (disease_history_data['farm_id'], disease_history_data['disease_type'], disease_history_data['image_path'])
        cursor = self.connection.cursor()
        cursor.execute(query, values)
        self.connection.commit()
        cursor.close()

    def get_all_predict(self):
        # Your code to get all disease history records goes here
        cursor = self.connection.cursor()
        cursor.execute(''' SELECT * FROM diseasehistory ''')
        disease_history = cursor.fetchall()
        cursor.close()
        return disease_history

    def get_predict(self, id):
        # Your code to get a specific disease history record by id goes here
        cursor = self.connection.cursor()
        cursor.execute(''' SELECT * FROM diseasehistory WHERE id = %s''', (id,))
        disease_history = cursor.fetchone()
        cursor.close()
        return disease_history