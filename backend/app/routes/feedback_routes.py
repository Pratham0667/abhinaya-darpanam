from flask import Blueprint, jsonify, request
from app.services.feedback_generator import generate_feedback

feedback_bp = Blueprint("feedback", __name__)


@feedback_bp.post("/feedback")
def feedback():
    payload = request.get_json(silent=True) or {}
    result = generate_feedback(payload)
    return jsonify(result), 501
