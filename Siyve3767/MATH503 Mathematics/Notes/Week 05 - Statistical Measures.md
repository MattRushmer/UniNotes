---
tags:
  - math503
  - mathematics
  - lecture
  - statistics
  - sampling
  - r-studio
  - exam-topic
---

# Week 05 - Statistical Measures (3.1-3.2)

> Auto-extracted from [[MATH503 Mathematics/Lectures/Week 05 - Lecture.pdf|Week 05 - Lecture.pdf]] (MATH503 Manual Ch 3, Sections 3.1-3.2; R Studio)

## Discrete vs continuous data
- **Discrete** data arise from counting and usually involve whole numbers (e.g. how many people took the bus; photons hitting a CCD pixel - no fractions of a photon)
- **Continuous** data arise from measuring and can be any value (e.g. travel time; microphone voltage over time)

## Descriptive statistics
- Describing features of a data set by generating summaries about data samples
- **Measures of central tendency** (averages): mean, median, mode
- **Measures of spread (variability)**: variance, standard deviation, range, maximum, minimum, lower/upper quartile, interquartile range

## The mean
- Sum of all values divided by the number of values; sample mean x-bar = sum(x_i)/n; population mean denoted by mu
- The mean is the **balance point** of the data
- Every value contributes; it is **sensitive to outliers and skew** - example: staff salaries 45k-56k with two outliers 120k and 135k -> mean $63k misleads; **median is better** for skewed data (same point in [[COMP517 Data Analysis/Notes/Week 03 - Exploratory Data Analysis|COMP517 W03]])

## Population vs sample
- **Population**: the complete set (e.g. all 249 MATH503 students S1 2026)
- **Sample**: a representative subset (e.g. randomly selected 30 students)
- We infer population behaviour from the sample - must choose samples carefully (sampling bias can go wrong!) - sampling theory is also used for [[COMP507 IT Project Management/Notes/08 - Quality Management|COMP507 quality control]] and [[COMP517 Data Analysis/Notes/Week 03 - Exploratory Data Analysis|COMP517 data profiling]]
- Population mean is mu; sample mean is x-bar

## The median
- The middle score of data arranged in order of magnitude
- Interpretation: 50% of values are below the median
- Even number of values: average of the two middle values
- **Less affected by outliers** (salary example: median 54k vs mean 63k)

## The mode
- The most common value in the data set; rarely used with continuous data
- Histograms show a dataset's shape: **unimodal** (one peak), **bimodal** (two peaks), **multimodal** (more than two peaks)

## Range
- Range = maximum value - minimum value (simplest measure of spread)
- Sets the boundaries of the scores - useful when a variable has a critical low/high threshold that should not be crossed (e.g. age 125 years means a data-entry mistake!)
- Limited: only uses the two extreme values

## Quartiles
- Break the data into quarters, like the median breaks it in half; there are **three** quartiles: Q1, Q2 (= median), Q3
- Interpretation (final exam and labs!):
  - Q1: 25% of values are <= Q1 (or 75% >= Q1)
  - Q2 (median): 50% of values are <= Q2
  - Q3: 75% of values are <= Q3 (or 25% >= Q3)
- **Interquartile range (IQR)** = Q3 - Q1 (the middle half of the data). Do not confuse with the RANGE
- Caution: there is no universal definition of quartiles (~4 definitions - see Wikipedia); RStudio can differ from the by-hand method

## Skew and outliers
- As data becomes skewed, the mean loses its ability to give the best central location - the skewed data drags it away from the typical value
- For skewed data or data with outliers, use **median + quartiles/IQR/range** instead of mean + standard deviation
- **Outliers** are points at an abnormal distance from the rest of the data (may be genuine, not always faulty)
- Outlier test: x > Q3 + 1.5xIQR, or x < Q1 - 1.5xIQR
- **Boxplots** (box-and-whisker) visualise quartiles, IQR and outliers - worked example compares filling times across 3 machines

## R / RStudio (lab)
- Download R from CRAN (https://cran.r-project.org/), then RStudio IDE from https://posit.co/download/rstudio-desktop/ - versions for Windows/Mac/Linux
- Define a data set with the `c()` operator: `data <- c(2,3,3,4,5,6,7,8)` - `c` means "combine/concatenate"; creates a vector; use `<-` (preferred) or `=`
- Central tendency: `mean(dataset)` and `median(dataset)`
- R has **no built-in mode function** (needs a custom function - not covered in this course)
- Practice with the built-in **AirPassengers** dataset
- RStudio's quartile definition can differ from the by-hand result - check this when comparing answers

## Housekeeping
- **Myimaths** portal: individual username/password, allocated tasks worth **25% of the final grade**

## Notes elsewhere in this vault
- Mean/median/percentiles also covered in [[COMP517 Data Analysis/Notes/Week 03 - Exploratory Data Analysis|COMP517 Week 03 EDA]]
- Distributions and skew feed into [[MATH503 Mathematics/Notes/Week 06 - Binomial Distribution|Week 06 - Binomial Distribution]]
- Practice: [[MATH503 Mathematics/Notes/Week 05 - Practice Questions|Week 05 - Practice Questions]]
