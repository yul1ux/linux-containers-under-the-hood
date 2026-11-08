#!/usr/bin/env python3
"""Check the approved 6-Part/19-Chapter docs scaffold and site boundary."""
import json
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
docs = root / "docs"
site = root / "site"
index = json.loads((root / "project/planning/chapter-index.json").read_text(encoding="utf-8"))
chapters = index["chapters"]
expected_counts = {1: 2, 2: 4, 3: 2, 4: 5, 5: 3, 6: 3}
if [c["number"] for c in chapters] != list(range(1, 20)):
    sys.exit("ERROR: expected chapters numbered 1 through 19")
counts = {p: sum(c["part"] == p for c in chapters) for p in expected_counts}
if counts != expected_counts:
    sys.exit(f"ERROR: approved Part allocation mismatch: {counts}")
config = (root / "mkdocs.yml").read_text(encoding="utf-8")
if not re.search(r"^docs_dir:\s*docs\s*$", config, re.M):
    sys.exit("ERROR: docs_dir must be docs")
if not re.search(r"^site_dir:\s*site\s*$", config, re.M):
    sys.exit("ERROR: site_dir must be site")
nav_paths = re.findall(r"part-\d{2}-[a-z0-9-]+/chapter-\d{2}-[a-z0-9-]+\.md", config)
if nav_paths != [c["path"] for c in chapters]:
    sys.exit("ERROR: MkDocs navigation differs from chapter index")
for c in chapters:
    p = docs / c["path"]
    lines = p.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != f"# Chapter {c['number']:02d} — {c['title']}":
        sys.exit(f"ERROR: heading/index mismatch: {p}")
    is_scaffold = any("Navigation scaffold only" in line for line in lines)
    if c["number"] == 1:
        if is_scaffold:
            sys.exit(f"ERROR: published Chapter 1 is still marked as a scaffold: {p}")
        if not any("Lab status:" in line and "Designed, not tested" in line for line in lines[:12]):
            sys.exit(f"ERROR: Chapter 1 must disclose that its lab is designed, not tested: {p}")
    elif not is_scaffold:
        sys.exit(f"ERROR: Chapter {c['number']} must remain a navigation scaffold until separately authorized: {p}")
if not (site / "index.html").is_file():
    sys.exit("ERROR: site/index.html missing")
if (site / "project").exists():
    sys.exit("ERROR: project records leaked into site output")
print("PASS: approved 6-Part / 19-Chapter structure and navigation")
print("PASS: Chapter 1 manuscript is present and its untested lab status is explicit")
print("PASS: Chapters 2–19 remain clearly marked as scaffolds")
print("PASS: site output exists and project/ is excluded")
