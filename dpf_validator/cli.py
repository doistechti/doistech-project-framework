from __future__ import annotations

import argparse
from pathlib import Path

from .discovery import discover_project
from .formatters import format_human, format_json
from .validators import validate_project

EXIT_OK = 0
EXIT_VALIDATION_ERROR = 1
EXIT_USAGE_ERROR = 2


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="python -m dpf_validator")
    subparsers = parser.add_subparsers(dest="command")

    validate = subparsers.add_parser("validate", help="Validate a DPF project")
    validate.add_argument("path", nargs="?", default=".")
    validate.add_argument("--format", choices=("human", "json"), default="human")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command != "validate":
        parser.print_help()
        return EXIT_USAGE_ERROR

    root = Path(args.path)
    if not root.exists():
        print(f"Caminho inexistente: {root}")
        return EXIT_USAGE_ERROR

    layout, discovery_findings = discover_project(root)
    if layout is None:
        from .results import ValidationReport

        report = ValidationReport(root=str(root.resolve()), findings=discovery_findings)
        _emit(report, args.format)
        return EXIT_VALIDATION_ERROR

    report = validate_project(layout)
    report.findings = discovery_findings + report.findings
    _emit(report, args.format)
    return EXIT_VALIDATION_ERROR if report.error_count else EXIT_OK


def _emit(report, output_format: str) -> None:
    if output_format == "json":
        print(format_json(report))
    else:
        print(format_human(report))
