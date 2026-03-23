from __future__ import annotations

from dataclasses import asdict, dataclass, field


@dataclass
class TriageResult:
    summary: str = ""
    severity: str = "Medium"
    category: str = "Infrastructure"
    component: str = "unknown"
    confidence: float = 0.7
    runbook_steps: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return asdict(self)
