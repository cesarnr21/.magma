#!/usr/bin/env python3
"""
notion_to_obsidian.py

Converts Notion-exported Markdown files into Obsidian-friendly notes by
turning the "Key: value" property block Notion puts under the title into
proper YAML frontmatter.

BEFORE:
    # Health Checks Project

    Status: not started
    Tags: infrastructure
    Priority: medium
    services: Health Checks (https://app.notion.com/p/Health-Checks-...)

    This is the actual body content...

AFTER:
    ---
    Status: not started
    Tags: infrastructure
    Priority: medium
    services: "[[Health Checks]]"
    ---

    # Health Checks Project

    This is the actual body content...

USAGE:
    python3 notion_to_obsidian.py /path/to/notion_export_folder [--dry-run]

    --dry-run   Show what would change without writing any files.

It recurses into all subfolders and processes every .md file it finds.
A backup of each modified file is saved next to it with a .bak extension
(only on the first run — it won't overwrite an existing .bak).
"""

import argparse
import re
import sys
from pathlib import Path

# Matches "Key: value" — keys are simple words/spaces, no leading '#' or '-'
PROP_LINE_RE = re.compile(r"^([A-Za-z][A-Za-z0-9 _]*):\s*(.*)$")

# Matches "Some Name (https://...)" so we can turn Notion relation-style
# values into Obsidian wikilinks: "Some Name (https://...)" -> "[[Some Name]]"
NOTION_LINK_RE = re.compile(r"([^,]+?)\s*\(https?://[^\)]+\)")


def convert_value(value: str) -> str:
    """
    Convert a raw property value into a YAML-safe representation.
    - Strips Notion URLs, keeping just the linked page name as a wikilink.
    - Splits comma-separated values into a YAML list.
    - Quotes any value that contains a colon, [[ ]], or leading/trailing
      whitespace so YAML doesn't choke on it.
    """
    # Split on commas that are NOT inside parentheses (so URLs with commas
    # in query strings don't get split apart).
    parts = re.split(r",\s*(?![^(]*\))", value)
    parts = [p.strip() for p in parts if p.strip()]

    converted = []
    for part in parts:
        m = NOTION_LINK_RE.match(part)
        if m:
            name = m.group(1).strip()
            converted.append(f"[[{name}]]")
        else:
            converted.append(part)

    if len(converted) == 0:
        return '""'
    if len(converted) == 1:
        v = converted[0]
        # Quote if it contains characters that would confuse YAML
        if re.search(r'[:#\[\]{}]', v) or v != v.strip():
            return f'"{v}"'
        return v
    # Multiple values -> YAML flow list
    quoted = []
    for v in converted:
        if re.search(r'[:#\[\]{}]', v):
            quoted.append(f'"{v}"')
        else:
            quoted.append(v)
    return "[" + ", ".join(quoted) + "]"


def find_property_block(lines):
    """
    Given the lines of a file (after any leading title line has been
    identified), find the contiguous run of "Key: value" lines and return
    (start_index, end_index_exclusive, list_of_(key,value)_pairs).
    Returns None if no property block is found.
    """
    props = []
    start = None
    i = 0
    n = len(lines)

    # Skip leading blank lines
    while i < n and lines[i].strip() == "":
        i += 1

    while i < n:
        line = lines[i]
        if line.strip() == "":
            break
        m = PROP_LINE_RE.match(line)
        if not m:
            break
        if start is None:
            start = i
        props.append((m.group(1).strip(), m.group(2).strip()))
        i += 1

    if not props:
        return None
    return start, i, props


def process_file(path: Path, dry_run: bool) -> bool:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    # Identify optional title line (starts with '#')
    idx = 0
    n = len(lines)
    while idx < n and lines[idx].strip() == "":
        idx += 1
    title_line = None
    if idx < n and lines[idx].lstrip().startswith("#"):
        title_line = lines[idx]
        idx += 1

    remaining = lines[idx:]
    block = find_property_block(remaining)
    if block is None:
        return False  # nothing to convert in this file

    start, end, props = block

    # Build frontmatter
    fm_lines = ["---"]
    for key, value in props:
        fm_lines.append(f"{key}: {convert_value(value)}")
    fm_lines.append("---")

    # Build new body: title (if any) + everything after the property block
    body_after = remaining[end:]
    # Trim a single leading blank line right after the property block
    if body_after and body_after[0].strip() == "":
        body_after = body_after[1:]

    new_lines = fm_lines + [""]
    if title_line is not None:
        new_lines.append(title_line)
        new_lines.append("")
    new_lines.extend(body_after)

    new_text = "\n".join(new_lines).rstrip() + "\n"

    if dry_run:
        print(f"--- Would convert: {path} ---")
        print(new_text[:500])
        print("...\n")
        return True

    backup = path.with_suffix(path.suffix + ".bak")
    if not backup.exists():
        backup.write_text(text, encoding="utf-8")
    path.write_text(new_text, encoding="utf-8")
    return True


def main():
    parser = argparse.ArgumentParser(description="Convert Notion property blocks to Obsidian frontmatter.")
    parser.add_argument("folder", help="Path to the folder containing your exported .md files")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing files")
    args = parser.parse_args()

    root = Path(args.folder)
    if not root.exists():
        print(f"Folder not found: {root}", file=sys.stderr)
        sys.exit(1)

    md_files = sorted(root.rglob("*.md"))
    if not md_files:
        print("No .md files found.")
        return

    changed = 0
    skipped = 0
    for f in md_files:
        try:
            if process_file(f, args.dry_run):
                changed += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"Error processing {f}: {e}", file=sys.stderr)

    action = "Would convert" if args.dry_run else "Converted"
    print(f"\n{action} {changed} file(s). Skipped {skipped} file(s) with no property block found.")
    if not args.dry_run and changed:
        print("Backups of original files were saved with a .bak extension.")


if __name__ == "__main__":
    main()
