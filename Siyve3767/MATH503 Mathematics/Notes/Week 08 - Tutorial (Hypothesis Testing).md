---
tags:
  - math503
  - mathematics
  - tutorial
  - hypothesis-testing
  - practice
  - exam-topic
---

# Week 08 - Tutorial (Hypothesis Testing)

> Auto-extracted from [[MATH503 Mathematics/Tutorials/Week 08 - Tutorial (Hypothesis Testing).pdf|Week 08 - Tutorial (Hypothesis Testing).pdf]]. Practice for [[MATH503 Mathematics/Notes/Week 08 - Hypothesis Testing|Week 08 - Hypothesis Testing]].

## Question 1 — mean, population sd known (IQ scores)
A principal claims his students are above-average intelligence. Sample: n=30, sample mean = 112.5. Population mean IQ = 100, population sd = 15. Test at 5% significance.
- This is a **one-sided test for a mean** (Hₐ: μ > 100) — population sd is known, so use the Normal distribution directly (no t-test needed)

## Question 2 — mean, large sample (drug response time)
100 rats injected with a drug; mean response time 1.05s, sample sd 0.5s, vs an untreated mean of 1.2s. Test at 5% whether the drug reduced response time.
- **Note in the brief**: population sd is unknown, so strictly a **t-test** applies — not covered in this course — but because n=100 > 30, the **Normal distribution is used as an approximation** (Central Limit Theorem territory, same idea as the binomial→normal bridge in [[MATH503 Mathematics/Notes/Week 07 - Normal Distribution and Z-Scores|Week 07]])

## Question 3 — proportion (Chardonnay orders)
Baseline: 1 in 10 people order Chardonnay (p=0.1). Sample: 50 people, 11 chose it. Test at **1%** significance whether the drink has become more popular.
- One-sided test for a **proportion** (Hₐ: p > 0.1), tighter significance level (α=0.01) than the standard 5%

## Question 4 — proportion, two-sided (red cars)
Claimed proportion of red cars p=0.3. Sample: n=15. Test H₀: p=0.3 vs Hₐ: p≠0.3 at **10%** significance. Determine the appropriate region and rejection region.
- Two-sided proportion test with a looser 10% significance level — practice finding **both** tails of the rejection region (per [[MATH503 Mathematics/Notes/Week 08 - Hypothesis Testing|Week 08 - Hypothesis Testing]]'s p-value/rejection-region/z-score methods)

## Method reminder (from the lecture note)
For each question: (1) identify proportion vs mean, (2) state H₀/Hₐ in words and symbols, (3) compute the p-value (binomial for proportions, normal for means with known/large-sample sd), (4) compare to α, (5) state the rejection/critical region.

## Related
- [[MATH503 Mathematics/Notes/Week 08 - Hypothesis Testing|Week 08 - Hypothesis Testing]] — worked examples and methods this tutorial applies
- [[MATH503 Mathematics/Notes/Week 06 - Binomial Distribution|Week 06 - Binomial Distribution]] (proportion tests use the binomial)
- [[MATH503 Mathematics/Index|Course index]]
