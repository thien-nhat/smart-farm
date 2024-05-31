from flask import Blueprint, request
from services.nof_service import NofService
from flask_jwt_extended import jwt_required, get_jwt_identity
import json
import datetime


nof_controller = Blueprint('nof_controller', __name__)
nof_service = NofService()

@nof_controller.route('/nof', methods=['GET'])
def get_all_nof():
    nofs = nof_service.get_all_nof()
    formatted_nofs = []
    for nof in nofs:
        formatted_nofs.append({
            "id": nof[0],
            "message": nof[1]
        })
    response = {
        "status": "success",
        "result": len(formatted_nofs),
        "data": formatted_nofs
    }
    return json.dumps(response)


@nof_controller.route('/nof', methods=['POST'])
def create_nof():
    nof = request.get_json()
    nof_service.create_nof(nof)
    response = {
            "status": "success",
            "message": 'nof created successfully',
            "data": {
                "message": nof['message']
            }
        }
    
    return json.dumps(response)

# @nof_controller.route('/nof/<int:nof_id>', methods=['GET'])
# @jwt_required()
# def get_nof(nof_id):
#     current_user = get_jwt_identity()
#     user_id = current_user['id']
#     print(user_id)

#     nof = nof_service.get_nof(nof_id)
#     print(nof)
#     response = {
#         "status": "success",
#         "nof": {
#             "id": nof[0],
#             "name": nof[1],
#             "user_id": nof[2],
#             "created_at": nof[4].isoformat() if isinstance(nof[4], datetime.date) else nof[4]
#         }
#     }
#     return json.dumps(response)

# @nof_controller.route('/nof/<int:nof_id>', methods=['PUT'])
# def update_nof(nof_id):
#     nof = request.get_json()
#     nof = nof_service.update_nof(nof_id, nof)
#     return json.dumps(nof)
# @nof_controller.route('/nof/<int:nof_id>', methods=['DELETE'])
# def delete_nof(nof_id):
#     nof_service.delete_nof(nof_id)
#     return json.dumps({"message": 'nof deleted successfully'})
