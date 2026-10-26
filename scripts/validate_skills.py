#!/usr/bin/env python3
"""Validate portable Agent Skills metadata and README catalog links."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
README = ROOT / "README.md"
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
CATALOG_PATTERN = re.compile(r"skills/([a-z0-9-]+)/SKILL\.md")


def parse_frontmatter(path: Path, content: str, errors: list[str]) -> tuple[dict[str, str], str]:
    if not content.startswith("---\n"):
        errors.append(f"{path.relative_to(ROOT)}: missing YAML frontmatter opener")
        return {}, ""

    end = content.find("\n---\n", 4)
    if end < 0:
        errors.append(f"{path.relative_to(ROOT)}: missing YAML frontmatter closer")
        return {}, ""

    metadata: dict[str, str] = {}
    for line_number, line in enumerate(content[4:end].splitlines(), start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            errors.append(f"{path.relative_to(ROOT)}:{line_number}: expected key: value metadata")
            continue
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip()
        if key in metadata:
            errors.append(f"{path.relative_to(ROOT)}:{line_number}: duplicate metadata key {key!r}")
        metadata[key] = value

    return metadata, content[end + len("\n---\n"):]


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md")) if SKILLS_DIR.exists() else []
    if not skill_files:
        errors.append("skills/: no skill directories with SKILL.md were found")

    seen_names: set[str] = set()
    actual_names: set[str] = set()

    for path in skill_files:
        relative = path.relative_to(ROOT)
        content = path.read_text(encoding="utf-8")
        metadata, body = parse_frontmatter(path, content, errors)
        name = metadata.get("name", "")
        description = metadata.get("description", "")

        if not name:
            errors.append(f"{relative}: required metadata field 'name' is empty or missing")
        elif not NAME_PATTERN.fullmatch(name):
            errors.append(f"{relative}: name must use lowercase letters, numbers, and single hyphens")
        elif len(name) > 64:
            errors.append(f"{relative}: name exceeds 64 characters")
        if name and name != path.parent.name:
            errors.append(f"{relative}: metadata name {name!r} must match directory {path.parent.name!r}")
        if name in seen_names and name:
            errors.append(f"{relative}: duplicate skill name {name!r}")
        if name:
            seen_names.add(name)
            actual_names.add(name)

        if not description:
            errors.append(f"{relative}: required metadata field 'description' is empty or missing")
        elif len(description) > 1024:
            errors.append(f"{relative}: description exceeds 1024 characters")
        if not body.strip():
            errors.append(f"{relative}: instruction body is empty")
        if len(content.splitlines()) > 500:
            warnings.append(f"{relative}: exceeds the recommended 500-line guidance size")

    if README.exists():
        readme_text = README.read_text(encoding="utf-8")
        catalog_names = set(CATALOG_PATTERN.findall(readme_text))
        for name in sorted(actual_names - catalog_names):
            errors.append(f"README.md: skill {name!r} exists but is not linked in the catalog")
        for name in sorted(catalog_names - actual_names):
            errors.append(f"README.md: catalog entry {name!r} has no matching skills/{name}/SKILL.md")
    else:
        errors.append("README.md: missing repository overview and skill catalog")

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        print(f"Validation failed with {len(errors)} error(s) and {len(warnings)} warning(s).")
        return 1
    print(f"Validated {len(skill_files)} skill(s); metadata and README catalog are consistent.")
    if warnings:
        print(f"Review {len(warnings)} warning(s) above.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
