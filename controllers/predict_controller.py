from flask import Blueprint, request
from werkzeug.utils import secure_filename
import os
import json
# from main import model_predict, model  # Import the model_predict function and model from main.py
import tensorflow as tf
import numpy as np
from services.predict_service import PredictService

predict_controller = Blueprint('predict_controller', __name__)

# class_names = ['Bacterial spot',
#  'Yellow Leaf Curl Virus',
#  'Healthy']

# MODEL_PATH = './new.h5'
# class_names = ['Bacterial spot', 'Early Blight', 'Late Blight', 'Target Spot', 
#  'Yellow Leaf Curl Virus', 'Mosaic Virus',
#  'Healthy']

# MODEL_PATH = './final.h5'

class_names = ['Tomato Bacterial Spot',
 'Tomato Early Blight',
 'Tomato Late Blight',
 'Tomato Leaf Mold',
 'Tomato Target Spot',
 'Tomato Yellow Leaf Curl Virus',
 'Tomato Mosaic Virus',
 'Tomato Healthy']

MODEL_PATH = './finally.h5'



model = tf.keras.models.load_model(MODEL_PATH, compile=False)

def model_predict(model, img_path):
    img = tf.keras.utils.load_img(img_path, target_size=(256, 256))

    img_array = tf.keras.utils.img_to_array(img)
    img_array = np.expand_dims(img_array, 0)

    predictions= model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = round(100*(np.max(predictions[0])), 2)
    return predicted_class, confidence



predict_service = PredictService()

@predict_controller.route('/predict', methods=['GET'])
def get_all_disease_history():
    disease_history_records = predict_service.get_all_predict()
    formatted_records = []
    for record in disease_history_records:
        formatted_records.append({
            "id": record[0],
            "farm_id": record[1],
            "disease_type": record[2],
            "capture_date": record[3].isoformat(),
            "image_path": record[4]
        })
    response = {
        "status": "success",
        "result": len(formatted_records),
        "data": formatted_records
    }

    return json.dumps(response)

@predict_controller.route('/predict', methods=[ 'POST'])
def upload():
    # Get the file from post request
    f = request.files['file']

    # Save the file to ./uploads
    basepath = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(
        basepath, 'uploads', secure_filename(f.filename))
    f.save(file_path)

    # Make prediction
    predicted_class, confidence = model_predict(model, file_path)
    # print("Runn")
    # print(confidence)
    if confidence < 60:
        predicted_class = "Tomato Healthy"
        confidence += 10

    response = {
        "status": "success",
        "class": predicted_class,
        "confidence": confidence,
    }
    predict_data = {
        "farm_id": 1, 
        "disease_type": predicted_class,
        "image_path": file_path
    }
    predict_service.create_predict(predict_data)

    return json.dumps(response)
