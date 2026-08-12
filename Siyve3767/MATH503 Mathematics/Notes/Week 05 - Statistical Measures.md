---
tags:
  - math503
  - mathematics
  - lecture
  - statistics
  - sampling
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
- The mean is **sensitive to outliers and skew** - example: staff salaries 45k-56k with two outliers 120k and 135k -> mean $63k misleads; **median is better** for skewed data (same point in [[COMP517 Data Analysis/Notes/Week 03 - Exploratory Data Analysis|COMP517 W03]])

## Population vs sample
- **Population**: the complete set (e.g. all 249 MATH503 students S1 2026)
- **Sample**: a representative subset (e.g. randomly selected 30 students)
- We infer population behaviour from the sample - must choose samples carefully (sampling bias can go wrong!) - sampling theory is also used for [[COMP507 IT Project Management/Notes/08 - Quality Management|COMP507 quality control]] and [[COMP517 Data Analysis/Notes/Week 03 - Exploratory Data Analysis|COMP517 data profiling]]
- Population mean is mu; sample mean is x-bar

## The median
- The middle score of data arranged in order of magnitude
- Interpretation: 50% of values are below the median
- Even number of values: average of the two middle values

## Notes elsewhere in this vault
- Mean/median/percentiles also covered in [[COMP517 Data Analysis/Notes/Week 03 - Exploratory Data Analysis|COMP517 Week 03 EDA]]
- Distributions and skew feed into [[MATH503 Mathematics/Notes/Week 06 - Binomial Distribution|Week 06 - Binomial Distribution]]
