from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

from .models import Document, ProjectLayout
from .results import Finding, SEVERITY_ERROR, SEVERITY_INFO, SEVERITY_WARNING, ValidationReport

ID_PATTERNS = {
    "project": re.compile(r"^PRJ-[A-Z0-9]+-\d{4}$"),
    "capability": re.compile(r"^CAP-[A-Z0-9]+-\d{4}$"),
    "epic": re.compile(r"^EPC-[A-Z0-9]+-\d{4}$"),
    "feature": re.compile(r"^FEAT-[A-Z0-9]+-\d{4}$"),
    "task": re.compile(r"^TASK-[A-Z0-9]+-\d{4}$"),
    "decision": re.compile(r"^ADR-[A-Z0-9]+-\d{4}$"),
    "release": re.compile(r"^REL-[A-Z0-9]+-\d{4}$"),
    "validation-report": re.compile(r"^VAL-[A-Z0-9]+-\d{4}$"),
    "project-state": re.compile(r"^(DOC|CTX)-[A-Z0-9]+(?:-[A-Z0-9]+)*-\d{4}$"),
}

STATUS_BY_KIND = {
    "project": {"draft", "active", "superseded", "archived"},
    "capability": {"draft", "active", "blocked", "done", "canceled", "archived"},
    "epic": {"draft", "active", "blocked", "done", "canceled", "archived"},
    "feature": {"draft", "ready", "active", "blocked", "implemented", "validated", "released", "canceled", "archived"},
    "task": {"draft", "ready", "active", "blocked", "done", "validated", "canceled", "archived"},
    "decision": {"proposed", "approved", "rejected", "superseded", "archived"},
    "release": {"planned", "ready", "approved", "released", "rolled-back", "canceled", "archived"},
    "project-state": {"draft", "active", "superseded", "archived"},
    "validation-report": {"draft", "active", "superseded", "archived"},
}


def validate_project(layout: ProjectLayout) -> ValidationReport:
    findings: list[Finding] = []
    findings.extend(_validate_structure(layout))
    findings.extend(_validate_documents(layout))
    findings.extend(_validate_links(layout))
    findings.extend(_validate_cross_document_rules(layout))
    findings.append(
        Finding(
            severity=SEVERITY_INFO,
            code="SUMMARY_VALIDATION_COMPLETED",
            message="Validação concluída.",
            path=str(layout.root),
        )
    )
    return ValidationReport(root=str(layout.root), findings=findings)


def _validate_structure(layout: ProjectLayout) -> list[Finding]:
    findings: list[Finding] = []
    required_paths = [
        layout.root / "README.md",
        layout.root / "AGENTS.md",
        layout.dpf_root / "PROJECT.md",
        layout.dpf_root / "PROJECT-STATE.md",
        layout.dpf_root / "dpf-project.yaml",
    ]
    for path in required_paths:
        if not path.exists():
            findings.append(
                Finding(
                    severity=SEVERITY_ERROR,
                    code="STRUCTURE_REQUIRED_PATH_MISSING",
                    message="Arquivo obrigatório ausente.",
                    path=str(path.relative_to(layout.root)),
                )
            )
    return findings


def _validate_documents(layout: ProjectLayout) -> list[Finding]:
    findings: list[Finding] = []
    task_status_maps: dict[str, dict[str, str]] = {}
    for doc in layout.documents:
        if doc.path.name == "TASKS.md":
            task_status_maps[str(doc.path.parent)] = doc.task_map_statuses

    for doc in layout.documents:
        findings.extend(_validate_single_document(doc))
    return findings


