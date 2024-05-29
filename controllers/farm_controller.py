from flask import Blueprint, request
from services.farm_service import FarmService
from flask_jwt_extended import jwt_required, get_jwt_identity
import json
import datetime


farm_controller = Blueprint('farm_controller', __name__)
farm_service = FarmService()

@farm_controller.route('/farm', methods=['GET'])
def get_all_farm():
    farms = farm_service.get_all_farm()
    formatted_farms = []
    for farm in farms:
        formatted_farms.append({
            "id": farm[0],
            "name": farm[1],
            "user_id": farm[2]
        })
    response = {
        "status": "success",
        "result": len(formatted_farms),
        "data": formatted_farms
    }
    return json.dumps(response)


@farm_controller.route('/farm', methods=['POST'])
def create_farm():
    farm = request.get_json()
    farm_service.create_farm(farm)
    response = {
            "status": "success",
            "message": 'farm created successfully',
            "data": {
                "id": farm['id'],
                "name": farm['name'],
                "user_id": farm['user_id']
            }
        }
    
    return json.dumps(response)

@farm_controller.route('/farm/<int:farm_id>', methods=['GET'])
@jwt_required()
def get_farm(farm_id):
    current_user = get_jwt_identity()
    user_id = current_user['id']
    print(user_id)

    farm = farm_service.get_farm(farm_id)
    print(farm)
    response = {
        "status": "success",
        "farm": {
            "id": farm[0],
            "name": farm[1],
            "user_id": farm[2],
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
