---
tags:
  - math503
  - mathematics
  - lecture
  - matrices
  - linear-algebra
  - exam-topic
---

# Week 10 - Matrices (6.1-6.3)

> Auto-extracted from [[MATH503 Mathematics/Lectures/Week 10 - Lecture.pdf|Week 10 - Lecture.pdf]] (MATH503 Manual, Ch 6) + [[MATH503 Mathematics/Lectures/Week 10 - Important Information.pdf|Week 10 - Important Information.pdf]]

## Housekeeping
- Myimaths: catch up if behind · Portfolio: two more activities in Weeks 10 and 11, check grades on Canvas
- Exam info page linked on Canvas (ECMS examinations) — more details "next week"
- Prereading for Week 11: Tan *Finite Mathematics* Section 9.1 (p498-503), via AUT library online

## Why matrices (in computer science)
- Projection of 3D images onto a 2D screen · encryption of message codes · page rank algorithms in search engines · recording data

## 6.1 Matrix definition and operations
- A **matrix** is a rectangular array of values with **dimension/order m × n** (m rows, n columns — rows specified first)
- **Square matrix**: m = n · **row matrix**: m = 1 · **column matrix**: n = 1
- Notation: a general m×n matrix A is written with entries aᵢⱼ
- **Equal matrices**: same dimension AND same corresponding entries
- **Special matrices**: **zero matrix** (all 0s) · **diagonal matrix** (nonzero only on the diagonal) · **identity matrix Iₙ** (1s on the diagonal, 0s elsewhere)
- **Transpose (Aᵀ)**: interchange rows and columns — the i,j-entry of A becomes the j,i-entry of Aᵀ
- **Matrix addition**: add corresponding entries (same dimensions required)
- **Scalar multiplication**: multiply every entry by the scalar
- **Matrix multiplication**: A (m×n) × B (n×p) → AB is m×p; entry cᵢⱼ = row i of A · column j of B (dot product); **AB ≠ BA in general** (non-commutative) — check dimensions line up (inner dimensions must match) before a product is even possible

## 6.2 Inverse of a matrix
- Square n×n matrix A has an inverse B (written A⁻¹) if **AB = BA = Iₙ**
- For a 2×2 matrix A = [[a₁₁,a₁₂],[a₂₁,a₂₂]]: first compute the **determinant** det(A) = a₁₁a₂₂ − a₁₂a₂₁
- **A⁻¹ = (1/det(A)) × [[a₂₂,−a₁₂],[−a₂₁,a₁₁]]** — swap the diagonal entries, negate the off-diagonal entries, divide by the determinant
- If det(A) = 0, the matrix has **no inverse** (singular)

## 6.3 Transformations with matrices
- A point (x,y) is represented as a column matrix; multiplying by a **transformation matrix T** moves the point: TP = new position
- A whole shape (multiple vertices) transforms by multiplying the transformation matrix by a matrix of all the vertices' coordinates at once
- **Reflection matrices**: `[[-1,0],[0,1]]` reflects in the y-axis (x=0) · `[[1,0],[0,-1]]` reflects in the x-axis (y=0) · `[[0,1],[1,0]]` reflects in y=x · `[[0,-1],[-1,0]]` reflects in y=-x
- **Rotation matrices** (about the origin): `[[0,1],[-1,0]]` = 90° clockwise · `[[0,-1],[1,0]]` = 90° anticlockwise · `[[-1,0],[0,-1]]` = 180°
- **Enlargement**: `[[k,0],[0,k]]` scales by factor k in both directions · **stretch**: `[[k,0],[0,1]]` stretches only in x (or `[[1,0],[0,k]]` only in y)
- **Shear**: `[[1,k],[0,1]]` shears in the x-direction by factor k (or `[[1,0],[k,1]]` in y)
- **Inverse of a transformation (T⁻¹)** undoes the effect of T
- **det(T)** tells you the area scale factor: Area of image = |det(T)| × Area of original; a **negative determinant means the transformation includes a reflection** (orientation flips)

## Related
- [[MATH503 Mathematics/Notes/Week 04 - Permutations and Counting|Week 04 - Permutations and Counting]] (prior algebra/notation foundations)
- [[MATH503 Mathematics/Course Overview|Course Overview]] — Weeks 10-11 = Matrices per the schedule
- [[MATH503 Mathematics/Index|Course index]] · [[MATH503 Mathematics/Research|Research Hub]]
