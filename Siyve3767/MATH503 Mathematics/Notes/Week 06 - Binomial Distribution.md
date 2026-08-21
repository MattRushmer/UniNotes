---
tags:
  - math503
  - mathematics
  - lecture
  - probability
  - distributions
  - expected-value
  - exam-topic
---

# Week 06 - Binomial Distribution (4.1)

> Auto-extracted from [[MATH503 Mathematics/Lectures/Week 06 - Lecture.pdf|Week 06 - Lecture.pdf]] (MATH503 Mathematics for Computing, 4.1)

## What it is
- A statistical tool to find the probability of the number of successes in a sequence of independent trials
- **BINS** conditions (must all be met):
  - **B**inary: trials have only 2 possible outcomes (success/failure, yes/no, true/false)
  - **I**ndependent: outcome of one trial has no effect on subsequent trials
  - **N**umber: fixed number of trials
  - **S**ame: probability of success/failure is fixed for all trials

## Key quantities
- N = number of trials; p = probability of success; q = 1 - p = probability of failure
- **Mean**: expected number of successes = Np — the same **expected value** logic drives [[COMP507 IT Project Management/Notes/Week 05 - Risk Management|COMP507 EMV]] and [[COMP507 IT Project Management/Notes/09 - Cost Management|COMP507 earned value]]
- **Variance**: Np(1-p) = Npq
- When N is very large, the Binomial is well approximated by the **Normal distribution** — see [[MATH503 Mathematics/Notes/Week 07 - Normal Distribution and Z-Scores|Week 07 - Normal Distribution and Z-Scores]]

## Bernoulli trials
- An experiment with only two possible outcomes labeled success (s) and failure (f)
- P(s) = p, P(f) = q = 1-p, and p + q = 1
- "Success" is context-dependent - defined by the person conducting the trial (e.g. a quality controller vs a factory owner may disagree)
- Examples: coin toss (p = 1/2); inspecting items (p = 1/10000)

## Binomial random variable
- X = number of successes in n identical Bernoulli trials; X is a **discrete random variable**
- Example: tossing a coin twice (n=2): sample space {HH, HT, TH, TT}; P(X=0)=1/4, P(X=1)=1/2, P(X=2)=1/4
- The binomial distribution is discrete - its probability mass function looks like a normal curve "with gaps"

## Notes elsewhere in this vault
- Builds on [[MATH503 Mathematics/Notes/Week 03 - Conditional Probability|Week 03 - Conditional Probability]] and [[MATH503 Mathematics/Notes/Week 04 - Permutations and Counting|Week 04 - Counting]]
- Bernoulli/Binomial sampling also mentioned in [[COMP507 IT Project Management/Notes/08 - Quality Management|COMP507 08 - Quality Management]] (statistical sampling)
