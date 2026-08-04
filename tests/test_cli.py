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


class CliTests(unittest.TestCase):
    maxDiff = None

    def run_cli(self, *args: str, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, "-m", "dpf_cli", *args],
            cwd=cwd or ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

    def make_copy(self, source: Path) -> Path:
        temp_dir = Path(tempfile.mkdtemp(prefix="dpf-cli-test-"))
        target = temp_dir / source.name
        shutil.copytree(source, target, symlinks=False)
        return target

    def test_help(self) -> None:
        result = self.run_cli("--help")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("dpf", result.stdout)
        self.assertIn("init", result.stdout)

    def test_version(self) -> None:
        result = self.run_cli("version")
        self.assertEqual(result.returncode, 0)
        self.assertIn("dpf-cli 0.1.0", result.stdout)

    def test_init_minimal(self) -> None:
        target = Path(tempfile.mkdtemp(prefix="dpf-cli-init-"))
        result = self.run_cli("init", "--path", str(target), "--name", "Init Project", "--context", "INI", "--minimal")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertTrue((target / "dpf" / "PROJECT.md").exists())
        self.assertFalse((target / "dpf" / "PLANNED.md").exists())
        self.assertFalse((target / "dpf" / "IMPLEMENTED.md").exists())
        self.assertFalse((target / "dpf" / "CHANGELOG.md").exists())
        validate = self.run_cli("validate", str(target))
        self.assertEqual(validate.returncode, 0, validate.stdout + validate.stderr)

    def test_init_default_is_richer_than_minimal(self) -> None:
        target = Path(tempfile.mkdtemp(prefix="dpf-cli-init-full-"))
        result = self.run_cli("init", "--path", str(target), "--name", "Full Project", "--context", "FUL")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertTrue((target / "dpf" / "PLANNED.md").exists())
        self.assertTrue((target / "dpf" / "IMPLEMENTED.md").exists())
        self.assertTrue((target / "dpf" / "CHANGELOG.md").exists())

    def test_init_conflict(self) -> None:
        target = Path(tempfile.mkdtemp(prefix="dpf-cli-conflict-"))
        (target / "README.md").write_text("existing\n", encoding="utf-8")
        result = self.run_cli("init", "--path", str(target), "--name", "Conflict Project", "--context", "CON")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Conflito", result.stdout)

    def test_init_dry_run(self) -> None:
        target = Path(tempfile.mkdtemp(prefix="dpf-cli-dry-"))
        result = self.run_cli("init", "--path", str(target), "--name", "Dry Project", "--context", "DRY", "--dry-run")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Dry run", result.stdout)
        self.assertFalse((target / "dpf" / "PROJECT.md").exists())

    def test_feature_create(self) -> None:
        project = self.make_copy(MINIMAL)
        result = self.run_cli(
            "feature",
            "create",
            "--path",
            str(project),
            "--epic",
            "EPC-TN-0001",
            "--title",
            "Export personal note",
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        validate = self.run_cli("validate", str(project))
        self.assertEqual(validate.returncode, 0, validate.stdout + validate.stderr)
        self.assertIn("Feature criada", result.stdout)

    def test_feature_create_generates_unique_ids(self) -> None:
        project = self.make_copy(MINIMAL)
        first = self.run_cli(
            "feature",
            "create",
            "--path",
            str(project),
            "--epic",
            "EPC-TN-0001",
            "--title",
            "Export personal note",
        )
        second = self.run_cli(
            "feature",
            "create",
            "--path",
            str(project),
            "--epic",
            "EPC-TN-0001",
            "--title",
            "Export personal note again",
        )
        self.assertEqual(first.returncode, 0, first.stdout + first.stderr)
        self.assertEqual(second.returncode, 0, second.stdout + second.stderr)
        self.assertIn("FEAT-TN-0002", first.stdout)
        self.assertIn("FEAT-TN-0003", second.stdout)

    def test_task_create(self) -> None:
        project = self.make_copy(MINIMAL)
        create_feature = self.run_cli(
            "feature",
            "create",
            "--path",
            str(project),
            "--epic",
            "EPC-TN-0001",
            "--title",
            "Export personal note",
        )
        self.assertEqual(create_feature.returncode, 0, create_feature.stdout + create_feature.stderr)
        result = self.run_cli(
            "task",
            "create",
            "--path",
            str(project),
            "--feature",
            "FEAT-TN-0002",
            "--title",
            "Document export constraints",
            "--depends-on",
            "TASK-TN-0001",
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        validate = self.run_cli("validate", str(project))
        self.assertEqual(validate.returncode, 0, validate.stdout + validate.stderr)

    def test_task_create_missing_feature(self) -> None:
        project = self.make_copy(MINIMAL)
        result = self.run_cli(
            "task",
            "create",
            "--path",
            str(project),
            "--feature",
            "FEAT-TN-9999",
            "--title",
            "Invalid task",
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Feature inexistente", result.stdout)

    def test_decision_create(self) -> None:
        project = self.make_copy(MINIMAL)
        result = self.run_cli(
            "decision",
            "create",
            "--path",
            str(project),
            "--title",
            "Track export boundaries",
            "--related",
            "FEAT-TN-0001",
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        validate = self.run_cli("validate", str(project))
        self.assertEqual(validate.returncode, 0, validate.stdout + validate.stderr)

    def test_release_prepare(self) -> None:
        project = self.make_copy(COMPLETE)
        result = self.run_cli(
            "release",
            "prepare",
            "--path",
            str(project),
            "--title",
            "Moderation scope",
            "--version",
            "1.1.0",
            "--feature",
            "FEAT-COM-0001",
            "--feature",
            "FEAT-COM-0002",
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        validate = self.run_cli("validate", str(project))
        self.assertEqual(validate.returncode, 0, validate.stdout + validate.stderr)

    def test_status_json(self) -> None:
        result = self.run_cli("status", "--path", str(COMPLETE), "--format", "json")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        payload = json.loads(result.stdout)
        self.assertIn("features_by_status", payload)
        self.assertIn("tasks_by_status", payload)
        self.assertIn("validation_errors", payload)
        self.assertEqual(payload["tasks_by_status"].get("ready"), 3)
        self.assertEqual(payload["tasks_by_status"].get("canceled"), 3)
        self.assertEqual(payload["tasks_by_status"].get("done"), 2)
        self.assertEqual(payload["tasks_by_status"].get("validated"), 1)

    def test_validate_integration_json(self) -> None:
        result = self.run_cli("validate", str(MINIMAL), "--format", "json")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        payload = json.loads(result.stdout)
        self.assertIn("findings", payload)

    def test_validate_exit_code_with_errors(self) -> None:
        project = self.make_copy(MINIMAL)
        (project / "dpf" / "PROJECT.md").unlink()
        result = self.run_cli("validate", str(project))
        self.assertEqual(result.returncode, 1)

    def test_unsafe_symlink_path(self) -> None:
        real_dir = Path(tempfile.mkdtemp(prefix="dpf-cli-real-"))
        link_dir = real_dir.parent / f"{real_dir.name}-link"
        try:
            link_dir.symlink_to(real_dir, target_is_directory=True)
        except OSError:
            self.skipTest("Symlinks not supported in this environment")
        result = self.run_cli("init", "--path", str(link_dir), "--name", "Unsafe", "--context", "UNS")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unsafe-symlink-path", result.stderr + result.stdout)


if __name__ == "__main__":
    unittest.main()
