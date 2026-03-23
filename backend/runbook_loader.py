from __future__ import annotations

import json
from pathlib import Path


def load_runbooks(path: Path) -> dict[str, list[str]]:
    return json.loads(path.read_text(encoding="utf-8"))
