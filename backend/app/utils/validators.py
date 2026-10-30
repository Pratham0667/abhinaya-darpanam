def validate_landmarks_payload(payload, require_complete=True):
    if not isinstance(payload, dict):
        return "Request body must be a JSON object."

    landmarks = payload.get("landmarks")
    if not isinstance(landmarks, list):
        return "'landmarks' must be a list."

    if require_complete and len(landmarks) != 21:
        return "Exactly 21 landmarks are required."

    if not require_complete and len(landmarks) == 0:
        return "At least one landmark is required."

    for index, point in enumerate(landmarks):
        if not isinstance(point, (list, tuple)) or len(point) != 3:
            return f"Landmark {index} must contain x, y, and z."
        if not all(isinstance(value, (int, float)) for value in point):
            return f"Landmark {index} coordinates must be numeric."

    return None
