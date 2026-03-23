import os
from pathlib import Path

from backend.triage_service import run_triage


def test_run_triage_mock_mode_returns_expected_shape() -> None:
    os.environ["TRIAGE_MODE"] = "mock"
    project_root = Path(__file__).resolve().parents[1]
    result = run_triage("sample incident text", project_root)

    assert result["severity"] in {"Critical", "High", "Medium", "Low"}
    assert result["category"]
    assert isinstance(result["runbook_steps"], list)
    assert result["runbook_steps"]
