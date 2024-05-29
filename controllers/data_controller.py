from flask import Blueprint, request
from services.data_service import DataService
import json
import datetime


data_controller = Blueprint('data_controller', __name__)
data_service = DataService()

@data_controller.route('/api/data', methods=['GET'])
def get_all_data():
    data = data_service.get_all_data()
    formatted_data = []
    for i in range(len(data)):
        if isinstance(data[i][4], datetime.date):
            data[i] = list(data[i])
            data[i][4] = data[i][4].isoformat()
            data[i] = tuple(data[i])
        formatted_data.append({
            "id": data[i][0],
            "temperature": data[i][1],
            "humidity": data[i][2],
            "soilMoisture": data[i][3],
            "ts": data[i][4]
        })
    
    response = {
        "status": "success",
        "result": len(formatted_data),
        "data": formatted_data
    }
    return json.dumps(response)

@data_controller.route('/api/data', methods=['POST'])
def create_data():
    data = request.get_json()
    data_service.create_data(data)
    # return "data created successfully", 201
    response = {
            "status": "success",
            "message": 'data created successfully',
            "data": {
                "temp": data['temp'],
                "humi": data['humi'],
                "soilMosdule": data['soilMosdule']
            }
        }
    
    return json.dumps(response)

@data_controller.route('/api/data/<int:data_id>', methods=['GET'])
def get_data(data_id):
    data = data_service.get_data(data_id)
    print(data)
    response = {
        "status": "success",
        "data": {
            "id": data[0],
            "name": data[1],
            "email": data[2],
            "created_at": data[4].isoformat() if isinstance(data[4], datetime.date) else data[4]
        }
    }
    return json.dumps(response)

@data_controller.route('/api/data/<int:data_id>', methods=['PUT'])
def update_data(data_id):
    data = request.get_json()
    data = data_service.update_data(data_id, data)
    return json.dumps(data)
@data_controller.route('/api/data/<int:data_id>', methods=['DELETE'])
def delete_data(data_id):
    data_service.delete_data(data_id)
    # return '', 204
    return json.dumps({"message": 'data deleted successfully'})
