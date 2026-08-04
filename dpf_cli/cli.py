from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import date
from pathlib import Path

from dpf_validator.discovery import discover_project
from dpf_validator.formatters import format_human, format_json

from . import __version__
from .constants import DPF_CLI_VERSION, DPF_SPEC_VERSION, EXIT_ERROR, EXIT_OK, EXIT_USAGE, TYPE_PREFIXES
from .ids import next_id, normalize_context, slugify
from .manifest import write_simple_yaml
from .project import (
    ProjectInfo,
    decision_index_path,
    ensure_safe_path,
    epic_directory,
    feature_directory,
    load_project,
    release_index_path,
    validate_project_root,
)
from . import templates


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="dpf", description="CLI oficial do DoisTech Project Framework")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("version", help="Show CLI version")

    init = subparsers.add_parser("init", help="Initialize a DPF project")
    init.add_argument("--path", default=".")
    init.add_argument("--name")
    init.add_argument("--context")
    init.add_argument("--owner", default="project-owner")
    init.add_argument("--project-id")
    init.add_argument("--minimal", action="store_true")
    init.add_argument("--dry-run", action="store_true")

    validate = subparsers.add_parser("validate", help="Validate a DPF project")
    validate.add_argument("path", nargs="?", default=".")
    validate.add_argument("--format", choices=("human", "json"), default="human")

    status = subparsers.add_parser("status", help="Summarize project status from documents")
    status.add_argument("--path", default=".")
    status.add_argument("--format", choices=("human", "json"), default="human")

    feature = subparsers.add_parser("feature", help="Feature operations")
    feature_sub = feature.add_subparsers(dest="feature_command")
    feature_create = feature_sub.add_parser("create", help="Create a Feature")
    feature_create.add_argument("--path", default=".")
    feature_create.add_argument("--title", required=True)
    feature_create.add_argument("--epic", required=True)

    task = subparsers.add_parser("task", help="Task operations")
    task_sub = task.add_subparsers(dest="task_command")
    task_create = task_sub.add_parser("create", help="Create a Task")
    task_create.add_argument("--path", default=".")
    task_create.add_argument("--title", required=True)
    task_create.add_argument("--feature", required=True)
    task_create.add_argument("--depends-on", action="append", default=[])

    decision = subparsers.add_parser("decision", help="Architecture decision operations")
    decision_sub = decision.add_subparsers(dest="decision_command")
    decision_create = decision_sub.add_parser("create", help="Create an ADR")
    decision_create.add_argument("--path", default=".")
    decision_create.add_argument("--title", required=True)
    decision_create.add_argument("--related", action="append", default=[])

    release = subparsers.add_parser("release", help="Release operations")
    release_sub = release.add_subparsers(dest="release_command")
    release_prepare = release_sub.add_parser("prepare", help="Prepare a Release")
    release_prepare.add_argument("--path", default=".")
    release_prepare.add_argument("--title", required=True)
    release_prepare.add_argument("--version", required=True)
    release_prepare.add_argument("--feature", action="append", default=[])

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return EXIT_USAGE

    try:
        if args.command == "version":
            print(f"dpf-cli {DPF_CLI_VERSION}")
            return EXIT_OK
        if args.command == "init":
            return cmd_init(args)
        if args.command == "validate":
            return cmd_validate(args)
        if args.command == "status":
            return cmd_status(args)
        if args.command == "feature" and args.feature_command == "create":
            return cmd_feature_create(args)
        if args.command == "task" and args.task_command == "create":
            return cmd_task_create(args)
        if args.command == "decision" and args.decision_command == "create":
            return cmd_decision_create(args)
        if args.command == "release" and args.release_command == "prepare":
            return cmd_release_prepare(args)
    except (ValueError, FileNotFoundError) as exc:
        print(str(exc))
        return EXIT_ERROR

    parser.print_help()
    return EXIT_USAGE


