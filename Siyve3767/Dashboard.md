---
tags:
  - dashboard
  - moc
  - vault-home
---

# 🧭 Dashboard

> Requires the **Dataview** community plugin (already installed in `.obsidian/plugins/dataview` — if you see raw code blocks below instead of a table/checklist, go to **Settings → Community plugins** and turn it on, then make sure "Dataview" is toggled on in the list).
>
> Live: the box grid and checklists below recompute every time you open this note — no manual refreshing needed. Click a course name to expand its full weekly summary and task list. Tick a checkbox to mark it done — it writes straight back to that course's `Index.md`.

## Courses — live status

```dataviewjs
const courses = [
  {name: "COMP504 — Networks", path: "COMP504 Networks/Index", emoji: "🌐"},
  {name: "COMP507 — IT Project Management", path: "COMP507 IT Project Management/Index", emoji: "📊"},
  {name: "COMP517 — Data Analysis", path: "COMP517 Data Analysis/Index", emoji: "📈"},
  {name: "MATH503 — Mathematics", path: "MATH503 Mathematics/Index", emoji: "🔢"}
];

const today = dv.date("today");
let rows = [];

for (const c of courses) {
  const page = dv.page(c.path);
  if (!page) {
    rows.push([`${c.emoji} ${c.name}`, "⚠️ page not found"]);
    continue;
  }

  const openDated = page.file.tasks.where(t => !t.completed && t.due);
  const sorted = Array.from(openDated).sort((a, b) => a.due - b.due);

  let status;
  if (sorted.length === 0) {
    status = "✅ Nothing with a known due date outstanding";
  } else {
    const next = sorted[0];
    const label = next.text.replace(/\[\w+::[^\]]+\]/g, "").trim();
    const days = Math.ceil(next.due.diff(today, "days").days);
    let icon = "🟢";
    if (days <= 3) icon = "🔴";
    else if (days <= 7) icon = "🟠";
    const dayText = days < 0 ? `**OVERDUE by ${-days}d**` : (days === 0 ? "**due today**" : `**${days}d left**`);
    status = `${icon} ${label} — ${dayText}`;
  }

  rows.push([`[[${c.path}|${c.emoji} ${c.name}]]`, status]);
}

dv.table(["Course", "Next due"], rows);
```

---

## 🌐 COMP504 Networks

