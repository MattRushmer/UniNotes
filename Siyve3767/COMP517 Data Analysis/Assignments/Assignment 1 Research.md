---
tags:
  - comp517
  - data-analysis
  - assignment
  - research
  - eda
  - exam-topic
---

# COMP517 Assignment 1 — Research

> Research companion for **Assignment One: Data Exploration and Analysis**, S2 2026 — 100 marks, due **Fri 11 Sep 2026, 5:00pm** (-5 marks/day late). Individual assignment, submitted via Turnitin (report up to 5,000 words + a separate `.ipynb`/`.py` code file). Source brief: [[COMP517 Data Analysis/Assignments/Assignment 1/Assignment 1_S2_2026.pdf|Assignment 1_S2_2026.pdf]]. Everything here is **synthesis + external sources** — the analysis and report are your own work.

## The assignment in one paragraph
Choose **one** of two provided datasets, then run a full EDA pipeline: (1) load + summarise the dataset, (2) pre-process it — missing values, duplicates, outliers, (3) explore and visualise the clean data, (4) multivariate analysis — correlations, categorical x count aggregation, mean/median aggregation, and a BMI->risk (or credit-score->loan) relationship, (5) conclusion, (6) present it all in a structured report with figures/tables but **no code in the report** (code goes in the separate file).

## Step-by-step guide

> Actionable plan mapped to the mark blocks — work top to bottom; each step feeds the next. *(100 marks total)*

### Step 0 — Pick your dataset (do this first)
Read both files' metadata, then commit to **one**. [[COMP517 Data Analysis/Assignments/Assignment 1/Dataset - Global Air Quality 2023|Dataset A]] = cleaning showcase; [[COMP517 Data Analysis/Assignments/Assignment 1/Dataset - Gen Z Mental Wellness|Dataset B]] = correlation story. You only need one.

### Step 1 — Load & summarise (10 marks)
`pd.read_csv(...)`, then `df.shape`, `df.info()`, `df.describe()`, `df.head()`, check dtypes and `df.isnull().sum()`. State the dataset's size and what each column means. (See [[COMP517 Data Analysis/Notes/Lab 02 - NumPy and pandas|Lab 02 - NumPy and pandas]].)

### Step 2 — Pre-processing (20 marks)
- **Missing values:** drop vs impute — *median* for skewed numerics, mean for symmetric, mode for categoricals, `interpolate()` for date-ordered data. **Justify every choice.**
- **Duplicates:** `df.duplicated().sum()` → check true repeats vs legit records (same city/date) → `drop_duplicates()`.
- **Outliers:** IQR (`Q1±1.5×IQR`) and/or z-score (`|z|>3`), plus box/scatter plots. Keep real extremes, remove data-entry errors, or winsorise. Show **scatterplots of outlier vs non-outlier points**. (IQR/quartiles: [[MATH503 Mathematics/Notes/Week 05 - Statistical Measures|MATH503 W05]].)

### Step 3 — Explore & visualise (25 marks)
Histograms for numerics, bar/pie for categoricals, box plots for spread; compare mean vs median to spot skew. **Every plot: title, labelled axes, legend.** (Formatting: [[COMP517 Data Analysis/Notes/Lab 04 - Univariate Visualisation|Lab 04 - Univariate Visualisation]].)

### Step 4 — Multivariate analysis (20 marks)
- **Correlation heatmap** (`df.select_dtypes('number').corr()` + seaborn) — report strong `|r| > 0.7` pairs.
- **Categorical × count:** pick 2 categoricals, plot how counts vary (grouped bar/heatmap).
- **Aggregation:** `groupby(...).agg(['mean','median'])` → table + graph.
- **"BMI→risk"-style analysis:** pick the analogous pair (e.g. screen time/sleep → wellbeing/burnout risk), show average + variation, discuss **two significances**. (Context: [[COMP517 Data Analysis/Notes/Week 03 - Exploratory Data Analysis|Week 03 - EDA]].)

