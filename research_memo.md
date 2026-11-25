# Research Memo: Operational Metric Benchmarks in Flexible Work Industry Reports

**Ticket:** 【S1-RES-014】Member Space Platform · Compilation of Operational Metric Benchmarks in the Flexible Work Industry Report
**Prepared for:** the Business Blueprint module of the Member Space Platform (fictional demo), to be used when defining North Star and baseline metrics.
**Access date of all sources:** 2026-11-19. Every source listed in this memo was re-fetched live (HTTP GET) on that date and returned HTTP 200; see `sources.csv` for the registry and `metric_benchmarks.csv` for the benchmark table.
**Scope note on values:** per the ticket, only percentages, ratios, durations, and headcounts are recorded. No monetary amounts appear anywhere in this memo, the benchmark table, or the discrepancy note. Where a public report page discloses only monetary figures (for example market-size values), the metric is recorded as not adoptable rather than converted or estimated.

## How to read this memo

The memo follows the five-section structure required by the ticket, organized by subject (each report): subject, methodology, adoptable points (which definitions can be directly adopted), non-applicable points (samples are predominantly overseas; differences between co-working and business membership spaces), and public source links. Five reports form the core set; one vendor benchmark and one reviewed-but-not-adopted report are documented separately at the end. All benchmark values extracted from these reports are registered row by row in `metric_benchmarks.csv` (26 rows, covering 19 distinct indicators); where reports define the same indicator differently, the rows are listed side by side and never merged or averaged, and the differences are explained in `definition_discrepancy_note.md`.

---

## Subject 1: Deskmag — 2025 Global Coworking Space Trends Survey

### Subject

Deskmag's 2025 Global Coworking Space Trends Survey is the latest edition of the industry survey series that has run since 2010 (as the Global Coworking Survey, replaced by the Coworking Trends Survey in 2021). The 2025 edition was published as a free multi-part online analysis titled "More Profitable Coworking Spaces Now Than Pre-Covid", written by Carsten Foertsch and dated May 19, 2025. It reports how coworking space operators worldwide rated their business situation, profitability, occupancy, space demand, challenges, and outlook at the start of 2025. It is the most direct industry-side source for occupancy and operator-level operational benchmarks published within the last three years.

### Methodology

The 2025 report is an operator self-report survey: coworking space businesses worldwide were surveyed about their current business situation, profitability over the past twelve months, occupancy, demand by space type, challenges, and expectations. The survey covers operators (businesses) rather than individual members; the archive page confirms that since 2021 the survey "surveyed providers only". The public summary pages do not disclose the number of participants, so the sample size is recorded in the benchmark table as "not disclosed on the public summary page" rather than guessed. Results are reported as percentages of responding operators, in some places split by settlement size (cities with over one million residents versus towns under 20,000 people) and by continent. Deskmag publishes results under a CC license requiring attribution and a link back, which the source links below satisfy.

### Adoptable points

- **Occupancy rate definition (B01, B02):** occupancy is reported as the share of occupied capacity across the operator's space, self-reported by operators. The plain percentage definition ("average of 68 percent at the start of 2025") can be directly adopted as the Member Space Platform's desk-occupancy North Star definition: occupied desk-days divided by available desk-days over a period, reported as a percentage. The split between "major cities" ("well above 70 percent") and smaller locations is a useful baseline segmentation: adopt a two-tier baseline (metro versus non-metro locations) rather than one blended target.
- **Profitability share as a health benchmark (B03, B04, B09, B10):** "54 percent of coworking space businesses were profitable, while 18 percent reported losses", and "about one in six coworking space operators surveyed reported a decline in profitability". The survey's framing — a distribution of operators by condition rather than a single average — can be adopted directly: the platform's operator-facing dashboard should show the distribution of member companies by account health band instead of only averages.
- **Expectation indicator (B09):** "Almost 80 percent expected a growing number of members" is a clean precedent for a forward-looking sentiment metric. The platform can adopt a quarterly member-company outlook pulse with the same wording logic (percentage expecting growth).
- **Challenge ranking (S02, part 2):** member acquisition is named "by far the biggest challenge", cited slightly less than in mid-2023, with "every third space operator" citing property costs. Adoptable as the rationale for making acquisition-channel composition a tracked metric in the CRM module.

### Non-applicable points

