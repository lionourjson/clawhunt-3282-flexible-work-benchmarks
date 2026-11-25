# Definition Discrepancy Note

**Ticket:** 【S1-RES-014】Member Space Platform · Compilation of Operational Metric Benchmarks in the Flexible Work Industry Report
**Purpose:** per the ticket, when different reports use inconsistent definitions for the same indicator, they are listed side by side and the differences are noted; values are never merged or averaged. This note records every side-by-side comparison (rows B01–B26 in `metric_benchmarks.csv`), so the Business Blueprint module can pick a definition — not a blend — for each North Star and baseline metric.

---

## Comparison 1: Occupancy rate / desk utilization rate (4 incompatible definitions)

| Side | Report | Published | Sample scope | Methodology | Value | Row |
|---|---|---|---|---|---|---|
| A | 2025 Global Coworking Space Trends Survey (Deskmag) | 2025 | Coworking operators worldwide (n not disclosed on public page) | Operator self-report survey | 68% average at the start of 2025 | B01 |
| B | Global Occupancy Planning Benchmark Report 2026 (JLL) | 2026 | 84 corporate organizations, 716 million sq ft, six regions | Measured corporate occupancy-planning data (space-level, badge/sensor backed) | 56% in 2026 (54% in 2025, 49% in 2024) | B15 |
| C | 2025 Americas Office Occupier Sentiment Survey (CBRE) | 2025 | Office-using companies across the US, Canada, Latin America (n not stated on page) | Occupier sentiment survey, Q2 2025 | 73% at capacity on peak days; 34% on average days | B18, B19 |
| D | Coworking Statistics and Key Trends Shaping the 2026 Flexible Workspace Industry (Allwork.Space) | 2025 | Global demand side, by industry vertical | Secondary aggregation of published surveys | BFSI sector occupancy 32.40% | B26 |

**Explanation of the differences.** All four are called "occupancy" or "utilization" but measure different quantities. A is supply-side operator self-report: share of an operator's own desks in use — the only side that approximates a membership space's desk occupancy. B is corporate-measured utilization: share of usable hours in which corporate space is actually used, measured from space-level data, systematically lower than A because it counts all working hours and unassigned space. C is a share-of-organizations statistic: the percentage of surveyed organizations whose space is (or is not) at capacity, not a percentage of space — 73% vs 34% describe distribution across organizations, not one office's utilization. D is a demand-side share: the weight of one industry within coworking demand, not space usage at all. **Decision for the Blueprint:** adopt A's supply-side definition (occupied desk-hours over available desk-hours) for the platform's occupancy North Star; keep C's peak/average split as two separate reported metrics; never present B or D as if comparable to A. The four values are recorded in four rows and are not averaged.

## Comparison 2: Break-even share inside the same aggregation (internal inconsistency)

| Side | Report | Published | Sample scope | Methodology | Value | Row |
|---|---|---|---|---|---|---|
| A | Allwork.Space statistics roundup, section "Global profitability levels at 54%" | 2025 | Global coworking industry (secondary aggregation) | Secondary aggregation citing underlying surveys | 28% break even (with 54% profitable, 18% at a loss) | B05 |
| B | Allwork.Space statistics roundup, section "Profitability Benchmarks for 2025" | 2025 | Global coworking industry (secondary aggregation) | Secondary aggregation citing underlying surveys | 22% break even (with 54% profitable, 18% at a loss) | B06 |

**Explanation of the differences.** The same article, citing the same headline pair (54% profitable, 18% at a loss), publishes two different break-even shares: 28% in one section and 22% in another. The 100% decomposition only closes in version A (54+28+18). The likely cause is that the two sections draw on different underlying survey sets (the article aggregates multiple reports), or one section restates a different survey edition. **Decision for the Blueprint:** use version A (28%) when a three-band decomposition is needed because it is internally consistent; treat 22% as an unexplained variant and record it side by side (both rows are kept in the table); do not average the two. The Deskmag primary source (54% profitable, 18% at a loss, per rows B03/B04) remains the audit-grade reference for the profitable/loss shares.

## Comparison 3: In-office attendance — expectation versus behavior (same survey, two sides)

