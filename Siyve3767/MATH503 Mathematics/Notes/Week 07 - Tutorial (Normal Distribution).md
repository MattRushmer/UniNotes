---
tags:
  - math503
  - mathematics
  - tutorial
  - normal-distribution
  - practice
  - exam-topic
---

# Week 07 - Tutorial (Normal Distribution)

> Auto-extracted from [[MATH503 Mathematics/Tutorials/Week 07 - Tutorial (Normal Distribution).pdf|Week 07 - Tutorial (Normal Distribution).pdf]]. Practice for [[MATH503 Mathematics/Notes/Week 07 - Normal Distribution and Z-Scores|Week 07 - Normal Distribution and Z-Scores]] — this tutorial **confirms the Week 07 note's topic and z-score approach against real course material**, since no Week 7 lecture deck exists in the vault yet.

## Tools introduced
- Graphics calculator emulator (Casio fx-9860G SD) or online Normal/Inverse Normal calculators
- **RStudio**: `pnorm(x, mean, sd)` = area to the left of x · `qnorm(area, mean, sd)` = boundary value for a given left-tail area · `rnorm(n, mean, sd)` = n random samples from the distribution
- These are exactly the R functions used the following week in [[MATH503 Mathematics/Notes/Week 08 - Hypothesis Testing|Week 08 - Hypothesis Testing]] (`pnorm`, `qnorm`) to compute p-values and rejection regions

## Question 1 — heights (mean 167cm, sd 5cm)
Find P(161<X<173), P(155<X<185), P(X<167), P(X>162), P(149<X<173), P(X>173).
- (a) 161-173 = μ±1.2σ (161 is 1.2σ below, 173 is 1.2σ above) — near but not exactly the 68% (μ±1σ) band from the empirical rule
- (b) 155-185 = μ±6σ/5 = μ±1.2σ each way... actually 155 is 2.4σ below and 185 is 3.6σ above — asymmetric, needs `pnorm` rather than the empirical rule alone
- (c) P(X<167) = 0.5 exactly, since 167 is the mean
- Use `pnorm()` for exact values; the empirical rule (68-95-99.7, from [[MATH503 Mathematics/Notes/Week 07 - Normal Distribution and Z-Scores|Week 07]]) only gives quick estimates at exactly ±1σ/±2σ/±3σ

## Question 2 — roller coaster height requirement
Minimum height 1.52m; children's heights ~ N(1.22, 0.61²). Find (a) % of children who qualify, (b) how many out of 850 children.
- z = (1.52 − 1.22) / 0.61 = 0.4918 → use `1 - pnorm(1.52, 1.22, 0.61)` for the qualifying proportion, then × 850 for the count

## Question 3 — Mensa IQ cutoff (top 2%)
IQ ~ N(100, 16²). Find the lowest IQ in the top 2%.
- This is an **inverse** problem — use `qnorm(0.98, 100, 16)` to find the cutoff score, the mirror operation of Question 1/2's `pnorm()` lookups

## Question 4 — light bulb lifespans (mean 10,000 hrs, sd 700 hrs)
(a) below what value do the weakest 10% last? (b) above what value do the strongest 5% last? (c) between what two values does the central 80% lie?
- (a) `qnorm(0.10, 10000, 700)` · (b) `qnorm(0.95, 10000, 700)` · (c) the central 80% is bounded by the 10th and 90th percentiles: `qnorm(0.10, ...)` and `qnorm(0.90, ...)` — same two-tailed logic as the confidence-interval framing in [[COMP507 IT Project Management/Notes/08 - Quality Management|COMP507 08 Quality Management]]'s certainty factors (1.960/1.645/1.281 = z-scores for 95%/90%/80%)

## Related
- [[MATH503 Mathematics/Notes/Week 07 - Normal Distribution and Z-Scores|Week 07 - Normal Distribution and Z-Scores]] — the theory and empirical rule this tutorial practises
- [[MATH503 Mathematics/Notes/Week 08 - Hypothesis Testing|Week 08 - Hypothesis Testing]] — the same `pnorm`/`qnorm` tools applied to testing claims
- [[MATH503 Mathematics/Index|Course index]]
