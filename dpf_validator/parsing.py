from __future__ import annotations

import re
from pathlib import Path


MAX_FILE_SIZE = 1_000_000
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
ID_INLINE_RE = re.compile(r"`([A-Z]+-[A-Z0-9]+-\d{4})`")
H1_ID_RE = re.compile(r"^#\s+([A-Z]+-[A-Z0-9]+-\d{4})\s*$", re.MULTILINE)
SECTION_ID_RE = re.compile(r"^`([A-Z]+-[A-Z0-9]+(?:-[A-Z0-9]+)*-\d{4})`$")
FRONT_MATTER_RE = re.compile(r"\A---\n(.*?)\n---\n?", re.DOTALL)


class ParseError(ValueError):
    pass


def safe_read_text(path: Path) -> str:
    if path.is_symlink():
        raise ParseError(f"symbolic-link-not-allowed:{path}")
    if path.stat().st_size > MAX_FILE_SIZE:
        raise ParseError(f"file-too-large:{path}")
    return path.read_text(encoding="utf-8")


def parse_front_matter(content: str) -> tuple[dict[str, object], str]:
    match = FRONT_MATTER_RE.match(content)
    if not match:
        return {}, content
    body = content[match.end() :]
    raw = match.group(1).splitlines()
    data: dict[str, object] = {}
    current_key: str | None = None
    for line in raw:
        if not line.strip():
            continue
        if line.startswith("  - ") and current_key:
            data.setdefault(current_key, [])
            value = line[4:].strip()
            assert isinstance(data[current_key], list)
            data[current_key].append(_scalar(value))
            continue
        if line.startswith("- ") and current_key:
            data.setdefault(current_key, [])
            value = line[2:].strip()
            assert isinstance(data[current_key], list)
            data[current_key].append(_scalar(value))
            continue
        if ":" not in line:
            raise ParseError("invalid-front-matter-line")
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        current_key = key
        if value == "":
            data[key] = []
            continue
        data[key] = _scalar(value)
    return data, body


def _scalar(value: str) -> object:
    if value.startswith(("'", '"')) and value.endswith(("'", '"')) and len(value) >= 2:
        return value[1:-1]
    return value


def extract_links(content: str) -> list[str]:
    return [match.group(1) for match in LINK_RE.finditer(content)]


def extract_section_lines(content: str, section_title: str) -> list[str]:
    lines = content.splitlines()
    collecting = False
    results: list[str] = []
    wanted = section_title.casefold()
    for line in lines:
        heading = HEADING_RE.match(line)
        if heading:
            title = heading.group(2).strip().casefold()
            if collecting and title != wanted:
                break
            if title == wanted:
                collecting = True
                continue
        if collecting:
            if line.strip():
                results.append(line.rstrip())
    return results


def find_first_id(content: str) -> str | None:
    h1 = H1_ID_RE.search(content)
    if h1:
        return h1.group(1)
    for line in extract_section_lines(content, "ID"):
        match = SECTION_ID_RE.fullmatch(line.strip())
        if match:
            return match.group(1)
    return None


def find_status(content: str) -> str | None:
    section = extract_section_lines(content, "Estado")
    if not section:
        return None
    first = section[0].strip()
    match = ID_INLINE_RE.search(first)
    if match:
        return match.group(1)
    if first.startswith("`") and first.endswith("`"):
        return first.strip("`")
    return first


def find_title_from_name(content: str) -> str | None:
    for line in content.splitlines():
        heading = HEADING_RE.match(line)
        if heading:
            value = heading.group(2).strip()
            if value:
                return value
    return None


def parse_task_status_table(content: str) -> dict[str, str]:
    lines = content.splitlines()
    task_statuses: dict[str, str] = {}
    for line in lines:
        if not line.startswith("|"):
            continue
        cells = [item.strip() for item in line.strip("|").split("|")]
        if len(cells) < 3:
            continue
        if cells[0].startswith("TASK-"):
            task_statuses[cells[0]] = cells[2]
    return task_statuses


def extract_acceptance_criteria(content: str) -> list[str]:
    return [line for line in extract_section_lines(content, "Critérios de aceite") if "AC-" in line]


def extract_release_items(content: str) -> list[str]:
    section = extract_section_lines(content, "Itens incluídos")
    return [match.group(1) for line in section for match in ID_INLINE_RE.finditer(line)]


def extract_justification(content: str) -> str | None:
    section = extract_section_lines(content, "Justificativa")
    if not section:
        return None
    return " ".join(item.strip() for item in section)


def has_completion_criteria(content: str, metadata: dict[str, object]) -> bool:
    if "definition_of_done" in metadata:
        value = metadata["definition_of_done"]
        if isinstance(value, list):
            return bool(value)
        if isinstance(value, str):
            return bool(value.strip())
    for title in ("Definition of Done", "Critérios de conclusão", "Criterios de conclusao"):
        if extract_section_lines(content, title):
            return True
    return False
