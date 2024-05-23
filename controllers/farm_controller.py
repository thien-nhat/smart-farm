from flask import Blueprint, request
from services.farm_service import farmService
import json
import datetime


farm_controller = Blueprint('farm_controller', __name__)
farm_service = farmService()

@farm_controller.route('/farm', methods=['POST'])
def create_farm():
    farm_farm = request.get_json()
    farm_service.create_farm(farm)
    # return "farm created successfully", 201
    response = {
            "status": "success",
            "message": 'farm created successfully',
            "farm": {
                "temp": farm['temp'],
                "humi": farm['humi'],
                "soilMosdule": farm['soilMosdule']
            }
        }
    
    return json.dumps(response)

@farm_controller.route('/farm/<int:farm_id>', methods=['GET'])
def get_farm(farm_id):
    farm = farm_service.get_farm(farm_id)
    print(farm)
    response = {
        "status": "success",
        "farm": {
            "id": farm[0],
            "name": farm[1],
            "email": farm[2],
            "created_at": farm[4].isoformat() if isinstance(farm[4], datetime.date) else farm[4]
        }
    }
    return json.dumps(response)

@farm_controller.route('/farm/<int:farm_id>', methods=['PUT'])
def update_farm(farm_id):
    farm = request.get_json()
    farm = farm_service.update_farm(farm_id, farm)
    return json.dumps(farm)
@farm_controller.route('/farm/<int:farm_id>', methods=['DELETE'])
def delete_farm(farm_id):
    farm_service.delete_farm(farm_id)
    # return '', 204
    return json.dumps({"message": 'farm deleted successfully'})
