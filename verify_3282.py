# -*- coding: utf-8 -*-
"""verify_3282.py — fail-closed self-check for deliverables/3282.

Ticket 【S1-RES-014】 (problem 3282). Read-only over the deliverables; writes nothing.
Env overrides (used for negative testing):
  PKG_DIR        package directory (default: this script's directory)
  TABLE_MIN_ROWS minimum benchmark-table rows (default 10, acceptance criterion 1)
Exit 0 only if every check passes; any failure raises AssertionError (exit 1).
"""
import csv
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

PKG = Path(os.environ.get("PKG_DIR", Path(__file__).resolve().parent))
TABLE_MIN_ROWS = int(os.environ.get("TABLE_MIN_ROWS", "10"))
TODAY = "2026-11-19"
EN = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
HDRS = {"User-Agent": EN, "Accept": "text/html,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip",
        "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none", "Connection": "close"}

RESULTS = []


def check(name, fn):
    try:
        detail = fn()
        RESULTS.append((True, name, detail or ""))
        print(f"[PASS] {name}" + (f" — {detail}" if detail else ""))
    except AssertionError as e:
        RESULTS.append((False, name, str(e)))
        print(f"[FAIL] {name} — {e}")
    except Exception as e:  # noqa: BLE001 — fail closed on any error
        RESULTS.append((False, name, repr(e)))
        print(f"[FAIL] {name} — {repr(e)}")


def read(p):
    return (PKG / p).read_text(encoding="utf-8")


def words(text):
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’\-\.]*", text))


# ---------------------------------------------------------------- load files
MEMO = read("research_memo.md")
NOTE = read("definition_discrepancy_note.md")
README = read("README.md")
with (PKG / "metric_benchmarks.csv").open(encoding="utf-8", newline="") as f:
    TABLE = list(csv.DictReader(f))
with (PKG / "sources.csv").open(encoding="utf-8", newline="") as f:
    SOURCES = list(csv.DictReader(f))


# ---------------------------------------------------------------- V1 memo
def v1():
    n = words(MEMO)
    assert 2500 <= n <= 4000, f"memo word count {n} outside 2500-4000"
    return f"words={n}"


def v2():
    for sec in ("### Subject", "### Methodology", "### Adoptable points",
                "### Non-applicable points", "### Public source links"):
        c = MEMO.count(sec)
        assert c >= 5, f"section '{sec}' count {c} < 5 (five core subjects)"
    assert "## Subject 1" in MEMO and "## Subject 5" in MEMO, "five subject headers missing"
    assert "Supplementary subject" in MEMO, "supplementary subject missing"
    assert "Reviewed but not adopted" in MEMO, "reviewed-but-not-adopted section missing"
    return "5 sections x 5 subjects + supplementary + reviewed-not-adopted"


# ---------------------------------------------------------------- V3 table
def v3a():
    assert len(TABLE) >= TABLE_MIN_ROWS, f"table rows {len(TABLE)} < {TABLE_MIN_ROWS}"
    return f"rows={len(TABLE)} (min {TABLE_MIN_ROWS})"


def v3b():
    req = ["report_name", "year", "sample_scope", "methodology", "value"]
    for i, row in enumerate(TABLE, 1):
        for col in req:
            v = (row.get(col) or "").strip()
            assert v, f"row {i} empty required column '{col}'"
    names = [r["indicator_name"].strip() for r in TABLE]
    assert len(set(names)) == len(names), "duplicate indicator_name rows (merge suspicion)"
    return f"5 required items non-empty on all {len(TABLE)} rows; names unique"


def v3c():
    allowed = {"percentage", "ratio", "duration", "headcount"}
    bad = [r["metric_no"] for r in TABLE if (r.get("unit_type") or "").strip() not in allowed]
    assert not bad, f"unit_type outside allowed set: {bad}"
    return f"unit_type values within {sorted(allowed)}"


# ---------------------------------------------------------------- V4 note
def v4():
    comps = re.findall(r"^## Comparison \d+", NOTE, re.M)
    assert len(comps) >= 2, f"only {len(comps)} side-by-side comparisons found (< 2)"
    exp = NOTE.count("Explanation of the differences")
    assert exp >= 2, f"'Explanation of the differences' count {exp} < 2"
    dec = NOTE.count("Decision for the Blueprint")
    assert dec >= 2, f"'Decision for the Blueprint' count {dec} < 2"
    return f"comparisons={len(comps)} explanations={exp} blueprint-decisions={dec}"


