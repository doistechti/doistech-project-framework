from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_TESTS = ["tests/test_validator.py", "tests/test_cli.py", "tests/test_automation.py"]
DEFAULT_EXAMPLES = ["examples/minimal-project", "examples/complete-project"]


@dataclass(slots=True)
class StepResult:
    name: str
    command: list[str]
    returncode: int
    stdout: str
    stderr: str
    blocking: bool = True

    @property
    def ok(self) -> bool:
        return self.returncode == 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run DPF quality gates for local automation and CI")
    parser.add_argument("profile", choices=("pr", "main", "release", "manual"))
    parser.add_argument("--project-path", default=".")
    parser.add_argument("--output-dir", default=".dpf-artifacts")
    parser.add_argument("--changed-files-file")
    parser.add_argument("--release-doc")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    output_dir = (ROOT / args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    project_path = resolve_project_path(args.profile, args.project_path, args.release_doc)
    steps: list[StepResult] = []
    steps.extend(run_common_steps(project_path))

    if args.profile == "pr":
        steps.extend(run_changed_files_step(args.changed_files_file))
    elif args.profile == "main":
        steps.append(run_step("dpf-version", ["./dpf", "version"]))
        steps.append(run_step("project-status", ["./dpf", "status", "--path", "examples/complete-project", "--format", "json"]))
    elif args.profile == "release":
        steps.extend(run_release_steps(project_path, args.release_doc))
    elif args.profile == "manual":
        if is_dpf_project(project_path):
            steps.append(run_step("manual-project-validate", ["./dpf", "validate", str(project_path), "--format", "json"]))
        else:
            steps.append(
                StepResult(
                    name="manual-project-validate",
                    command=["skip", str(project_path)],
                    returncode=0,
                    stdout="target path is not a DPF project; skipped direct project validation\n",
                    stderr="",
                    blocking=False,
                )
            )

    report = {
        "profile": args.profile,
        "project_path": str(project_path),
        "steps": [asdict(step) for step in steps],
        "error_count": sum(1 for step in steps if step.blocking and step.returncode != 0),
        "warning_count": sum(1 for step in steps if not step.blocking and step.returncode != 0),
    }
    (output_dir / "quality-gate-report.json").write_text(json.dumps(report, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
    summary = render_summary(report)
    (output_dir / "quality-gate-summary.md").write_text(summary, encoding="utf-8")
    summary_target = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_target:
        with open(summary_target, "a", encoding="utf-8") as handle:
            handle.write(summary)

    print(summary, end="")
    return 1 if report["error_count"] else 0


def run_common_steps(project_path: Path) -> list[StepResult]:
    tests = list(DEFAULT_TESTS)
    if os.environ.get("DPF_SKIP_AUTOMATION_TESTS") == "1":
        tests = [item for item in tests if item != "tests/test_automation.py"]
    steps = [
        run_step("compileall", [sys.executable, "-m", "compileall", "dpf_cli", "dpf_validator", "tests", "scripts"]),
        run_step("unit-tests", [sys.executable, "-m", "unittest", "-v", *tests]),
        run_step("validate-example-minimal", ["./dpf", "validate", DEFAULT_EXAMPLES[0], "--format", "json"]),
        run_step("validate-example-complete", ["./dpf", "validate", DEFAULT_EXAMPLES[1], "--format", "json"]),
        run_schema_sanity(),
    ]
    if project_path != ROOT and is_dpf_project(project_path):
        steps.append(run_step("validate-target-project", ["./dpf", "validate", str(project_path), "--format", "json"]))
    return steps


def run_release_steps(project_path: Path, release_doc: str | None) -> list[StepResult]:
    steps: list[StepResult] = []
    if not release_doc:
        return [StepResult("release-doc-missing", ["--release-doc"], 1, "", "release-doc-required\n", True)]
    release_path = (ROOT / release_doc).resolve()
    steps.append(check_release_document(project_path, release_path))
    changelog = project_path / "dpf" / "CHANGELOG.md"
    if not changelog.exists():
        changelog = project_path / "CHANGELOG.md"
    steps.append(
        StepResult(
            name="release-changelog-check",
            command=["check", str(changelog)],
            returncode=0 if changelog.exists() else 1,
            stdout=f"{changelog}\n" if changelog.exists() else "",
            stderr="" if changelog.exists() else "CHANGELOG missing\n",
            blocking=True,
        )
    )
    return steps


def resolve_project_path(profile: str, project_path_arg: str, release_doc: str | None) -> Path:
    project_path = (ROOT / project_path_arg).resolve()
    if profile != "release":
        return project_path
    if is_dpf_project(project_path):
        return project_path
    if not release_doc:
        return project_path
    release_path = (ROOT / release_doc).resolve()
    discovered = nearest_dpf_project(release_path.parent)
    return discovered or project_path


def is_dpf_project(path: Path) -> bool:
    return (path / "dpf").is_dir() and (path / "dpf" / "dpf-project.yaml").exists()


def nearest_dpf_project(path: Path) -> Path | None:
    current = path
    while True:
        if is_dpf_project(current):
            return current
        if current == current.parent:
            return None
        current = current.parent


def run_changed_files_step(changed_files_file: str | None) -> list[StepResult]:
    if not changed_files_file:
        return [
            StepResult(
                name="changed-files",
                command=["check", "changed-files"],
                returncode=0,
                stdout="changed files file not provided\n",
                stderr="",
                blocking=False,
            )
        ]
    path = (ROOT / changed_files_file).resolve()
    if not path.exists():
        return [
            StepResult(
                name="changed-files",
                command=["check", str(path)],
                returncode=1,
                stdout="",
                stderr="changed files file missing\n",
                blocking=False,
            )
        ]
    content = path.read_text(encoding="utf-8")
    return [
        StepResult(
            name="changed-files",
            command=["check", str(path)],
            returncode=0,
            stdout=content,
            stderr="",
            blocking=False,
        )
    ]


def run_schema_sanity() -> StepResult:
    schema_root = ROOT / "schemas"
    outputs: list[str] = []
    try:
        for path in sorted(schema_root.rglob("*.json")):
            payload = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(payload, dict) and "$ref" in payload:
                outputs.append(f"{path.relative_to(ROOT)} uses $ref")
        return StepResult("schema-sanity", ["python-json-load", "schemas/**/*.json"], 0, "\n".join(outputs) + ("\n" if outputs else ""), "", True)
    except json.JSONDecodeError as exc:
        return StepResult("schema-sanity", ["python-json-load", "schemas/**/*.json"], 1, "", f"{exc}\n", True)


def check_release_document(project_path: Path, release_path: Path) -> StepResult:
    if not release_path.exists():
        return StepResult("release-doc-check", ["check", str(release_path)], 1, "", "release doc missing\n", True)
    content = release_path.read_text(encoding="utf-8")
    filename = release_path.name
    if not filename.startswith("REL-"):
        return StepResult("release-doc-check", ["check", str(release_path)], 1, "", "release doc file name must start with REL-\n", True)
    if "## Itens incluídos" not in content:
        return StepResult("release-doc-check", ["check", str(release_path)], 1, "", "release doc missing included items section\n", True)
    return StepResult("release-doc-check", ["check", str(release_path)], 0, f"{release_path.relative_to(ROOT)}\n", "", True)


def run_step(name: str, command: list[str], blocking: bool = True) -> StepResult:
    process = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
    return StepResult(name, command, process.returncode, process.stdout, process.stderr, blocking)


def render_summary(report: dict[str, object]) -> str:
    lines = [
        f"# DPF Quality Gate Summary",
        "",
        f"- profile: `{report['profile']}`",
        f"- project_path: `{report['project_path']}`",
        f"- blocking_errors: `{report['error_count']}`",
        f"- warnings: `{report['warning_count']}`",
        "",
        "## Steps",
        "",
    ]
    for step in report["steps"]:
        assert isinstance(step, dict)
        status = "OK" if step["returncode"] == 0 else ("WARN" if not step["blocking"] else "FAIL")
        lines.append(f"- `{status}` `{step['name']}`")
    lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    raise SystemExit(main())
