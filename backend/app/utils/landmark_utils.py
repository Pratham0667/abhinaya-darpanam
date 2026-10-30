"""Helpers for landmark data."""

def flatten_landmarks(landmarks):
    return [coordinate for point in landmarks for coordinate in point]
