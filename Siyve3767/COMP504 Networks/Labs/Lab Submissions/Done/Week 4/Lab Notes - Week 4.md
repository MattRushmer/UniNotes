---
tags:
  - comp504
  - networks
  - lab
  - tcp-ip
  - osi
  - exam-topic
---

# Week 4 Lab — Investigating the TCP/IP and OSI Models

> Assistance note for [[COMP504 Networks/Labs/Lab Submissions/Done/Week 4/Packet Tracer-Investigating the TCP-IP and OSI Models-1.docx|Investigating the TCP-IP and OSI Models.docx]] — **status: DONE, answers filled in** ✅

## What this lab covers
- **PDU (Protocol Data Unit)** names at each layer — the core exam concept:
  - Layer 4 (Transport): **segment**
  - Layer 3 (Network): **packet**
  - Layer 2 (Data Link): **frame**
  - Layer 1 (Physical): **bits**
- **TCP/IP vs OSI** model relationship; how data is encapsulated as it travels
- **DNS** role: matches hostnames (www.osi.local) to IP addresses
- Packet Tracer **Simulation mode**: stepping through events, examining PDU details (In/Out Layers)

## Your answers (verified present)
- HTTP on Layer 7; TCP handshake + DNS lookup happen before the page loads
- A URL not in the DNS table fails; typing the server's IP skips DNS and works

## Quick check before submitting
- Screenshots of the OSI Model tab (Out Layers L7/L4/L3) and at least one DNS packet are requested in the brief — make sure they're in the docx

## Related vault notes
- [[COMP504 Networks/Notes/Ch05 - Transport Layer Part 1|Ch05 - Transport Layer (Part 1)]] — TCP/UDP, segments
- [[COMP504 Networks/Notes/Ch05 - Transport Layer Part 2|Ch05 - Transport Layer (Part 2)]]
- [[COMP504 Networks/Notes/Default Gateway|Default Gateway]] — the gateway shown in the PDU
