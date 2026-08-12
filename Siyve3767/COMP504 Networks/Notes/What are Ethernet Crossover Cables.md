---
tags:
  - comp504
  - networks
  - lab
  - ethernet
  - cabling
---

# What are Ethernet Crossover Cables?

> Auto-extracted from [[COMP504 Networks/Labs/What are Ethernet Crossover Cables.pdf|What are Ethernet Crossover Cables.pdf]] (Computer Cable Store article)

## Summary
- A **crossover cable** connects two same-type Ethernet devices directly (PC–PC, router–router, switch–switch) with no switch/router in between
- Internal wiring **reverses** the transmit/receive pairs: output pins on one end connect to input pins on the other
- A **straight-through cable** connects different-type devices (PC–switch, router–switch, PC–router)

## Wiring standards
- Two ANSI/TIA/EIA standards: **T568A** and **T568B** — differ in the position of the orange and green pairs
- Straight-through: same standard both ends · Crossover: T568A one end, T568B the other
- Crossover cables are often labelled "Crossover" or "Xover"

## Auto MDI-X
- Modern devices support **Auto MDI-X** — they auto-detect the connection type, so either cable works

## Related
- [[COMP504 Networks/Notes/Lab 01 - Ethernet Cable Configuration|Lab 01 - Ethernet Cable Configuration]] · [[COMP504 Networks/Notes/Ch07 - Wired and Wireless LANs|Ch07 - LANs]] · [[COMP504 Networks/Index|Course index]]
