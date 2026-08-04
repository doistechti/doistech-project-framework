from __future__ import annotations

import json

from .results import SEVERITY_ERROR, SEVERITY_INFO, SEVERITY_WARNING, ValidationReport


def format_human(report: ValidationReport) -> str:
    lines = [
        f"Projeto: {report.root}",
        f"Erros: {report.error_count}",
        f"Avisos: {report.warning_count}",
        f"Informacoes: {report.info_count}",
        "",
    ]
    for finding in report.findings:
        prefix = {
            SEVERITY_ERROR: "ERRO",
            SEVERITY_WARNING: "AVISO",
            SEVERITY_INFO: "INFO",
        }[finding.severity]
        line = f"[{prefix}] {finding.code}: {finding.message}"
        if finding.path:
            line += f" ({finding.path})"
        if finding.detail:
            line += f" -> {finding.detail}"
        lines.append(line)
    return "\n".join(lines)


def format_json(report: ValidationReport) -> str:
    return json.dumps(report.to_dict(), ensure_ascii=True, indent=2)
