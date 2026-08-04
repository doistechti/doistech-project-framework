from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MINIMAL = ROOT / "examples" / "minimal-project"
COMPLETE = ROOT / "examples" / "complete-project"


class ValidatorTests(unittest.TestCase):
    maxDiff = None

    def run_validator(self, target: Path, output_format: str = "human") -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, "-m", "dpf_validator", "validate", str(target), "--format", output_format],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

    def make_copy(self, source: Path) -> Path:
        temp_dir = Path(tempfile.mkdtemp(prefix="dpf-validator-test-"))
        target = temp_dir / source.name
        shutil.copytree(source, target, symlinks=False)
        return target

    def test_minimal_project_valid(self) -> None:
        result = self.run_validator(MINIMAL)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_complete_project_valid(self) -> None:
        result = self.run_validator(COMPLETE)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_duplicate_id(self) -> None:
        project = self.make_copy(MINIMAL)
        duplicate = project / "dpf" / "decisions" / "ADR-TN-0001-duplicate.md"
        duplicate.write_text((project / "dpf" / "decisions" / "ADR-TN-0001-single-user-document-boundary.md").read_text(encoding="utf-8"), encoding="utf-8")
        result = self.run_validator(project)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("ID_DUPLICATE", result.stdout)

    def test_broken_link(self) -> None:
        project = self.make_copy(MINIMAL)
        readme = project / "README.md"
        readme.write_text(readme.read_text(encoding="utf-8") + "\n- [broken](./missing-file.md)\n", encoding="utf-8")
        result = self.run_validator(project)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("LINK_BROKEN", result.stdout)

    def test_orphan_task(self) -> None:
        project = self.make_copy(MINIMAL)
        task = project / "dpf" / "capabilities" / "CAP-TN-0001-task-capture" / "epics" / "EPC-TN-0001-personal-task-notes" / "features" / "FEAT-TN-0001-register-task-note" / "tasks" / "TASK-TN-0001-define-note-capture-flow.md"
        task.write_text(task.read_text(encoding="utf-8").replace("parent: FEAT-TN-0001", "parent: EPC-TN-0001"), encoding="utf-8")
        result = self.run_validator(project)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("TASK_PARENT_FEATURE_MISMATCH", result.stdout)

    def test_feature_without_acceptance(self) -> None:
        project = self.make_copy(MINIMAL)
        feature = project / "dpf" / "capabilities" / "CAP-TN-0001-task-capture" / "epics" / "EPC-TN-0001-personal-task-notes" / "features" / "FEAT-TN-0001-register-task-note" / "FEATURE.md"
        feature.write_text(feature.read_text(encoding="utf-8").split("## Critérios de aceite")[0], encoding="utf-8")
        result = self.run_validator(project)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("FEATURE_ACCEPTANCE_MISSING", result.stdout)

    def test_invalid_state(self) -> None:
        project = self.make_copy(MINIMAL)
        feature = project / "dpf" / "capabilities" / "CAP-TN-0001-task-capture" / "epics" / "EPC-TN-0001-personal-task-notes" / "features" / "FEAT-TN-0001-register-task-note" / "FEATURE.md"
        feature.write_text(feature.read_text(encoding="utf-8").replace("status: released", "status: completed"), encoding="utf-8")
        result = self.run_validator(project)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("DOC_STATUS_INVALID", result.stdout)

    def test_release_inconsistent(self) -> None:
        project = self.make_copy(COMPLETE)
        feature = project / "dpf" / "capabilities" / "CAP-COM-0001-event-publication" / "epics" / "EPC-COM-0001-event-publishing" / "features" / "FEAT-COM-0001-publish-community-event" / "FEATURE.md"
        text = feature.read_text(encoding="utf-8").replace("`released`", "`ready`", 1)
        feature.write_text(text, encoding="utf-8")
        result = self.run_validator(project)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("RELEASE_WITH_INCOMPLETE_FEATURE", result.stdout)

    def test_malformed_file(self) -> None:
        project = self.make_copy(MINIMAL)
        task = project / "dpf" / "capabilities" / "CAP-TN-0001-task-capture" / "epics" / "EPC-TN-0001-personal-task-notes" / "features" / "FEAT-TN-0001-register-task-note" / "tasks" / "TASK-TN-0001-define-note-capture-flow.md"
        task.write_text("---\nid TASK-TN-0001\n---\n# broken\n", encoding="utf-8")
        result = self.run_validator(project)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("PARSE_DOCUMENT_ERROR", result.stdout)

    def test_symlink_path_unsafe(self) -> None:
        project = self.make_copy(MINIMAL)
        target = project / "dpf" / "validation" / "reports" / "outside-link.md"
        outside = Path(tempfile.gettempdir()) / "outside-link-target.md"
        outside.write_text("external", encoding="utf-8")
        try:
            target.symlink_to(outside)
        except OSError:
            self.skipTest("Symlinks not supported in this environment")
        result = self.run_validator(project)
        self.assertEqual(result.returncode, 0)
        self.assertIn("SECURITY_SKIPPED_SYMLINK", result.stdout)

    def test_json_output(self) -> None:
        result = self.run_validator(MINIMAL, output_format="json")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        payload = json.loads(result.stdout)
        self.assertIn("findings", payload)
        self.assertIn("error_count", payload)

    def test_exit_code_for_errors(self) -> None:
        project = self.make_copy(MINIMAL)
        (project / "dpf" / "PROJECT.md").unlink()
        result = self.run_validator(project)
        self.assertEqual(result.returncode, 1)


if __name__ == "__main__":
    unittest.main()
