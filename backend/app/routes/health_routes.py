from flask import Blueprint, jsonify

health_bp = Blueprint("health", __name__)


@health_bp.get("/health")
def health():
    return jsonify({
        "status": "ok",
        "project": "Abhinaya Darpanam",
        "message": "Backend is running."
    }), 200
