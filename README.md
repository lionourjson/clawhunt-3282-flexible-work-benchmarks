# README — 【S1-RES-014】Member Space Platform · Compilation of Operational Metric Benchmarks in the Flexible Work Industry Report

Prepared for the Business Blueprint module of the Member Space Platform (fictional demo). All cited sources are real, publicly accessible industry reports published within the last 3 years; every source was fetched live on 2026-11-19 and returned HTTP 200. All figures recorded are percentages, ratios, durations, or headcounts only — no monetary values anywhere in this package. Fictional data statement: the client platform referenced in this package is Member Space Platform (fictional demo); no real client name appears in any deliverable.

## Acceptance criteria — verbatim cross-reference (first screen)

| # | Acceptance criterion (verbatim) | How it is satisfied | Where to verify |
|---|---|---|---|
| 1 | "1. The indicator benchmark table must contain no fewer than 10 indicators, with each row including 5 items: report name, year, sample scope, methodology, and value." | `metric_benchmarks.csv` carries 26 rows over 19 distinct indicators (>= 10). Columns `report_name`, `year`, `sample_scope`, `methodology`, `value` are present and non-empty on every row. | Run `verify_3282.py` (checks V3a/V3b); or open the CSV and inspect columns D–H |
| 2 | "2. At least 2 indicators must provide a side-by-side comparison of different report methodologies, along with an explanation of the differences." | `definition_discrepancy_note.md` records 5 side-by-side comparisons (occupancy/utilization across 4 definitions; break-even share internal inconsistency; attendance expectation vs behavior; meeting room utilization rate vs demand ranking; time-to-sustainability population mismatch), each with a table and an "Explanation of the differences" paragraph; values are never merged or averaged. | Check V4 in `verify_3282.py`; or read comparisons 1–5 in the note |
| 3 | "3. No fewer than 4 cited reports, all published within the last 3 years with accessible links." | 5 cited core reports, all published 2025–2026: Deskmag 2025 survey analysis (2025-05-19), Allwork.Space statistics roundup (2025-12-04), CoworkingCafe Q4 2024 report (2025-01-27), CBRE 2025 Americas Occupier Sentiment Survey (2025-08-11), JLL Global Occupancy Planning Benchmark Report 2026 (2026-05-19). All links registered in `sources.csv` (S01–S06) with access_date 2026-11-19 and access_status HTTP 200, re-fetched live during self-check. | Check V6/V7 in `verify_3282.py`; or fetch any URL in `sources.csv` |
| 4 | "4. No monetary values in the table." | Values in `metric_benchmarks.csv` are restricted to percentages, ratios, durations, and headcounts by a `unit_type` column constrained to {percentage, ratio, duration, headcount}; the self-check scans every deliverable body, the table, and the registry for currency symbols and currency-word amount patterns and fails closed on any hit. Where a report page disclosed only monetary figures (iiMedia S08), the report was recorded as reviewed-but-not-adopted with no value extracted. | Check V9 in `verify_3282.py` |

## Scope of This Ticket — item-by-item mapping