# ---------------------------------------------------------------- V5/V6 sources
def v5():
    role_core = [s for s in SOURCES if (s.get("role_in_memo") or "").startswith("core report")]
    assert len(role_core) >= 4, f"core cited reports {len(role_core)} < 4"
    publishers = {s["publisher"] for s in role_core}
    assert len(publishers) >= 4, f"distinct core report publishers {len(publishers)} < 4"
    for s in role_core:
        y = int(s["year"])
        assert 2024 <= y <= 2026, f"core report {s['source_id']} year {y} outside last 3 years"
        assert s["access_date"] == TODAY, f"core report {s['source_id']} access_date != {TODAY}"
        assert s["access_status"] == "HTTP 200", f"core report {s['source_id']} access_status"
        assert s["url"].startswith("https://"), f"core report {s['source_id']} non-https url"
    return (f"core report rows={len(role_core)} across {len(publishers)} distinct publishers "
            f"({sorted(publishers)}); all 2024-2026, all {TODAY} HTTP 200")


def v6():
    assert len(SOURCES) >= 8, f"source registry rows {len(SOURCES)} < 8"
    for i, s in enumerate(SOURCES, 1):
        for col in ("source_id", "publisher", "report_name", "url",
                    "access_date", "access_status", "role_in_memo"):
            assert (s.get(col) or "").strip(), f"source row {i} missing '{col}'"
    ids = [s["source_id"] for s in SOURCES]
    assert len(set(ids)) == len(ids), "duplicate source_id"
    return f"registry rows={len(SOURCES)} (>=8), all required fields present"


# ---------------------------------------------------------------- V7 live GET
def v7():
    import gzip
    failures = []
    for s in SOURCES:
        req = urllib.request.Request(s["url"], headers=HDRS)
        try:
            with urllib.request.urlopen(req, timeout=40) as r:
                st = r.getcode()
                raw = r.read()
            if raw[:2] == b"\x1f\x8b":
                raw = gzip.decompress(raw)
            ok = st == 200 and len(raw) > 1000
        except Exception as e:  # noqa: BLE001
            ok, st = False, repr(e)[:60]
        if not ok:
            failures.append(f"{s['source_id']}:{st}")
    assert not failures, f"live re-fetch failures: {failures}"
    return f"all {len(SOURCES)} registered sources re-fetched live right now: failures=[]"


# ---------------------------------------------------------------- V8 citations
def v8():
    memo_ids = set(re.findall(r"\bS\d{2}\b", MEMO)) | set(re.findall(r"\bS\d{2}\b", NOTE))
    reg_ids = {s["source_id"] for s in SOURCES}
    unreg = sorted(memo_ids - reg_ids)
    assert not unreg, f"memo/note cite unregistered sources: {unreg}"
    core_ids = {s["source_id"] for s in SOURCES
                if (s.get("role_in_memo") or "").startswith("core report")}
    missing = sorted(core_ids - memo_ids)
    assert not missing, f"core reports never cited in memo/note: {missing}"
    for row in TABLE:
        for sid in re.findall(r"S\d{2}", row.get("source_id", "")):
            assert sid in reg_ids, f"table row {row['metric_no']} cites unregistered {sid}"
    return f"memo/note cites {sorted(memo_ids)} all registered; core reports all cited"


# ---------------------------------------------------------------- V9 money
MONEY_PATTERNS = [
    re.compile(r"[$€£¥]\s*\d"), re.compile(r"\bUS\$"), re.compile(r"\bUSD\b"),
    re.compile(r"\bEUR\b"), re.compile(r"\bGBP\b"), re.compile(r"\bCNY\b"),
    re.compile(r"\d[\d,\.]*\s*(?:USD|EUR|GBP|CNY|dollars?|euros?|yuan|renminbi)\b", re.I),
    re.compile(r"\d[\d,\.]*\s*(?:元|万元|亿元|美元|英镑|欧元|人民币)"),
    re.compile(r"\b\d[\d,\.]*\s*(?:million|billion)\s+(?:dollars|euros|USD)\b", re.I),
]


def v9():
    hits = []
    for fname, text in (("research_memo.md", MEMO), ("definition_discrepancy_note.md", NOTE),
                        ("README.md", README)):
        for pat in MONEY_PATTERNS:
            for m in pat.finditer(text):
                hits.append(f"{fname}:{m.group(0)!r}")
    for row in TABLE:
        joined = " ".join(str(v) for v in row.values())
        for pat in MONEY_PATTERNS:
            for m in pat.finditer(joined):
                hits.append(f"metric_benchmarks.csv[{row['metric_no']}]:{m.group(0)!r}")
    for s in SOURCES:
        joined = " ".join(str(v) for v in s.values())
        for pat in MONEY_PATTERNS:
            for m in pat.finditer(joined):
                hits.append(f"sources.csv[{s['source_id']}]:{m.group(0)!r}")
    assert not hits, f"monetary values found: {hits[:10]}"
    return "zero monetary-pattern hits across memo/note/README/table/registry"


