#!/usr/bin/env python3
"""Validate the approved 6-Part/19-Chapter documentation structure."""

import json
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
docs = root / "docs"
site = root / "site"

index = json.loads(
    (root / "project/planning/chapter-index.json").read_text(
        encoding="utf-8"
    )
)

chapters = index["chapters"]

expected_counts = {1: 2, 2: 4, 3: 2, 4: 5, 5: 3, 6: 3}
valid_statuses = {"published", "scaffold"}

# 1. Chapter numbering
if [c["number"] for c in chapters] != list(range(1, 20)):
    sys.exit("ERROR: expected chapters numbered 1 through 19")

# 2. Part allocation
counts = {
    p: sum(c["part"] == p for c in chapters)
    for p in expected_counts
}

if counts != expected_counts:
    sys.exit(f"ERROR: approved Part allocation mismatch: {counts}")

# 3. MkDocs configuration
config = (root / "mkdocs.yml").read_text(encoding="utf-8")

if not re.search(r"^docs_dir:\s*docs\s*$", config, re.M):
    sys.exit("ERROR: docs_dir must be docs")

if not re.search(r"^site_dir:\s*site\s*$", config, re.M):
    sys.exit("ERROR: site_dir must be site")

# 4. Navigation validation
nav_paths = re.findall(
    r"part-\d{2}-[a-z0-9-]+/chapter-\d{2}-[a-z0-9-]+\.md",
    config
)

if nav_paths != [c["path"] for c in chapters]:
    sys.exit("ERROR: MkDocs navigation differs from chapter index")

published = []
scaffolds = []

# 5. Chapter validation
for c in chapters:
    number = c["number"]
    status = c.get("status")

    if status not in valid_statuses:
        sys.exit(
            f"ERROR: Chapter {number} has invalid or missing status: {status}"
        )

    p = docs / c["path"]

    if not p.is_file():
        sys.exit(f"ERROR: Chapter file missing: {p}")

    lines = p.read_text(encoding="utf-8").splitlines()

    if not lines or lines[0] != (
        f"# Chapter {number:02d} — {c['title']}"
    ):
        sys.exit(f"ERROR: heading/index mismatch: {p}")

    is_scaffold = any(
        "Navigation scaffold only" in line
        for line in lines
    )

    if status == "published":
        if is_scaffold:
            sys.exit(
                f"ERROR: Published Chapter {number} "
                "is still marked as a scaffold"
            )

        published.append(number)

        if number in (1, 2, 3):
            if not any(
                "Lab status:" in line
                and "Designed, not tested" in line
                for line in lines[:12]
            ):
                sys.exit(
                    f"ERROR: Chapter {number} must disclose "
                    "that its lab is designed, not tested"
                )

    elif status == "scaffold":
        if not is_scaffold:
            sys.exit(
                f"ERROR: Chapter {number} must remain "
                "a navigation scaffold"
            )

        scaffolds.append(number)

# 6. Site boundary validation
if not (site / "index.html").is_file():
    sys.exit("ERROR: site/index.html missing")

if (site / "project").exists():
    sys.exit("ERROR: project records leaked into site output")

# 7. Success report
print("PASS: approved 6-Part / 19-Chapter structure and navigation")
print(f"PASS: Published chapters: {published}")
print(f"PASS: Scaffold chapters: {scaffolds}")
print("PASS: Chapter headings and status declarations are valid")
print("PASS: site output exists and project/ is excluded")
