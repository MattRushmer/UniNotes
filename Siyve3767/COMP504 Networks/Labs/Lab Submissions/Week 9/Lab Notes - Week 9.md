---
tags:
  - comp504
  - networks
  - lab
  - vlsm
  - subnetting
  - exam-topic
---

# Week 9 Lab — Design & Implement a VLSM Addressing Scheme

> Assistance note for [[COMP504 Networks/Labs/Lab Submissions/Week 9/Packet Tracer - IPv4 VLSM Design and Implementation.docx|IPv4 VLSM Design and Implementation.docx]] — **status: NOT DONE — VLSM table is blank** ⚠️

## Worked solution — network **192.168.203.0/24**

Host needs (largest first): PS-115=32, PD-2=21, PS-101=19, PD1-1=14, WAN=2

| Subnet | Hosts | Block (2^n) | Prefix | Network | First | Last | Broadcast |
|---|---|---|---|---|---|---|---|
| PS-115 LAN | 32 | 64 (/26, n=6) | /26 | 192.168.203.0 | .1 | .62 | .63 |
| PD-2 LAN | 21 | 32 (/27, n=5) | /27 | 192.168.203.64 | .65 | .94 | .95 |
| PS-101 LAN | 19 | 32 (/27, n=5) | /27 | 192.168.203.96 | .97 | .126 | .127 |
| PD1-1 LAN | 14 | 16 (/28, n=4) | /28 | 192.168.203.128 | .129 | .142 | .143 |
| WAN | 2 | 4 (/30, n=2) | /30 | 192.168.203.144 | .145 | .146 | .147 |

**Method reminder:** find the smallest n where 2^n − 2 ≥ hosts needed. 32 → n=6 → /26; 21 → n=5 → /27; 2 → n=2 → /30. Next subnet starts at previous broadcast + 1.

## Device config rules (from the brief)
- Routers **Police** + **Schools**: first usable IP on each LAN link + WAN link (Schools takes the LAST usable on the WAN)
- Switches: **second** usable IP on VLAN 1 + `ip default-gateway` (so management is reachable from all LANs)
- Hosts: last usable IP in their subnet
- Verify with ping across subnets

## Related vault notes
- [[COMP504 Networks/Notes/VLSM Subnetting - Block Method|VLSM Subnetting - Block Method]] — the 2^n block method, **your best reference**
- [[COMP504 Networks/Notes/Number Systems|Number Systems]] — binary conversions
- [[COMP504 Networks/Notes/Identifying IPv4 Addresses - Examples|Identifying IPv4 Addresses]]
- [[COMP504 Networks/Labs/Lab Submissions/Week 9/Example-Design and Implement a VLSM Addressing Scheme.docx|Example VLSM scheme (worked)]] — the red worked example in your folder (10.1.1.0/24)
