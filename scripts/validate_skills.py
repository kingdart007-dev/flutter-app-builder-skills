#!/usr/bin/env python3
"""Validate Agent Skills metadata, catalog entries, and relative Markdown links."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
CATALOG_PATTERN = re.compile(r"skills/([^/]+)/SKILL\.md")
MARKDOWN_LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
FENCED_BLOCK_PATTERN = re.compile(r"(?ms)^\s*```[^\n]*\n.*?^\s*```\s*$")


def parse_frontmatter(path: Path, content: str, errors: list[str]) -> tuple[dict[str, str], str]:
    """Parse the simple scalar frontmatter used by this collection."""
    relative = path.as_posix()
    if not content.startswith("---\n"):
        errors.append(f"{relative}: missing YAML frontmatter opener")
        return {}, ""

    end = content.find("\n---\n", 4)
    if end < 0:
        errors.append(f"{relative}: missing YAML frontmatter closer")
        return {}, ""

    metadata: dict[str, str] = {}
    for line_number, line in enumerate(content[4:end].splitlines(), start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            errors.append(f"{relative}:{line_number}: expected key: value metadata")
            continue
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip()
        if key in metadata:
            errors.append(f"{relative}:{line_number}: duplicate metadata key {key!r}")
        metadata[key] = value

    return metadata, content[end + len("\n---\n"):]


def _unquote(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'", '"'):
        return value[1:-1]
    return value


def _markdown_files(root: Path) -> list[Path]:
    return sorted(
        path for path in root.rglob("*.md")
        if ".git" not in path.parts and not any(part.startswith(".venv") for part in path.parts)
    )


def _validate_markdown_links(root: Path, errors: list[str]) -> None:
    for markdown_path in _markdown_files(root):
        text = markdown_path.read_text(encoding="utf-8")
        text = FENCED_BLOCK_PATTERN.sub("", text)
        for match in MARKDOWN_LINK_PATTERN.finditer(text):
            target = match.group(1).strip()
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            if not target or target.startswith(("#", "//")):
                continue
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                continue
            local_target = target.split("#", 1)[0].split("?", 1)[0].strip()
            if not local_target:
                continue
            candidate = (markdown_path.parent / local_target).resolve()
            if not candidate.exists():
                relative_file = markdown_path.relative_to(root)
                errors.append(
                    f"{relative_file}: broken relative Markdown link {target!r}"
                )


def validate(root: Path) -> tuple[list[str], list[str], int]:
    """Return (errors, warnings, number_of_skill_files) for a repository root."""
    root = root.resolve()
    errors: list[str] = []
    warnings: list[str] = []
    skills_dir = root / "skills"
    if not skills_dir.is_dir():
        errors.append("skills/: directory is missing")
        skill_dirs: list[Path] = []
    else:
        skill_dirs = sorted(path for path in skills_dir.iterdir() if path.is_dir())
        if not skill_dirs:
            errors.append("skills/: no skill directories were found")

    skill_files: list[Path] = []
    directory_names: set[str] = set()
    seen_metadata_names: set[str] = set()

    for skill_dir in skill_dirs:
        path = skill_dir / "SKILL.md"
        relative = path.relative_to(root).as_posix()
        directory_names.add(skill_dir.name)
        if not path.is_file():
            errors.append(f"{relative}: skill directory is missing SKILL.md")
            continue

        skill_files.append(path)
        content = path.read_text(encoding="utf-8")
        metadata, body = parse_frontmatter(path, content, errors)
        name = _unquote(metadata.get("name", "").strip())
        description = _unquote(metadata.get("description", "").strip())

        if not name:
            errors.append(f"{relative}: required metadata field 'name' is empty or missing")
        elif not NAME_PATTERN.fullmatch(name):
            errors.append(
                f"{relative}: name must use lowercase letters, numbers, and single hyphens"
            )
        elif len(name) > 64:
            errors.append(f"{relative}: name exceeds 64 characters")
        if name and name != skill_dir.name:
            errors.append(
                f"{relative}: metadata name {name!r} must match directory {skill_dir.name!r}"
            )
        if name in seen_metadata_names and name:
            errors.append(f"{relative}: duplicate skill metadata name {name!r}")
        if name:
            seen_metadata_names.add(name)

        if not description:
            errors.append(
                f"{relative}: required metadata field 'description' is empty or missing"
            )
        elif len(description) > 1024:
            errors.append(f"{relative}: description exceeds 1024 characters")
        if not body.strip():
            errors.append(f"{relative}: instruction body is empty")
        if len(content.splitlines()) > 500:
            warnings.append(f"{relative}: exceeds the recommended 500-line guidance size")

    readme = root / "README.md"
    if not readme.is_file():
        errors.append("README.md: missing repository overview and skill catalog")
    else:
        readme_text = readme.read_text(encoding="utf-8")
        catalog_entries = CATALOG_PATTERN.findall(readme_text)
        catalog_names = set(catalog_entries)
        for name in sorted(set(catalog_entries)):
            if catalog_entries.count(name) > 1:
                errors.append(f"README.md: catalog entry for {name!r} appears more than once")
        for name in sorted(directory_names - catalog_names):
            errors.append(f"README.md: skill directory {name!r} is not linked in the catalog")
        for name in sorted(catalog_names - directory_names):
            errors.append(f"README.md: catalog entry {name!r} has no matching skill directory")

    _validate_markdown_links(root, errors)
    return errors, warnings, len(skill_files)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=ROOT,
        help="repository root to validate (defaults to the current skills repository)",
    )
    args = parser.parse_args(argv)
    errors, warnings, skill_count = validate(args.root)

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        print(f"Validation failed with {len(errors)} error(s) and {len(warnings)} warning(s).")
        return 1

    print(
        f"Validated {skill_count} skill(s); metadata, catalog, and Markdown links are consistent."
    )
    if warnings:
        print(f"Review {len(warnings)} warning(s) above.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