### Step 5 — Conclusion (15 marks)
Summarise findings, challenges + how you fixed them, and 2–3 next steps (feature engineering, modelling, more data).

### Step 6 — Write the report (10 marks for structure)
Title + name + student ID, table of contents, list of figures/tables, answer each question, labelled figures with captions. **Keep all code in the separate file.**

### Step 7 — Submit
Upload report + code file separately (don't zip).

> ⚠️ The brief's `loan_dataset.csv` / `diabetes_dataset.csv` examples are **generic placeholders** — map that style of analysis onto your chosen dataset.

## Your two datasets (verified from the files)

### Dataset A — Global Air Quality 2023 (messy)
- File: [[COMP517 Data Analysis/Assignments/Assignment 1/Dataset - Global Air Quality 2023/global_air_quality_data_messy.csv|global_air_quality_data_messy.csv]] + `README.md`
- **30,450 rows**, columns: City, Country, Date, PM2.5, PM10, NO2, SO2, CO, O3, Temperature, Humidity, Wind Speed
- Deliberately messy: injected missing values, duplicates, outliers, inconsistent case/spacing, shuffled rows
- Derived from the Kaggle *Global Air Quality Dataset* by WAQI786 — https://www.kaggle.com/datasets/waqi786/global-air-quality-dataset
- **Good choice if** you want to show off data-cleaning and pollutant-outlier handling.

### Dataset B — Gen Z Mental Wellness & Digital Lifestyle (synthetic)
- File: [[COMP517 Data Analysis/Assignments/Assignment 1/Dataset - Gen Z Mental Wellness/genz_mental_wellness_synthetic_dataset.csv|genz_mental_wellness_synthetic_dataset.csv]]
- **10,000 rows**, 22 columns: Age, Gender, Country, Student_Working_Status, Daily_Social_Media_Hours, Screen_Time_Hours, Night_Scrolling_Frequency, Online_Gaming_Hours, Content_Type_Preference, Exercise_Frequency_per_Week, Daily_Sleep_Hours, Caffeine_Intake_Cups, Study_Work_Hours_per_Day, Overthinking_Score, Anxiety_Score, Mood_Stability_Score, Social_Comparison_Index, Sleep_Quality_Score, Motivation_Level, Emotional_Fatigue_Score, Wellbeing_Index, Burnout_Risk
- Synthetic Kaggle dataset (hammadansari7) — https://www.kaggle.com/datasets/hammadansari7/gen-z-mental-wellness-and-digital-lifestyle-patterns
- **Good choice if** you want richer multivariate analysis: many numeric scores + categoricals, and clear correlations to investigate (screen time vs sleep vs wellbeing).

## EDA playbook (what each mark block needs)

### 2. Pre-processing (20 marks)
- **Missing values**: check `df.isnull().sum()`. Decide removal vs imputation — drop rows only when missing is negligible (<5-10%) or a column is mostly empty; impute otherwise. Use **median for skewed numerics** (pollutants, income-like data), mean for normal distributions, mode for categoricals, or `df.interpolate()` for time-series (AQI by date). *Justify every choice* — that's where the marks are.
- **Duplicates**: `df.duplicated().sum()`, inspect, then `df.drop_duplicates()`. Check whether "duplicates" are true repeats or legitimately distinct records (same user/city on different dates) before removing.
- **Outliers**: statistical (IQR: Q1-1.5*IQR / Q3+1.5*IQR; z-score |z|>3) **and** visual (box plots, scatter plots). Then keep (real extreme events like pollution spikes), remove (data-entry errors), or transform/cap (winsorise). Justify. The brief specifically wants **scatterplots of outlier/non-outlier points**.

### 3. Explore & visualise (25 marks)
- Summary stats: `df.describe()` — compare mean vs median to detect skew, note std dev.
- Distributions: histograms for numerics, bar/pie for categoricals, box plots for spread.
- Every plot needs a **title, labelled axes, legend** — the report presentation block (10 marks) explicitly checks this.

### 4. Multivariate analysis (20 marks)
- **Correlations**: `df.select_dtypes('number').corr()` + seaborn heatmap with annotations. Look for strong |r| > 0.7 pairs; report the interesting ones (e.g. screen time vs sleep, anxiety vs overthinking in Dataset B).
- **Categorical x count**: pick 2 categorical variables rationally and plot how the `count` varies across them (grouped bar / heatmap) — the brief asks for one plot combining two categoricals.
- **Aggregation**: `groupby(...).agg(mean, median)` on the `count` column — table + graph.
- **BMI -> risk / credit -> loan style analysis**: for your dataset, pick the analogous pair (e.g. in Dataset B: BMI is available, plus wellbeing/anxiety scores) and show the average + variation with an appropriate plot, discussing two significances of the analysis.
- **Note:** the brief's examples (`loan_dataset.csv`, `diabetes_dataset.csv`) are generic placeholders — neither exists in your download; pick the equivalent columns from your chosen dataset.

### 5. Conclusion (15 marks)
Summarise key findings, challenges + how you fixed them, and 2-3 sensible next steps (feature engineering, modelling, more data).

## Links to your existing notes
- [[COMP517 Data Analysis/Notes/Week 01 - Introduction to Data Analysis|Week 01 - Introduction]] — course context, LO1/LO2
- [[COMP517 Data Analysis/Notes/Week 03 - Exploratory Data Analysis|Week 03 - Exploratory Data Analysis]] — EDA concepts, profiling, distributions — **core reference**
- [[COMP517 Data Analysis/Notes/Lab 01 - Basic Python Programming|Lab 01 - Basic Python]] — Python essentials
- [[COMP517 Data Analysis/Notes/Lab 02 - NumPy and pandas|Lab 02 - NumPy and pandas]] — DataFrame loading, cleaning, groupby
- [[COMP517 Data Analysis/Notes/Lab 04 - Univariate Visualisation|Lab 04 - Univariate Visualisation]] — histograms, box plots, formatting plots
- [[MATH503 Mathematics/Notes/Week 05 - Statistical Measures|MATH503 - Statistical Measures]] — mean/median/std, population vs sample (cross-course)
- [[MATH503 Mathematics/Notes/Week 06 - Binomial Distribution|MATH503 - Binomial Distribution]] — distributions context (cross-course)
- [[COMP517 Data Analysis/Research|COMP517 Research Hub]] — hypothesis testing / ANOVA / regression are upcoming course topics this assignment's "next steps" can preview

## External sources (not from your vault)
- **Kaggle — Global Air Quality Dataset** (WAQI786): https://www.kaggle.com/datasets/waqi786/global-air-quality-dataset
- **Kaggle — Gen Z Mental Wellness dataset** (hammadansari7): https://www.kaggle.com/datasets/hammadansari7/gen-z-mental-wellness-and-digital-lifestyle-patterns
- **pandas user guide — missing data**: https://pandas.pydata.org/docs/user_guide/missing_data.html
- **pandas user guide — groupby/aggregation**: https://pandas.pydata.org/docs/user_guide/groupby.html
- **seaborn — correlation heatmaps**: https://seaborn.pydata.org/generated/seaborn.heatmap.html

## Flags & to-dos
1. **Choose your dataset early** — you only need one. Dataset A showcases cleaning; Dataset B showcases multivariate story-telling. Both were verified present and readable in your download.
2. **No code in the report** — code lives only in the `.ipynb`/`.py`; the report presents findings, figures, tables. Including code in the report is penalised.
3. **Report structure** (10 marks): title + name + student ID, table of contents, list of figures/tables, answers to each question, labelled figures/captions.
4. The brief's `loan_dataset.csv` / `diabetes_dataset.csv` examples are placeholders — don't search for them; map the same style of analysis onto your chosen dataset.