def cmd_init(args: argparse.Namespace) -> int:
    root = ensure_safe_path(Path(args.path))
    name = args.name or root.name.replace("-", " ").title()
    context = (args.context or normalize_context(name)).upper()
    project_id = args.project_id or f"PRJ-{context}-0001"
    today = date.today().isoformat()

    operations = _init_operations(root, project_id, name, context, args.owner, today, minimal=args.minimal)
    conflicts = [path for path, _ in operations if path.exists()]
    if conflicts:
        print("Conflito: arquivos já existem e não serão sobrescritos.")
        for path in conflicts:
            print(f"- {path}")
        return EXIT_ERROR

    if args.dry_run:
        print("Dry run. Arquivos que seriam criados:")
        for path, _ in operations:
            print(f"- {path}")
        return EXIT_OK

    for path, content in operations:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    report = validate_project_root(root)
    print("Projeto DPF inicializado.")
    print(f"- raiz: {root}")
    print(f"- id: {project_id}")
    print(f"- contexto: {context}")
    print(f"- validacao: {report.error_count} erros, {report.warning_count} avisos")
    print("Próximos passos:")
    print("- revisar dpf/PROJECT.md")
    print("- definir Capability e Epic iniciais")
    print("- usar `dpf feature create` para iniciar o backlog")
    return EXIT_ERROR if report.error_count else EXIT_OK


def _init_operations(root: Path, project_id: str, name: str, context: str, owner: str, today: str, minimal: bool) -> list[tuple[Path, str]]:
    manifest = {
        "project_id": project_id,
        "project_name": name,
        "dpf_version": DPF_SPEC_VERSION,
        "structure_version": DPF_SPEC_VERSION,
        "prompt_spec_version": DPF_SPEC_VERSION,
        "size_profile": "small",
        "project_state": "dpf/PROJECT-STATE.md",
        "capabilities_path": "dpf/capabilities",
        "release_index": "dpf/RELEASES.md",
        "decision_index": "dpf/decisions/DECISIONS.md",
    }
    manifest_lines = "\n".join(f"{key}: {value}" for key, value in manifest.items()) + "\n"
    operations = [
        (root / "README.md", templates.root_readme(name)),
        (root / "AGENTS.md", templates.root_agents()),
        (root / ".gitignore", templates.root_gitignore()),
        (root / "dpf" / "PROJECT.md", templates.project_doc(project_id, name, owner, today)),
        (root / "dpf" / "PROJECT-STATE.md", templates.project_state_doc(context, name, today)),
        (root / "dpf" / "RELEASES.md", templates.releases_index_doc(context)),
        (root / "dpf" / "dpf-project.yaml", manifest_lines),
        (root / "dpf" / "product" / "PRODUCT-VISION.md", templates.product_vision_doc(name, context)),
        (root / "dpf" / "architecture" / "SYSTEM-DESIGN.md", templates.system_design_doc(context)),
        (root / "dpf" / "decisions" / "DECISIONS.md", templates.decisions_index_doc()),
    ]
    if not minimal:
        operations.extend(
            [
                (root / "dpf" / "PLANNED.md", templates.planned_doc()),
                (root / "dpf" / "IMPLEMENTED.md", templates.implemented_doc()),
                (root / "dpf" / "CHANGELOG.md", templates.changelog_doc()),
                (root / "dpf" / "validation" / "TESTS.md", templates.tests_doc()),
                (root / "dpf" / "context" / "AGENT-CONTEXT.md", templates.agent_context_doc()),
            ]
        )
    return operations


def cmd_validate(args: argparse.Namespace) -> int:
    root = Path(args.path)
    report = validate_project_root(root)
    if args.format == "json":
        print(format_json(report))
    else:
        print(format_human(report))
    return EXIT_ERROR if report.error_count else EXIT_OK


