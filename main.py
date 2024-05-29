
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


app = Flask(__name__)
CORS(app)
app.register_blueprint(user_controller) # api service
app.register_blueprint(data_controller) # api service
app.register_blueprint(farm_controller) # api service
app.register_blueprint(pump_controller) # api service
app.register_blueprint(predict_controller) # api service

app.config['JWT_SECRET_KEY'] = 'thesis-secret-key' 
jwt = JWTManager(app)



API_URL = "http://localhost:8080/api/data"  # Replace with the actual API URL
BEARER_TOKEN = "your_bearer_token_here"  # Replace with your actual Bearer token

# Variable to store the latest data
latest_data = {"temp": None, "humidity": None}


def fetch_data():
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }
    try:
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        # Store or process the data as needed
        global latest_data
        latest_data = data
        print(f"Fetched data: {latest_data}")
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
    app.run(debug=True, port=5000)