- **Sample is predominantly overseas:** Deskmag's survey covers operators worldwide with a strong Europe/North America weighting (the 2025 analysis is explicitly titled as covering Europe and North America). Settlement-size effects (small towns performing worse) do not transfer to a business membership space serving about 100 member companies concentrated in one metro market.
- **Coworking versus business membership space:** Deskmag's population includes hot-desk-led freelance coworking. A business membership space sells company memberships with longer commitments; its occupancy churns on contract cycles, not on daily hot-desk demand. The 68% global desk-occupancy figure is therefore a sanity band, not a target.
- **Self-report bias:** all values are operator self-reports without audit; the platform's own metrics will be measured from system data, so definitional drift must be watched when benchmarking.

### Public source links

- S01 — Deskmag, "More Profitable Coworking Spaces Now Than Pre-Covid" (2025 Global Coworking Space Trends Survey, part 1), published 2025-05-19: https://www.deskmag.com/en/coworking-spaces/2025-global-coworking-space-trends-europe-north-america-market-business-survey-analysis-report (accessed 2026-11-19, HTTP 200)
- S02 — Deskmag, part 2 of the same analysis (occupancy, challenges and economic outlook): https://www.deskmag.com/en/coworking-news/2025-global-coworking-space-trends-europe-north-america-market-business-survey-analysis-report?limitstart=1 (accessed 2026-11-19, HTTP 200)
- S09 — Deskmag, archive index of all Global Coworking Survey and Coworking Trends Survey publications: https://www.deskmag.com/en/coworking-statistics-all-results-of-the-global-coworking-survey-research-studies-948 (accessed 2026-11-19, HTTP 200)

---

## Subject 2: Allwork.Space — "Coworking Statistics and Key Trends Shaping the 2026 Flexible Workspace Industry"

### Subject

Allwork.Space is a flexible-workspace industry publication. Its statistics roundup "Coworking Statistics and Key Trends Shaping the 2026 Flexible Workspace Industry" by Sheya Michaelides, published December 4, 2025, aggregates the industry's most recent survey results and market data into a single reference article. It is one of the report examples explicitly named in the ticket scope (Allwork.Space industry surveys). Its most useful contribution to this ticket is a set of operator profitability, retention, and prevalence benchmarks for 2025, plus region-level inventory headcounts.

### Methodology

