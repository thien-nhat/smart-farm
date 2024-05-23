import sys
import os
import glob
import re
import numpy as np
import json
import time

#keras
from keras.models import load_model
from keras.preprocessing import image

#tensorflow
import tensorflow as tf
from tensorflow.keras import models, layers
#flask
from flask import Flask, jsonify, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer
from flask import Flask
from flask_jwt_extended import JWTManager

import requests
from apscheduler.schedulers.background import BackgroundScheduler

from controllers.user_controller import user_controller #api service

# Config database
# from flask import Flask, render_template, request
# from flask_mysqldb import MySQL
# import MySQLdb

app = Flask(__name__)
app.register_blueprint(user_controller) # api service
app.config['JWT_SECRET_KEY'] = 'thesis-secret-key' 
jwt = JWTManager(app)

# app.config['MYSQL_HOST'] = "localhost"
# app.config['MYSQL_USER'] = "nhatthien"
# app.config['MYSQL_PASSWORD'] = "12345"
# app.config['MYSQL_DB'] = "shop"

# mysql = MySQL(app)
# try:
#     with app.app_context():

#         conn = mysql.connection
#         cursor = conn.cursor()
#         cursor.execute('SELECT 1')
# except MySQLdb.Error as e:
#     print(f"Error connecting to MySQL: {e}")


# Define a flask app
# app = Flask(__name__)
import mysql.connector
connection = mysql.connector.connect(host='localhost', user='nhatthien', password='12345', database='do_an')
if connection.is_connected():
    print("Connected to MySQL database")
else:
    print("Connection failed")

#model saved with Keras model.save()
MODEL_PATH = 'new.h5'
model = tf.keras.models.load_model(MODEL_PATH, compile=False)


# Load your trained model



print('Model loaded. Check http://127.0.0.1:5000/')

class_names = ['Tomato Bacterial spot',
 'Tomato Yellow Leaf Curl Virus',
 'Tomato Healthy']

def model_predict(model, img_path):
    img = tf.keras.utils.load_img(img_path, target_size=(256, 256))

    img_array = tf.keras.utils.img_to_array(img)
    img_array = np.expand_dims(img_array, 0)

    predictions= model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = round(100*(np.argmax(predictions[0])), 2)
    return predicted_class, confidence

@app.route('/', methods=['GET'])
def index():
    return json.dumps({"message": "Hello"})

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # if file_path is None or file_path.empty():
        # time.sleep(0.025)
        # file_path = "uploads\predict.JPG"
        
        # Make prediction
        predicted_class, confidence = model_predict(model, file_path)
        response = {
            "status": "success",
            "class": predicted_class,
        }
        return json.dumps(response)
    return None

# @app.route('/login', methods = ['POST', 'GET'])
# def login():
#     if request.method == 'GET':
#         return "Login via the login Form"
     
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         password = request.form['password']
#         cursor = connection.cursor()
#         print(name, email, password)
#         cursor.execute(''' INSERT INTO users(name, email, password) VALUES(%s,%s,%s)''',(name,email, password))
#         connection.commit()
#         cursor.close()
#         return "Done!!"


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


app.run(host='localhost', port=5000)

if __name__ == '__main__':
    app.run(debug=True)