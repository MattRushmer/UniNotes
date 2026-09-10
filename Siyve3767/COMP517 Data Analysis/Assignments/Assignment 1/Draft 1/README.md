---
tags:
  - comp517
  - data-analysis
  - assignment
  - draft
---

# COMP517 Assignment 1 — Draft 1

Full draft of Assignment One (Data Exploration and Analysis), dataset choice: **Global Air Quality 2023 (Messy)**. See [[COMP517 Data Analysis/Assignments/Assignment 1 Research|Assignment 1 Research]] for the assignment brief context.

## What to actually submit to Canvas/Turnitin (2 files, uploaded separately, not zipped)

1. **`air_quality_eda.py`** — the Python code file. Runs standalone; regenerates every figure/table in the report into `figures/`.
2. **`COMP517 Assignment 1 Report - Draft.docx`** — the report. **Before submitting:**
   - Fill in `[Full Name]` and `[Student ID]` on the title page.
   - Open in Word and right-click the Table of Contents → **Update Field** (it's a live TOC field, not hard-coded page numbers).
   - Proofread the written commentary — it's a full first draft based on the real output of the script, not placeholder text, but it's worth a read-through in your own voice before submitting.
   - Check the word count (Word's status bar) stays under the 5,000-word limit — currently ~3,200 words of prose, so there's headroom.

## Everything else in this folder (not for submission, just working files)

- **`Data Cleaning Log.md`** — a full technical audit trail of every transformation applied to the dataset, step by step, with exact before/after numbers and the reasoning for each decision. This is the "show your working" companion to Section 2 of the report, and also documents every bug caught and fixed during review (see below) — read this if you want to defend a specific number in the report or explain a methodology choice to the marker.
- `figures/` — every PNG the script generates, plus 3 CSV tables (`summary_statistics.csv`, `aggregation_pm25_by_country.csv`, `risk_score_by_temperature_band.csv`) used to build the report's tables. Regenerated every time you run the script.
- `run_output.txt` — the full console output from the last run (all the printed stats), kept for reference if you want to double-check a number in the report against the raw output.

## Review process this draft went through

Beyond the initial build, `air_quality_eda.py` was checked by two independent automated code-review passes (a Python specialist and a general code-quality reviewer, each run separately and each actually executing the script rather than just reading it), plus a manual web-research check of the EPA PM2.5 breakpoints used in Section 4.4. That process caught and fixed one genuinely significant bug — **global (not per-country) mean imputation was flattening the "median PM2.5 by Country" comparison in Section 4.3 into a near-constant value, hiding a real ~4-point spread between countries** — plus several smaller correctness and clarity issues (a factually-wrong code comment, a misleading console-log line, outdated EPA breakpoints, a matplotlib legend bug, and hemisphere-biased season labels that would have mislabelled the majority-Northern-Hemisphere data as "Winter" in June). Every one of these is written up in full in `Data Cleaning Log.md`, including the wrong value, why it was wrong, and what it was changed to — nothing was fixed silently.

## Key findings baked into this draft (so you can sanity-check them yourself)

- 30,450 rows → 16,553 after removing 13,897 exact duplicate rows (45.6%).
- ~5% missing values in each of the 6 pollutant columns only; imputed with each column's mean **computed separately per country** (skew was ~0 for all of them, so mean was the statistically correct choice over median; per-country rather than global was a fix made during review — see above).
- **Zero statistical outliers found** in any numeric column (IQR and z-score both agree) — the dataset's values are hard-bounded/clipped rather than long-tailed, despite the source README claiming injected outliers. This is reported as a genuine finding, not glossed over.
- **No meaningful correlation between any pair of variables** (max |r| = 0.02) — treated as evidence the columns were generated independently, with the real-world implications discussed in Section 4.
- Average PM2.5 genuinely varies by country (mean 75.47–80.24, median 74.59–78.75 across the top 10) — a real, if modest, cross-country difference, correctly recovered only after the per-country imputation fix above.
- Temperature has no effect on the derived Air Quality Risk score (using the EPA's current, post-May-2024 PM2.5 breakpoints) — also reported honestly as a null result, with two discussed significances per the brief's requirement.

If you'd rather have a stronger/more dramatic story in the multivariate section (i.e. this dataset genuinely doesn't have much correlation to report), the alternative would have been the Gen Z Mental Wellness dataset — worth keeping in mind if a marker pushes back on "why are all your correlations near zero."
