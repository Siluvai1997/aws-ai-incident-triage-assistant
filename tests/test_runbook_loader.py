from pathlib import Path

from app.utils.runbook_loader import load_runbooks


def test_load_runbooks_contains_categories() -> None:
    project_root = Path(__file__).resolve().parents[1]
    runbooks = load_runbooks(project_root / "data" / "runbooks" / "runbooks.json")
    assert "Application outage" in runbooks
    assert len(runbooks["Kubernetes"]) > 0
