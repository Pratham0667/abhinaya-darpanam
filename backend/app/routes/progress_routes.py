from flask import Blueprint, jsonify

progress_bp = Blueprint("progress", __name__)


@progress_bp.get("/progress")
def progress():
    return jsonify({
        "status": "not_implemented",
        "message": "Progress analytics will be connected after user and practice-session tables are designed."
    }), 501
