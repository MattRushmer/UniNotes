---
tags:
  - comp507
  - project-management
  - lecture
  - schedule
  - critical-path
  - exam-topic
---

# Week 06 - Schedule Management

> Auto-extracted from [[COMP507 IT Project Management/Lectures/Week 06 - Schedule Management.pptx|Week 06 - Schedule Management.pptx]] — Daniel Vaipulu

## Schedule management processes
1. **Plan schedule management** → schedule management plan (WBS model, methodology, accuracy/units, control thresholds, performance measurement rules, baseline, reporting)
2. **Define activities** (from the **WBS**) — an activity/task (work package) has expected duration, cost, resource requirements
3. **Sequence activities** — identify relationships (predecessors, successors, leads/lags)
4. **Estimate activity resources & durations**
5. **Develop the schedule**
6. **Control the schedule** — critical path, milestone reports, progress reports, schedule change control, tracking Gantt, variance analysis, **Earned Value Analysis (EVA)**

## WBS → activities → work packages
- WBS breaks project work into phases → tasks → sub-tasks; the bottom-level **work package** has its own duration, cost, resources
- Parent task duration/cost = sum of its sub-tasks; a predecessor task must finish before successors start

## Milestones & dependencies
- **Milestone** = significant event with zero duration (often a KPI)
- Dependencies: **mandatory** (hard logic, inherent) · **discretionary** (soft logic, team-defined) · **external** (non-project activities)

## Network diagrams
- Show activity sequencing: **Activity-on-Arrow (AoA/ADM)** — arrows = activities, only finish-to-start · **Precedence Diagram Method (PDM)** — boxes = activities, shows all dependency types, used by PM software
- Bursts (one node → many activities) and merges (many → one)

## Estimates & PERT
- **Three-point estimate**: optimistic, most likely, pessimistic
- **PERT weighted average** = (optimistic + 4 × most likely + pessimistic) / 6 — used when duration estimates are highly uncertain

## Gantt charts
- Standard format for displaying schedule: activities + start/finish dates; symbols — black diamond (milestone), thick bars (summary tasks), lighter bars (task durations), arrows (dependencies); **tracking Gantt** shows progress vs baseline

## Critical path method (CPM)
- **Critical path** = the longest path through the network diagram; determines the earliest project completion; has the least **slack/float**
- **Free float** = delay without delaying the next activity's start · **Total float** = delay without delaying project finish
- **Forward pass** → early start/finish · **Backward pass** → late start/finish
- More than one critical path possible; critical path can change as the project progresses
- If a critical-path activity slips: overtime, more staff, outsourcing, pulling resources, or cutting quality/scope

## Related
- [[COMP507 IT Project Management/Notes/Week 06 - Scope Management|Week 06 - Scope]] (WBS) · [[COMP507 IT Project Management/Notes/09 - Cost Management|Cost]] (EVM) · [[COMP507 IT Project Management/Notes/Week 01 - Introduction to ITPM|Week 01]] (A1 Part 2: schedule, network diagram, critical path) · [[COMP507 IT Project Management/Index|Course index]]