def cmd_status(args: argparse.Namespace) -> int:
    info = load_project(Path(args.path))
    layout, findings = discover_project(info.root)
    if layout is None:
        print("Projeto inválido ou incompleto.")
        return EXIT_ERROR
    report = validate_project_root(info.root)
    features = Counter()
    tasks = Counter()
    releases: list[dict[str, str | None]] = []
    blocked: list[str] = []
    task_map_statuses: dict[str, str] = {}
    task_paths_seen: set[str] = set()

    for doc in layout.documents:
        if doc.doc_kind == "task-map":
            task_map_statuses.update(doc.task_map_statuses)

    for doc in layout.documents:
        if doc.doc_kind == "feature" and doc.status:
            features[doc.status] += 1
            if doc.status == "blocked":
                blocked.append(doc.doc_id or doc.rel_path)
        if doc.doc_kind == "task":
            resolved_status = doc.status
            if not resolved_status and doc.doc_id:
                resolved_status = task_map_statuses.get(doc.doc_id)
            if resolved_status:
                tasks[resolved_status] += 1
                task_paths_seen.add(doc.doc_id or doc.rel_path)
                if resolved_status == "blocked":
                    blocked.append(doc.doc_id or doc.rel_path)
        if doc.doc_kind == "release":
            releases.append({"id": doc.doc_id, "status": doc.status})

    for task_id, status in task_map_statuses.items():
        if task_id in task_paths_seen:
            continue
        tasks[status] += 1
        if status == "blocked":
            blocked.append(task_id)

    payload = {
        "project": info.manifest.get("project_name"),
        "project_id": info.manifest.get("project_id"),
        "features_by_status": dict(features),
        "tasks_by_status": dict(tasks),
        "releases": releases,
        "validation_errors": report.error_count,
        "validation_warnings": report.warning_count,
        "blocked": blocked,
    }
    if args.format == "json":
        print(json.dumps(payload, ensure_ascii=True, indent=2))
    else:
        print(f"Projeto: {payload['project']} ({payload['project_id']})")
        print("Features por estado:")
        for key, value in sorted(features.items()):
            print(f"- {key}: {value}")
        print("Tasks por estado:")
        for key, value in sorted(tasks.items()):
            print(f"- {key}: {value}")
        print("Releases:")
        if releases:
            for item in releases:
                print(f"- {item['id']}: {item['status']}")
        else:
            print("- nenhuma")
        print(f"Validação: {report.error_count} erros, {report.warning_count} avisos")
        print("Bloqueados:")
        if blocked:
            for item in blocked:
                print(f"- {item}")
        else:
            print("- nenhum")
    return EXIT_ERROR if report.error_count else EXIT_OK


def cmd_feature_create(args: argparse.Namespace) -> int:
    info = load_project(Path(args.path))
    epic_dir = epic_directory(info.root, args.epic)
    if epic_dir is None:
        print(f"Epic inexistente: {args.epic}")
        return EXIT_ERROR
    feature_id = next_id(info.root, TYPE_PREFIXES["feature"], info.context)
    slug = slugify(args.title)
    feature_dir = epic_dir / "features" / f"{feature_id}-{slug}"
    feature_file = feature_dir / "FEATURE.md"
    tasks_index = feature_dir / "TASKS.md"
    features_index = epic_dir / "FEATURES.md"
    today = date.today().isoformat()
    if feature_dir.exists():
        print(f"Conflito: diretório já existe: {feature_dir}")
        return EXIT_ERROR
    feature_dir.mkdir(parents=True)
    feature_file.write_text(templates.feature_doc(feature_id, args.title, args.epic, today), encoding="utf-8")
    tasks_index.write_text(templates.tasks_index_doc(), encoding="utf-8")
    _append_index_entry(features_index, f"- [{feature_id} — {args.title}](./features/{feature_id}-{slug}/FEATURE.md)\n")
    report = validate_project_root(info.root)
    print(f"Feature criada: {feature_id}")
    return EXIT_ERROR if report.error_count else EXIT_OK


