---
tags:
  - comp517
  - data-analysis
  - assignment
  - data-cleaning
  - changelog
---

# Data Cleaning Log — Global Air Quality 2023 (Messy)

> Technical record of every transformation applied to the raw dataset by [[COMP517 Data Analysis/Assignments/Assignment 1/Draft 1/air_quality_eda|air_quality_eda.py]], in the exact order it runs, with exact before/after numbers and the reasoning behind each decision. This is the "show your working" companion to Section 2 of the report — the report explains *why* in prose; this log is the precise audit trail. Source file: `Dataset - Global Air Quality 2023/global_air_quality_data_messy.csv`.

**Raw input:** 30,450 rows × 12 columns (City, Country, Date, PM2.5, PM10, NO2, SO2, CO, O3, Temperature, Humidity, Wind Speed).
**Final cleaned output:** 16,553 rows × 12 original columns + 4 derived columns (Quarter, AQ_Risk_Category, AQ_Risk_Score, Temperature_Band).

> This log describes the **final, corrected** pipeline as it stands after two automated code-review passes (see "Fixes made after the first draft" below) — it is not a record of an unreviewed first attempt. Where a fix changed a number that ended up in the report, both the wrong and corrected value are given so the change is traceable.

## Step 1 — Text normalisation (City, Country)

- **Problem:** the "messy" generator randomised case and whitespace on every text field (e.g. `"SYDNEY"`, `"Sydney"`, `" Sydney "` all appear as separate raw values).
- **Fix applied:** `.str.strip()` then `.str.title()` on both `City` and `Country` — **without** first casting to `str` with `.astype(str)`. An earlier version did cast to `str` first, which is a latent bug: `.astype(str)` turns a real missing value (`NaN`) into the literal text `"nan"`, which then silently passes any later `isnull()` check and never gets imputed. It didn't affect this particular run (`City`/`Country` have 0 raw missing values in this file), but was fixed anyway before it could bite on a re-run with a different messy-data seed — caught during the second automated code review pass.
- **Result:**
  - `City`: 120 raw unique values → **20** unique values after cleaning (i.e. the 120 raw variants were really just 20 real cities spelled/cased 6 ways on average).
  - `Country`: 19 raw unique values → 19 unique values after cleaning (no case-duplication existed at the country level — every raw value already mapped 1:1 to a real country).
- **Bug caught and fixed during cleaning:** `.str.title()` mangles acronyms — it turned `"UAE"` → `"Uae"`, `"UK"` → `"Uk"`, `"USA"` → `"Usa"`. A manual correction dictionary (`{"Uae": "UAE", "Uk": "UK", "Usa": "USA"}`) was applied immediately after title-casing to restore the correct acronym form. Caught by inspecting the raw unique value list before deciding on a cleaning method, rather than trusting `.str.title()` blindly.

## Step 2 — Date parsing

- **Problem:** `Date` was stored as text, format unconfirmed.
- **Fix applied:** confirmed the format was `M/D/YYYY` — values such as `10/27/2023` rule out `D/M/YYYY`, since there is no 27th month — then parsed with `pd.to_datetime(..., format="%m/%d/%Y", errors="coerce")`.
- **Result:** all 30,450 rows parsed successfully; **0 rows** failed to parse (no `NaT` values produced). Date range confirmed as 1 Jan 2023 – 28 Dec 2023.
- A derived `Quarter` column was added at this point for later analysis (calendar quarter, labelled by month range — e.g. "Q1: Dec-Feb" — rather than a hemisphere-specific season name; see the review-pass fix below for why). An earlier version also added a `Month` column that was never actually used anywhere in the analysis; removed as dead code during the second review pass.
- **Fallback logic for any row where Date fails to parse (this run: 0 rows, so untested in practice):** an earlier version used `df["Date"].interpolate(method="linear")`, justified by a comment claiming "records are time-ordered per city" — checked directly and found **false** (`df['City'].is_monotonic_increasing` is `False`; rows are shuffled, e.g. the first five alternate Johannesburg/Istanbul/Berlin/Sydney/Dubai). Linear interpolation on a shuffled row order would average two unrelated cities' dates into a fabricated timestamp. Fixed by dropping any row with an unparseable date instead (`df.dropna(subset=["Date"])`), since a date cannot be safely guessed without a real ordering — caught during the second automated code review pass.

## Step 3 — Missing values

- **Problem:** the six pollutant columns had missing values; no other column did.

