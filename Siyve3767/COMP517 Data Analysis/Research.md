---
tags:
  - comp517
  - data-analysis
  - research
  - moc
---

# COMP517 Data Analysis — Research Hub

> Open questions, under-explored topics, and external leads found while reading the course notes. Everything here is **synthesis + external sources** — the course notes themselves were not edited.

## Table of contents
1. [[COMP517 Data Analysis/Research#1-eda-in-python-vs-theory|EDA in Python vs theory]]
2. [[COMP517 Data Analysis/Research#2-handling-missing-data-in-practice|Handling missing data in practice]]
3. [[COMP517 Data Analysis/Research#3-hypothesis-testing-anova-and-linear-regression|Hypothesis testing, ANOVA, and linear regression]]
4. [[COMP517 Data Analysis/Research#4-correlation-vs-causation|Correlation vs causation]]
5. [[COMP517 Data Analysis/Research#5-s2-2025-vs-s2-2026-content-gaps|S2 2025 vs S2 2026 content gaps]]
6. [[COMP517 Data Analysis/Research#cross-course-connections|Cross-course connections]]

---

## 1. EDA in Python vs theory

### Summary
The Week 03 note explains **what EDA is** (Tukey, graphical vs non-graphical, univariate vs multivariate) and Lab 04 covers univariate visualisation, but the vault has no worked example of a **full EDA workflow in Python** (load, profile, clean, describe, visualise, hypothesise). The course plan in Week 01 promises exactly that progression, so a consolidated "EDA with pandas/seaborn" note would bridge theory and labs.

### Links to existing notes
- [[COMP517 Data Analysis/Notes/Week 03 - Exploratory Data Analysis|Week 03 - EDA]] (theory, steps, classification)
- [[COMP517 Data Analysis/Notes/Lab 04 - Univariate Visualisation|Lab 04 - Univariate Visualisation]]
- [[COMP517 Data Analysis/Notes/Lab 02 - NumPy and pandas|Lab 02 - NumPy and pandas]] (tooling)
- [[COMP517 Data Analysis/Notes/Week 01 - Introduction to Data Analysis|Week 01]] (course plan, EDA in the pipeline)

### External sources (not from my vault)
- **Pandas: Working with missing data** — isna(), dropna(), fillna(), interpolation. https://pandas.pydata.org/docs/user_guide/missing_data.html
- **Programming Historian: Linear regression with scikit-learn** — a full worked workflow (part of the EDA-to-modelling arc). https://programminghistorian.org/en/lessons/linear-regression

### Connections
- EDA's "describe and visualise" is the **descriptive statistics** of [[MATH503 Mathematics/Notes/Week 05 - Statistical Measures|MATH503 W05]] (#statistics, #sampling) — see [[COMP517 Data Analysis/Research#cross-course-connections|Cross-course connections]].

---

## 2. Handling missing data in practice

### Summary
Week 03 lists **noisy data, missing values, and duplicates** as data-quality problems and mentions **imputation**, but no lab or note actually shows how to handle missing values in pandas (isna/dropna/fillna/interpolate, or the distinction between MCAR/MAR/MNAR). Given Assignment 2 involves real cleaning, this is a practical gap worth closing with a worked notebook-style note.

### Links to existing notes
- [[COMP517 Data Analysis/Notes/Week 03 - Exploratory Data Analysis|Week 03 - EDA]] (data quality, data wrangling)
- [[COMP517 Data Analysis/Notes/Lab 02 - NumPy and pandas|Lab 02]] (DataFrame basics to build on)
- [[COMP517 Data Analysis/Techbook Summary.txt|Techbook Summary]] (Data Wrangling with Python — the course text for exactly this)

### External sources (not from my vault)
- **Pandas: Working with missing data** — the definitive API guide. https://pandas.pydata.org/docs/user_guide/missing_data.html
- **Data Wrangling with Python (Kazil & Jarmul)** — the course techbook; cleaning chapters map directly to this gap.

### Connections
- Missing data is the data-side twin of **statistical sampling** in [[COMP507 IT Project Management/Notes/08 - Quality Management|COMP507 08 Quality]] (#sampling) and [[MATH503 Mathematics/Notes/Week 05 - Statistical Measures|MATH503 W05]] — sampling bias = missing-not-at-random.

---

## 3. Hypothesis testing, ANOVA, and linear regression

### Summary
The Week 01 course plan lists **hypothesis testing, ANOVA, and linear regression** as topics, but the vault contains **no notes on any of them** — they are the biggest gap in the course. These are also the topics most likely to feel hard without worked examples. (Note: the deck covering them may not have been uploaded yet, or may be in the S2 2026 materials I have not seen.)

### Links to existing notes
- [[COMP517 Data Analysis/Notes/Week 01 - Introduction to Data Analysis|Week 01]] (course plan listing these topics)
- [[COMP517 Data Analysis/Notes/Week 03 - Exploratory Data Analysis|Week 03]] (statistics foundations they build on)

### External sources (not from my vault)
- **Analytics Vidhya: Hypothesis testing for beginners** — null/alternative, p-values, Type I/II errors. https://www.analyticsvidhya.com/blog/2021/07/hypothesis-testing-made-easy-for-the-data-science-beginners/
- **Codecademy: ANOVA with statsmodels** — Python implementation with OLS + anova_lm. https://www.codecademy.com/resources/docs/python/statsmodels/anova-and-hypothesis-testing
- **Programming Historian: Linear regression** — conceptual + scikit-learn code. https://programminghistorian.org/en/lessons/linear-regression
- **scikit-learn: LinearRegression docs** — the API reference. https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html

### Connections
- Hypothesis testing is the **confirmatory (CDA)** side of the EDA-vs-CDA distinction in Week 03, and the **Binomial to Normal** bridge in [[MATH503 Mathematics/Notes/Week 06 - Binomial Distribution|MATH503 W06]] is exactly what makes p-value tests work (#statistics, #expected-value).

---

## 4. Correlation vs causation

### Summary
Correlation appears in the course plan ("Data Aggregation and Correlation") and in scatter diagrams (Lab 04, Week 03), but no note addresses the classic trap: **correlation does not equal causation** — and the distinction between confounding variables, spurious correlations, and experimental vs observational data. EDA's own steps mention confounding variables and interactions, exactly where this matters.

### Links to existing notes
- [[COMP517 Data Analysis/Notes/Week 03 - Exploratory Data Analysis|Week 03 - EDA]] (confounding variables, interactions, scatter plots)
- [[COMP517 Data Analysis/Notes/Lab 04 - Univariate Visualisation|Lab 04]] (scatter plots for relationships)

### External sources (not from my vault)
- **Wikipedia: Correlation does not imply causation** — classic examples and confounders. https://en.wikipedia.org/wiki/Correlation_does_not_imply_causation
- **Tyler Vigen: Spurious Correlations** — entertaining real examples for exam recall. https://www.tylervigen.com/spurious-correlations

### Connections
- The same trap appears in **PM decision-making** — e.g. [[COMP507 IT Project Management/Notes/Week 02 - PM Concepts, Phases and Lifecycle|COMP507 Week 02]]'s success-rate statistics are correlational, not causal (#terminology).

---

## 5. S2 2025 vs S2 2026 content gaps

### Summary
My only Week 03 deck is from **S2 2025** (flagged in its note and the Index); everything else is S2 2026. Also, the course plan promises more topics (time series, aggregation, statistical foundations) than any note covers. **Open question: is the S2 2025 deck still current, and are the missing lecture decks simply not uploaded yet?** If they exist on Canvas, adding them would close the biggest gaps above.

### Links to existing notes
- [[COMP517 Data Analysis/Notes/Week 03 - Exploratory Data Analysis|Week 03 - EDA]] (S2 2025 note)
- [[COMP517 Data Analysis/Index|Course Index]] (S2 2025 warning)

### External sources (not from my vault)
- None needed — this is a **vault-internal gap**, resolved by checking Canvas for S2 2026 decks.

### Connections
- Links to the general "missing materials" issue also flagged in [[MATH503 Mathematics/Research#5-missing-weeks|MATH503 Research]].

---

## Cross-course connections

Topics here that also live in other courses' research hubs:
- **Statistics & distributions** → shared with [[MATH503 Mathematics/Research#cross-course-connections|MATH503 Research]] (descriptive stats, distributions) and [[COMP507 IT Project Management/Research#cross-course-connections|COMP507 Research]] (sampling, Six Sigma) — #statistics, #sampling.
- **Binary / data representation** → shared with [[COMP504 Networks/Research#cross-course-connections|COMP504 Research]] (COMP517 W01 binary connects to COMP504 Number Systems).
- **Expected value / probability** → see [[MATH503 Mathematics/Research#cross-course-connections|MATH503 Research]] (Bayes/conditional probability underpins data analysis).

Back to [[COMP517 Data Analysis/Research#table-of-contents|top]] · [[COMP517 Data Analysis/Index|Course index]]
