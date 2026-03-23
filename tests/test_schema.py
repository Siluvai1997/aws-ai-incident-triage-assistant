from backend.schema import TriageResult


def test_schema_defaults() -> None:
    result = TriageResult()
    assert result.severity == "Medium"
    assert result.category == "Infrastructure"
    assert result.component == "unknown"