| Column | Missing (count) | Missing (%) |
|---|---|---|
| PM2.5 | 1,552 | 5.10% |
| PM10 | 1,561 | 5.13% |
| NO2 | 1,593 | 5.23% |
| SO2 | 1,475 | 4.84% |
| CO | 1,496 | 4.91% |
| O3 | 1,600 | 5.25% |
| City, Country, Date, Temperature, Humidity, Wind Speed | 0 | 0.00% |

- **Decision process:** skewness was computed for every numeric column *before* choosing an imputation method, rather than assuming pollutant data is skewed. All six pollutant columns returned skew between −0.02 and 0.02 (essentially symmetric).
- **Fix applied:** mean imputation for all six pollutant columns (mean is the statistically correct choice for symmetric data; median would only have been preferred if skew had been meaningfully non-zero) — computed **within each `Country` group** (`df.groupby("Country")[col].transform("mean")`), not as one dataset-wide number.
- **Why "within each Country group" and not a single global mean — this was itself a bug fix, not the original design:** the first draft used one global `df[col].mean()`. That is what a straightforward reading of "impute missing values" suggests, and it is statistically defensible in isolation — but it silently broke a *different* part of the analysis. Two independent automated code reviews, run separately, both caught the same problem: because ~5–10% of every country's rows got the exact same repeated global-mean value, and PM2.5 is close to symmetric, that repeated value ended up sitting at (or next to) the middle sorted position for **every** country's own subgroup. The result: the "median PM2.5 by Country" table in report Section 4.3 showed **77.65 for 9 of the top 10 countries** — not because those countries genuinely have the same median, but purely as a side effect of the imputation method. One reviewer independently confirmed this by re-computing the medians with missing rows simply dropped instead of filled, and got genuinely different values spread across an 11-point range. Fixed by imputing within each country's own data instead of with one shared value; Section 4.3 of the report now reports the corrected result (medians genuinely range 74.59–78.75 across the top 10 countries).
- **Console-log accuracy fix:** an earlier version printed a skew-based mean/median decision for all 9 numeric columns, including the 3 weather columns that have 0 missing values and are never actually imputed — misleadingly implying 9 columns were imputed when only 6 are. Fixed to print "no missing values, skipped" for any column with nothing to impute, so the console transcript (which the report is built from) accurately reflects what the code does.
- **Result:** 0 missing values remain anywhere in the dataset after this step.
- **Known remaining side-effect (see report Sections 3.2 and 4.3):** even with per-country imputation, the imputed points still form a visible (if less severe) band in the histograms and outlier scatterplots, because the ~19 countries' own PM2.5 means happen to sit close together (75.5–80.2). This is now a *genuine* tight clustering of real per-country statistics rather than one artificial repeated constant, and is reported as such rather than hidden.

## Step 4 — Duplicate rows

| Check | Rows | % of 30,450 |
|---|---|---|
| Exact duplicates (all 12 columns identical) | 13,897 | 45.64% |
| Rows sharing the same City + Country + Date | 25,375 | 83.32% |

- **Fix applied:** `df.drop_duplicates()` — removes only the 13,897 **exact** duplicates.
- **Result:** 30,450 → **16,553 rows**.
- **Decision and why:** the gap between the two numbers above (25,375 vs 13,897) means ~11,478 rows share a city/date with another row but report *different* pollutant/weather readings. These were deliberately **kept**, not dropped, because:
  1. A single city can legitimately have multiple monitoring stations, or more than one reading per day.
  2. The dataset has no station ID or sub-day timestamp to distinguish "genuine second reading" from "injected near-duplicate noise" — dropping them would be a guess, not a justified decision.
  - This is flagged as an acknowledged limitation in the report (Section 5.2, Challenge 1), not resolved silently.

## Step 5 — Outlier detection

- **Method:** IQR rule (flag `< Q1 − 1.5×IQR` or `> Q3 + 1.5×IQR`) applied to all 9 numeric columns, computed on the de-duplicated 16,553-row dataset. Cross-checked on PM2.5 with the z-score rule (`|z| > 3`).

| Column | Lower bound | Upper bound | Outliers found |
|---|---|---|---|
| PM2.5 | −53.02 | 208.31 | 0 |
| PM10 | −67.83 | 276.97 | 0 |
| NO2 | −33.45 | 136.84 | 0 |
| SO2 | −18.61 | 69.20 | 0 |
| CO | −3.98 | 13.98 | 0 |
| O3 | −67.58 | 277.94 | 0 |
| Temperature | −35.41 | 65.07 | 0 |
| Humidity | −35.04 | 144.37 | 0 |
| Wind Speed | −9.19 | 29.66 | 0 |

