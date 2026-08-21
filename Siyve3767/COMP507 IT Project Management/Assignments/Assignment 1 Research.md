---
tags:
  - comp507
  - project-management
  - assignment
  - research
  - exam-topic
---
								
# COMP507 Assignment 1 — Research

> Research companion for **Assignment 1 (Team Wiki Project)**, S2 2026 — worth **50%** of the final grade. Source brief: [[COMP507 IT Project Management/Assignments/Assignment 1/Assignment 1_S2_2026.pdf|Assignment 1_S2_2026.pdf]]. Everything in this note is **synthesis + external sources** — your submitted documents are your own work.

## The assignment in one paragraph
Your team plans a **Wiki** that reviews and compares **two cloud-based (SaaS) project management software (PMS)** so ECMS can help R&D students pick one. ECMS will save ~$1.2M/year over 3 years by switching from upfront licenses to a $15/user/year subscription (up to 350 Sem1 + 150 Sem2 students/year, i.e. up to 500 users/year). Budget: $200,000. The wiki must compare at least one feature per PMBOK process group (Initiating, Planning, Executing, Monitoring/Controlling, Closing). **Microsoft Project is excluded** (though you may investigate MS Project 2021's features to help decide what to compare). Max 4,500 words. Both parts are submitted as one team document each, on Canvas. Team size = **4 students** (self-organised; TAs have final say on numbers/members).

### ✅ Verified against the brief PDF (`Assignment 1_S2_2026.pdf`) — full scenario numbers
- **PMS usage fee**: $15.00/user/year
- **Enrolment**: up to 350 students Sem 1 + 150 Sem 2, per academic year through 2027
- **Internet charge**: $6/student/month in 2025, **rising 10% per year through 2027** — this is a real cost line that belongs in the business case's cost side; it's easy to miss because it's buried in the scenario paragraph, not the checklist
- **Budget allocated**: $200,000 for the Wiki project itself
- **Expected savings**: ~$1,200,000/year for 3 years (from dropping upfront PMS licenses in favour of SaaS)
- **Existing IT infrastructure** for hosting the Wiki + accessing the PMS in labs is stated as **already sufficient** (no extra infrastructure cost to model)
- **⚠️ Scenario date inconsistency**: the brief's fictional project timeline (planning starts 1 Aug 2025, implementation done 30 Dec 2025, Wiki live 1 Feb 2026 for "Semester 1, 2026") doesn't match the real S2 2026 assignment dates (Part 1 due 23 Aug 2026, Part 2 due 20 Sep 2026) — this looks like a template carried over from a prior year's offering without updating the scenario dates. **Worth asking the lecturer which year to anchor the NPV/financial-year calculations to** (the scenario's 2025/2026/2027, or shifted one year to 2026/2027/2028) before finalising the business case financials.

## Deadlines
- **Part 1 — Sun 23 Aug, 11:30pm** (items 1–11): Business case (25), Stakeholder register (5), Stakeholder management strategy (10), Project charter incl. roles & Team Leader (20), Team contract (10), Kick-off meeting agenda + minutes (5), Client meeting agenda + minutes (5), Team meeting agenda + minutes (5), Risk register v1 (5), Issue register v1 (5), Milestone report v1 (5)
- **Part 2 — Sun 20 Sep, 11:30pm** (items 12–20, ✅ verified against the brief PDF): Communications management plan (10), Change management plan (10), Scope statement (15), WBS (20), Project schedule — baseline + network diagram + critical path analysis (20), Risk register v2 (5), Issue register v2 (5), Milestone report v2 (5), Lessons-learned report (10)
- Peer rating form + group rating form must accompany each part.

## Research: cloud-based PMS candidates

### Candidates (Microsoft Project excluded)
| Tool | Free tier | Entry paid | Mid/Pro | Notes |
|---|---|---|---|---|
| **Asana** | Free (2 users) | Starter ~$10.99/user/mo | Advanced ~$24.99 | Task-centric, timelines (Gantt), portfolios, forms |
| **Trello** | Free (10 boards) | Standard ~$5 | Premium ~$10 | Kanban-first, simplest to learn |
| **Jira** | Free (10 users) | Standard ~$7.91 | Premium ~$14.54 | Software/agile focused, sprint reports |
| **ClickUp** | Free forever | Unlimited ~$7 | Business ~$12 | Most features per dollar, docs built in |
| **Monday.com** | Free (2 seats) | Basic ~$9 | Standard ~$12 / Pro ~$19 | Visual boards, automations |
| **Wrike** | Free | Team ~$10 | Business ~$25 | Timelines, workload views |
| **Zoho Projects** | Free (5 users) | Premium ~$4–5 | Enterprise ~$9–10 | **Built-in Earned Value Management (EVM)** |
| **Smartsheet** | 14-day trial | Pro ~$9–12 | Business ~$19–24 | Spreadsheet-centric, strong for PMO/EVM, formulas |

