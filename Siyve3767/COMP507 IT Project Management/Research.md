---
tags:
  - comp507
  - project-management
  - research
  - moc
---

# COMP507 IT Project Management — Research Hub

> Open questions, under-explored topics, and external leads found while reading the course notes. Everything here is **synthesis + external sources** — the course notes themselves were not edited.

## Table of contents
1. [[COMP507 IT Project Management/Research#1-pmbok-edition-which-one-does-this-course-follow|PMBOK edition — which one does this course follow?]]
2. [[COMP507 IT Project Management/Research#2-project-success-failure-statistics|Project success/failure statistics — do the numbers still hold?]]
3. [[COMP507 IT Project Management/Research#3-agile-vs-predictive-in-an-rd-project|Agile vs predictive — which does this course expect?]]
4. [[COMP507 IT Project Management/Research#4-evidence-of-roi-and-business-cases|Evidence of ROI and business cases]]
5. [[COMP507 IT Project Management/Research#5-the-t-skilled-generalist-debate|The "T-skilled generalist" debate]]
6. [[COMP507 IT Project Management/Research#6-stakeholder-register-in-practice|Stakeholder register in practice]]
7. [[COMP507 IT Project Management/Research#cross-course-connections|Cross-course connections]]

---

## 1. PMBOK edition — which one does this course follow?

### Summary
There is a real conflict in my notes: the course is described as **PMI/PMBOK-based** with the **10 knowledge areas + 5 process groups** (Week 01), the techbook is the **PMBOK Guide 6th ed.** (2017), yet Week 02 mentions a "PMBOK 8th ed flavour". The PMBOK 7th ed. (2021) replaced knowledge areas/process groups with **12 principles + 8 performance domains**, and an 8th edition is expected around 2026. **Open question: which edition (or hybrid) does the course and its assignments actually expect?** Worth checking with the lecturer before the exam.

### Links to existing notes
- [[COMP507 IT Project Management/Notes/Week 01 - Introduction to ITPM|Week 01 - Introduction to ITPM]] (10 knowledge areas, 5 process groups)
- [[COMP507 IT Project Management/Notes/Week 02 - PM Concepts, Phases and Lifecycle|Week 02 - PM Concepts, Phases and Lifecycle]] ("PMBOK 8th ed flavour", 12 principles)
- [[COMP507 IT Project Management/Techbook Summary.txt|Techbook Summary]] (PMBOK Guide 6th ed, Essential)

### External sources (not from my vault)
- **Project Management Academy: PMBOK 7 vs 6** — what changed structurally, and why 10 knowledge areas still matter for the PMP exam. https://projectmanagementacademy.net/resources/blog/pmbok-guide-7th-edition-vs-6th-edition/
- **The PM PrepCast: PMBOK knowledge areas & process groups** — the 6th-ed. framework in detail. https://www.project-management-prepcast.com/pmbok-knowledge-areas-and-pmi-process-groups
- **Career Sprints: PMBOK 7 vs 6** — rationale and community reaction. https://www.careersprints.com/post/key-differences-between-pmbok-7-vs-pmbok-6-a-thorough-guide

### Connections
- Knowledge areas are the frame for every week's note ([[COMP507 IT Project Management/Notes/Week 06 - Scope Management|scope]], [[COMP507 IT Project Management/Notes/09 - Cost Management|cost]], [[COMP507 IT Project Management/Notes/08 - Quality Management|quality]], [[COMP507 IT Project Management/Notes/12 - Resource Management|resource]], etc.) — the same 10 knowledge areas appear in [[COMP507 IT Project Management/Notes/Week 04 - Stakeholder Management|stakeholder management]] as the 10th KA.

---

## 2. Project success/failure statistics

### Summary
Week 02 cites **Standish CHAOS 2020** (31% cancelled, 35% challenged, 34% successful) and a **PwC** figure (only 2.5% of corporations consistently meet scope/time/cost). These numbers drive the "why PM matters" argument but are often quoted loosely — CHAOS's success definitions changed in 2015 (satisfaction/value-based), and newer reports show ~29-31% success with ~50% challenged and ~19% failed. **Open question: are the lecture's exact figures current, and what counts as "success" in the definition being used?**

### Links to existing notes
- [[COMP507 IT Project Management/Notes/Week 02 - PM Concepts, Phases and Lifecycle|Week 02 - PM Concepts, Phases and Lifecycle]] (CHAOS, PwC, Gartner figures)
- [[COMP507 IT Project Management/Notes/Week 01 - Introduction to ITPM|Week 01]] (why ITPM knowledge matters)

### External sources (not from my vault)
- **The Story: CHAOS Report analysis** — how Standish changed its success definition over time. https://thestory.is/en/journal/chaos-report/
- **OpenCommons: CHAOS report outcomes** — aggregated success/challenged/failed tables. https://opencommons.org/CHAOS_Report_on_IT_Project_Outcomes
- **McKinsey: Delivering large-scale IT projects** — 45% over budget, 7% over time, 56% less value. https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/delivering-large-scale-it-projects-on-time-on-budget-and-on-value
- **PwC: Transformation & project management survey** — the 2.5% and 40% KPI-failure figures. https://www.pwc.com/m1/en/publications/transformation-and-project-management-survey.html

### Connections
- Success criteria (scope/time/cost) connect to **EVM** in [[COMP507 IT Project Management/Notes/09 - Cost Management|Cost Management]] (#expected-value) and to the [[COMP504 Networks/Notes/Ch11 - Network Security|COMP504 security]] cost-of-breach argument.

---

## 3. Agile vs predictive — which does this course expect?

### Summary
Agile appears repeatedly in my notes — daily stand-ups (Communication), product backlog (Scope), "agile implementations advantage" (PwC research) — but there is **no dedicated agile lecture note**, and the course is otherwise PMI/predictive (phases, WBS, critical path). **Open question: how much agile is examinable, and how does it fit with the R&D project coursework?** The R&D project courses (COMP702/703) referenced in Week 01 may be where agile actually shows up.

### Links to existing notes
- [[COMP507 IT Project Management/Notes/Week 06 - Scope Management|Week 06 - Scope Management]] (product backlog, requirements)
- [[COMP507 IT Project Management/Notes/07 - Communication Management|07 - Communication Management]] (daily stand-ups, kanban)
- [[COMP507 IT Project Management/Notes/Week 01 - Introduction to ITPM|Week 01]] (R&D project courses COMP702/703)

### External sources (not from my vault)
- **PMI: Agile Practice Guide** — the official agile-vs-predictive framing. https://www.pmi.org/pmbok-guide-standards/practice-guides/agile
- **Scrum.org: Scrum Guide** — the reference for sprints/backlogs/stand-ups. https://scrumguides.org/

### Connections
- Kanban/backlog ideas overlap with **COMP517's data-analysis workflow** (iterative, exploratory) in [[COMP517 Data Analysis/Notes/Week 03 - Exploratory Data Analysis|COMP517 W03 EDA]] — both are iterative processes.

---

## 4. Evidence of ROI and business cases

### Summary
The Tutorial 03 note walks through **NPV, ROI, discount factors, and payback period** with a worked example (7% discount rate, 150k costs, 200k benefits), and the Northwest Airlines case study shows a business-side sponsor justifying a system on **direct sales savings (13% commissions + 18% overhead)**. What's under-explored: the **relationship between ROI/EMV and the cost-management EVM** from Week 09 — the notes treat them in separate lectures, but they're the same financial-thinking family.

### Links to existing notes
- [[COMP507 IT Project Management/Notes/Tutorial 03 - Business Case ROI Calculation|Tutorial 03 - Business Case ROI]]
- [[COMP507 IT Project Management/Notes/09 - Cost Management|09 - Cost Management]] (EVM, budgets)
- [[COMP507 IT Project Management/Notes/Northwest Airlines - Case Study|Northwest Airlines case study]] (business case in practice)

### External sources (not from my vault)
- **Wikipedia: Net present value** — the formula and why discounting matters. https://en.wikipedia.org/wiki/Net_present_value
- **Investopedia: Return on investment (ROI)** — standard definitions and limitations. https://www.investopedia.com/terms/r/returnoninvestment.asp

### Connections
- NPV/ROI connect to **statistical expected value** in [[MATH503 Mathematics/Notes/Week 06 - Binomial Distribution|MATH503 W06]] (#expected-value) — see [[COMP507 IT Project Management/Research#cross-course-connections|Cross-course connections]].

---

## 5. The "T-skilled generalist" debate

### Summary
Week 01 argues the industry is moving from specialists to **"T-skilled" generalists** — broad across many areas with depth in one — and the techbook includes an optional article **"Beyond the Generalist: Technical Expertise in ITPM"** (Thorpe & Krstić, 2025). The two seem to pull in different directions: the lecture celebrates the generalist trend while the article title suggests going *beyond* generalism. **Open question: does the article argue for or against the T-shaped model, and which view does the course endorse?**

### Links to existing notes
- [[COMP507 IT Project Management/Notes/Week 01 - Introduction to ITPM|Week 01 - Introduction to ITPM]] (T-skilled generalists, PM roles)
- [[COMP507 IT Project Management/Techbooks/Beyond the Generalist - Technical Expertise in ITPM.ris|Beyond the Generalist (Thorpe & Krstić, 2025)]] (Optional techbook article)
- [[COMP507 IT Project Management/Techbook Summary.txt|Techbook Summary]] (Essential/Optional flags)

### External sources (not from my vault)
- **The article itself (RIS citation only in my vault)** — worth reading in full; the RIS file holds metadata, not content. If you can get the PDF, this debate resolves itself.
- **PMI: Talent Triangle / PMP role shift** — PMI's official view on hybrid technical + leadership skills. https://www.pmi.org/certifications/certification-resources/what-is-the-pmp

### Connections
- The generalist-vs-specialist debate is a **career/industry theme** with no counterpart in other courses — a candidate for the vault-level Themes note (see proposal at the end).

---

## 6. Stakeholder register in practice

### Summary
Week 04 covers the **stakeholder register** (name, position, type, role, contact) and analysis (internal/external, critical stakeholders), and Week 07's communication plan builds directly on it for Assignment 1 Part 2. What's under-explored: **how to prioritise stakeholders** — the classic **power/interest grid** isn't in my notes, and the register template in the lecture is comprehensive but the *analysis method* is thinner.

### Links to existing notes
- [[COMP507 IT Project Management/Notes/Week 04 - Stakeholder Management|Week 04 - Stakeholder Management]] (register, analysis)
- [[COMP507 IT Project Management/Notes/07 - Communication Management|07 - Communication Management]] (stakeholder communications analysis → A1 Part 2)
- [[COMP507 IT Project Management/Notes/Northwest Airlines - Case Study|Northwest Airlines case study]] (top management as key stakeholder)

### External sources (not from my vault)
- **PMI: Stakeholder engagement** — power/interest grid and engagement levels (4th ed.-onward). https://www.pmi.org/learning/library/stakeholder-engagement-basics-10508
- **PM PrepCast: Stakeholder analysis** — power/interest, salience model. https://www.project-management-prepcast.com/pmbok-knowledge-areas-and-pmi-process-groups (Stakeholder Management section)

### Connections
- Stakeholder register/analysis directly supports **Assignment 1 Part 2** (per Week 07) — see also the **RACI** chart in [[COMP507 IT Project Management/Notes/12 - Resource Management|12 - Resource Management]].

---

## Cross-course connections

Topics here that also live in other courses' research hubs:
- **Statistics & quality (sampling, Six Sigma)** → shared with [[MATH503 Mathematics/Research#cross-course-connections|MATH503 Research]] and [[COMP517 Data Analysis/Research#cross-course-connections|COMP517 Research]] (COMP507 08 Quality uses Bernoulli/Binomial from MATH503 W06).
- **Risk & security** → shared with [[COMP504 Networks/Research#cross-course-connections|COMP504 Research]] (COMP507 W05 risk ↔ COMP504 Ch11 security, #risk, #terminology).
- **Expected value / EVM** → shared with [[MATH503 Mathematics/Research#cross-course-connections|MATH503 Research]] (mean = Np → EMV → EVM, #expected-value).
- **Binary & data representation** → see [[COMP504 Networks/Research#cross-course-connections|COMP504 Research]] and [[COMP517 Data Analysis/Research#cross-course-connections|COMP517 Research]].

Back to [[COMP507 IT Project Management/Research#table-of-contents|top]] · [[COMP507 IT Project Management/Index|Course index]]