This is a secondary aggregation: the article compiles figures from underlying industry reports and surveys (including Deskmag's 2025 survey, as the article itself references Deskmag) and re-publishes them with short interpretive notes. The article does not field its own survey and does not restate each underlying sample; the sample scope for each figure is therefore recorded as "global coworking industry (secondary aggregation of published surveys)". Two sections of the same article state materially different break-even shares (28% in one section, 22% in another) while both state 54% profitable and 18% at a loss — a documented internal inconsistency that this ticket records side by side (rows B05 and B06) and explains in the discrepancy note instead of averaging.

### Adoptable points

- **Retention proxy (B08):** "55% of members stay long-term in the same space". This is adoptable as a first baseline for the member-retention North Star of the membership platform: share of members retained beyond a defined long-term threshold (the article does not fix the threshold; the Business Blueprint must define one, for example retained past 12 months, and record it explicitly).
- **Time-to-sustainability (B07):** "About 72% of operators reach profitability within 2 years" is a duration-anchored benchmark. Adoptable as the baseline for a "time to steady state" metric for new member companies on the platform (for example, share reaching sustained weekly usage within two years), keeping the 2-year window and the percentage framing.
- **Desk-sharing prevalence (B11):** "Desk-sharing, present in 61% of flexible offices". Adoptable when sizing desk inventory and defining desk-utilization measurement: if roughly three in five flexible offices desk-share, the platform's desk-utilization metric should assume shared assignment rather than dedicated seats as the default.
- **Scale headcounts (B12, B25):** "total users are estimated at 5.5–6 million" globally in 2025, and "Flex represents just 2% of office inventory" in the US. Both are headcount/percentage framing that can anchor TAM-style context numbers on the executive dashboard without any monetary display.
- **Demand-side occupancy by industry (B26):** the Banking, Financial Services, and Insurance (BFSI) sector "has the highest occupancy (32.40%)" among industries. This is a demand-side definition of occupancy (share of industry demand within coworking usage, not share of desks occupied) — adoptable only with the definition made explicit; see the discrepancy note, which contrasts it with the supply-side occupancy definitions of Deskmag, JLL, and CBRE.

### Non-applicable points

- **Sample is predominantly overseas:** the article aggregates predominantly North American and European data; the US-centric rows (flex share of inventory) do not transfer directly to other markets.
- **Aggregation without restated samples:** because the article does not restate each underlying sample, its figures cannot be used where an auditable sample is required; those rows cite the underlying survey directly (see Subject 1).
- **Coworking versus business membership space:** the 55% long-term retention figure blends freelancers and company tenants. Company members of a business membership space sign contracts with the operator; churn timing differs. The figure is a baseline band, not a substitute for contract-cycle cohort analysis.
- **Internal inconsistency:** the same article publishes two different break-even shares; this must not be merged (see `definition_discrepancy_note.md`, comparison 2).

### Public source links

- S03 — Allwork.Space, "Coworking Statistics and Key Trends Shaping the 2026 Flexible Workspace Industry", published 2025-12-04: https://allwork.space/2025/12/coworking-statistics-and-key-trends-shaping-the-2026-flexible-workspace-industry (accessed 2026-11-19, HTTP 200)

---

## Subject 3: CoworkingCafe — Coworking Industry Report Q4 2024

### Subject

CoworkingCafe (a listing platform) publishes quarterly US national coworking market reports. The Q4 2024 edition, "Coworking Industry Report Q4 2024: U.S. National Coworking Sector Expands in Q4 as Majority of MSAs Add Spaces" by Andreea Neculae, published January 27, 2025, tracks the number of coworking spaces nationwide and across the 25 largest US markets, total square footage, and leading operators. It matches the ticket's example list ("Coworking Resources annual reports" style market trackers; the equivalent US listing-data report) and supplies inventory headcounts and growth rates within the last three years.

### Methodology

The report's own methodology section states: "To compile this report, we used proprietary data from CoworkingCafe to determine the number of coworking spaces per market, as well as the total square footage and leading operators. The study relied solely on the listing data available on CoworkingCafe as of January 2025. The top 25 markets analyzed were established by our sister company Yardi Matrix and were ranked based on allocated square footage." The sample is therefore a listing inventory (a census of listed spaces), not a survey; the national inventory count (7,695 spaces at the end of 2024) doubles as the sample size. Quarter-over-quarter comparisons are computed against the previous edition (Q3 2024, 7,538 spaces).

### Adoptable points

- **Inventory headcount and growth as baseline metrics (B13, B14):** "the national coworking inventory reached 7,695 spaces", "a 2% increase from Q3, which recorded 7,538 spaces". The inventory-plus-QoQ-growth pattern is directly adoptable for the platform's supply-side metrics: count of member companies and of active locations, reported with quarter-over-quarter growth in percentage terms.
- **Market-level segmentation:** the report publishes market-level counts (for example Salt Lake City +8% quarter-over-quarter, the highest among the 25 largest markets; Minneapolis the only top-25 decline). Adoptable as the template for city-level dashboards: absolute headcount plus quarter-over-quarter percentage, per market.
- **Listing-census methodology:** the definition "count of listed spaces as of a cutoff date" is adoptable verbatim for the platform's directory metrics (count of active resource-partner listings as of month end), which needs no sampling at all.

### Non-applicable points

- **Sample is overseas:** the report covers the United States only; market rankings and square-footage figures do not transfer to other regions.
- **Area-based figures excluded:** the report expresses several results in square feet (total and average space size). Square footage is neither a percentage, ratio, duration, nor headcount, and the ticket forbids recording values beyond the four allowed types, so those figures are not carried into the benchmark table.
- **Listing census bias:** a listing inventory counts listed spaces, not operating spaces; a space absent from the platform is invisible. The platform's own directory metrics must state the same "as-of" cutoff language to stay comparable.
- **Coworking versus business membership space:** coworking inventory counts any flexible-workspace listing; a business membership space's "supply" is member companies and partner resources, so inventory growth here is only a framing reference.

### Public source links

- S04 — CoworkingCafe, "Coworking Industry Report Q4 2024", published 2025-01-27: https://www.coworkingcafe.com/blog/national-coworking-report-q4-2024 (accessed 2026-11-19, HTTP 200)

---

## Subject 4: CBRE — 2025 Americas Office Occupier Sentiment Survey

### Subject

CBRE's "Adaptive Spaces 2025 Americas Office Occupier Sentiment Survey", published August 11, 2025 (survey fielded Q2 2025), examines portfolio strategies and office attendance policies for office-using companies across the US, Canada, and Latin America. It matches the ticket's example list (CBRE flexible office reports). Its contribution to this ticket is a corporate-side view of utilization and attendance — the demand side that fills flexible spaces — with explicit peak-versus-average utilization framing.

### Methodology

The report is an occupier sentiment survey: CBRE Research surveyed corporate real estate executives at office-using companies across the US, Canada, and Latin America in Q2 2025, with results reported as percentages of responding organizations, split by company size and space type. The public report page does not state the number of respondents, so the benchmark table records "sample size not stated on the public report page". Figures are percentages of organizations (for example, "Seventy-three percent of organizations report office utilization is effectively at capacity on peak attendance days"), plus mean attendance durations ("employers expect 3.2 days in-office per week"). Results are labeled "Source: CBRE Research, 2025 Americas Occupier Sentiment Survey, Q2 2025" throughout. Key figures are corroborated by trade-press coverage (Facilities Dive, August 11, 2025), which is registered as a supplementary source.

### Adoptable points

- **Peak-versus-average utilization split (B18, B19):** the survey's core finding — 73% of organizations report utilization effectively at capacity on peak attendance days while only 34% report average attendance at capacity (up from 28% in 2024) — is directly adoptable as a two-metric definition pair for the platform's space-utilization dashboard: peak-day utilization and average utilization must be reported separately, never blended. This is the single most adoptable methodological convention in the reviewed reports.
- **Capacity-band definition (B19, B20):** "effectively at capacity" is defined in the report as the 61–100% occupied band, and "66% of organizations report office space that is less than 60% utilized on an average basis". The banded reporting (below 60%, 61–100%) can be adopted for the platform's utilization bands.
- **Expectation versus behavior duration pair (B21):** "employers expect 3.2 days in-office per week in 2025" while "employees show up on average 2.9 days per week". The expected-versus-actual pair is adoptable as the definition for any attendance or usage expectation metric: always record both sides.
- **Ratio planning convention (B22):** people-to-seat ratios ("more than 1.5:1" expected by 73% of respondents by 2027) are adoptable for seat-planning metrics in the member-portal and space-management modules, as a ratio (people per seat), not a percentage.

### Non-applicable points

- **Sample is overseas and corporate:** the survey covers the Americas and measures corporate employers, not flexible-space operators. Corporate attendance utilization measures employer-mandated presence, not member-company voluntary usage.
- **Corporate portfolios differ structurally:** corporate offices allocate space per employee; membership spaces allocate per company and per event. The 1.5:1 people-to-seat planning ratio must be re-derived from platform data before being used as a baseline.
- **Peak/average semantics:** CBRE's "capacity" bands refer to office attendance against workplace capacity, not revenue-bearing desk occupancy. The band definitions transfer; the absolute percentages do not.

### Public source links

- S05 — CBRE, "2025 Americas Office Occupier Sentiment Survey (Adaptive Spaces)", published 2025-08-11: https://www.cbre.com/insights/reports/2025-americas-office-occupier-sentiment-survey (accessed 2026-11-19, HTTP 200)
- S10 — Facilities Dive, "Office occupiers seek ways to improve vibrancy of space: CBRE" (corroborating coverage), published 2025-08-11: https://www.facilitiesdive.com/news/office-occupiers-seek-ways-to-improve-vibrancy-of-space-cbre/757315 (accessed 2026-11-19, HTTP 200)

---

## Subject 5: JLL — Global Occupancy Planning Benchmark Report 2026

### Subject

JLL's "Global Occupancy Planning Benchmark Report 2026" by Wei Xie and Maddie Holmes, published May 19, 2026, benchmarks corporate office utilization across regions using occupancy-planning data. It matches the ticket's example list (JLL flexible office reports) and provides the most methodologically explicit utilization benchmark reviewed here, including the actual-versus-target gap and a specialized space-type breakdown.

### Methodology

The report states its sample explicitly: "drawing from 84 organizations representing 716 million square feet across North America, Latin America, Europe, Middle East, Africa, and Asia Pacific". Utilization is measured from corporate occupancy-planning data (the report discusses badge-count limitations and advocates space-level utilization data), and results are reported as percentages with regional splits and year-over-year series ("56%, up from 54% in 2025 and 49% in 2024, inching closer to the pre-pandemic level of 61%"). Unlike the sentiment surveys, this is a benchmark of measured portfolio data from participating organizations rather than attitudinal self-reports.

### Adoptable points

- **Utilization definition with a data-quality floor (B15):** the measured-utilization definition — share of usable hours in which space is actually used, derived from space-level data — is adoptable as the platform's space-utilization metric definition, together with JLL's insistence on space-level (not building-level) badge data. The multi-year series (49% → 54% → 56%) shows how to present baselines as trend lines, not single points.
- **Actual-versus-target gap (B17):** "the actual-to-target gap narrowed from 25 to 18 percentage points". Adoptable as a governance metric: every utilization target on the executive dashboard must be paired with the current actual, and the gap reported in percentage points.
- **Specialized space-type baselines (B16):** technical spaces sit "at just 45% utilization against a 72% target" while representing "23% of portfolios". The convention of baselining each space type separately (meeting rooms, event areas, phone booths) rather than one blended figure is directly adoptable for the platform's resource-matching module.
- **Attendance-structure percentages:** "62% now require fixed in-office days, up from 49% in 2025, and 70% of employees attend three to five days per week". Adoptable framing for corporate-member engagement reporting on the membership platform.

### Non-applicable points

- **Corporate, not coworking:** the 84 organizations are corporate occupiers, not flexible-space operators; their utilization includes employer-mandated attendance, so levels are not interchangeable with member-company usage rates.
- **Sample skews large global enterprises:** 84 organizations with 716 million square feet under management is a large-portfolio population; a 100-member-company membership space cannot adopt the levels, only the definitions.
- **Region mix:** the benchmark spans six regions; regional series (for example EMEA declining from 58% to 55%) must not be averaged into a single global expectation.

### Public source links

- S06 — JLL, "Global Occupancy Planning Benchmark Report 2026", published 2026-05-19: https://www.jll.com/en-us/insights/occupancy-benchmark-report (accessed 2026-11-19, HTTP 200)

---

## Supplementary subject: Nexudus vendor benchmark (not counted as a cited report)

### Subject

Nexudus (coworking management software vendor) published "Reduce no-shows and improve team bookings in your coworking space" by Carlos Almansa on March 21, 2025. It provides rare public benchmarks for meeting room utilization — one of the metrics named in the ticket scope that the five core reports do not quantify.

### Methodology

This is a vendor blog benchmark: figures are stated as industry-level statistics ("45% of coworking spaces generate revenue from meeting room bookings", "The average meeting room utilization rate is only 30%", "No-shows account for up to 20% of lost bookings") without a disclosed sample or methodology on the page. It is registered as a supplementary source and excluded from the count of cited reports; its rows carry the note "methodology not disclosed on page".

### Adoptable points

- Meeting room utilization (B23): the 30% average is a usable sanity band for the platform's meeting room utilization baseline, provided the definition (booked hours over available hours) is fixed locally and the figure is labeled as vendor benchmark with undisclosed methodology.
- No-show share (B24): "up to 20% of lost bookings" motivates a no-show-rate metric (no-show bookings over total bookings) in the resource-booking module.

### Non-applicable points

- Vendor interest bias: the source sells booking software; figures should be treated as directional, never as audited benchmarks.
- Methodology undisclosed: sample scope and size are unknown; the rows cannot satisfy audit-grade evidence requirements.

### Public source links

- S07 — Nexudus, "Reduce no-shows and improve team bookings in your coworking space", published 2025-03-21: https://nexudus.com/blog/new-in-nexudus-reduce-no-shows-and-improve-team-bookings-in-your-coworking-space (accessed 2026-11-19, HTTP 200)

---

## Reviewed but not adopted: iiMedia Research 2024-2025 China Collaborative Office report

The ticket's example list also names co-working industry reports publicly released by domestic research institutions. The closest publicly accessible recent candidate found, iiMedia Research's "2024-2025 China Collaborative Office Industry and Benchmark Case Report" (free summary page, published August 15, 2024, HTTP 200 on 2026-11-19), was reviewed and not adopted for two reasons, recorded here so the Blueprint team can revisit it. First, its subject is collaborative office software (the Chinese-language summary labels the sector as collaborative office), not flexible workspace operations, so its metrics measure software adoption rather than space operations. Second, the free page discloses its headline findings only as market-size values in monetary units, which this ticket forbids recording; the underlying detailed report is gated. No monetary value was extracted or recorded. The page is registered as S08 in `sources.csv` with role "reviewed but not adopted".

## Coverage of the ticket's named metric list

The ticket lists example metrics "including occupancy rate or desk utilization rate, member churn rate or retention rate, average member tenure, customer acquisition channel composition, community event participation rate, meeting room utilization rate, member satisfaction or NPS, number of members served per community manager, etc." Across the five core reports and the supplementary benchmark, the reviewed public reports quantify: occupancy rate and desk utilization (B01, B02, B15, B16), retention (B08), meeting room utilization (B23), no-show and demand patterns for meeting and event spaces (B24 and Deskmag's demand-by-space-type findings), operator growth expectations (B09), inventory and growth (B13, B14), and several corporate utilization conventions (B17–B22). For four listed metrics — average member tenure, customer acquisition channel composition, community event participation rate, and members served per community manager — the public pages of the recent reports reviewed here state no quantified benchmark (Deskmag's staffing and tenure breakdowns sit in its paid detailed report; the free summary pages name member acquisition as the top challenge without publishing channel-composition data). This is recorded explicitly rather than filled with figures of unverifiable origin: the benchmark table carries 26 rows over 19 distinct indicators, all traceable to the registered sources, and the Business Blueprint should source the four missing metrics from platform first-party data once the product ships.
