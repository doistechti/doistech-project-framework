from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
WORKFLOWS = ROOT / ".github" / "workflows"


class AutomationTests(unittest.TestCase):
    maxDiff = None

    def run_gate(self, *args: str) -> subprocess.CompletedProcess[str]:
        env = dict(os.environ)
        env["DPF_SKIP_AUTOMATION_TESTS"] = "1"
        return subprocess.run(
            [sys.executable, "scripts/automation/run_quality_gate.py", *args],
            cwd=ROOT,
            text=True,
            capture_output=True,
            env=env,
            check=False,
        )

    def test_manual_quality_gate(self) -> None:
        output_dir = Path(tempfile.mkdtemp(prefix="dpf-automation-manual-"))
        result = self.run_gate("manual", "--project-path", ".", "--output-dir", str(output_dir))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        report = json.loads((output_dir / "quality-gate-report.json").read_text(encoding="utf-8"))
        self.assertEqual(report["error_count"], 0)
        self.assertEqual(report["profile"], "manual")

    def test_release_quality_gate(self) -> None:
        output_dir = Path(tempfile.mkdtemp(prefix="dpf-automation-release-"))
        result = self.run_gate(
            "release",
            "--project-path",
            ".",
            "--release-doc",
            "examples/complete-project/dpf/releases/REL-COM-0001-community-event-publishing.md",
            "--output-dir",
            str(output_dir),
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        report = json.loads((output_dir / "quality-gate-report.json").read_text(encoding="utf-8"))
        self.assertEqual(report["project_path"], str((ROOT / "examples" / "complete-project").resolve()))
        summary = (output_dir / "quality-gate-summary.md").read_text(encoding="utf-8")
        self.assertIn("release-doc-check", summary)

    def test_manual_quality_gate_fails_for_invalid_project(self) -> None:
        temp_dir = Path(tempfile.mkdtemp(prefix="dpf-automation-invalid-"))
        try:
            dpf_dir = temp_dir / "dpf"
            dpf_dir.mkdir(parents=True, exist_ok=True)
            (dpf_dir / "dpf-project.yaml").write_text("project_id: PRJ-BAD-0001\n", encoding="utf-8")
            result = self.run_gate("manual", "--project-path", str(temp_dir), "--output-dir", str(temp_dir / "artifacts"))
            self.assertNotEqual(result.returncode, 0)
        finally:
            shutil.rmtree(temp_dir, ignore_errors=True)

    def test_workflow_files_exist(self) -> None:
        expected = {
            "dpf-pr.yml",
            "dpf-main.yml",
            "dpf-release-preparation.yml",
            "dpf-manual-validation.yml",
        }
        found = {path.name for path in WORKFLOWS.glob("*.yml")}
        self.assertTrue(expected.issubset(found))

    def test_workflows_use_minimal_permissions_and_runner(self) -> None:
        for path in WORKFLOWS.glob("*.yml"):
            content = path.read_text(encoding="utf-8")
            self.assertIn("contents: read", content, path.name)
            self.assertIn("persist-credentials: false", content, path.name)
            self.assertIn("actions/checkout@v4", content, path.name)
            self.assertIn("actions/setup-python@v5", content, path.name)
            self.assertIn("scripts/automation/run_quality_gate.py", content, path.name)
            self.assertNotIn("pull_request_target", content, path.name)


if __name__ == "__main__":
    unittest.main()
