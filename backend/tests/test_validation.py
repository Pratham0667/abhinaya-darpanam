from app.utils.validators import validate_landmarks_payload


def test_rejects_missing_landmarks():
    assert validate_landmarks_payload({}) is not None


def test_accepts_one_landmark_for_scaffold():
    payload = {"landmarks": [[0.1, 0.2, 0.0]]}
    assert validate_landmarks_payload(payload, require_complete=False) is None
