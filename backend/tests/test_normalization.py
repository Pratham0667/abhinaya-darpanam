from app.services.normalization import normalize_landmarks
import pytest

def test_normalization_is_explicitly_pending():
    with pytest.raises(NotImplementedError):
        normalize_landmarks([[0.0, 0.0, 0.0]] * 21)
