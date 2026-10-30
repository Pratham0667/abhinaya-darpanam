from flask import Blueprint, jsonify

auth_bp = Blueprint("auth", __name__)

@auth_bp.post("/auth/register")
def register():
    return jsonify({"status": "not_implemented", "message": "Registration will be implemented with the database and password hashing."}), 501

@auth_bp.post("/auth/login")
def login():
    return jsonify({"status": "not_implemented", "message": "Login will be implemented with the database and JWT."}), 501
