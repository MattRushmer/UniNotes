---
tags:
  - math503
  - mathematics
  - lecture
  - statistics
  - practice
  - exam-topic
---

# Week 05 - Practice Questions (Statistical Measures)

> Practice for [[MATH503 Mathematics/Notes/Week 05 - Statistical Measures|Week 05 - Statistical Measures]] (Manual Ch 3, Sections 3.1-3.2). Worked answers at the bottom.

## 1. Mean of running times
An algorithm's running times (seconds) are:
`4.3, 4.2, 4.7, 4.3, 4.1, 4.2, 4.3, 4.25, 4.2, 4.4`
Calculate the mean (give 2 significant figures).

## 2. Median (odd vs even count)
Find the median of:
- (a) `3, 4, 6, 8, 11` (seconds)
- (b) `2, 3, 4, 5, 7, 9` (seconds)

## 3. Mean vs median under skew
Salaries (thousands): `45, 48, 56, 54, 55, 55, 46, 32, 47, 120, 135`
Find the mean and the median. Which better represents the "typical" salary, and why?

## 4. Range, quartiles and IQR
Marks: `24, 31, 58, 55, 60, 63, 54, 45, 36, 28, 32`
Find: range, median (Q2), Q1, Q3, and the interquartile range.

## 5. Outlier test
Using the marks data from Q4 (Q1 = 31, Q3 = 58), decide whether a mark of **120** would be flagged as an outlier.

## 6. Interpreting quartiles
For the marks data from Q4, write an interpretation sentence for each of Q1, Q2 and Q3.

## 7. R / RStudio
Write the R code to:
- (a) Store the values `2, 3, 3, 4, 5, 6, 7, 8` in a variable called `data`.
- (b) Compute its mean and median.

---

## Answers

**1.** Sum = 42.95, n = 10, so mean = 42.95 / 10 = **4.295 ≈ 4.3 s** (2 s.f.).

**2.**
- (a) Ordered already: middle value is 6 → median = **6 s** (50% below 6 s).
- (b) Middle lies between 4 and 5 → median = (4 + 5) / 2 = **4.5 s**.

**3.** Sum = 693, n = 11 → mean = 693 / 11 = **63k**. Ordered: `32, 45, 46, 47, 48, 54, 55, 55, 56, 120, 135` → median = **54k**.
The **median (54k)** is better: the two large salaries (120k, 135k) skew the mean up to 63k, which misrepresents most workers (45k–56k range).

**4.** Sorted: `24, 28, 31, 32, 36, 45, 54, 55, 58, 60, 63` (n = 11).
- Range = 63 − 24 = **39**
- Q2 (median) = 6th value = **45**
- Q1 = median of lower half `24, 28, 31, 32, 36` = **31**
- Q3 = median of upper half `54, 55, 58, 60, 63` = **58**
- IQR = 58 − 31 = **27**

**5.** IQR = 27. Upper fence = Q3 + 1.5 × IQR = 58 + 40.5 = **98.5**. Since 120 > 98.5, it **would be flagged as an outlier**. (Lower fence = 31 − 40.5 = −9.5, so nothing below is possible here.)

**6.**
- Q1 = 31 → "25% of students got a mark of 31 or lower" (or "75% got 31 or higher").
- Q2 = 45 → "50% of students got a mark of 45 or lower".
- Q3 = 58 → "75% of students got a mark of 58 or lower" (or "25% got 58 or higher").

**7.**
```r
data <- c(2, 3, 3, 4, 5, 6, 7, 8)  # (a) define the vector
mean(data)                          # (b) mean
median(data)                        # (b) median
```
