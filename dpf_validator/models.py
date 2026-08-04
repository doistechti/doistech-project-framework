from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(slots=True)
class Document:
    path: Path
    rel_path: str
    doc_kind: str
    metadata: dict[str, object] = field(default_factory=dict)
    content: str = ""
    links: list[str] = field(default_factory=list)
    task_map_statuses: dict[str, str] = field(default_factory=dict)
    acceptance_criteria: list[str] = field(default_factory=list)
    release_items: list[str] = field(default_factory=list)
    justification: str | None = None
    completion_criteria_present: bool = False

    @property
    def doc_id(self) -> str | None:
        value = self.metadata.get("id")
        return value if isinstance(value, str) else None

    @property
    def status(self) -> str | None:
        value = self.metadata.get("status")
        return value if isinstance(value, str) else None

    @property
    def parent_feature_id(self) -> str | None:
        value = self.metadata.get("parent_feature_id")
        return value if isinstance(value, str) else None

    @property
    def parent_epic_id(self) -> str | None:
        value = self.metadata.get("parent_epic_id")
        return value if isinstance(value, str) else None


@dataclass(slots=True)
class ProjectLayout:
    root: Path
    dpf_root: Path
    documents: list[Document]
