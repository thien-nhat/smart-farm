import db_connector
import requests
API_URL = 'https://demo.thingsboard.io/api/plugins/telemetry/DEVICE/4c2fe410-cd78-11ed-9b15-dd2dac50548f/SHARED_SCOPE'
BEARER_TOKEN = "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ2YW4ucGhhbWRpbmh2YW4yMkBoY211dC5lZHUudm4iLCJ1c2VySWQiOiI1NGI3Njg1MC0xYjM0LTExZWYtYTQzNS1hYjNhMWQ1MzVmM2UiLCJzY29wZXMiOlsiVEVOQU5UX0FETUlOIl0sInNlc3Npb25JZCI6ImM2MWQwZGNjLTZmMDItNDdlYi1hMzA1LWU4NDZhOGNjNzk3ZiIsImV4cCI6MTcxODUwOTcyNCwiaXNzIjoidGhpbmdzYm9hcmQuaW8iLCJpYXQiOjE3MTY3MDk3MjQsImZpcnN0TmFtZSI6IlbEgk4iLCJsYXN0TmFtZSI6IlBI4bqgTSDEkMOMTkgiLCJlbmFibGVkIjp0cnVlLCJwcml2YWN5UG9saWN5QWNjZXB0ZWQiOnRydWUsImlzUHVibGljIjpmYWxzZSwidGVuYW50SWQiOiI2NTMzYWEzMC1iOGNiLTExZWQtOWIxNS1kZDJkYWM1MDU0OGYiLCJjdXN0b21lcklkIjoiMTM4MTQwMDAtMWRkMi0xMWIyLTgwODAtODA4MDgwODA4MDgwIn0.IDusyZ1K9xDDzyAI29F4ot5UFO5DwtsKFdydci233CJNl26qJrQ4LmMpLjET5oeULwVIBQWKfJq_Zxy0vXH76g"  # Replace with your actual Bearer token

headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }

# Need to replace all information
class PumpRepository:
        
    def create_pump(self, pump):
        self.connection = db_connector.create_connection()
        cursor = self.connection.cursor()
        cursor.execute(''' INSERT INTO pumps(pump_name, farm_id, status) VALUES(%s,%s,%s)''', 
                        (pump['pump_name'], pump['farm_id'], pump['status']))
        self.connection.commit()
        cursor.close()
        self.connection.close()

    def get_all_pump(self):
        self.connection = db_connector.create_connection()
        cursor = self.connection.cursor()
        cursor.execute(''' SELECT * FROM pumps ''')
        pump = cursor.fetchall()
        cursor.close()
        self.connection.close()
        return pump

    def get_pump(self, id):
        self.connection = db_connector.create_connection()
        cursor = self.connection.cursor()
        cursor.execute(''' SELECT * FROM pumps WHERE id = %s''', (id,))
        pump = cursor.fetchone()
        cursor.close()
        self.connection.close()
        return pump

    def update_pump(self, id, changes):
        self.connection = db_connector.create_connection()
        cursor = self.connection.cursor()

        sql = "UPDATE pumps SET " + ", ".join(f"{key} = %s" for key in changes.keys()) + " WHERE id = %s"
        params = list(changes.values()) + [id]

        cursor.execute(sql, params)
        self.connection.commit()
        cursor.close()
        self.connection.close()

    def delete_pump(self, id):
        self.connection = db_connector.create_connection()
        cursor = self.connection.cursor()
        cursor.execute(''' DELETE FROM pumps WHERE id = %s''', (id,))
        self.connection.commit()
        cursor.close()
        self.connection.close()

    def turn_pump_on(self):
        print("Turning on pump")
        try:
            requests.post(API_URL, headers=headers, json={'PUMP': 'ON'})
        except requests.RequestException as e:
            print(f"Error turn on pump !!!")

    def turn_pump_off(self):
        requests.post(API_URL, headers=headers, json={'PUMP': 'OFF'})


    