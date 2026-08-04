from __future__ import annotations

import re
import unicodedata
from pathlib import Path


ID_RE = re.compile(r"\b([A-Z]+-[A-Z0-9]+-\d{4})\b")


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    lowered = ascii_text.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", lowered).strip("-")
    return slug or "item"


def normalize_context(value: str) -> str:
    slug = slugify(value).replace("-", "")
    candidate = slug[:8].upper()
    return candidate or "DPF"


def find_existing_ids(root: Path, prefix: str, context: str) -> set[str]:
    matches: set[str] = set()
    pattern = f"{prefix}-{context}-"
    for path in root.rglob("*"):
        if path.is_symlink():
            continue
        if path.is_file() and path.suffix in {".md", ".yaml", ".yml", ".json", ".txt"}:
            try:
                content = path.read_text(encoding="utf-8")
            except OSError:
                continue
            for match in ID_RE.finditer(content):
                value = match.group(1)
                if value.startswith(pattern):
                    matches.add(value)
        if pattern in path.name:
            match = re.match(rf"({re.escape(prefix)}-{re.escape(context)}-\d{{4}})", path.name)
            if match:
                matches.add(match.group(1))
    return matches


def next_id(root: Path, prefix: str, context: str) -> str:
    used = find_existing_ids(root, prefix, context)
    index = 1
    while True:
        candidate = f"{prefix}-{context}-{index:04d}"
        if candidate not in used:
            return candidate
        index += 1
