from __future__ import annotations

import json
from pathlib import Path

from backend.triage_service import run_triage

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def handler(event, context):  # noqa: ANN001, D401
    """AWS Lambda entrypoint for incident triage."""
    incident_text = event.get("incident_text", "")
    if not incident_text:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "incident_text is required"}),
        }

    result = run_triage(incident_text=incident_text, project_root=PROJECT_ROOT)
    return {
        "statusCode": 200,
        "body": json.dumps(result),
    }
