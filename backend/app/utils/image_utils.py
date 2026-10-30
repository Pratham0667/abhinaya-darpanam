"""Image preprocessing helpers."""

def validate_image_extension(filename):
    allowed = {".jpg", ".jpeg", ".png", ".webp"}
    from pathlib import Path
    return Path(filename).suffix.lower() in allowed
