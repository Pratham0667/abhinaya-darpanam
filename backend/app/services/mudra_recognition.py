from app.services.normalization import normalize_landmarks
from app.services.similarity_matching import find_nearest_mudra


def recognize_from_landmarks(landmarks):
    # Pipeline wiring placeholder. The normalization and DB search layers are next milestones.
    return {
        "status": "not_implemented",
        "message": "Recognition pipeline is scaffolded but not active yet.",
        "received_landmark_count": len(landmarks)
    }
