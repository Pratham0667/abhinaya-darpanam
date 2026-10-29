from flask import Blueprint, jsonify, request
from app.services.mudra_recognition import recognize_from_landmarks
from app.utils.validators import validate_landmarks_payload

recognition_bp = Blueprint("recognition", __name__)


@recognition_bp.post("/recognize")
def recognize():
    payload = request.get_json(silent=True)
    error = validate_landmarks_payload(payload, require_complete=False)
    if error:
        return jsonify({"error": error}), 400

    result = recognize_from_landmarks(payload["landmarks"])
    return jsonify(result), 501 if result.get("status") == "not_implemented" else 200
