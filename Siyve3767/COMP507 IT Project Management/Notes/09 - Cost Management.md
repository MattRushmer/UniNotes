---
tags:
  - comp507
  - project-management
  - lecture
  - cost
  - evm
  - expected-value
  - exam-topic
---

# 09 - Cost Management

> Auto-extracted from [[COMP507 IT Project Management/Lectures/09 - Cost Management.pptx|09 - Cost Management.pptx]]
> Source text: *Information Technology Project Management* (Schwalbe, 2019), Chapter 7

## What is cost?
- **Cost** = a resource sacrificed or foregone to achieve a specific objective; usually measured in monetary units
- **Project cost management** = processes to ensure the project is completed within an **approved budget**

## Cost management processes (5)
1. **Plan cost management** - organizational policies, procedures, documentation
2. **Estimate costs** (business/portfolio level) - approximation of resources needed
3. **Determine the budget** (project level) - allocate the estimate to work items to establish a **baseline**
4. **Execute the budget**
5. **Control costs** - controlling changes to the project budget

## Basic cost concepts
- **Profits** = revenues minus expenditures . **Profit margin** = profits/revenues
- **Life cycle costing** = total cost of ownership (development + support costs)
- **Cash flow analysis** - estimated annual costs/benefits and resulting cash flow
- Cost/benefit types: **tangible vs intangible** . **direct vs indirect** . **sunk cost** (ignore when deciding what to invest in)
- **Learning curve theory** - unit cost decreases as more units are produced
- **Reserves**: **contingency reserves** (known/predictable unknowns, part of the cost baseline) vs **management reserves** (unknown/unpredictable unknowns)

## Cost management plan contents
- Level of accuracy . units of measure (man-hour? man-day? FTE?) . organizational procedure links . **control thresholds** (e.g. 10% variation from baseline) . performance measurement rules (CPI, SPI) . reporting formats . process descriptions

## Estimating costs
- **Analogous / top-down** (cost of a previous similar project) . **Bottom-up** (sum individual work items) . **Three-point** (most likely, optimistic, pessimistic) . **Parametric** (mathematical model from project parameters)
- Typical problems: estimates done too quickly, lack of experience, bias toward underestimation, management desires accuracy
- Before estimating: gather info, ask how the estimate will be used, clarify ground rules and assumptions

## Budget and baseline
- Allocate the cost estimate to individual work items **over time**, based on activities in the **WBS** (see [[COMP507 IT Project Management/Notes/Week 06 - Scope Management|Week 06 - Scope Management]])
- Produce a **cost baseline**: time-phased budget used to measure and monitor cost performance

## Earned Value Management (EVM)
- Performance measurement technique integrating **scope, time, and cost** data against a baseline (original plan + approved changes)
- Three values per activity (from the WBS): **Planned Value (PV)** . **Actual Cost (AC)** . **Earned Value (EV)** (EV = PV x rate of performance) — "earned" = expected value of completed work ([[MATH503 Mathematics/Notes/Week 06 - Binomial Distribution|MATH503 W06]])

### EVM formulas
| Term | Formula | Interpretation |
|---|---|---|
| Cost variance (CV) | CV = EV - AC | < 0 = over budget |
| Schedule variance (SV) | SV = EV - PV | < 0 = behind schedule |
| Cost performance index (CPI) | CPI = EV/AC | < 100% = over budget |
| Schedule performance index (SPI) | SPI = EV/PV | < 100% = behind schedule |
| Estimate at completion (EAC) | EAC = BAC/CPI | forecast final cost |
| Estimate to complete (ETC) | ETC = EAC - AC | remaining cost to finish |
| Budget at completion (BAC) | original total budget | - |

### Worked example (web server, $10k, 1 week)
- PV = $10,000 . 50% done at week 1 -> EV = $5,000 . AC = $15,000
- CV = -$10,000 (over) . SV = -$5,000 (behind) . CPI = 33% . SPI = 50%
- EAC = BAC/CPI: e.g. $100k budget with CPI 81.76% -> EAC = $122,308; completion 12 months / SPI 94.2% -> ~13 months
- EVM used worldwide (esp. Middle East, South Asia, Canada, Europe); often required for defence/government projects

## Notes elsewhere in this vault
- EVM links to [[COMP507 IT Project Management/Notes/Week 06 - Schedule Management|Week 06 - Schedule Management]] (schedule baseline, SPI)
- ROI/business case context in [[COMP507 IT Project Management/Notes/Tutorial 03 - Business Case ROI Calculation|Tutorial 03 - Business Case ROI Calculation]]
- Homework: Chapter 11 Risk Management -> [[COMP507 IT Project Management/Notes/Week 05 - Risk Management|Week 05 - Risk Management]]