| Side | Report | Published | Sample scope | Methodology | Value | Row |
|---|---|---|---|---|---|---|
| A | 2025 Americas Office Occupier Sentiment Survey (CBRE) | 2025 | Office-using companies across the Americas | Occupier sentiment survey, Q2 2025 | Employers expect 3.2 days in-office per week | B21 |
| B | 2025 Americas Office Occupier Sentiment Survey (CBRE) | 2025 | Same sample | Same survey, employee-behavior side | Employees show up on average 2.9 days per week | B21 |

**Explanation of the differences.** Both numbers come from the same survey; the difference is definitional position: A measures employer expectation (policy), B measures actual attendance (behavior). The 0.3-day gap is the survey's documented "expectation gap". **Decision for the Blueprint:** any attendance or usage expectation metric on the platform must record the expected and the actual value as a pair in the same row, never only one side; a target without its actual is not a benchmark.

## Comparison 4: Meeting room utilization — measured booking rate versus demand popularity

| Side | Report | Published | Sample scope | Methodology | Value | Row |
|---|---|---|---|---|---|---|
| A | Reduce no-shows and improve team bookings in your coworking space (Nexudus) | 2025 | Coworking spaces on the vendor platform (methodology not disclosed) | Vendor blog benchmark citing booking statistics | Average meeting room utilization 30% | B23 |
| B | 2025 Global Coworking Space Trends Survey (Deskmag) | 2025 | Coworking operators worldwide (n not disclosed on public page) | Operator self-report survey (demand ranking, not a rate) | Meeting spaces "remained especially popular worldwide" (no rate published) | S02 |
| C | Global Occupancy Planning Benchmark Report 2026 (JLL) | 2026 | 84 corporate organizations | Measured corporate occupancy-planning data | Small meeting rooms and focus rooms rising as space types; no single utilization rate published on the public page | S06 |

**Explanation of the differences.** A is the only quantified meeting-room utilization rate found in the public pages reviewed: a booking-data-derived rate (booked hours over available hours) with undisclosed sample and vendor interest. B is a demand ranking from operators — it says meeting spaces are the most demanded space type but publishes no utilization rate, so it cannot be placed on the same scale. C discusses the space-type trend (phone booths and small meeting rooms replacing larger ones) without publishing a rate on its public page. **Decision for the Blueprint:** adopt the rate definition from A (booked hours over available hours) but source the platform's own baseline from first-party booking data; treat 30% as a directional vendor benchmark, and the Deskmag demand ranking as qualitative demand evidence only.

## Comparison 5: Time-to-sustainability — duration benchmark with different measurement populations

| Side | Report | Published | Sample scope | Methodology | Value | Row |
|---|---|---|---|---|---|---|
| A | Coworking Statistics and Key Trends Shaping the 2026 Flexible Workspace Industry (Allwork.Space) | 2025 | Global coworking industry (secondary aggregation) | Secondary aggregation of published surveys | 72% of operators reach profitability within 2 years | B07 |
| B | 2025 Global Coworking Space Trends Survey (Deskmag) | 2025 | Coworking operators worldwide | Operator self-report survey | No duration-to-profitability statistic on the public summary pages (profitability levels only, by settlement size) | B03, B04 |

**Explanation of the differences.** A supplies the only duration-anchored figure in the reviewed public pages; B measures profitability levels at a point in time but does not publish the time dimension on its free pages. The two are therefore complementary rather than contradictory, but they must not be combined into a single statement: A's "within 2 years" window and population are not restated per underlying survey. **Decision for the Blueprint:** if a time-to-steady-state metric is adopted, copy A's explicit window convention (a fixed window plus a share reaching the state within it) but compute the baseline from platform data; label any external reference with its undisclosed-restatement caveat.

---

**Summary.** Five comparisons are recorded, covering four indicators with conflicting definitions (occupancy/utilization across four definitions; break-even share with an internal aggregation inconsistency; attendance expectation versus behavior; meeting room utilization rate versus demand ranking; time-to-sustainability population mismatch). Every conflicting value is kept as a separate row in `metric_benchmarks.csv`; none is merged, averaged, or normalized. All quoted values are percentages, ratios, durations, or headcounts; no monetary values appear in this note.
