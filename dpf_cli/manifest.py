from __future__ import annotations

from pathlib import Path


def read_simple_yaml(path: Path) -> dict[str, str]:
    data: dict[str, str] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def write_simple_yaml(path: Path, data: dict[str, str]) -> None:
    lines = [f"{key}: {value}" for key, value in data.items()]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
