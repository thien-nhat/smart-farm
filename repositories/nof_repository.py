
import db_connector 


# Need to replace all information
class NofRepository:

    def create_nof(self, nof):
        self.connection = db_connector.create_connection()
        cursor = self.connection.cursor()
        cursor.execute(''' INSERT INTO notification(message) VALUES(%s)''', (nof['message'],))  # note the comma
        self.connection.commit()
        cursor.close()
        self.connection.close()

    def get_all_nof(self):
        self.connection = db_connector.create_connection()
        cursor = self.connection.cursor()
        cursor.execute(''' SELECT * FROM notification ''')
        nof = cursor.fetchall()
        cursor.close()
        self.connection.close()
        return nof

    def get_nof(self, id):
        self.connection = db_connector.create_connection()
        cursor = self.connection.cursor()
        cursor.execute(''' SELECT * FROM notification WHERE id = %s''', (id,))
        nof = cursor.fetchone()
        cursor.close()
        self.connection.close()
        return nof


    def delete_nof(self, id):
        self.connection = db_connector.create_connection()
        cursor = self.connection.cursor()
        cursor.execute(''' DELETE FROM notification WHERE id = %s''', (id,))
        self.connection.commit()
        cursor.close()
        self.connection.close()


    