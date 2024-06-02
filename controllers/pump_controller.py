from flask import Blueprint, request
from services.pump_service import PumpService
import json
import datetime


pump_controller = Blueprint('pump_controller', __name__)
pump_service = PumpService()

@pump_controller.route('/pump', methods=['GET'])
def get_all_pump():
    nofs = pump_service.get_all_pump()
    formatted_nofs = []
    for nof in nofs:
        formatted_nofs.append({
            "id": nof[0],
            "name": nof[1],
            "status": nof[3]
        })
    response = {
        "status": "success",
        "result": len(formatted_nofs),
        "data": formatted_nofs
    }
    return json.dumps(response)

@pump_controller.route('/pump', methods=['POST'])
def create_pump():
    pump = request.get_json()
    pump_service.create_pump(pump)
    # return "pump created successfully", 201
    response = {
            "status": "success",
            "message": 'pump created successfully',
        }
    
    return json.dumps(response)

@pump_controller.route('/pump/<int:pump_id>', methods=['GET'])
def get_pump(pump_id):
    pump = pump_service.get_pump(pump_id)
    print(pump)
    response = {
        "status": "success",
        "pump": {
            "id": pump[0],
            "name": pump[1],
            "email": pump[2],
            "created_at": pump[4].isoformat() if isinstance(pump[4], datetime.date) else pump[4]
        }
    }
    return json.dumps(response)

@pump_controller.route('/pump/<int:pump_id>', methods=['PUT'])
def update_pump(pump_id):
    pump = request.get_json()
    pump = pump_service.update_pump(pump_id, pump)
    return json.dumps(pump)
@pump_controller.route('/pump/<int:pump_id>', methods=['DELETE'])
def delete_pump(pump_id):
    pump_service.delete_pump(pump_id)
    # return '', 204
    return json.dumps({"message": 'pump deleted successfully'})
