---
tags:
  - math503
  - mathematics
  - research
  - moc
---

# MATH503 Mathematics — Research Hub

> Open questions, under-explored topics, and external leads found while reading the course notes. Everything here is **synthesis + external sources** — the course notes themselves were not edited.

## Table of contents
1. [[MATH503 Mathematics/Research#1-bayes-theorem-and-the-monty-hall-problem|Bayes' theorem and the Monty Hall problem]]
2. [[MATH503 Mathematics/Research#2-the-normal-distribution-and-z-scores|The normal distribution and z-scores]]
3. [[MATH503 Mathematics/Research#3-permutations-vs-combinations|Permutations vs combinations]]
4. [[MATH503 Mathematics/Research#4-statistics-and-data-science-connections|Statistics and data-science connections]]
5. [[MATH503 Mathematics/Research#5-missing-weeks|Missing weeks]]
6. [[MATH503 Mathematics/Research#cross-course-connections|Cross-course connections]]

---

## 1. Bayes' theorem and the Monty Hall problem

### Summary
Week 03 covers **conditional probability** (P(E|F) = P(E and F)/P(F)), independent events, and the product rule, and it lists the **Monty Hall problem** as a topic — but my notes never actually solve Monty Hall or introduce **Bayes' theorem** (the reverse conditional P(A|B) from P(B|A)). Bayes' is the natural next step after conditional probability, appears in almost every statistics course, and is directly relevant to the data-science motivation the lecture itself states ("conditional probability helps data scientists").

### Links to existing notes
- [[MATH503 Mathematics/Notes/Week 03 - Conditional Probability|Week 03 - Conditional Probability]]
- [[MATH503 Mathematics/Notes/Week 06 - Binomial Distribution|Week 06 - Binomial Distribution]] (probability foundations, expected value)
- [[MATH503 Mathematics/Notes/Week 04 - Permutations and Counting|Week 04 - Counting]] (outcome spaces for Monty Hall)

### External sources (not from my vault)
- **Wikipedia: Bayes' theorem** — formula, priors/likelihood/posterior, worked examples. https://en.wikipedia.org/wiki/Bayes%27_theorem
- **Brilliant: Bayes' theorem** — step-by-step with intuition. https://brilliant.org/wiki/bayes-theorem/
- **Wikipedia: Monty Hall problem** — why switching wins 2/3 of the time. https://en.wikipedia.org/wiki/Monty_Hall_problem
- **arXiv: What's So Hard about the Monty Hall Problem?** (Alvarado, 2024) — a university-level Bayesian treatment. https://arxiv.org/html/2405.00884v1

### Connections
- Bayes' theorem is the mathematical engine behind **COMP517 hypothesis testing** (posterior = updated belief; p-values are conditional probabilities) — see [[MATH503 Mathematics/Research#cross-course-connections|Cross-course connections]].

---

## 2. The normal distribution and z-scores

### Status: ✅ filled (researched note, not yet verified against a real lecture)
[[MATH503 Mathematics/Notes/Week 07 - Normal Distribution and Z-Scores|Week 07 - Normal Distribution and Z-Scores]] now covers the bell curve, μ/σ, the 68-95-99.7 empirical rule, z-score standardization, and reading the standard normal table — written externally since no Week 7 deck exists in the vault. **Still worth checking against the actual Week 7 lecture** once you get it, for notation/terminology your lecturer prefers.

### Summary
Week 06 explicitly says the binomial is well approximated by the **Normal distribution "the subject of the week 7 lecture"** — but my vault has **no Week 7 note**. The normal curve, z-scores, and the 68-95-99.7 rule are therefore a promised-but-missing topic. The only sigma/percentile material I have is in COMP507 Quality (z-scores, certainty factors) and COMP517 EDA (normal vs skewed distributions), which both assume it.

### Links to existing notes
- [[MATH503 Mathematics/Notes/Week 06 - Binomial Distribution|Week 06 - Binomial Distribution]] (binomial-to-normal bridge, BINS)
- [[MATH503 Mathematics/Notes/Week 05 - Statistical Measures|Week 05 - Statistical Measures]] (mean/median, spread, percentiles)
- [[COMP507 IT Project Management/Notes/08 - Quality Management|COMP507 08 Quality]] (z-scores, certainty factors, Six Sigma) — cross-course
- [[COMP517 Data Analysis/Notes/Week 03 - Exploratory Data Analysis|COMP517 W03 EDA]] (normal vs skewed distributions) — cross-course

### External sources (not from my vault)
- **Wikipedia: Normal distribution** — properties, 68-95-99.7 rule. https://en.wikipedia.org/wiki/Normal_distribution
- **Khan Academy: Z-scores** — standardising and reading the table. https://www.khanacademy.org/math/statistics-probability/modeling-distributions-of-data/z-scores-intro

### Connections
- The normal distribution is the shared statistical bridge across **all four courses** (see the Themes proposal at the end of this note) — #statistics, #distributions.

---

## 3. Permutations vs combinations

### Summary
Week 04 covers the **multiplication principle and factorial notation**, and its title promises **permutations** — but my notes never reach the **permutation (nPr) and combination (nCr) formulas**, which are what the binomial distribution's coefficient (n choose x) actually needs in Week 06. That's a real pedagogical gap: Week 06 uses nCr implicitly but the counting note stops one step short.

### Links to existing notes
- [[MATH503 Mathematics/Notes/Week 04 - Permutations and Counting|Week 04 - Permutations and Counting]] (multiplication principle, factorials)
- [[MATH503 Mathematics/Notes/Week 06 - Binomial Distribution|Week 06 - Binomial Distribution]] (needs nCr for P(X=x))

### External sources (not from my vault)
- **Wikipedia: Combination** — nCr formula and relation to permutations. https://en.wikipedia.org/wiki/Combination
- **Khan Academy: Combinations** — intuition and practice. https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:prob-comb/x9e81a4f98389efdf:combinations/v/combination-formula

### Connections
- The same nPr/nCr counting logic drives **COMP504 VLSM block sizing** (2^n) — see [[COMP504 Networks/Research#cross-course-connections|COMP504 Research]] (#combinatorics).

---

## 4. Statistics and data-science connections

### Summary
MATH503's own lectures repeatedly motivate probability via **data science and machine learning** (Week 03: "conditional probability helps data scientists"), but the course content stays abstract — no applied statistics note connects the math to actual data analysis. Since the vault now has COMP517 (Python data analysis) and COMP507 (quality sampling), there's a natural bridge topic: **how MATH503's probability/statistics powers real analysis** (mean/median for EDA, binomial for sampling, normal for z-tests).

### Links to existing notes
- [[MATH503 Mathematics/Notes/Week 05 - Statistical Measures|Week 05 - Statistical Measures]] (mean/median/percentiles)
- [[MATH503 Mathematics/Notes/Week 06 - Binomial Distribution|Week 06 - Binomial Distribution]]
- [[MATH503 Mathematics/Notes/Week 03 - Conditional Probability|Week 03 - Conditional Probability]] (data-science motivation)
- [[COMP517 Data Analysis/Notes/Week 03 - Exploratory Data Analysis|COMP517 W03 EDA]] — cross-course
- [[COMP507 IT Project Management/Notes/08 - Quality Management|COMP507 08 Quality]] — cross-course

### External sources (not from my vault)
- **Foundations of Data Science (Adhikari & DeNero)** — the free online text COMP517 references; bridges stats intuition and code. https://inferentialthinking.com/

### Connections
- This is the single biggest cross-course thread in the vault — see [[MATH503 Mathematics/Research#cross-course-connections|Cross-course connections]] and the Themes proposal below.

---

## 5. Missing weeks

### Summary
My vault only has **Weeks 3-6** notes for MATH503 (conditional probability, counting, statistical measures, binomial). The [[MATH503 Mathematics/Course Overview|Course Overview]] now lists the full 12-week plan, so the gaps are known:
- Missing **Weeks 1-2**: Sets and probability, Venn diagrams
- Missing **Weeks 7-12**: Probability distributions + hypothesis testing (7-8), relations and functions (9), matrices (10-11), review (12)

The Week 04 Notes PDF is also an image scan with no readable text. **Open question: are these weeks somewhere else in the vault, on Canvas, or not yet released?**

### Links to existing notes
- [[MATH503 Mathematics/Notes/Week 04 - Notes (image scan)|Week 04 - Notes (image scan)]] (OCR pending)
- [[MATH503 Mathematics/Course Overview|Course Overview]] (full 12-week schedule)
- [[MATH503 Mathematics/Index|Course Index]] (missing-weeks warning)
- [[MATH503 Mathematics/Notes/Week 06 - Binomial Distribution|Week 06]] (points forward to Week 7)

### External sources (not from my vault)
- None needed — this is a **vault-internal gap**, resolved by checking Canvas.

### Connections
- The same "missing materials" issue affects [[COMP517 Data Analysis/Research#5-s2-2025-vs-s2-2026-content-gaps|COMP517]] — worth checking both courses in one pass on Canvas.

---

## Cross-course connections

Topics here that also live in other courses' research hubs:
- **Statistics & distributions** → shared with [[COMP517 Data Analysis/Research#cross-course-connections|COMP517 Research]] (EDA, descriptive stats) and [[COMP507 IT Project Management/Research#cross-course-connections|COMP507 Research]] (sampling, Six Sigma) — #statistics, #sampling, #distributions.
- **Expected value / probability** → shared with [[COMP507 IT Project Management/Research#cross-course-connections|COMP507 Research]] (mean = Np → EMV → EVM, #expected-value) and underpins [[COMP517 Data Analysis/Research#cross-course-connections|COMP517]] hypothesis testing.
- **Combinatorics / powers of two** → shared with [[COMP504 Networks/Research#cross-course-connections|COMP504 Research]] (2^n subnetting blocks, communication-channels formula, #combinatorics).
- **Binary & data representation** → see [[COMP504 Networks/Research#cross-course-connections|COMP504 Research]] and [[COMP517 Data Analysis/Research#cross-course-connections|COMP517 Research]].

Back to [[MATH503 Mathematics/Research#table-of-contents|top]] · [[MATH503 Mathematics/Index|Course index]]