- **Result: zero outliers in every column**, by both methods. This was investigated rather than accepted at face value: every column's true min/max sit at suspiciously round, fixed values (e.g. PM2.5 exactly 5.02–149.98, Humidity exactly 10.01–99.99%), indicating the generator clipped values to fixed physical bounds instead of drawing from a long-tailed distribution. IQR bounds computed on such bounded, near-uniform data extend past the data's real min/max, so nothing is ever flagged — even though the dataset's own README claims "noisy/outlier AQI values" were injected.
- **Fix applied:** none — no values were removed, capped, or transformed on outlier grounds, because none were genuinely found. This null result is reported as-is in the report rather than manufacturing outliers to satisfy the brief.
- **Separate physical-validity check:** rows with `Humidity` outside 0–100% or negative `Wind Speed` were also checked directly (independent of the IQR test). **0 rows removed** — all values already fall within physically valid ranges. This check now runs **before** the IQR bound calculation above (an earlier version ran it after, which meant the IQR bounds and the scatterplot figures could in principle have been computed on two slightly different versions of the data if this filter had ever removed a row; reordered during the second review pass so both use the same final `df`, even though the practical effect here is nil since 0 rows are removed either way).
- **Code-cleanliness fix:** the PM2.5/PM10 IQR bounds used for the outlier scatterplots (Figures 2–3) were originally recalculated a second time in a separate loop, duplicating the calculation already done above. Fixed to compute the mask once per column and reuse it for both the summary table and the scatterplots.

## Step 6 — Derived columns for multivariate analysis (Section 4.4 of the report)

Not a cleaning step, but documented here for completeness since these columns don't exist in the raw data:

- `AQ_Risk_Category`: PM2.5 mapped to the standard US EPA 6-level category (Good / Moderate / Unhealthy for Sensitive Groups / Unhealthy / Very Unhealthy / Hazardous) using EPA's **current** (post-6-May-2024) 24-hour PM2.5 breakpoints: Good ≤ 9.0, Moderate ≤ 35.4, Unhealthy for Sensitive Groups ≤ 55.4, Unhealthy ≤ 125.4, Very Unhealthy ≤ 225.4, otherwise Hazardous (all µg/m³) — see the breakpoint-correction fix below.
- `AQ_Risk_Score`: the same category, ordinally encoded 1 (Good) → 6 (Hazardous), so an average and standard deviation could be computed (mirroring a numeric "risk score" outcome).
- `Temperature_Band`: `Temperature` binned into 5 ranges (<0°C, 0–10°C, 10–20°C, 20–30°C, >30°C) for the temperature-vs-risk comparison.

## Fixes made after the first draft (review pass)

