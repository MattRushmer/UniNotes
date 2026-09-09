---
tags:
  - math503
  - mathematics
  - lecture
  - hypothesis-testing
  - p-value
  - exam-topic
---

# Week 08 - Hypothesis Testing (5.1-5.2)

> Auto-extracted from [[MATH503 Mathematics/Lectures/Week 08 - Lecture.pdf|Week 08 - Lecture.pdf]] (MATH503 Manual, Ch 5) + [[MATH503 Mathematics/Lectures/Week 08 - Important Information.pdf|Week 08 - Important Information.pdf]]

## Housekeeping
- Reading: manual p57-65 (hypothesis testing), Sections 5.2-5.3 (power sets, Cartesian product — needed for relations/functions)
- Section 5.1 (linear functions) is self-study via Myimaths ("Equations of a line 1, 2, 3")
- Myimaths tasks = 25% of final grade; tutorials = 30%; questions go to the Canvas discussion board by Sunday midnight
- Pre-reading for Week 9: manual 5.4 (Relations, p154-158/164-168 online via Garnier & Taylor) and 5.5 (Functions)

## What hypothesis testing is
- The **second most common method of statistical inference** (after confidence intervals) used to draw conclusions about a population from a sample
- Decides in favour of or against a claim; MATH503 covers testing for the **population proportion (p)** and the **population mean (μ)**
- Relies on info from a **random sample** of the population of interest — same population/sample distinction as [[MATH503 Mathematics/Notes/Week 05 - Statistical Measures|Week 05 - Statistical Measures]]

## Null and alternative hypotheses
- **Null hypothesis (H₀)**: the claim being weighed against — a historical value, established claim, or product specification
- **Alternative hypothesis (Hₐ / H₁)**: what you're trying to find evidence *for* — what you want to prove
- Example (proportion): free-throw shooter claims p = 0.8, you suspect exaggeration → H₀: p = 0.80, Hₐ: p < 0.80
- Example (mean): AUT students claimed to study 8.75 hrs/week historically; new sample suggests 10.25 hrs/week → H₀: μ = 8.75, Hₐ: μ > 8.75 (or < / ≠, depending on the question)

## One-sided vs two-sided tests
- **One-sided (one-tailed)**: Hₐ states the parameter is *greater than* or *less than* the null value (Options 1 & 2 above)
- **Two-sided (two-tailed)**: Hₐ states the parameter is simply *different from* the null value (≠) (Option 3)
- You must read the scenario and decide which of the three options applies — that decision is itself part of the test

## The p-value
- **p-value** = the probability of obtaining results at least as extreme as the one observed, **given that H₀ is true**
- For Hₐ: `<` → extreme cases in the **left tail** · Hₐ: `>` → **right tail** · Hₐ: `≠` → **both tails**
- **Significance level (α)**: the arbitrary threshold for "statistically significant" — most common is **5% (0.05)**
- **Decision rule**: p-value < α → **reject H₀** · p-value > α → **cannot reject H₀** (note: never "accept" H₀, only fail to reject it)

## Worked example — proportion (election candidate)
- Candidate claims 40% support; sample of 20 people, only 3 say yes; test at 5% significance
- H₀: p = 0.4 · Hₐ: p < 0.4 (one-sided, left tail — testing if she's *over*-estimating)
- p-value = P(≤3 supporters out of 20 | p=0.4), using the **Binomial distribution** (n=20, p=0.4) — see [[MATH503 Mathematics/Notes/Week 06 - Binomial Distribution|Week 06 - Binomial Distribution]]
- `pbinom(3,20,0.4) = 0.016` (1.6%) < 0.05 → **reject H₀** — she is over-estimating her support
- **Critical/rejection region**: the largest count where cumulative probability stays under 5% — here, "3 or fewer supporters out of 20" (since `pbinom(4,20,0.4)=5.1%` already exceeds 5%)

## Worked example — mean, three equivalent methods (test mark)
- H₀: μ = 56.9, Hₐ: μ < 56.9; test statistic x̄ ~ Normal(56.9, σ=2.08) [σ/√n from population sd 6.9, n=11]; observed x̄ = 56
- **Method 1 — p-value**: `pnorm(56, 56.9, 2.08) = 0.3326` > 0.05 → no evidence to reject H₀
- **Method 2 — rejection region**: critical value = `qnorm(0.05, 56.9, 2.08) = 53.48` → rejection region is x̄ < 53.48; observed 56 isn't in it → no evidence to reject
- **Method 3 — Z-score**: critical z = −1.6449 (one-tailed, 5%); observed z = (56−56.9)/2.08 = −0.4327, which is > −1.6449 (not past the critical value) → no evidence to reject
- All three methods agree — this is the direct application of [[MATH503 Mathematics/Notes/Week 07 - Normal Distribution and Z-Scores|Week 07 - Normal Distribution and Z-Scores]]'s standardization and z-table logic to decision-making

## Worked example — mean, two-sided test (kiwi bird weights)
- Sample of 30 kiwi weights, sample mean x̄ = 1.030333 kg, sample sd s = 0.1006696; national mean μ = 1 kg
- H₀: μ = 1 · Hₐ: μ ≠ 1 (two-sided, since the question is just "does it differ")
- p-value = 2 × P(X̄ > 1.030333) = **0.099** > 0.05 → no evidence to reject H₀ — this forest's kiwi don't differ significantly from the national average

## Related
- [[MATH503 Mathematics/Notes/Week 06 - Binomial Distribution|Week 06 - Binomial Distribution]] (binomial p-values for proportions)
- [[MATH503 Mathematics/Notes/Week 07 - Normal Distribution and Z-Scores|Week 07 - Normal Distribution and Z-Scores]] (the z-score/p-value machinery this week applies)
- [[MATH503 Mathematics/Notes/Week 08 - Tutorial (Hypothesis Testing)|Week 08 - Tutorial (Hypothesis Testing)]] — practice questions
- [[COMP517 Data Analysis/Research#3-hypothesis-testing-anova-and-linear-regression|COMP517 Research #3]] — this note closes that flagged gap; hypothesis testing is the confirmatory (CDA) counterpart to [[COMP517 Data Analysis/Notes/Week 03 - Exploratory Data Analysis|COMP517 W03 EDA]]'s exploratory approach
- [[MATH503 Mathematics/Index|Course index]] · [[MATH503 Mathematics/Research|Research Hub]]
