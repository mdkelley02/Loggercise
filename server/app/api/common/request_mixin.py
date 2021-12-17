from flask_restx import Resource
from functools import wraps
from flask import request
from firebase_admin import auth

def auth_required(func):
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return "Missing authorization header", 400
        try:
            decoded_token = auth.verify_id_token(token)
            kwargs["decoded_token"] = decoded_token
            return func(*args, **kwargs)
        except Exception as e:
            return "Invalid token", 400

        return wrapper

class AuthResource(Resource):
    method_decorators = [auth_required]