from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from dpf_validator.discovery import discover_project
from dpf_validator.validators import validate_project

from .manifest import read_simple_yaml


@dataclass(slots=True)
class ProjectInfo:
    root: Path
    dpf_root: Path
    manifest_path: Path
    manifest: dict[str, str]

    @property
    def context(self) -> str:
        project_id = self.manifest.get("project_id", "PRJ-DPF-0001")
        parts = project_id.split("-")
        return parts[1] if len(parts) >= 3 else "DPF"


def ensure_safe_path(path: Path) -> Path:
    if path.is_symlink():
        raise ValueError(f"unsafe-symlink-path:{path}")
    return path.resolve()


def load_project(path: Path) -> ProjectInfo:
    root = ensure_safe_path(path)
    dpf_root = root / "dpf"
    manifest_path = dpf_root / "dpf-project.yaml"
    if not manifest_path.exists():
        raise FileNotFoundError(f"manifest-not-found:{manifest_path}")
    manifest = read_simple_yaml(manifest_path)
    return ProjectInfo(root=root, dpf_root=dpf_root, manifest_path=manifest_path, manifest=manifest)


def validate_project_root(path: Path):
    layout, discovery_findings = discover_project(path)
    if layout is None:
        from dpf_validator.results import ValidationReport

        report = ValidationReport(root=str(path.resolve()), findings=discovery_findings)
        return report
    report = validate_project(layout)
    report.findings = discovery_findings + report.findings
    return report


def find_doc_by_id(root: Path, doc_id: str) -> Path | None:
    pattern = re.compile(rf"\b{re.escape(doc_id)}\b")
    for path in root.rglob("*.md"):
        if path.is_symlink():
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except OSError:
            continue
        if pattern.search(content):
            return path
    return None


def feature_directory(root: Path, feature_id: str) -> Path | None:
    for path in root.rglob(f"{feature_id}-*"):
        if path.is_dir():
            feature_file = path / "FEATURE.md"
            if feature_file.exists():
                return path
    path = find_doc_by_id(root, feature_id)
    if path and path.name == "FEATURE.md":
        return path.parent
    return None


def epic_directory(root: Path, epic_id: str) -> Path | None:
    for path in root.rglob(f"{epic_id}-*"):
        if path.is_dir():
            epic_file = path / "EPIC.md"
            if epic_file.exists():
                return path
    path = find_doc_by_id(root, epic_id)
    if path and path.name == "EPIC.md":
        return path.parent
    return None


def release_index_path(info: ProjectInfo) -> Path:
    value = info.manifest.get("release_index", "dpf/RELEASES.md")
    return info.root / value


def decision_index_path(info: ProjectInfo) -> Path:
    value = info.manifest.get("decision_index", "dpf/decisions/DECISIONS.md")
    return info.root / value
