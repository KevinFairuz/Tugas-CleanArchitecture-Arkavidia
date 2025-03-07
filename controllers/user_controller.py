from flask import request, jsonify
from services.user_service import UserService

def get_users():
    users = UserService.get_users()
    return jsonify(users)

def create_user():
  data = request.get_json()
  response = UserService.create_user(data)
  return jsonify(response)
