from flask import Blueprint, jsonify

mudra_bp = Blueprint("mudras", __name__)

# Database-backed mudra records will replace this placeholder in the DB milestone.
STARTER_MUDRAS = [
    {"id": 1, "name": "Pataka", "category": "Asamyukta Hasta"},
    {"id": 2, "name": "Tripataka", "category": "Asamyukta Hasta"},
]


@mudra_bp.get("/mudras")
def list_mudras():
    return jsonify({
        "status": "placeholder",
        "count": len(STARTER_MUDRAS),
        "mudras": STARTER_MUDRAS,
        "note": "Starter sample only; full 28-mudra catalogue will be added."
    }), 200


@mudra_bp.get("/mudras/<int:mudra_id>")
def get_mudra(mudra_id):
    mudra = next((item for item in STARTER_MUDRAS if item["id"] == mudra_id), None)
    if mudra is None:
        return jsonify({"error": "Mudra not found"}), 404
    return jsonify({"status": "placeholder", "mudra": mudra}), 200
