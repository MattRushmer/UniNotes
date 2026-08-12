---
tags:
  - comp507
  - project-management
  - lecture
  - quality
  - statistics
  - sampling
  - distributions
  - terminology
  - exam-topic
---

# 08 - Quality Management

> Auto-extracted from [[COMP507 IT Project Management/Lectures/08 - Quality Management.pptx|08 - Quality Management.pptx]]
> Source text: *Information Technology Project Management* (Schwalbe, 2019), Chapter 8

## Purpose and definitions
- Purpose: ensure the project **satisfies the needs for which it was undertaken** - meet/exceed stakeholder needs and expectations
- ISO definition: "Totality of characteristics of an entity that bear on its ability to satisfy stated or implied needs" (ISO8042:1994); "The degree to which a set of inherent characteristics fulfils requirements" (ISO9000:2000)
- Other views: **conformance to requirements** . **fitness for use** - quality must be **measurable**
- IT quality is harder to measure: many components (3-tier), large-scale, distributed, layered, middleware/microservices, cloud/edge/AI environments

## Common quality attributes
- **Availability** (probability a service is available) . **Reliability** (failures/month) . **Performance** (throughput and latency) . **Scalability** . **Usability** . **Integrity** (conformance to description) . **Security** (authn/authz/confidentiality) . **Conformance to standards** . **Deadlock-free** (important for concurrent systems; one-lane bridge example)

## Quality management processes (3)
1. **Plan quality management** - identifying relevant quality standards; a **metric** is a standard of measurement
2. **Manage quality** (assurance) - translating the quality plan into executable activities
3. **Control quality** - monitoring results against standards

## Who is responsible
- Project managers are ultimately responsible; references: ISO (iso.org), IEEE (ieee.org), SEI/CMMI (sei.cmu.edu/cmmi)
- Scope aspects affecting quality: **functional requirements** and **non-functional** quality attributes (usability, performance, reliability, maintainability)

## Managing quality (assurance)
- **Quality assurance**: all activities related to satisfying relevant quality standards
- **Lean**: maximize customer value while minimizing waste
- **Benchmarking**: comparing practices/products to other projects
- **Quality audit**: structured review to identify lessons learned

## Quality control tools and techniques
- **Cause-and-effect (fishbone) diagrams** + **5 Whys** root-cause analysis
- **Control charts** + **7 run rule** (7 consecutive points above/below mean or trending = non-random problem)
- **Checksheets** . **Scatter diagrams** (correlation; e.g. younger users more satisfied) . **Histograms** . **Pareto charts** (80/20 rule) . **Flowcharts** . **Run charts** (trends over time)
- Main outputs: **acceptance decisions, rework, process adjustments**

## Statistical sampling and Six Sigma (see [[MATH503 Mathematics/Notes/Week 06 - Binomial Distribution|MATH503 W06]] for the Bernoulli/Binomial maths)
- Sample size formula: sample size = 0.25 x (certainty factor / acceptable error)^2
- Certainty factors (z-scores): 95% -> 1.960 . 90% -> 1.645 . 80% -> 1.281
- One sigma ~ 68.27% certainty, two sigma ~ 95.45%
- **Six Sigma**: <= 3.4 defects per million opportunities (mathematically 4.5 sigma); **DMAIC** = Define, Measure, Analyze, Improve, Control
- Bernoulli/Binomial sampling distribution; normal distribution N(mu,sigma) — see [[MATH503 Mathematics/Notes/Week 06 - Binomial Distribution|MATH503 W06]] and [[MATH503 Mathematics/Notes/Week 05 - Statistical Measures|MATH503 W05]]; data-quality angle in [[COMP517 Data Analysis/Notes/Week 03 - Exploratory Data Analysis|COMP517 W03]]

## Testing
- Test during almost every phase, not just at the end
- **Unit** -> **Integration** -> **System** -> **User acceptance testing (UAT)**
- **Usability testing** != UAT - it informs design before you build: paper prototypes (50% more input), mock-ups, hallway testing, remote usability, heuristic evaluation, A/B testing, think-aloud protocol, eye tracking

## Maturity models
- **CMMI** levels: Incomplete -> Performed -> Managed -> Defined -> Quantitatively Managed -> Optimizing
- **OPM3** (PMI): 180 best practices, 2,400+ capabilities/outcomes/KPIs
- **Software Quality Function Deployment (QFD)**: user requirements -> software planning

## Quality assurance plan structure
- Intro (purpose, policy, scope) -> management (roles) -> required documentation -> procedures (walkthrough, review, audit, evaluation, process improvement) -> problem/noncompliance reporting -> metrics -> checklist forms

## Notes elsewhere in this vault
- Homework link: Chapter 7 Cost Management -> [[COMP507 IT Project Management/Notes/09 - Cost Management|09 - Cost Management]]
- Quality attributes <-> non-functional requirements in [[COMP507 IT Project Management/Notes/Week 06 - Scope Management|Week 06 - Scope Management]]
