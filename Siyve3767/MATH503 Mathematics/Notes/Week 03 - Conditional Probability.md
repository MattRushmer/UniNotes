---
tags:
  - math503
  - mathematics
  - lecture
  - probability
  - exam-topic
---

# Week 03 - Conditional Probability

> Auto-extracted from [[MATH503 Mathematics/Lectures/Week 03 - Lecture.pdf|Week 03 - Lecture.pdf]] (MATH503 Mathematics for Computing, 1.5)

## Why it matters
- Conditional probability helps data scientists get better results from a given data set; helps machine learning engineers build more accurate prediction models

## The idea
- The probability of an event can change given extra information
- Example: probability of selling a TV on a normal day = 30% vs given that it is a public holiday = 70%
  - P(TV | R) = 30% (random day) vs P(TV | H) = 70% (public holiday)

## Formula
- Conditional probability of event E given event F:
  - **P(E|F) = P(E ∩ F) / P(F)**, where P(F) ≠ 0
- Worked example: 200 students, 80 female, 140 study astronomy (40 female) - use Venn diagram and contingency table; find P(A), P(A|F)

## Related concepts
- Independent events
- Product rule of probability (and tree diagrams)
- Product rule for independent events
- **Monty Hall problem**

## Notes elsewhere in this vault
- Probability foundations lead to [[MATH503 Mathematics/Notes/Week 06 - Binomial Distribution|Week 06 - Binomial Distribution]] and [[MATH503 Mathematics/Notes/Week 04 - Permutations and Counting|Week 04 - Counting]]
- Distributions/sampling also appear in [[COMP517 Data Analysis/Notes/Week 03 - Exploratory Data Analysis|COMP517 Week 03 EDA]]
