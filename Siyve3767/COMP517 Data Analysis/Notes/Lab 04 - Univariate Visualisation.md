---
tags:
  - comp517
  - data-analysis
  - lab
  - python
  - visualisation
  - exam-topic
---

# Lab 04 - Exploratory Data Analysis: Univariate Visualisation

> Auto-extracted from [[COMP517 Data Analysis/Labs/Lab 04 - Tasks.pdf|Lab 04 - Tasks.pdf]]

## Purpose
- Overview of plots and charts used in **univariate** data visualization (one variable at a time)
- Dataset: `sample_video_games_sales.csv` (video game sales by region, name, publisher, platform)
- Libraries: pandas, NumPy, scipy.stats, seaborn, matplotlib (`import matplotlib.pyplot as plt`, `import seaborn as sns`)

## Data loading and inspection
- Load CSV and inspect with `df.head()` and `df.info()`
- Column data types from `df.info()` guide your choice of visualization method

## Visualizing amounts
- **Bar graphs** (vertical or horizontal) - most prevalent for numerical values per category; alternative: dot plots
- Task 1: distribution of game genres - `df["Genre"].value_counts()` to count occurrences
- Other common univariate methods: histograms, pie charts, scatter plots (each suits different data types)

## Key idea
- Matching visualization approach to data characteristics (quantitative vs qualitative) significantly enhances effectiveness and uncovers patterns/relationships

## Notes elsewhere in this vault
- Visualization theory: [[COMP517 Data Analysis/Notes/Week 03 - Exploratory Data Analysis|Week 03 - EDA]]
- Tooling base: [[COMP517 Data Analysis/Notes/Lab 02 - NumPy and pandas|Lab 02 - NumPy and pandas]]
