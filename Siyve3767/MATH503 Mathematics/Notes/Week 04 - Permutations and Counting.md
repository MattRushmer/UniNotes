---
tags:
  - math503
  - mathematics
  - lecture
  - combinatorics
  - permutations
  - number-systems
  - exam-topic
---

# Week 04 - Permutations and Counting (2.1)

> Auto-extracted from [[MATH503 Mathematics/Lectures/Week 04 - Lecture.pdf|Week 04 - Lecture.pdf]] (MATH503 Mathematics for Computing, 2.1)

## Probability and counting
- With equally likely outcomes: **P(E) = n(E) / n(S)**
- When n(S) is large you cannot list all outcomes - **counting principles** are needed to find n(S) and n(E)

## The multiplication principle
- To find the number of choices/arrangements of different types of items: **multiply**
- Choose A things *and* B things *and* C things -> multiply; choose A *or* B *or* C -> add
- Probability trees: multiply across branches
- Examples: combination lock with 3 letters (with/without repetition); computer word of 8 bits -> 2^8 = 256 possible words (8-bit words = the binary of [[COMP504 Networks/Notes/Number Systems|COMP504 Number Systems]]; block math used in [[COMP504 Networks/Notes/VLSM Subnetting - Block Method|COMP504 VLSM]])

## Factorial notation
- **n! = n x (n-1) x (n-2) x ... x 3 x 2 x 1**, and **0! = 1**
- Simplification practice: 6!/3!, 6!/(2!3!), n!/(n-2)!, (n-2)!/(n-1)!, n(n-1)!, n! - (n-1)!
- Factorials in R: `factorial(5)`; use logs/stirling approximations for very large factorials

## Notes elsewhere in this vault
- Counting feeds into probability in [[MATH503 Mathematics/Notes/Week 03 - Conditional Probability|Week 03 - Conditional Probability]] and [[MATH503 Mathematics/Notes/Week 06 - Binomial Distribution|Week 06 - Binomial Distribution]] (nCr selections)