| # | Ticket scope item | Where satisfied |
|---|---|---|
| S1 | Research subjects: publicly released flexible office / co-working industry reports from the past 3 years, at least 4 (e.g., Deskmag/GCUC-type surveys, Allwork.Space, CBRE or JLL reports, domestic research institutions) | 5 core reports 2025–2026: Deskmag 2025 survey analysis; Allwork.Space 2025 roundup; CoworkingCafe Q4 2024; CBRE 2025 Americas survey; JLL 2026 benchmark. Domestic institution example checked: iiMedia 2024-2025 report page (S08) — reviewed but not adopted (monetary-only disclosures, software-sector subject); recorded in memo section "Reviewed but not adopted" |
| S2 | >= 10 operational metrics with public benchmarks (occupancy/desk utilization, churn/retention, meeting room utilization, etc.) | `metric_benchmarks.csv`: 26 rows, 19 distinct indicators, including occupancy (B01/B02/B15/B16), retention (B08), meeting room utilization (B23), no-shows (B24), inventory/growth (B13/B14), utilization conventions (B17–B22) |
| S3 | Each metric records report name, publication year, sample scope (region and sample size), metric definition, value | Columns `report_name`, `year`, `sample_scope`, `methodology`, `value` on every row; sample size where not published is recorded as "not disclosed on the public page" (never guessed) |
| S4 | Inconsistent definitions listed side by side, differences noted, never merged or averaged | `definition_discrepancy_note.md` comparisons 1–5; each conflicting value is its own row (e.g., B05 vs B06) |
| S5 | Values only as percentages, ratios, durations, headcounts; no monetary amounts | `unit_type` column constrained to {percentage, ratio, duration, headcount}; package-wide currency-pattern scan fails closed |
| S6 | "Metric Benchmark Table" + "Definition Discrepancy Note" for Business Blueprint North Star / baseline definitions | `metric_benchmarks.csv` + `definition_discrepancy_note.md`; each comparison ends with a "Decision for the Blueprint" paragraph |
| S7 | Memo five-section structure by subject: subject / methodology / adoptable points / non-applicable points / public source links | `research_memo.md`: five subjects (Deskmag, Allwork.Space, CoworkingCafe, CBRE, JLL) each with exactly the five required sections, plus supplementary subject (Nexudus vendor benchmark) and reviewed-but-not-adopted section (iiMedia) |

## Deliverables

| File | Content |
|---|---|
| D1 `research_memo.md` | Research memo, Markdown, 2,500–4,000 words, five-section structure by subject |
| D2 `metric_benchmarks.csv` | Metric Benchmark Table — 26 rows (each row a distinct reported indicator; conflicting definitions kept as separate rows per the no-merge rule), 10 columns incl. the 5 required items per row |
| D3 `definition_discrepancy_note.md` | Definition Discrepancy Note — 5 side-by-side methodology comparisons with explanations |
| D4 `sources.csv` | Source Registry — 10 registered sources with publisher, publication date, year, URL, access date, access status, role |
| — `verify_3282.py` | Fail-closed self-check script (re-loads every deliverable, re-fetches all sources live, scans for monetary values and sensitive patterns) |

## One-command re-verification

```
python -I -X utf8 D:/clawhunt/deliverables/3282/verify_3282.py
```

Expected outcome: every check prints `[PASS]`, the run ends with `SELF-CHECK PASS`, and the exit code is 0. The script re-fetches all 10 registered source URLs live over HTTPS (network required); if any source stops returning HTTP 200, the check fails closed. Environment variables: `PKG_DIR` (package directory override, used for negative testing in a scratch copy) and `TABLE_MIN_ROWS` (minimum benchmark-table rows, default 10).

## Constraints honored

- Fictional data only: all client-side references are Member Space Platform (fictional demo); no real personal or company information is used on the client side; cited reports are real public sources, quoted verbatim where marked.
- No client name in any deliverable beyond the fictional demo name.
- Values: percentages, ratios, durations, headcounts only; no monetary amounts recorded anywhere (ticket rule and acceptance criterion 4).
- Inconsistent definitions listed side by side and explained; never merged or averaged.
- No third-party SDK, no code dependencies: the package is documentation + CSV + one read-only self-check script using the Python standard library only.
- Configuration (package directory, minimum row threshold) read from environment variables.

## Method honesty notes

- Sample sizes that the public report pages do not disclose are recorded as "not disclosed on the public page" — never inferred.
- The Allwork.Space article's internal inconsistency (break-even 28% vs 22%) is kept as two separate rows with an explanation, not averaged.
- One metric in the ticket's example list could not be found as a quantified public benchmark in the last-3-years public pages reviewed: average member tenure, customer acquisition channel composition, community event participation rate, and members served per community manager have no published figures on the free pages of the reviewed reports (Deskmag's staffing/tenure detail sits in its paid report). This is stated openly in the memo's "Coverage of the ticket's named metric list" section; the table carries only traceable figures.
- Supplementary sources are clearly typed: Nexudus is a vendor benchmark (not counted among the cited reports); Facilities Dive is corroborating trade coverage; iiMedia is reviewed-but-not-adopted.
