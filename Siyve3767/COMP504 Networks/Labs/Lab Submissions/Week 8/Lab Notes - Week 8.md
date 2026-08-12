---
tags:
  - comp504
  - networks
  - lab
  - default-gateway
  - troubleshooting
  - exam-topic
---

# Week 8 Lab — Troubleshoot Default Gateway Issues

> Assistance note for [[COMP504 Networks/Labs/Lab Submissions/Week 8/10.3.5 Packet Tracer - Troubleshoot Default Gateway Issues.docx|10.3.5 Troubleshoot Default Gateway Issues.docx]] — **status: NOT DONE — answers still blank** ⚠️

## Complete the addressing table first (this unlocks the marks)
| Device | Interface | IP | Mask | Default Gateway |
|---|---|---|---|---|
| R1 | G0/0 | 192.168.10.1 | 255.255.255.0 | N/A (router) |
| R1 | G0/1 | 192.168.11.1 | 255.255.255.0 | N/A (router) |
| S1 | VLAN 1 | 192.168.10.2 | 255.255.255.0 | **192.168.10.1** |
| S2 | VLAN 1 | 192.168.11.2 | 255.255.255.0 | **192.168.11.1** |
| PC1 | NIC | 192.168.10.10 | 255.255.255.0 | **192.168.10.1** |
| PC2 | NIC | 192.168.10.11 | 255.255.255.0 | **192.168.10.1** |
| PC3 | NIC | 192.168.11.10 | 255.255.255.0 | **192.168.11.1** |
| PC4 | NIC | 192.168.11.11 | 255.255.255.0 | **192.168.11.1** |

**Rule of thumb:** a host's default gateway is the router interface on the SAME subnet as the host. A router interface is never its own gateway. PCs without a gateway can't leave their subnet.

## Troubleshooting method (mark-earning structure)
1. **Verify documentation** — complete the table
2. **Isolate** — ping same-subnet devices first (PC1 → PC2, PC1 → S1), then remote (PC1 → R1, PC1 → PC3)
3. **Document** the failure (e.g. "PC1 IP is wrong")
4. **Fix** and **verify** — re-ping, record "Verified"
5. Note the brief already shows one issue: **PC1 IP address is wrong → change it**

## Related vault notes
- [[COMP504 Networks/Notes/Default Gateway|Default Gateway]] — exact topic of this lab
- [[COMP504 Networks/Notes/Identifying IPv4 Addresses - Examples|Identifying IPv4 Addresses]] — subnet/gateway logic
- [[COMP504 Networks/Notes/VLSM Subnetting - Block Method|VLSM Subnetting]] — if you need to re-subnet
