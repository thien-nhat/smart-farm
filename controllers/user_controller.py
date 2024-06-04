from flask import Blueprint, request
from services.user_service import UserService
import json
import datetime
from flask_jwt_extended import create_access_token

from email.message import EmailMessage
import ssl
import smtplib


# email_sender = 'ngonhatthien2@gmail.com'
email_sender = 'thien.webdev@gmail.com'
# email_password = 'ampc yiii dvma ddxs'
email_password = 'wntikcloxgiyuuzf'

user_controller = Blueprint('user_controller', __name__)
user_service = UserService()

@user_controller.route('/users', methods=['POST'])
def create_user():
    user_data = request.get_json()
    user_service.create_user(user_data)
    # return "User created successfully", 201
    response = {
            "status": "success",
            "message": 'User created successfully',
            "data": {
                "name": user_data['name'],
                "email": user_data['email']
            }
        }
    
    return json.dumps(response)

@user_controller.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user(user_id)
    print(user)
    response = {
        "status": "success",
        "data": {
            "id": user[0],
            "name": user[1],
            "email": user[2],
            "created_at": user[4].isoformat() if isinstance(user[4], datetime.date) else user[4]
        }
    }
    return json.dumps(response)

@user_controller.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user_data = request.get_json()
    user = user_service.update_user(user_id, user_data)
    return json.dumps(user)
@user_controller.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user_service.delete_user(user_id)
    # return '', 204
    return json.dumps({"message": 'User deleted successfully'})

@user_controller.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    user = user_service.authenticate_user(username, password)
    if user:
        access_token = create_access_token(identity={'id': user[0], 'username': username})
        response = {
            "status": "success",
            "token": access_token,
            "data": {
                "id": user[0],
                "name": user[1],
                "username": user[2],
                "email": user[3],
                "created_at": user[5].isoformat() if isinstance(user[4], datetime.date) else user[4]
            }
        }
        # em = EmailMessage()
        # em['From'] = "Smart Farm"
        # em['To'] =  user[3]
        # em['subject'] = 'Login Notification'
        # em.set_content('""" You have logged in to the system """')
        # context = ssl.create_default_context()
        # with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        #     smtp.login(email_sender, email_password)
        #     smtp.sendmail(email_sender, email, em.as_string())
            
        return json.dumps(response)
    else:
        return 'Invalid email or password'