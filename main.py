
from flask import Flask, jsonify
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS

import requests
from apscheduler.schedulers.background import BackgroundScheduler

from controllers.user_controller import user_controller #api service
from controllers.data_controller import data_controller #api service
from controllers.farm_controller import farm_controller #api service
from controllers.pump_controller import pump_controller #api service
from controllers.predict_controller import predict_controller #api servicepump_controller #api service
from controllers.nof_controller import nof_controller #api servicepump_controller #api service


app = Flask(__name__)
CORS(app)
app.register_blueprint(user_controller) # api service
app.register_blueprint(data_controller) # api service
app.register_blueprint(farm_controller) # api service
app.register_blueprint(pump_controller) # api service
app.register_blueprint(predict_controller) # api service
app.register_blueprint(nof_controller) # api service

app.config['JWT_SECRET_KEY'] = 'thesis-secret-key' 
jwt = JWTManager(app)



API_URL = "https://demo.thingsboard.io/api/plugins/telemetry/DEVICE/4c2fe410-cd78-11ed-9b15-dd2dac50548f/values/timeseries?keys=temperature%2Chumidity%2CsoilMoisture&useStrictDataTypes=true&fbclid=IwAR1Cu4BUQYVIJVR_fOmmypSm2BXehnid8iO__7dOVAUnDy6-eX8NgtoLgpA"  # Replace with the actual API URL
BEARER_TOKEN = "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ2YW4ucGhhbWRpbmh2YW4yMkBoY211dC5lZHUudm4iLCJ1c2VySWQiOiI1NGI3Njg1MC0xYjM0LTExZWYtYTQzNS1hYjNhMWQ1MzVmM2UiLCJzY29wZXMiOlsiVEVOQU5UX0FETUlOIl0sInNlc3Npb25JZCI6ImM2MWQwZGNjLTZmMDItNDdlYi1hMzA1LWU4NDZhOGNjNzk3ZiIsImV4cCI6MTcxODUwOTcyNCwiaXNzIjoidGhpbmdzYm9hcmQuaW8iLCJpYXQiOjE3MTY3MDk3MjQsImZpcnN0TmFtZSI6IlbEgk4iLCJsYXN0TmFtZSI6IlBI4bqgTSDEkMOMTkgiLCJlbmFibGVkIjp0cnVlLCJwcml2YWN5UG9saWN5QWNjZXB0ZWQiOnRydWUsImlzUHVibGljIjpmYWxzZSwidGVuYW50SWQiOiI2NTMzYWEzMC1iOGNiLTExZWQtOWIxNS1kZDJkYWM1MDU0OGYiLCJjdXN0b21lcklkIjoiMTM4MTQwMDAtMWRkMi0xMWIyLTgwODAtODA4MDgwODA4MDgwIn0.IDusyZ1K9xDDzyAI29F4ot5UFO5DwtsKFdydci233CJNl26qJrQ4LmMpLjET5oeULwVIBQWKfJq_Zxy0vXH76g"  # Replace with your actual Bearer token

# Variable to store the latest data
latest_data = {"temp": None, "humi": None, "soilMoisture": None}


from services.data_service import DataService

data_service = DataService()

def fetch_data():
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }
    try:
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        # Store or process the data as needed
        data1 = {
                'temp': data['temperature'][0]['value'],
                'humi': data['humidity'][0]['value'],
                'soilMoisture': data['soilMoisture'][0]['value']
        }
        global latest_data
        if data1 != latest_data:
            latest_data = data1
            print(f"Fetched data: {latest_data}")
            
            # data_service.create_data(data)  # Call the create_data method
            if 'temp' in data1 and 'humi' in data1 and 'soilMoisture' in data1:
                data_service.create_data(data1)  # Call the create_data method
            else:
                print("Fetched data does not contain 'temp', 'humi', or 'soilMoisture'.")
        else:
            print("Data is the same as the latest data. No new data fetched.")
    except requests.RequestException as e:
        print(f"Error fetching data !!!")

# Scheduler to fetch data every 10 seconds
scheduler = BackgroundScheduler()
scheduler.add_job(fetch_data, 'interval', seconds=10)
scheduler.start()

@app.route('/latest-data', methods=['GET'])
def get_latest_data():
    return jsonify(latest_data)


# app.run(host='localhost', port=5000)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000, debug=False)
    # app.run(host='localhost', port=5000)