def _validate_single_document(doc: Document) -> list[Finding]:
    findings: list[Finding] = []
    if doc.doc_kind in {"task-map", "support"}:
        return findings
    doc_id = doc.doc_id
    if not doc_id:
        findings.append(Finding(SEVERITY_ERROR, "DOC_ID_MISSING", "Documento sem identificador.", doc.rel_path))
    else:
        pattern = ID_PATTERNS.get(doc.doc_kind)
        if pattern and not pattern.fullmatch(doc_id):
            findings.append(Finding(SEVERITY_ERROR, "DOC_ID_INVALID", "Identificador inválido para o tipo do artefato.", doc.rel_path, doc_id))

    required_metadata = {
        "project": ("title", "status"),
        "feature": ("title", "status"),
        "task": ("title",),
        "decision": ("title", "status"),
        "release": ("title", "status"),
        "project-state": ("title", "status"),
        "validation-report": ("title", "status"),
    }
    for field in required_metadata.get(doc.doc_kind, ()):
        if field not in doc.metadata:
            findings.append(Finding(SEVERITY_ERROR, f"DOC_{field.upper()}_MISSING", f"Documento sem `{field}`.", doc.rel_path))
    status = doc.status
    if status:
        allowed = STATUS_BY_KIND.get(doc.doc_kind)
        if allowed and status not in allowed:
            findings.append(Finding(SEVERITY_ERROR, "DOC_STATUS_INVALID", "Estado inválido para o tipo do artefato.", doc.rel_path, status))

    if doc.doc_kind == "feature" and not doc.acceptance_criteria:
        findings.append(Finding(SEVERITY_ERROR, "FEATURE_ACCEPTANCE_MISSING", "Feature sem critérios de aceite.", doc.rel_path))

    if doc.doc_kind == "task" and not doc.completion_criteria_present:
        findings.append(Finding(SEVERITY_ERROR, "TASK_COMPLETION_CRITERIA_MISSING", "Task sem critérios de conclusão.", doc.rel_path))

    if doc.doc_kind == "release" and not doc.release_items:
        findings.append(Finding(SEVERITY_ERROR, "RELEASE_EMPTY", "Release sem conteúdo incluído.", doc.rel_path))

    if status == "canceled" and not (doc.metadata.get("cancellation_reason") or doc.justification):
        findings.append(Finding(SEVERITY_ERROR, "CANCELED_WITHOUT_REASON", "Artefato cancelado sem justificativa.", doc.rel_path))

    if doc.doc_kind == "task" and not doc.parent_feature_id:
        findings.append(Finding(SEVERITY_ERROR, "TASK_PARENT_FEATURE_MISSING", "Task sem Feature pai identificável.", doc.rel_path))
    if doc.doc_kind == "task":
        parent_value = doc.metadata.get("parent")
        derived_parent = doc.metadata.get("derived_parent_feature_id")
        if isinstance(parent_value, str) and (not parent_value.startswith("FEAT-") or (isinstance(derived_parent, str) and parent_value != derived_parent)):
            findings.append(Finding(SEVERITY_ERROR, "TASK_PARENT_FEATURE_MISMATCH", "Task declara parent incompatível com a Feature que a contém.", doc.rel_path, parent_value))

    if doc.doc_kind == "feature" and not doc.parent_epic_id:
        findings.append(Finding(SEVERITY_ERROR, "FEATURE_PARENT_EPIC_MISSING", "Feature sem Epic pai identificável.", doc.rel_path))

    return findings


def _validate_links(layout: ProjectLayout) -> list[Finding]:
    findings: list[Finding] = []
    for doc in layout.documents:
        for link in doc.links:
            if link.startswith(("http://", "https://", "mailto:", "#")):
                continue
            candidate = (doc.path.parent / link).resolve()
            try:
                candidate.relative_to(layout.root.resolve())
            except ValueError:
                findings.append(Finding(SEVERITY_ERROR, "LINK_OUTSIDE_PROJECT", "Link relativo resolve fora do projeto.", doc.rel_path, link))
                continue
            if not candidate.exists():
                findings.append(Finding(SEVERITY_ERROR, "LINK_BROKEN", "Link relativo quebrado.", doc.rel_path, link))
    return findings


def _validate_cross_document_rules(layout: ProjectLayout) -> list[Finding]:
    findings: list[Finding] = []
    docs_by_id: dict[str, Document] = {}
    duplicates: defaultdict[str, list[str]] = defaultdict(list)
    task_tables: dict[str, dict[str, str]] = {}
    for doc in layout.documents:
        if doc.doc_id:
            duplicates[doc.doc_id].append(doc.rel_path)
            docs_by_id[doc.doc_id] = doc
        if doc.path.name == "TASKS.md" and doc.task_map_statuses:
            task_tables[str(doc.path.parent)] = doc.task_map_statuses

    for doc_id, paths in duplicates.items():
        if len(paths) > 1:
            findings.append(Finding(SEVERITY_ERROR, "ID_DUPLICATE", "Identificador duplicado no projeto.", detail=json.dumps(paths), path=doc_id))

    _validate_task_map_consistency(layout, docs_by_id, task_tables, findings)
    _validate_release_consistency(layout, docs_by_id, findings)
    _validate_dependency_cycles(layout, docs_by_id, findings)
    _validate_archived_active_conflicts(layout, findings)
    return findings


