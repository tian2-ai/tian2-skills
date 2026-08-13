#!/usr/bin/env python3
"""Mine the local Yau winners archive for prior titles matching topic keywords.

Evidence aid for yau-topic-finder. It does NOT score topics — it surfaces real prior
winner titles so the model can learn the texture of what has placed (and warn against
same-subject cargo-culting). Never fabricates entries: it only reports what is on disk.

Usage:
    python3 mine_winners.py "sieve goldbach number theory"
    python3 mine_winners.py --subject math "isoperimetric"
    python3 mine_winners.py --json "MOF CO2 separation"

Resolves the archive relative to this file, so it is path-independent. Idempotent and
read-only.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]
WINNERS_DIR = SKILL_ROOT / "references" / "winners"
INDEX_CSV = SKILL_ROOT / "references" / "winners_index.csv"

SUBJECT_ALIASES = {
    "math": ("math", "数学"),
    "physics": ("physics", "物理"),
    "chemistry": ("chemistry", "化学"),
    "biology": ("biology", "生物"),
    "cs": ("computer-science", "计算机"),
    "econ": ("economics", "经济"),
}


def tokenize(text: str) -> list[str]:
    return [t for t in re.split(r"[^a-zA-Z0-9一-鿿]+", text.lower()) if len(t) > 1]


def score_line(line: str, keywords: list[str]) -> int:
    low = line.lower()
    return sum(1 for kw in keywords if kw in low)


def harvest_readmes(keywords: list[str], subject: str | None) -> list[tuple[int, str, str]]:
    """Return (hits, year, title-line) from per-year README.md files."""
    results: list[tuple[int, str, str]] = []
    if not WINNERS_DIR.exists():
        return results
    subj_terms = SUBJECT_ALIASES.get(subject, ()) if subject else ()
    for readme in sorted(WINNERS_DIR.glob("*/README.md")):
        year = readme.parent.name
        for raw in readme.read_text(encoding="utf-8", errors="replace").splitlines():
            line = raw.strip()
            # title lines look like: - **[Title](path.pdf)**
            if not line.startswith("- **["):
                continue
            if subj_terms and not any(s in line.lower() for s in subj_terms):
                # README groups by subject heading, so also accept by path slug
                if subject and SUBJECT_ALIASES[subject][0] not in line.lower():
                    pass  # keep; heading context not on this line. fall through to keyword test
            hits = score_line(line, keywords)
            if hits:
                m = re.search(r"\*\*\[(.+?)\]", line)
                title = m.group(1) if m else line
                results.append((hits, year, title))
    return results


def harvest_index(keywords: list[str], subject: str | None) -> list[tuple[int, str, str]]:
    """Return (hits, subject, title) from the flat winners_index.csv."""
    results: list[tuple[int, str, str]] = []
    if not INDEX_CSV.exists():
        return results
    subj_terms = SUBJECT_ALIASES.get(subject, ()) if subject else ()
    with INDEX_CSV.open(encoding="utf-8", errors="replace") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            subj = (row.get("subject") or "").strip()
            title = (row.get("paper_title") or "").strip()
            if not title:
                continue
            if subj_terms and not any(s in subj.lower() for s in subj_terms):
                continue
            hits = score_line(title, keywords)
            if hits:
                results.append((hits, subj, title))
    return results


def main() -> int:
    ap = argparse.ArgumentParser(description="Mine local Yau winners archive by keyword.")
    ap.add_argument("query", help="space-separated keywords")
    ap.add_argument("--subject", choices=sorted(SUBJECT_ALIASES), default=None)
    ap.add_argument("--top", type=int, default=15)
    ap.add_argument("--json", action="store_true", dest="as_json")
    args = ap.parse_args()

    keywords = tokenize(args.query)
    if not keywords:
        print("No usable keywords.", file=sys.stderr)
        return 2

    readme_hits = harvest_readmes(keywords, args.subject)
    index_hits = harvest_index(keywords, args.subject)

    readme_hits.sort(key=lambda r: (-r[0], r[1]))
    index_hits.sort(key=lambda r: -r[0])
    readme_hits = readme_hits[: args.top]
    index_hits = index_hits[: args.top]

    if args.as_json:
        print(json.dumps({
            "query": keywords,
            "subject": args.subject,
            "archive_present": WINNERS_DIR.exists(),
            "matches_from_readmes": [
                {"hits": h, "year": y, "title": t} for h, y, t in readme_hits
            ],
            "matches_from_index": [
                {"hits": h, "subject": s, "title": t} for h, s, t in index_hits
            ],
        }, ensure_ascii=False, indent=2))
        return 0

    if not WINNERS_DIR.exists() and not INDEX_CSV.exists():
        print("Archive not found on disk — report this to the student; widen the score range.")
        return 0

    if not readme_hits and not index_hits:
        print(f"No prior winner titles match {keywords} (subject={args.subject}).")
        print("Archive is SILENT here — treat as low-confidence, not as a green light.")
        return 0

    if readme_hits:
        print("== Prior winners (by-year README) ==")
        for h, y, t in readme_hits:
            print(f"  [{y}] ({h} kw) {t}")
    if index_hits:
        print("\n== Prior entries (flat index) ==")
        for h, s, t in index_hits:
            print(f"  ({s}; {h} kw) {t}")
    print("\nReminder: copying any of these in the SAME subject is a penalty. "
          "Learn the texture; bring your own idea.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
