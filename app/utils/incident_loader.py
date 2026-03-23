from __future__ import annotations

import json
from pathlib import Path


def list_sample_incidents(directory: Path) -> list[str]:
    return sorted([path.name for path in directory.glob("*.json")])


def load_sample_incident(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))
