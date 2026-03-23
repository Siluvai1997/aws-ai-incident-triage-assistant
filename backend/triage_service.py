from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from backend.bedrock_client import invoke_bedrock
from backend.formatter import extract_json_object
from backend.runbook_loader import load_runbooks
from backend.schema import TriageResult


MOCK_OUTPUT = {
    "summary": "The incident indicates elevated application errors after a recent deployment, likely affecting customer transactions.",
    "severity": "High",
    "category": "Application outage",
    "component": "payment-api",
    "confidence": 0.86,
}


def _load_prompt(project_root: Path, incident_text: str) -> str:
    template = (project_root / "backend" / "prompt_template.txt").read_text(encoding="utf-8")
    return template.replace("{{INCIDENT_TEXT}}", incident_text)


def _parse_bedrock_payload(payload: dict[str, Any]) -> dict[str, Any]:
    text_parts: list[str] = []
    for output_message in payload.get("output", {}).get("message", {}).get("content", []):
        if "text" in output_message:
            text_parts.append(output_message["text"])
    if not text_parts:
        raise ValueError("No text output returned from Bedrock")
    return extract_json_object("\n".join(text_parts))


def run_triage(incident_text: str, project_root: Path) -> dict[str, Any]:
    mode = os.getenv("TRIAGE_MODE", "mock").lower()
    runbooks = load_runbooks(project_root / "data" / "runbooks" / "runbooks.json")

    if mode == "bedrock":
        prompt = _load_prompt(project_root, incident_text)
        payload = invoke_bedrock(prompt)
        triage_data = _parse_bedrock_payload(payload)
    else:
        triage_data = MOCK_OUTPUT.copy()

    category = triage_data.get("category", "Infrastructure")
    triage_data["runbook_steps"] = runbooks.get(category, ["Review logs", "Validate system health", "Escalate if needed"])

    result = TriageResult(**triage_data)
    return result.to_dict()