def _validate_task_map_consistency(
    layout: ProjectLayout,
    docs_by_id: dict[str, Document],
    task_tables: dict[str, dict[str, str]],
    findings: list[Finding],
) -> None:
    for doc in layout.documents:
        if doc.doc_kind == "task" and doc.doc_id:
            task_map = task_tables.get(str(doc.path.parent.parent))
            if not task_map:
                if not doc.status:
                    findings.append(Finding(SEVERITY_ERROR, "TASK_STATUS_UNRESOLVED", "Task sem estado local e sem mapa TASKS.md utilizável.", doc.rel_path))
                else:
                    findings.append(Finding(SEVERITY_WARNING, "TASK_MAP_MISSING", "TASKS.md ausente ou sem tabela parseável para a Feature.", doc.rel_path))
                continue
            map_status = task_map.get(doc.doc_id)
            if not map_status:
                findings.append(Finding(SEVERITY_ERROR, "TASK_NOT_IN_MAP", "Task não encontrada no mapa TASKS.md da Feature.", doc.rel_path))
                continue
            if doc.status and map_status != doc.status:
                findings.append(Finding(SEVERITY_ERROR, "TASK_STATUS_MISMATCH", "Status da Task diverge do mapa TASKS.md.", doc.rel_path, f"{doc.status} != {map_status}"))
            if not doc.status:
                doc.metadata["status"] = map_status

    for doc in layout.documents:
        if doc.doc_kind != "feature":
            continue
        feature_status = doc.status
        if feature_status not in {"implemented", "validated", "released"}:
            continue
        feature_task_dir = doc.path.parent / "tasks"
        open_statuses = {"draft", "ready", "active", "blocked"}
        open_tasks: list[str] = []
        for task_doc in layout.documents:
            if task_doc.doc_kind == "task" and task_doc.path.parent == feature_task_dir and task_doc.status in open_statuses:
                open_tasks.append(task_doc.doc_id or task_doc.rel_path)
        if open_tasks:
            findings.append(Finding(SEVERITY_ERROR, "FEATURE_COMPLETE_WITH_OPEN_TASKS", "Feature concluída com Tasks abertas.", doc.rel_path, ", ".join(open_tasks)))


def _validate_release_consistency(layout: ProjectLayout, docs_by_id: dict[str, Document], findings: list[Finding]) -> None:
    acceptable = {"implemented", "validated", "released"}
    for doc in layout.documents:
        if doc.doc_kind != "release" or doc.status != "released":
            continue
        incomplete: list[str] = []
        for feature_id in doc.release_items:
            feature_doc = docs_by_id.get(feature_id)
            if not feature_doc or feature_doc.status not in acceptable:
                incomplete.append(feature_id)
        if incomplete:
            findings.append(Finding(SEVERITY_ERROR, "RELEASE_WITH_INCOMPLETE_FEATURE", "Release concluída com Feature incompleta ou ausente.", doc.rel_path, ", ".join(incomplete)))


def _validate_dependency_cycles(layout: ProjectLayout, docs_by_id: dict[str, Document], findings: list[Finding]) -> None:
    graph: dict[str, list[str]] = {}
    for doc in layout.documents:
        if doc.doc_id:
            deps = doc.metadata.get("dependencies")
            if isinstance(deps, list):
                graph[doc.doc_id] = [item for item in deps if isinstance(item, str)]

    visited: set[str] = set()
    stack: set[str] = set()

    def visit(node: str) -> bool:
        if node in stack:
            return True
        if node in visited:
            return False
        visited.add(node)
        stack.add(node)
        for neighbor in graph.get(node, []):
            if neighbor in docs_by_id and visit(neighbor):
                return True
        stack.remove(node)
        return False

    for node in graph:
        if visit(node):
            findings.append(Finding(SEVERITY_WARNING, "DEPENDENCY_CYCLE_DETECTED", "Dependência circular detectável entre artefatos.", path=node))
            break


def _validate_archived_active_conflicts(layout: ProjectLayout, findings: list[Finding]) -> None:
    for doc in layout.documents:
        if doc.status == "archived":
            parts = {part.casefold() for part in doc.path.parts}
            if "active" in parts:
                findings.append(Finding(SEVERITY_ERROR, "ARCHIVED_ACTIVE_CONFLICT", "Documento arquivado ainda aparece em caminho com semântica ativa.", doc.rel_path))
