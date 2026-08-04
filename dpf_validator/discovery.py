from __future__ import annotations

from pathlib import Path

from .models import Document, ProjectLayout
from .parsing import (
    ParseError,
    extract_acceptance_criteria,
    extract_justification,
    extract_links,
    extract_release_items,
    find_first_id,
    find_status,
    find_title_from_name,
    has_completion_criteria,
    parse_front_matter,
    parse_task_status_table,
    safe_read_text,
)
from .results import Finding, SEVERITY_ERROR, SEVERITY_WARNING


def discover_project(root: Path) -> tuple[ProjectLayout | None, list[Finding]]:
    findings: list[Finding] = []
    root = root.resolve()
    dpf_root = root / "dpf"
    if not dpf_root.is_dir():
        findings.append(
            Finding(
                severity=SEVERITY_ERROR,
                code="STRUCTURE_NO_DPF_ROOT",
                message="Diretório `dpf/` não encontrado no caminho informado.",
                path=str(root),
            )
        )
        return None, findings

    documents: list[Document] = []
    for path in sorted(root.rglob("*.md")):
        if path.is_symlink():
            findings.append(
                Finding(
                    severity=SEVERITY_WARNING,
                    code="SECURITY_SKIPPED_SYMLINK",
                    message="Link simbólico ignorado por segurança.",
                    path=str(path.relative_to(root)),
                )
            )
            continue
        if not _is_within_root(root, path.resolve()):
            findings.append(
                Finding(
                    severity=SEVERITY_ERROR,
                    code="SECURITY_PATH_ESCAPE",
                    message="Arquivo resolve fora da raiz do projeto.",
                    path=str(path),
                )
            )
            continue
        kind = classify_document(path, dpf_root)
        if kind is None:
            continue
        try:
            raw_content = safe_read_text(path)
            metadata, body = parse_front_matter(raw_content)
        except ParseError as exc:
            findings.append(
                Finding(
                    severity=SEVERITY_ERROR,
                    code="PARSE_DOCUMENT_ERROR",
                    message="Falha ao ler ou interpretar documento.",
                    path=str(path.relative_to(root)),
                    detail=str(exc),
                )
            )
            continue
        if "id" not in metadata:
            found_id = find_first_id(body)
            if found_id:
                metadata["id"] = found_id
        if "status" not in metadata:
            found_status = find_status(body)
            if found_status:
                metadata["status"] = found_status
        if "title" not in metadata:
            found_title = find_title_from_name(body)
            if found_title:
                metadata["title"] = found_title
        _fill_parent_metadata(path, metadata)
        document = Document(
            path=path,
            rel_path=str(path.relative_to(root)),
            doc_kind=kind,
            metadata=metadata,
            content=body,
            links=extract_links(body),
            task_map_statuses=parse_task_status_table(body) if path.name == "TASKS.md" else {},
            acceptance_criteria=extract_acceptance_criteria(body),
            release_items=extract_release_items(body) if path.name.startswith("REL-") or path.name == "RELEASES.md" else [],
            justification=extract_justification(body),
            completion_criteria_present=has_completion_criteria(body, metadata),
        )
        documents.append(document)
    return ProjectLayout(root=root, dpf_root=dpf_root, documents=documents), findings


def _is_within_root(root: Path, candidate: Path) -> bool:
    try:
        candidate.relative_to(root)
        return True
    except ValueError:
        return False


def classify_document(path: Path, dpf_root: Path) -> str | None:
    name = path.name
    if path == dpf_root / "PROJECT.md":
        return "project"
    if path == dpf_root / "PROJECT-STATE.md":
        return "project-state"
    if name == "TASKS.md" and "features" in path.parts:
        return "task-map"
    if name == "FEATURE.md":
        return "feature"
    if name == "CAPABILITY.md":
        return "capability"
    if name == "EPIC.md":
        return "epic"
    if name.startswith("TASK-") and "tasks" in path.parts:
        return "task"
    if name.startswith("ADR-"):
        return "decision"
    if name.startswith("REL-") and "releases" in path.parts and "notes" not in path.parts:
        return "release"
    if "validation" in path.parts and name.startswith("VAL-"):
        return "validation-report"
    return "support"


def _fill_parent_metadata(path: Path, metadata: dict[str, object]) -> None:
    parent_value = metadata.get("parent")
    if isinstance(parent_value, str) and parent_value.startswith("FEAT-"):
        metadata.setdefault("parent_feature_id", parent_value)
    if isinstance(parent_value, str) and parent_value.startswith("EPC-"):
        metadata.setdefault("parent_epic_id", parent_value)

    if "parent_feature_id" not in metadata and "tasks" in path.parts:
        try:
            feature_dir = path.parent.parent.name
            if feature_dir.startswith("FEAT-"):
                metadata["derived_parent_feature_id"] = _id_from_directory_name(feature_dir)
                metadata["parent_feature_id"] = metadata["derived_parent_feature_id"]
        except Exception:
            pass
    if "parent_epic_id" not in metadata and "features" in path.parts:
        try:
            feature_index = path.parts.index("features")
            epic_dir = path.parts[feature_index - 1]
            if epic_dir.startswith("EPC-"):
                metadata["derived_parent_epic_id"] = _id_from_directory_name(epic_dir)
                metadata["parent_epic_id"] = metadata["derived_parent_epic_id"]
        except Exception:
            pass


def _id_from_directory_name(value: str) -> str:
    parts = value.split("-")
    return "-".join(parts[:3])
