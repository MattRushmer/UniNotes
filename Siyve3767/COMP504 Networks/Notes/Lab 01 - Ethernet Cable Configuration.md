---
tags:
  - comp504
  - networks
  - lab
  - ethernet
  - cabling
---

# Lab 01 - Ethernet Cable Configuration

> Auto-extracted from [[COMP504 Networks/Labs/Lab 01 - Ethernet Cable Configuration.pptx|Lab 01 - Ethernet Cable Configuration.pptx]]

## Straight-through vs crossover
- **Straight-through cable**: one wiring standard on both ends (T568A–T568A or T568B–T568B)
- **Crossover cable**: different wiring standard per end (T568A one end, T568B the other) — the transmit/receive pairs are swapped

## When to use which
- Equipment classes: **DTE** (data terminal equipment — computers, laptops, printers) vs **DCE** (data circuit equipment — switches, hubs, routers)
- **Crossover**: same-type devices — router–router, switch–switch, PC–PC, PC–router
- **Straight-through**: different-type devices — router–switch, PC–switch
- Modern devices with **Auto MDI-X** detect the cable type automatically (see [[COMP504 Networks/Notes/What are Ethernet Crossover Cables|What are Ethernet Crossover Cables]])

## Related
- [[COMP504 Networks/Notes/Ch07 - Wired and Wireless LANs|Ch07 - LANs]] (Ethernet media) · [[COMP504 Networks/Notes/Ch01 - Introduction|Ch01]] · [[COMP504 Networks/Index|Course index]]