*External pricing, verify current figures: asana.com/pricing, atlassian.com/software/jira/pricing, monday.com/pricing, clickup.com/pricing, zoho.com/projects, wrike.com/price, smartsheet.com/pricing*

### Feature mapping to the 5 PMBOK process groups
- **Initiating** — project charters, intake forms, stakeholder mapping: Asana Forms/Portfolios, Monday.com, ClickUp Forms
- **Planning** — WBS, scheduling, Gantt, resources, budgets: Smartsheet Gantt + formulas, Wrike timelines, ClickUp milestones/dependencies, Asana Timeline
- **Executing** — task assignment, collaboration, docs, communication: all tools (Kanban, comments, attachments)
- **Monitoring/Controlling** — EVM, time tracking, dashboards, automation: **Zoho Projects (built-in EVM)**, Smartsheet formulas/activity logs, Asana/Monday/ClickUp dashboards
- **Closing** — sign-off, archiving, final reports: Jira sprint closure reports, Zoho status locking, Smartsheet exports

### Two strong candidates to compare (suggestion)
**Asana vs Smartsheet** — clean, defensible contrast:
- Asana = task-centric, modern UX, adoption-friendly; Smartsheet = spreadsheet-centric, formula-driven, EVM/PMO strength
- For R&D student teams doing industry projects, the deciding criteria could be: cost per student, learning curve, EVM/reporting support, and how each covers all 5 process groups
- **Tip:** your wiki criteria section must state *why* you picked your two tools — make the criteria explicit (cost, process-group coverage, usability, support) and reuse them in the comparison table.

## Links to your existing notes
- [[COMP507 IT Project Management/Notes/Week 01 - Introduction to ITPM|Week 01 - Intro to ITPM]] — PM framework (PMI/PMBOK) the assignment references
- [[COMP507 IT Project Management/Notes/Week 02 - PM Concepts, Phases and Lifecycle|Week 02 - Phases & Lifecycle]] — Initiating → Closing context
- [[COMP507 IT Project Management/Notes/Week 04 - Stakeholder Management|Week 04 - Stakeholder Management]] — stakeholder register + management strategy (items 2–3)
- [[COMP507 IT Project Management/Notes/Week 05 - Risk Management|Week 05 - Risk Management]] — risk register v1/v2 (items 9, 17)
- [[COMP507 IT Project Management/Notes/Week 06 - Scope Management|Week 06 - Scope Management]] — scope statement + WBS (items 14–15)
- [[COMP507 IT Project Management/Notes/Week 06 - Schedule Management|Week 06 - Schedule Management]] — schedule baseline, network diagram, critical path (item 16)
- [[COMP507 IT Project Management/Notes/07 - Communication Management|07 - Communications Management]] — communications plan (item 12)
- [[COMP507 IT Project Management/Notes/08 - Quality Management|08 - Quality Management]] — the quality goals your scope statement must state
- [[COMP507 IT Project Management/Notes/09 - Cost Management|09 - Cost Management]] — business case financials, EVM
- [[COMP507 IT Project Management/Notes/12 - Resource Management|12 - Resource Management]] — team contract, roles, resource planning
- [[COMP507 IT Project Management/Notes/Tutorial 03 - Business Case ROI Calculation|Tutorial 03 - Business Case ROI]] — NPV/ROI/payback methods for the business case (item 1)
- [[COMP507 IT Project Management/Notes/Northwest Airlines - Case Study|Northwest Airlines Case Study]] — worked example of business-side project justification
- [[COMP507 IT Project Management/Research|COMP507 Research Hub]]

## External sources (not from your vault)
- **PMI PMBOK Guide** — the process-group framework the assignment is built on. https://www.pmi.org/pmbok-guide-standards/foundational/pmbok
- **Asana Pricing** — https://asana.com/pricing
- **Jira Pricing** — https://www.atlassian.com/software/jira/pricing
- **Monday.com Pricing** — https://monday.com/pricing
- **ClickUp Pricing** — https://clickup.com/pricing
- **Zoho Projects Pricing** — https://www.zoho.com/projects/zohoprojects-pricing.html
- **Wrike Pricing** — https://www.wrike.com/price/
- **Smartsheet Pricing** — https://www.smartsheet.com/pricing

## ⚠️ Flags & to-dos
1. **Business case is done.** `Templates/1. business case.doc` now has all 10 sections + Exhibit A financial analysis. The stale `Business Case.odt` (only ever had the pasted brief text) has been deleted. One cleanup item remains: Section 8 still has meta-references ("per the brief's stated timeline", "confirm with the lecturer") that should be reworded before submission — see [[COMP507 IT Project Management/Assignments/Assignment 1/Assignment 1 Checklist|checklist]] item 1.
2. **Pricing changes over time** — re-verify any per-user figures before submitting; cite the date you checked.
3. **Word limit 4,500** — the wiki content (both PMS) must fit; plan the comparison tables to be information-dense, not wordy.
4. Verify with your lecturer whether the $15/user/year fee and the 350/150 enrolment figures should appear in your business case calculations (they're given in the brief).
