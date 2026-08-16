#!/usr/bin/env python3
"""
Dependency-free package validation for the Bespoke skill.

Checks, using only the Python standard library (no PyYAML, no third-party
packages, so this runs anywhere Python 3 runs with zero setup):

1. SKILL.md has valid, parseable frontmatter with the required fields.
2. SKILL.md's name and version match .claude-plugin/plugin.json.
3. Every references/*.md file that SKILL.md's "Reference files" section
   names actually exists on disk.
4. .claude-plugin/marketplace.json, if present, lists a plugin entry whose
   name matches plugin.json.

Exit code 0 on success, 1 on any failure, with a plain-English reason for
each failure printed to stdout.

Usage: python3 scripts/validate_package.py
"""

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def fail(errors, message):
    errors.append(message)


def parse_frontmatter(skill_md_text):
    """
    Extract the small, flat set of fields this repo's SKILL.md actually
    uses (name, description, license, compatibility, metadata.version)
    with plain regex rather than a full YAML parser. This is intentionally
    narrow: it is not a general YAML implementation, it is a reader for
    the specific portable frontmatter shape this repo commits to.
    """
    match = re.match(r"^---\n(.*?)\n---", skill_md_text, re.DOTALL)
    if not match:
        return None
    block = match.group(1)

    fields = {}
    name_match = re.search(r"^name:\s*(.+)$", block, re.MULTILINE)
    if name_match:
        fields["name"] = name_match.group(1).strip()

    desc_match = re.search(r"^description:\s*(.+)$", block, re.MULTILINE)
    if desc_match:
        fields["description"] = desc_match.group(1).strip()

    license_match = re.search(r"^license:\s*(.+)$", block, re.MULTILINE)
    if license_match:
        fields["license"] = license_match.group(1).strip()

    # metadata: block, then an indented version: line beneath it
    metadata_match = re.search(
        r"^metadata:\s*\n((?:[ \t]+.+\n?)+)", block, re.MULTILINE
    )
    if metadata_match:
        version_match = re.search(
            r"^\s*version:\s*(.+)$", metadata_match.group(1), re.MULTILINE
        )
        if version_match:
            fields["metadata.version"] = version_match.group(1).strip().strip('"').strip("'")

    return fields


def extract_referenced_files(skill_md_text):
    """
    Find every `references/...` path mentioned anywhere in SKILL.md.
    Deliberately broad (matches inline code-span references, not just the
    dedicated list at the bottom) so a reference used only in prose still
    gets checked.
    """
    return sorted(set(re.findall(r"references/[\w\-]+\.md", skill_md_text)))


def main():
    errors = []

    skill_md_path = REPO_ROOT / "SKILL.md"
    if not skill_md_path.exists():
        print("FAIL: SKILL.md not found at repo root.")
        sys.exit(1)

    skill_md_text = skill_md_path.read_text(encoding="utf-8")
    frontmatter = parse_frontmatter(skill_md_text)

    if frontmatter is None:
        fail(errors, "SKILL.md has no parseable '---' frontmatter block.")
        frontmatter = {}

    for required in ("name", "description"):
        if required not in frontmatter:
            fail(errors, f"SKILL.md frontmatter is missing required field '{required}'.")

    if "metadata.version" not in frontmatter:
        fail(errors, "SKILL.md frontmatter is missing metadata.version.")

    # Cross-check against .claude-plugin/plugin.json, if present
    plugin_json_path = REPO_ROOT / ".claude-plugin" / "plugin.json"
    if plugin_json_path.exists():
        try:
            plugin_data = json.loads(plugin_json_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            fail(errors, f".claude-plugin/plugin.json is not valid JSON: {e}")
            plugin_data = {}

        if plugin_data.get("name") != frontmatter.get("name"):
            fail(
                errors,
                f"Name mismatch: SKILL.md says '{frontmatter.get('name')}', "
                f"plugin.json says '{plugin_data.get('name')}'.",
            )

        if plugin_data.get("version") != frontmatter.get("metadata.version"):
            fail(
                errors,
                f"Version mismatch: SKILL.md metadata.version is "
                f"'{frontmatter.get('metadata.version')}', plugin.json version is "
                f"'{plugin_data.get('version')}'.",
            )
    else:
        print("NOTE: no .claude-plugin/plugin.json found, skipping plugin sync check.")

    # Cross-check marketplace.json, if present
    marketplace_json_path = REPO_ROOT / ".claude-plugin" / "marketplace.json"
    if marketplace_json_path.exists():
        try:
            marketplace_data = json.loads(marketplace_json_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            fail(errors, f".claude-plugin/marketplace.json is not valid JSON: {e}")
            marketplace_data = {}

        for required in ("name", "owner", "plugins"):
            if required not in marketplace_data:
                fail(errors, f"marketplace.json is missing required field '{required}'.")

        plugin_names = [p.get("name") for p in marketplace_data.get("plugins", [])]
        if frontmatter.get("name") not in plugin_names:
            fail(
                errors,
                f"marketplace.json's plugins list {plugin_names} does not include "
                f"'{frontmatter.get('name')}'.",
            )

    # Check every references/*.md path SKILL.md mentions actually exists
    referenced = extract_referenced_files(skill_md_text)
    for rel_path in referenced:
        full_path = REPO_ROOT / rel_path
        if not full_path.exists():
            fail(errors, f"SKILL.md references '{rel_path}', which does not exist.")

    if not referenced:
        print("NOTE: SKILL.md does not mention any references/*.md files.")

    # Flag orphaned reference files SKILL.md never mentions (warning, not a failure)
    references_dir = REPO_ROOT / "references"
    if references_dir.exists():
        on_disk = {f"references/{p.name}" for p in references_dir.glob("*.md")}
        orphaned = sorted(on_disk - set(referenced))
        for orphan in orphaned:
            print(f"WARNING: '{orphan}' exists but SKILL.md never references it.")

    print()
    if errors:
        print(f"FAILED: {len(errors)} issue(s) found.")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("PASSED: package metadata is synchronized and all references resolve.")
        sys.exit(0)


if __name__ == "__main__":
    main()
