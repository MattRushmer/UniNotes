---
tags:
  - math503
  - mathematics
  - research
  - statistics
  - distributions
  - expected-value
  - exam-topic
---

# Week 07 - The Normal Distribution and Z-Scores

> ⚠️ **Not auto-extracted from a lecture** — no Week 7 slide deck exists in the vault yet. This note was researched externally to close the gap flagged in [[MATH503 Mathematics/Research#2-the-normal-distribution-and-z-scores|MATH503 Research #2]]: Week 06 explicitly promises "the Normal distribution — the subject of the Week 7 lecture," and both [[COMP507 IT Project Management/Notes/08 - Quality Management|COMP507 08 Quality]] (certainty factors) and [[COMP517 Data Analysis/Notes/Week 03 - Exploratory Data Analysis|COMP517 W03 EDA]] (normal vs skewed distributions) already assume this content. **Replace/merge this note once the real Week 7 deck is available** — check it against the actual lecture for terminology and notation your lecturer uses.
>
> Sources: Wikipedia — Normal distribution (https://en.wikipedia.org/wiki/Normal_distribution) · Khan Academy — Z-scores (https://www.khanacademy.org/math/statistics-probability/modeling-distributions-of-data/z-scores-intro) · Khan Academy — Normal distributions and the empirical rule · NIST/SEMATECH e-Handbook of Statistical Methods.

## Why this follows Week 6
- [[MATH503 Mathematics/Notes/Week 06 - Binomial Distribution|Week 06]] covers the **Binomial distribution** — discrete, counts successes in n Bernoulli trials, mean = Np, variance = Npq
- As **n gets large** (rule of thumb: Np ≥ 5 and N(1−p) ≥ 5), the binomial's bar-chart shape smooths into a bell curve — this is a special case of the **Central Limit Theorem**: sums/means of many independent random quantities tend toward a Normal distribution, whatever the original distribution looked like
- This is *why* the Normal distribution shows up everywhere in statistics: exam marks, heights, measurement error, sampling distributions of the mean — anything that's the sum of many small independent effects

## What the Normal distribution is
- A **continuous** probability distribution (unlike the discrete Binomial) — written **N(μ, σ²)**, read "Normal with mean μ and variance σ²" (σ = standard deviation)
- The classic symmetric **bell curve**: highest at the centre, tails off symmetrically on both sides, never quite touches zero
- Fully described by just two numbers: **μ (mu)** — the centre — and **σ (sigma)** — the spread. Change μ and the curve shifts left/right; change σ and it gets narrower/wider without changing shape
- Properties: **mean = median = mode** (all at the centre, by symmetry); total area under the curve = 1 (it's a probability density, so *area* under a range of the curve = probability of landing in that range, not the height itself)
- **Standard Normal distribution** = the special case N(0, 1) — mean 0, standard deviation 1. Every Normal distribution can be converted to this one via standardization (below)

## The empirical rule (68-95-99.7 rule)
For any Normal distribution, the proportion of data within k standard deviations of the mean is fixed:
| Range | Proportion of data |
|---|---|
| μ ± 1σ | ≈ **68%** |
| μ ± 2σ | ≈ **95%** |
| μ ± 3σ | ≈ **99.7%** |

- This is exactly the "one sigma ≈ 68.27%, two sigma ≈ 95.45%" figure already used in [[COMP507 IT Project Management/Notes/08 - Quality Management|COMP507 08 Quality]] for Six Sigma quality control — same maths, project-management framing
- Anything beyond ±3σ is rare (<0.3% of data) — this is the statistical backbone of **outlier detection** and of manufacturing quality control (Six Sigma aims for defects almost 4.5σ out)

## Standardization: the z-score
- A **z-score** converts any Normal value into "how many standard deviations from the mean is it":

  **z = (x − μ) / σ**

- z = 0 → exactly at the mean · z = +1 → one SD above the mean · z = −2 → two SDs below the mean
- Standardizing lets you compare values from *different* Normal distributions on the same scale (e.g. "was a 72 in an exam averaging 65/σ=8 better than an 80 in one averaging 75/σ=10?" → z-scores: (72−65)/8 = 0.875 vs (80−75)/10 = 0.5 → the 72 was relatively better)
- For a **sample** rather than a known population, x̄ and s replace μ and σ: z = (x − x̄) / s

## Reading z-scores as probabilities
- The **standard normal table** (z-table) gives the area under the curve to the left of a given z — i.e. P(Z ≤ z) — the cumulative probability
- Worked example: z = 1.96 → table gives ≈ 0.975, meaning 97.5% of values fall below 1.96 SDs above the mean → this is where the **95% "certainty factor" of 1.960** in [[COMP507 IT Project Management/Notes/08 - Quality Management|COMP507 08 Quality]]'s sample-size formula comes from: it's the two-tailed 95% cutoff (2.5% in each tail)
- Same logic for the other COMP507 certainty factors: 90% → z ≈ 1.645 · 80% → z ≈ 1.281 — these are just z-scores for common confidence levels, read straight off the standard normal table

## Worked example
A machine fills bottles with a mean volume of 500 mL, σ = 5 mL (Normally distributed).
1. What proportion of bottles are filled between 495 mL and 505 mL? → that's μ ± 1σ → **≈ 68%** (empirical rule)
2. What's the z-score for a bottle filled at 512 mL? → z = (512 − 500) / 5 = **2.4** → unusually full (more than 2 SDs above the mean)
3. What proportion of bottles are under 490 mL? → z = (490 − 500)/5 = −2 → from the empirical rule, ~95% lie within ±2σ, so ~5% lie outside, split across both tails → **≈ 2.5%** below 490 mL

## Connections across the vault
- **[[COMP507 IT Project Management/Notes/08 - Quality Management|COMP507 08 Quality Management]]** — the sample-size formula `0.25 × (certainty factor / acceptable error)²` and Six Sigma's "≤3.4 defects per million" both run directly on z-scores and the empirical rule above
- **[[COMP517 Data Analysis/Notes/Week 03 - Exploratory Data Analysis|COMP517 W03 EDA]]** — "normal vs skewed" distribution shape is exactly this curve; skewness near 0 (±0.5) signals data close to Normal, which is when mean+SD are trustworthy summary stats (vs [[MATH503 Mathematics/Notes/Week 05 - Statistical Measures|Week 05]]'s median+IQR for skewed data)
- **[[COMP517 Data Analysis/Assignments/Assignment 1 Research|COMP517 Assignment 1]]** — the outlier tests it recommends (IQR *and* z-score, `|z| > 3`) are two different-but-related outlier rules: IQR-based (Week 05, distribution-free) vs z-score-based (this note, assumes roughly Normal data)
- **[[MATH503 Mathematics/Notes/Week 06 - Binomial Distribution|Week 06 - Binomial Distribution]]** — the binomial-to-normal bridge (Np ≥ 5 rule) explained above
- This is also the mathematical foundation for **hypothesis testing / p-values**, the flagged gap in [[COMP517 Data Analysis/Research#3-hypothesis-testing-anova-and-linear-regression|COMP517 Research #3]] — a p-value is essentially "how far into the tail of a Normal (or related) distribution does my result fall"

## Related
- [[MATH503 Mathematics/Notes/Week 06 - Binomial Distribution|Week 06 - Binomial Distribution]] · [[MATH503 Mathematics/Notes/Week 05 - Statistical Measures|Week 05 - Statistical Measures]] · [[MATH503 Mathematics/Research|Research Hub]] · [[MATH503 Mathematics/Index|Course index]]
