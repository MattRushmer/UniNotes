---
tags:
  - comp517
  - data-analysis
  - lecture
  - eda
  - statistics
  - sampling
  - exam-topic
---

# Week 03 - Exploratory Data Analysis: Data Preparation

> Auto-extracted from [[COMP517 Data Analysis/Lectures/Week 03 - Lecture (S2 2025).pdf|Week 03 - Lecture (S2 2025).pdf]]
> Note: this lecture deck is from S2 2025 (earlier session) - check for S2 2026 updates

## Data types (organization and format)
- **Structured**: highly organized, easily searchable; relational databases and spreadsheets; tabular format, predefined schema, high integrity
- **Semi-structured** and **unstructured**: less organized (text, media)
- Characteristics: dimensionality, sparsity, resolution, **distribution** (uniform, normal/Gaussian, skewed)

## Attribute types
- **Quantitative**: meaningful numbers - **discrete** (countable values, e.g. die 1-6) vs **continuous** (any value in a range, e.g. height, temperature)
- **Categorical/qualitative**: values in categories - **nominal** (no natural order, e.g. gender) vs **ordinal** (natural order, e.g. satisfaction ranking); can be coded numerically

## Data wrangling
- **Data Cleaning**: identify and handle missing, incorrect, inconsistent values (imputation, correcting errors)
- **Data Transformation**: convert/rescale data (aggregating, summarizing, normalizing)
- **Data Integration**: combine multiple sources into a unified dataset
- **Data Reduction**: reduce data while preserving informational content
- **Data Formatting**: consistent and standardized presentation (types, units, rules)

## Data quality
- **Data Profiling**: understand structure, content, relationships - analyze distributions, identify NULLs, outliers, data types (see also [[MATH503 Mathematics/Notes/Week 05 - Statistical Measures|MATH503 population vs sample]] and [[COMP507 IT Project Management/Notes/08 - Quality Management|COMP507 statistical sampling]])
- **Data Validation**: verify data conforms to rules/constraints (date formats, numeric ranges)
- Common problems: noise and outliers, missing values, duplicate data

## Exploratory Data Analysis (EDA)
- EDA = analysis of datasets using numerical methods and graphical tools; exploring for patterns, trends, underlying structure, anomalies
- Tukey: "EDA is detective work... Unless detective finds the clues, judge or jury has nothing to consider" - judge/jury = **confirmatory data analysis (CDA)**
- EDA vs CDA: EDA has no hypothesis at first and generates hypotheses using mostly graphical methods; CDA starts with a hypothesis and tests the null hypothesis with statistical models

### Aims of EDA
- Maximize insight into a dataset, uncover underlying structure, extract important variables, detect outliers/anomalies, test underlying assumptions, develop valid models

### Steps of EDA
1. Generate good research questions
2. Data restructuring (new variables, rates/percentages, dummy variables)
3. Use appropriate graphical tools + descriptive statistics
4. Understand structure, relationships, anomalies
5. Identify confounding variables, interactions, multicollinearity
6. Handle missing observations
7. Decide on transformations
8. Decide on hypotheses from research questions

### Classification
- Non-graphical (summary statistics) vs graphical (diagrams)
- Univariate (one variable) vs bivariate/multivariate (two or more) - always do univariate first
- Example datasets: Places Rated Almanac (9 variables, 329 US metros); breast cancer survival; teenager well-being after economic hardship

## Summarizing data: descriptive statistics
- **Measures of central tendency/location**: mean (sensitive to outliers and skewness - use median or trimmed mean instead), median, mode — same point as [[MATH503 Mathematics/Notes/Week 05 - Statistical Measures|MATH503 W05]]
- **Measures of spread**: range, and others; skewness ~0 (in -0.5..0.5) = symmetrical
- **Percentiles**: value below which X% of observations fall (e.g. 20th percentile)

## Notes elsewhere in this vault
- Python tooling for EDA in [[COMP517 Data Analysis/Notes/Lab 02 - NumPy and pandas|Lab 02]] and [[COMP517 Data Analysis/Notes/Lab 04 - Univariate Visualisation|Lab 04]]
- Distribution concepts also appear in [[MATH503 Mathematics/Notes/Week 05 - Statistical Measures|MATH503 W05 (statistical measures)]] and [[MATH503 Mathematics/Notes/Week 06 - Binomial Distribution|MATH503 W06 (binomial)]]; quality-control statistics in [[COMP507 IT Project Management/Notes/08 - Quality Management|COMP507 08 Quality]]
