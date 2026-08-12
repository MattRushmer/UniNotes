---
tags:
  - comp517
  - data-analysis
  - lab
  - python
  - numpy
  - pandas
---

# Lab 02 - Introduction to NumPy and pandas

> Auto-extracted from [[COMP517 Data Analysis/Labs/Lab 02 - Tasks.pdf|Lab 02 - Tasks.pdf]]

## NumPy library
- **NumPy** (Numerical Python): open-source, essential for numerical computing; supports large multi-dimensional arrays/matrices + high-level math functions
- Install via pip or brew; ships with Anaconda; import with alias `np` (community convention)

## NumPy arrays vs Python lists
- NumPy arrays are **homogeneous** (all elements same type: bool, int, float, long, double) - efficient memory storage and optimized math operations
- Python lists can hold mixed types but are less memory-efficient and slower for certain operations

## Creating arrays
- 1-D array (vector): `np.array([10, 20, 30, 40, 50])`
- 2-D array (matrix): `np.array([[10, 20, 30], [40, 50, 60]])` (outer brackets)
- Arrays of zeros or ones, identity matrices, random arrays, range arrays

## pandas DataFrames
- Introduced alongside NumPy; foundational for tabular data analysis (data loading, inspection, manipulation)
- Used with `df.head()` and `df.info()` to inspect rows and column data types (see [[COMP517 Data Analysis/Notes/Lab 04 - Univariate Visualisation|Lab 04]])

## Notes elsewhere in this vault
- Builds on [[COMP517 Data Analysis/Notes/Lab 01 - Basic Python Programming|Lab 01 - Basic Python Programming]]
- Data inspection/cleaning context: [[COMP517 Data Analysis/Notes/Week 03 - Exploratory Data Analysis|Week 03 - EDA]]
