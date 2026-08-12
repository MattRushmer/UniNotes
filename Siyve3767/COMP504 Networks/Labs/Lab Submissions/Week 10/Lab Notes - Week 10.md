---
tags:
  - comp504
  - networks
  - lab
  - vlsm
  - ssh
  - final
  - exam-topic
---

# Week 10 Lab — Packet Tracer Final Lab (Practice)

> Assistance note for [[COMP504 Networks/Labs/Lab Submissions/Week 10/Packet Tracer Final Lab-1.docx|Packet Tracer Final Lab.docx]] and [[COMP504 Networks/Labs/Lab Submissions/Week 10/Cisco Basic Configuration-2.docx|Cisco Basic Configuration.docx]] — **status: NOT DONE — VLSM table + configs blank** ⚠️

## Part 1 — VLSM design, network **49.50.10.0/24**

Host needs: LAN-Sales=70, LAN-Design=56, LAN-Admin=26, WAN=2

| Subnet | Hosts | Block (2^n) | Prefix | Network | First | Last | Broadcast |
|---|---|---|---|---|---|---|---|
| LAN-Sales | 70 | 128 (/25, n=7) | /25 | 49.50.10.0 | .1 | .126 | .127 |
| LAN-Design | 56 | 64 (/26, n=6) | /26 | 49.50.10.128 | .129 | .190 | .191 |
| LAN-Admin | 26 | 32 (/27, n=5) | /27 | 49.50.10.192 | .193 | .222 | .223 |
| WAN | 2 | 4 (/30, n=2) | /30 | 49.50.10.224 | .225 | .226 | .227 |

## Part 2 — Router PR security config (from the brief)
```
hostname PR
banner motd #No Unauthorized Access#
ip domain-name CCNA.net
enable secret Ciscoenpa55
security passwords min-length 10
username Admin privilege 15 secret Adminpa55
no ip domain-lookup
service password-encryption
line console 0
 password Ciscoconpa55
 login
 exec-timeout 10 0
line vty 0 4
 transport input ssh
 exec-timeout 10 0
 login local
crypto key generate rsa     ! 1024-bit key
banner login #No Unauthorised Access#
login block-for 180 attempts 4 within 30
```

## Interfaces + switches + hosts
- Interfaces: IPv4 per the table above, descriptions **SALES / DESIGN / ADMIN**, `no shutdown`
- Switch: SVI (VLAN 1) with **second** usable IP, `ip default-gateway`, `no shut`
- PCs: subsequent usable IPs; verify with ping PC-to-PC
- Use **Check Results → Assessment Items** in Packet Tracer to verify (ignore IPv6 items)

## Submission checklist (marks!)
- Screenshots of router basic config, interfaces, switch config, and ping results inside the docx (the brief explicitly asks for these)
- Upload the .docx AND the .pka

## Related vault notes
- [[COMP504 Networks/Notes/VLSM Subnetting - Block Method|VLSM Subnetting - Block Method]]
- [[COMP504 Networks/Notes/Ch11 - Network Security|Ch11 - Network Security]] — SSH, device hardening
- [[COMP504 Networks/Notes/Default Gateway|Default Gateway]]