> [!info]- Click to expand: tasks + weekly summary
> **Tasks** — check off as labs are completed
> ```dataview
> TASK
> FROM "COMP504 Networks"
> WHERE !completed
> SORT due ASC
> ```
>
> **Weekly summary** *(week numbers per the [[COMP504 Networks/Notes/FINAL EXAM Revision (2026)|Final Exam Revision]] deck's own chapter-weighting table — chapters run somewhat out of numeric order, so treat as approximate)*
>
> | Week(s) | Topic | Note |
> |---|---|---|
> | W1 | Intro to data communications, OSI/TCP-IP layers | [[COMP504 Networks/Notes/Ch01 - Introduction\|Ch01]] |
> | W3 | Data link layer, error detection · **lab**: switch config | [[COMP504 Networks/Labs/Lab Submissions/Done/Week 3/Lab Notes - Week 3\|Lab 3]] |
> | W4–5 | Network & Transport layers, IPv4, UDP/TCP · **lab**: OSI/TCP-IP investigation | [[COMP504 Networks/Notes/Ch05 - Transport Layer Part 1\|Ch05 P1]] · [[COMP504 Networks/Notes/Ch05 - Transport Layer Part 2\|Ch05 P2]] · [[COMP504 Networks/Labs/Lab Submissions/Done/Week 4/Lab Notes - Week 4\|Lab 4]] |
> | W6 | Wired & wireless LANs, CSMA/CD vs CSMA/CA | [[COMP504 Networks/Notes/Ch07 - Wired and Wireless LANs\|Ch07]] |
> | W7 | Backbone networks & VLANs | [[COMP504 Networks/Notes/Ch08 - Backbone Networks\|Ch08]] |
> | W8 | **lab**: default gateway troubleshooting | [[COMP504 Networks/Labs/Lab Submissions/Week 8/Lab Notes - Week 8\|Lab 8]] |
> | W9 | **lab**: VLSM addressing design | [[COMP504 Networks/Labs/Lab Submissions/Week 9/Lab Notes - Week 9\|Lab 9]] |
> | W10 | Wide area networks · **lab**: final practice | [[COMP504 Networks/Notes/Ch09 - Wide Area Networks\|Ch09]] · [[COMP504 Networks/Labs/Lab Submissions/Week 10/Lab Notes - Week 10\|Lab 10]] |
> | W11 | Network security | [[COMP504 Networks/Notes/Ch11 - Network Security\|Ch11]] |
>
> [[COMP504 Networks/Index|Full course index]] · [[COMP504 Networks/Research|Research hub]]

---

## 📊 COMP507 IT Project Management

> [!info]- Click to expand: tasks + weekly summary
> **Tasks — Assignment 1 (Wiki, cloud PMS comparison), 50% of grade**
> ```dataview
> TASK
> FROM "COMP507 IT Project Management"
> WHERE !completed
> SORT due ASC
> ```
> Full breakdown: [[COMP507 IT Project Management/Assignments/Assignment 1/Assignment 1 Checklist|Assignment 1 Checklist]]
>
> **Weekly summary**
>
> | Week | Topic | Note |
> |---|---|---|
> | 01 | Intro to ITPM, PMI/PMBOK framework, assessment overview | [[COMP507 IT Project Management/Notes/Week 01 - Introduction to ITPM\|Week 01]] |
> | 02 | PM concepts, project phases & lifecycle, triple constraint | [[COMP507 IT Project Management/Notes/Week 02 - PM Concepts, Phases and Lifecycle\|Week 02]] |
> | 04 | Stakeholder management, register & analysis | [[COMP507 IT Project Management/Notes/Week 04 - Stakeholder Management\|Week 04]] |
> | 05 | Risk management, 7 risk processes | [[COMP507 IT Project Management/Notes/Week 05 - Risk Management\|Week 05]] |
> | 06 | Schedule management (critical path, PERT) & scope management (WBS) | [[COMP507 IT Project Management/Notes/Week 06 - Schedule Management\|Schedule]] · [[COMP507 IT Project Management/Notes/Week 06 - Scope Management\|Scope]] |
> | 07 | Communications management (PMI model, 5 Cs, tailoring) | [[COMP507 IT Project Management/Notes/07 - Communication Management\|07]] |
> | 08 | Quality management (Six Sigma, sampling, testing) | [[COMP507 IT Project Management/Notes/08 - Quality Management\|08]] |
> | 09 | Cost management (EVM formulas) | [[COMP507 IT Project Management/Notes/09 - Cost Management\|09]] |
> | 12 | Resource management (motivation theories, RACI, Tuckman) | [[COMP507 IT Project Management/Notes/12 - Resource Management\|12]] |
>
> ⚠️ The "07/08/09/12" numbering is the source slide files' own — exact week alignment is unconfirmed (flagged in the course [[COMP507 IT Project Management/Index|Index]]).
>
> [[COMP507 IT Project Management/Index|Full course index]] · [[COMP507 IT Project Management/Research|Research hub]]

---

## 📈 COMP517 Data Analysis

> [!info]- Click to expand: tasks + weekly summary
> **Tasks — Assignment 1 (Data Exploration & Analysis), 100 marks**
> ```dataview
> TASK
> FROM "COMP517 Data Analysis"
> WHERE !completed
> SORT due ASC
> ```
> Full guide: [[COMP517 Data Analysis/Assignments/Assignment 1 Research|Assignment 1 Research]]
>
> **Weekly summary**
>
> | Week | Topic | Note |
> |---|---|---|
> | 01 | Why data matters, data analysis process, KDD | [[COMP517 Data Analysis/Notes/Week 01 - Introduction to Data Analysis\|Week 01]] |
> | 03 | Exploratory Data Analysis (EDA vs CDA, data quality) — ⚠️ deck dated S2 2025 | [[COMP517 Data Analysis/Notes/Week 03 - Exploratory Data Analysis\|Week 03]] |
> | Lab 01 | Python basics, Jupyter | [[COMP517 Data Analysis/Notes/Lab 01 - Basic Python Programming\|Lab 01]] |
> | Lab 02 | NumPy arrays, pandas DataFrames | [[COMP517 Data Analysis/Notes/Lab 02 - NumPy and pandas\|Lab 02]] |
> | Lab 04 | Univariate visualisation | [[COMP517 Data Analysis/Notes/Lab 04 - Univariate Visualisation\|Lab 04]] |
>
> [[COMP517 Data Analysis/Index|Full course index]] · [[COMP517 Data Analysis/Research|Research hub]]

---

## 🔢 MATH503 Mathematics

> [!info]- Click to expand: tasks + weekly summary
> **Tasks** *(no single "assignment" — continuous assessment, see [[MATH503 Mathematics/Course Overview|Course Overview]]: Portfolio 30% ongoing, Myimaths 25% ongoing due every Sunday midnight)*
> ```dataview
> TASK
> FROM "MATH503 Mathematics"
> WHERE !completed
> SORT due ASC
> ```
>
> **Weekly summary**
>
> | Week | Topic | Note |
> |---|---|---|
> | 03 | Conditional probability, Monty Hall | [[MATH503 Mathematics/Notes/Week 03 - Conditional Probability\|Week 03]] |
> | 04 | Permutations, counting, factorials | [[MATH503 Mathematics/Notes/Week 04 - Permutations and Counting\|Week 04]] |
> | 05 | Statistical measures (mean/median/mode, quartiles, IQR) | [[MATH503 Mathematics/Notes/Week 05 - Statistical Measures\|Week 05]] |
> | 06 | Binomial distribution (BINS, mean = Np) | [[MATH503 Mathematics/Notes/Week 06 - Binomial Distribution\|Week 06]] |
> | 07 | Normal distribution & z-scores — ⚠️ no lecture deck, tutorial-verified | [[MATH503 Mathematics/Notes/Week 07 - Normal Distribution and Z-Scores\|Week 07]] |
> | 08 | Hypothesis testing (p-values, proportion & mean tests) | [[MATH503 Mathematics/Notes/Week 08 - Hypothesis Testing\|Week 08]] |
> | 10 | Matrices (operations, inverse, transformations) | [[MATH503 Mathematics/Notes/Week 10 - Matrices\|Week 10]] |
>
> Missing: Weeks 1–2 (sets/Venn), 9 (relations & functions), 11 (matrices continued) — see [[MATH503 Mathematics/Research#5-missing-weeks|Research: Missing weeks]]
>
> [[MATH503 Mathematics/Index|Full course index]] · [[MATH503 Mathematics/Research|Research hub]]

---

## Related
[[Home|Vault Home]]
