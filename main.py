import sys
import os
import glob
import re
import numpy as np
import json

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


# Define a flask app
app = Flask(__name__)

#model saved with Keras model.save()
MODEL_PATH = 'new.h5'
model = tf.keras.models.load_model(MODEL_PATH, compile=False)


# Load your trained model



print('Model loaded. Check http://127.0.0.1:5000/')

class_names = ['Tomato___Bacterial_spot',
 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
 'Tomato___healthy']

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
    return render_template('index.html')

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

        # Make prediction
        predicted_class, confidence = model_predict(model, file_path)

        return json.dumps({'class': predicted_class})
    return None

if __name__ == '__main__':
    app.run(debug=True)