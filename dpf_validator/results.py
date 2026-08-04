from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any


SEVERITY_ERROR = "erro"
SEVERITY_WARNING = "aviso"
SEVERITY_INFO = "informacao"


@dataclass(slots=True)
class Finding:
    severity: str
    code: str
    message: str
    path: str | None = None
    detail: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class ValidationReport:
    root: str
    findings: list[Finding]

    @property
    def error_count(self) -> int:
        return sum(1 for item in self.findings if item.severity == SEVERITY_ERROR)

    @property
    def warning_count(self) -> int:
        return sum(1 for item in self.findings if item.severity == SEVERITY_WARNING)

    @property
    def info_count(self) -> int:
        return sum(1 for item in self.findings if item.severity == SEVERITY_INFO)

    def to_dict(self) -> dict[str, Any]:
        return {
            "root": self.root,
            "error_count": self.error_count,
            "warning_count": self.warning_count,
            "info_count": self.info_count,
            "findings": [item.to_dict() for item in self.findings],
        }