- **Pie chart legend bug (Figure 6, "Share of Records by Calendar Quarter"):** the first draft's pie chart had an empty legend box — `matplotlib` raised `UserWarning: No artists with labels found to put in legend`, because the wedge labels had been removed (to fix an earlier label-overlap problem) without re-wiring the legend to the wedge objects. Fixed by capturing the wedge handles returned by `plt.pie()` and passing them explicitly to `plt.legend(wedges, quarter_counts.index, ...)`. Verified fixed by re-running the script and confirming the warning no longer appears in `run_output.txt`, and by visually re-inspecting the regenerated figure.
- **Legend clipping on figures with an external legend:** `savefig()` was updated to pass `bbox_inches="tight"` to `plt.savefig()`, so legends placed outside the plot axes (e.g. the quarter pie chart, the mean/median PM2.5 bar chart) are no longer cut off at the image edge.
- **Hemisphere-biased season labels (caught on self-review, before any agent was asked to look):** the original `Season` column labelled quarters "Summer (Dec-Feb)", "Winter (Jun-Aug)", etc. This is the correct convention for Southern-Hemisphere countries (South Africa, Australia) but is *backwards* for the Northern-Hemisphere countries that actually dominate the dataset — including the USA, which alone supplies ~9.5% of all records. Reporting "Winter" for USA readings taken in June–August would have been factually wrong. Fixed by renaming the column to `Quarter` and relabelling every bucket by month range only (e.g. "Q3: Jun-Aug"), with no hemisphere-specific season name attached anywhere. The underlying grouping logic and every count/percentage is unchanged — only the label changed — so no figures needed re-analysis, only relabelling and regenerating.
- **Outdated EPA PM2.5 breakpoints (caught via web research, cross-checked against EPA's own AQS breakpoint table):** the first draft's `pm25_risk()` function used the pre-2024 EPA breakpoints (Good ≤ 12, Moderate ≤ 35.4, Unhealthy-Sensitive ≤ 55.4, Unhealthy ≤ 150.4, Very Unhealthy ≤ 250.4) — still the version most commonly quoted online, but superseded by the EPA's 6 May 2024 AQI revision, which lowered several thresholds (e.g. "Good" dropped from ≤12 to ≤9.0 µg/m³). Verified directly against EPA's own AQS breakpoint table (`aqs.epa.gov/aqsweb/documents/codetables/aqi_breakpoints.csv`) rather than trusting a secondary summary. Fixed by updating `pm25_risk()` to the current breakpoints (Good ≤ 9.0, Moderate ≤ 35.4, Unhealthy-Sensitive ≤ 55.4, Unhealthy ≤ 125.4, Very Unhealthy ≤ 225.4, otherwise Hazardous). **Side-effect worth knowing:** under the old (wrong) breakpoints, this dataset's PM2.5 values (max 149.98) could never reach the "Very Unhealthy" or "Hazardous" categories at all — every reading silently capped out at "Unhealthy" (category 4) or below, so Table 6 / Figure 11 in the first draft understated the real spread of the risk score. Under the corrected breakpoints, "Very Unhealthy" (category 5) is genuinely reachable and does appear in the data (see the updated boxplot whiskers extending to 5.0). The conclusion itself is unchanged — risk score still shows no relationship with temperature band — but the numbers in Table 6 shifted slightly (means now 3.58–3.68, previously 3.41–3.49) and are now correct.

### Independent code-review pass (two review agents, run separately on the same file)

After the fixes above, `air_quality_eda.py` was reviewed independently by two separate automated reviewers (one Python-specialist, one general code-quality) — each ran the script fresh and re-derived the printed numbers rather than only reading the source. **Both independently flagged the same HIGH-severity issue as their top finding**, which is the most significant fix in this whole log:

- **HIGH — global (dataset-wide) mean imputation was silently flattening the "median PM2.5 by Country" result (Section 4.3):** already described in full under Step 3 above. Both reviewers, working separately, re-ran the aggregation with missing values simply dropped instead of imputed and confirmed the countries' *true* medians are genuinely spread out (one reviewer measured a spread as wide as 71.04–81.94) — proving the flat 77.65-for-9-of-10-countries result in the first draft was an artefact, not a finding. **Fixed** by switching to per-country imputation (see Step 3); Section 4.3 of the report was then rewritten with the corrected, differentiated results.
- **MEDIUM — `.astype(str)` before the City/Country null-check could mask future missing values.** Fixed (see Step 1).
- **MEDIUM — the Date-interpolation fallback's comment made a factually false claim about the data being city-ordered, and would have produced a nonsensical fabricated date if it had ever fired.** Fixed by dropping unparseable-date rows instead (see Step 2).
- **MEDIUM — the console log implied all 9 numeric columns were imputed when only the 6 with missing values actually were.** Fixed (see Step 3).
- **LOW — duplicate IQR bound calculation for PM2.5/PM10 (once in the outlier summary, again for the scatterplots).** Fixed by computing each column's outlier mask once and reusing it (see Step 5).
- **LOW — unused `import numpy as np`** (numpy was never actually called anywhere in the script). Removed.
- **LOW — a `median` column that exactly duplicated `describe()`'s existing `50%` column** in the exported summary-statistics CSV. Simplified to a rename instead of a duplicate.
- Both reviewers, after the fixes above, confirmed the script runs cleanly end-to-end with **zero errors and zero warnings**, and everything else they checked (Quarter derivation, IQR/z-score logic, duplicate-handling counts, risk-category ordering, the correlation loop) was verified correct as originally written.

## Summary of net effect

| Stage | Rows | Columns |
|---|---|---|
| Raw file | 30,450 | 12 |
| After text/date cleaning (no rows removed) | 30,450 | 12 + 1 derived (Quarter) |
| After missing-value imputation (no rows removed) | 30,450 | 13 |
| After exact-duplicate removal | **16,553** | 13 |
| After outlier check (0 removed) | 16,553 | 13 |
| Final, with risk/temperature-band columns added for Section 4.4 | 16,553 | 16 |

**45.7% of the raw rows were removed overall — entirely due to exact duplication, not missing data or outliers.** No row was ever dropped for having a missing value or an outlier; only for being a byte-for-byte repeat of another row.