# ---------------------------------------------------------------- V10 sensitive
SENSITIVE = [
    re.compile(r"clawhunt_key|api[_-]?key|Bearer\s+[A-Za-z0-9]|\bsk-[A-Za-z0-9]{8}", re.I),
    re.compile(r"[CD]:\\+Users\\+[A-Za-z]+"), re.compile(r"https?://(localhost|127\.0\.0\.1)"),
    re.compile(r"BEGIN [A-Z]+ PRIVATE KEY"),
]


def v10():
    hits = []
    for fname, text in (("research_memo.md", MEMO), ("definition_discrepancy_note.md", NOTE),
                        ("README.md", README)):
        for i, line in enumerate(text.splitlines(), 1):
            for pat in SENSITIVE:
                if pat.search(line):
                    hits.append(f"{fname}:{i}:{pat.pattern[:30]}")
    for row in TABLE:
        for pat in SENSITIVE:
            for key, v in row.items():
                if pat.search(str(v)):
                    hits.append(f"metric_benchmarks.csv[{row['metric_no']}]:{key}")
    assert not hits, f"sensitive-pattern hits: {hits[:10]}"
    return "zero sensitive-pattern hits (key/absolute-path/localhost/private-key)"


# ---------------------------------------------------------------- V11 en locale
ZH_RUN = re.compile(r"[\u4e00-\u9fff]{2,}")


def v11():
    bad = []
    for fname, text in (("research_memo.md", MEMO), ("definition_discrepancy_note.md", NOTE),
                        ("README.md", README)):
        m = ZH_RUN.search(text)
        if m:
            bad.append(f"{fname}:{m.group(0)!r}")
    for row in TABLE:
        m = ZH_RUN.search(" ".join(str(v) for v in row.values()))
        if m:
            bad.append(f"metric_benchmarks.csv:{m.group(0)!r}")
    assert not bad, f"Chinese runs found (response_locale=en): {bad[:6]}"
    return "zero Chinese runs in deliverable bodies (en locale)"


# ---------------------------------------------------------------- V12 README AC
ACS = [
    "1. The indicator benchmark table must contain no fewer than 10 indicators, with each row including 5 items: report name, year, sample scope, methodology, and value.",
    "2. At least 2 indicators must provide a side-by-side comparison of different report methodologies, along with an explanation of the differences.",
    "3. No fewer than 4 cited reports, all published within the last 3 years with accessible links.",
    "4. No monetary values in the table.",
]


def v12():
    missing = [a for a in ACS if a not in README]
    assert not missing, f"acceptance criteria not verbatim in README: {len(missing)} missing"
    return "acceptance criteria 4/4 verbatim in README"


# ---------------------------------------------------------------- V13 fictional
def v13():
    assert "Member Space Platform (fictional demo)" in MEMO, "memo missing fictional statement"
    assert "Member Space Platform (fictional demo)" in README, "README missing fictional statement"
    return "fictional-client statement present in memo and README"


# ---------------------------------------------------------------- V14 scope map
def v14():
    for tag in ("S1", "S2", "S3", "S4", "S5", "S6", "S7",
                "D1", "D2", "D3", "D4", "research_memo.md", "metric_benchmarks.csv",
                "definition_discrepancy_note.md", "sources.csv"):
        assert tag in README, f"README scope mapping missing '{tag}'"
    return "README scope mapping covers S1-S7, D1-D4 and all four deliverable files"


def main():
    print(f"PKG_DIR={PKG}  TABLE_MIN_ROWS={TABLE_MIN_ROWS}")
    check("V1a memo word count 2500-4000", v1)
    check("V2 five-section structure x 5 subjects (+supplementary, +not-adopted)", v2)
    check("V3a benchmark table rows >= TABLE_MIN_ROWS", v3a)
    check("V3b every row carries report_name/year/sample_scope/methodology/value", v3b)
    check("V3c unit_type constrained to percentage/ratio/duration/headcount", v3c)
    check("V4 >= 2 side-by-side comparisons with explanations and Blueprint decisions", v4)
    check("V5 core cited reports >= 4, all within last 3 years, stamped+200", v5)
    check("V6 source registry >= 8 rows, all fields present, ids unique", v6)
    check("V7 all registered sources re-fetched live right now", v7)
    check("V8 memo/note/table citations == registry (bidirectional)", v8)
    check("V9 no monetary values in any deliverable body or table", v9)
    check("V10 sensitive-pattern scan zero hits", v10)
    check("V11 no Chinese runs in deliverable bodies (en locale)", v11)
    check("V12 acceptance criteria verbatim in README 4/4", v12)
    check("V13 fictional-client statement present", v13)
    check("V14 README scope mapping complete", v14)
    fails = [r for r in RESULTS if not r[0]]
    print()
    if fails:
        print(f"SELF-CHECK FAIL ({len(fails)} failed of {len(RESULTS)} checks)")
        sys.exit(1)
    print(f"SELF-CHECK PASS ({len(RESULTS)} checks)")
    sys.exit(0)


if __name__ == "__main__":
    main()
