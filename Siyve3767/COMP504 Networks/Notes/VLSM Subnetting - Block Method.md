---
tags:
  - comp504
  - networks
  - reference
  - subnetting
  - vlsm
  - combinatorics
  - exam-topic
---

# VLSM Subnetting - Block Method

> Auto-extracted from [[COMP504 Networks/Reference/VLSM Subnetting - Block Method.pdf|VLSM Subnetting - Block Method.pdf]] (Bobby Yang, revised 25 Aug 2021)

## Rules
- If there are n host bits, the host address space is a **block of fixed size 2ⁿ** (multiplication principle / powers of two — see [[MATH503 Mathematics/Notes/Week 04 - Permutations and Counting|MATH503 W04]])
- Blocks start at fixed boundaries: k·2ⁿ where k = 0, 1, 2, …
- Blocks must not overlap
- First address in the block = **network address** (host bits all 0) · last = **broadcast** (host bits all 1)
- Host bits can occur in any octet; the octet where the host part starts = the **boundary octet**

## Finding network & broadcast (example)
- 202.56.64.134/27 → 5 host bits → block size 2⁵ = 32 → blocks start 0, 32, 64, 96, 128… → address lies in 128–159 → network **202.56.64.128**, broadcast **202.56.64.159**
- 203.45.156.148/18 → boundary in 3rd octet, 6 host bits → block size 64 → network **203.45.128.0**, broadcast **203.45.191.255**

## Designing subnets (VLSM)
- Work **biggest subnet first**; each block must not overlap
- 192.168.2.0/24 → Subnet A (60 hosts) = /26 block 0–63 · Subnet B (20 hosts) = /27 block 64–95 · Subnet C (12 hosts) = /28 block 96–111
- 203.45.128.0/18 → Subnet A /22 = 203.45.128.0–131.255 · Subnet B /25 = 203.45.132.0–132.127

## Related
- [[COMP504 Networks/Notes/Ch05 - Transport Layer Part 2|Ch05 Part 2]] (subnet masks & prefix length) · [[COMP504 Networks/Notes/Number Systems|Number Systems]] · [[COMP504 Networks/Notes/Identifying IPv4 Addresses - Examples|IPv4 examples]] · [[COMP504 Networks/Index|Course index]]
