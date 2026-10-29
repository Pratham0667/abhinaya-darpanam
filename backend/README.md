# Abhinaya Darpanam — Backend Starter

A modular Flask backend scaffold for the Bharatanatyam mudra recognition project.

## Current scope
This starter includes:
- Flask application factory and development entry point
- API blueprints for health, mudras, recognition, feedback, and progress
- Service-layer placeholders for MediaPipe, normalization, matching, and feedback
- Configuration and environment examples
- Basic request validation and starter tests

**Database integration is intentionally not implemented yet.** We will review this structure first, then add PostgreSQL + pgvector together.

## Setup
Python 3.10–3.12 is recommended.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
cp .env.example .env
python run.py
```

Server: `http://127.0.0.1:5000`

## Starter endpoints
- `GET /api/health`
- `GET /api/mudras`
- `GET /api/mudras/<mudra_id>`
- `POST /api/recognize`
- `POST /api/feedback`
- `GET /api/progress`

Recognition and data endpoints currently return clearly marked placeholder responses until their services and database are implemented.

## Example recognition request
```json
{
  "landmarks": [
    [0.1, 0.2, 0.0]
  ]
}
```
The example above is deliberately incomplete; the final recognition API will validate 21 landmarks (x, y, z) after we implement the pipeline.

## Project layout
```text
backend/
  app/
    routes/       Flask blueprints
    services/     Recognition and feedback logic
    utils/        Input validation helpers
  tests/
  .env.example
  requirements.txt
  run.py
```

## Next milestone
Review the folder structure and endpoint names. After you approve them, we will design the PostgreSQL schema, enable pgvector, and implement the database connection and repository layer.
