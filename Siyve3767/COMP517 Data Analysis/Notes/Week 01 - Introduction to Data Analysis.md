---
tags:
  - comp517
  - data-analysis
  - lecture
  - number-systems
  - exam-topic
---

# Week 01 - Why Data Matters (Introduction)

> Auto-extracted from [[COMP517 Data Analysis/Lectures/Week 01 - Introduction.pdf|Week 01 - Introduction.pdf]]

## Data, information, knowledge
- **Data** = "factual information (measurements or statistics) used as a basis for reasoning, discussion, or calculation" (Merriam-Webster); the key bit is *factual* - all data use depends on data being true and correct
- **Information** = data in context with meaning (e.g. $10 - USD, AUD or NZD?)
- **Knowledge** = understanding of meaning ($10 NZD is an expensive cup of coffee)
- Importance of data: provides information to support decision-making by identifying patterns and trends to drive innovation

## Why data analysis matters
- Better customer targeting - don't waste resources on uninterested demographics
- Know target customers better - spending habits, disposable income, areas of interest
- Better problem-solving - informed decisions are more likely to succeed
- Key principle: **if data cannot influence your decision or answer your question, using it is probably not worth it**

## Data analysis process (5 steps)
1. **Collecting data** - gather from several sources
2. **Preprocessing** - filter, clean, transform into required format
3. **Analyzing and finding insights** - explore, describe, visualize
4. **Insights interpretation** - understand impact of each variable
5. **Storytelling** - communicate results as a story a layman can understand

## Knowledge Discovery from Data (KDD)
- Objective: extract hidden interesting patterns from large databases, warehouses, repositories
- Steps: 1. Data Cleaning 2. Data Integration 3. Data Selection 4. Data Transformation 5. Data Mining 6. Pattern Evaluation 7. Knowledge Presentation

## Data Analysis vs Data Science
- **Data Science**: interdisciplinary; scientific approach to extract insights from structured AND unstructured data; develops models and prediction algorithms (stock price, weather, disease, fraud, recommendations)
- **Data Analysis**: subdomain of data science; explores data to discover patterns for business decisions (descriptive statistics, visualization, statistical analysis, reports)
- **Data scientists** focus on what *will happen*; **data analysts** focus on what *has happened*
- Analyst skillset: statistics, SQL, data visualization; Scientist skillset: + ML, NLP, deep learning

## Types of data analysis
- **Diagnostic**: "Why did this happen?" - identify patterns using statistical analysis
- **Predictive**: "What is most likely to happen?" - patterns in old data + current events; no 100% accuracy
- **Prescriptive**: recommends actions to achieve desired results; mixes insights + AI/ML algorithms
- **Quantitative**: raw data processed into numerical data - hypothesis testing, mean/average

## Computers and data scale
- Computers store data as binary states (1/0): high/low voltage, off/on, frequencies, magnetic polarity — binary in depth: [[COMP504 Networks/Notes/Number Systems|COMP504 Number Systems]]
- bit = 1 or 0; byte = 8 bits; kB, MB, GB, TB, PB, EB, ZB, YB (powers of 1000)
- ~2.5 quintillion bytes created daily; big data analytics needed to make it useful
- Cost: carbon emissions; in some cases 80% of data is duplicated
- Data flows: Netflix ~1GB/hour; Facebook ~4 PB/day; SKA ~8 TB/second processed

## Data journalism and statistics examples
- Data journalism: using data to uncover/report news stories (DW, GIJN)
- COVID vaccine effectiveness example: comparing infection counts in vaccinated vs unvaccinated groups

## Course context
- Textbook: *Python Data Analysis* (Navlani et al., 2021) + *Python for Data Analysis* (McKinney, 2018) + Foundations of Data Science (Adhikari & DeNero)
- Course topics: data loading/file formats, EDA (see [[COMP517 Data Analysis/Notes/Week 03 - Exploratory Data Analysis|Week 03 - EDA]]), data cleaning, aggregation & correlation, visualization (see [[COMP517 Data Analysis/Notes/Lab 04 - Univariate Visualisation|Lab 04]]), time series, hypothesis testing, ANOVA, linear regression