def cmd_task_create(args: argparse.Namespace) -> int:
    info = load_project(Path(args.path))
    feature_dir = feature_directory(info.root, args.feature)
    if feature_dir is None:
        print(f"Feature inexistente: {args.feature}")
        return EXIT_ERROR
    task_id = next_id(info.root, TYPE_PREFIXES["task"], info.context)
    slug = slugify(args.title)
    task_dir = feature_dir / "tasks"
    task_dir.mkdir(exist_ok=True)
    task_path = task_dir / f"{task_id}-{slug}.md"
    if task_path.exists():
        print(f"Conflito: arquivo já existe: {task_path}")
        return EXIT_ERROR
    today = date.today().isoformat()
    task_path.write_text(templates.task_doc(task_id, args.title, args.feature, today, args.depends_on), encoding="utf-8")
    tasks_index = feature_dir / "TASKS.md"
    if not tasks_index.exists():
        tasks_index.write_text(templates.tasks_index_doc(), encoding="utf-8")
    _append_task_row(tasks_index, task_id, args.title, "draft")
    report = validate_project_root(info.root)
    print(f"Task criada: {task_id}")
    return EXIT_ERROR if report.error_count else EXIT_OK


def cmd_decision_create(args: argparse.Namespace) -> int:
    info = load_project(Path(args.path))
    decision_id = next_id(info.root, TYPE_PREFIXES["decision"], info.context)
    slug = slugify(args.title)
    decision_path = info.dpf_root / "decisions" / f"{decision_id}-{slug}.md"
    if decision_path.exists():
        print(f"Conflito: arquivo já existe: {decision_path}")
        return EXIT_ERROR
    today = date.today().isoformat()
    decision_path.parent.mkdir(parents=True, exist_ok=True)
    decision_path.write_text(templates.decision_doc(decision_id, args.title, today, args.related), encoding="utf-8")
    _append_index_entry(decision_index_path(info), f"- [{decision_id} — {args.title}](./{decision_path.name})\n")
    report = validate_project_root(info.root)
    print(f"Decision criada: {decision_id}")
    return EXIT_ERROR if report.error_count else EXIT_OK


def cmd_release_prepare(args: argparse.Namespace) -> int:
    info = load_project(Path(args.path))
    if not args.feature:
        print("Ao menos uma Feature deve ser informada com --feature.")
        return EXIT_USAGE
    layout, _ = discover_project(info.root)
    available_features: dict[str, str | None] = {}
    if layout is not None:
        for doc in layout.documents:
            if doc.doc_kind == "feature" and doc.doc_id:
                available_features[doc.doc_id] = doc.status
    invalid = [feature_id for feature_id in args.feature if feature_id not in available_features]
    if invalid:
        print("Features inexistentes:")
        for item in invalid:
            print(f"- {item}")
        return EXIT_ERROR
    incompatible = [feature_id for feature_id in args.feature if available_features.get(feature_id) in {"draft", "blocked", "canceled", "archived"}]
    if incompatible:
        print("Features incompatíveis para release:")
        for item in incompatible:
            print(f"- {item}: {available_features.get(item)}")
        return EXIT_ERROR
    release_id = next_id(info.root, TYPE_PREFIXES["release"], info.context)
    slug = slugify(args.title)
    release_path = info.dpf_root / "releases" / f"{release_id}-{slug}.md"
    today = date.today().isoformat()
    release_path.parent.mkdir(parents=True, exist_ok=True)
    release_path.write_text(templates.release_doc(release_id, args.title, today, args.feature, args.version), encoding="utf-8")
    _append_index_entry(release_index_path(info), f"- [{release_id} — {args.title}](./releases/{release_path.name})\n")
    report = validate_project_root(info.root)
    print(f"Release preparada: {release_id}")
    return EXIT_ERROR if report.error_count else EXIT_OK


def _append_index_entry(path: Path, entry: str) -> None:
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("", encoding="utf-8")
    content = path.read_text(encoding="utf-8")
    if entry.strip() in content:
        raise ValueError(f"duplicate-index-entry:{entry.strip()}")
    if content and not content.endswith("\n"):
        content += "\n"
    path.write_text(content + entry, encoding="utf-8")


def _append_task_row(path: Path, task_id: str, title: str, status: str) -> None:
    row = f"| {task_id} | {title} | {status} | pendente |\n"
    content = path.read_text(encoding="utf-8")
    if task_id in content:
        raise ValueError(f"duplicate-task-row:{task_id}")
    if not content.endswith("\n"):
        content += "\n"
    path.write_text(content + row, encoding="utf-8")
