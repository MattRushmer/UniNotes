---
tags:
  - comp504
  - networks
  - exam-prep
  - exam-topic
---

# COMP504 - Final Exam Revision (2026)

> Auto-extracted from [[COMP504 Networks/Exam Prep/FINAL EXAM Revision (2026).pptx|FINAL EXAM Revision (2026).pptx]] — lecturers Nurul Sarkar & Duaa Al-Hamid

## Exam logistics
- **Closed book**, online via Canvas · **100 multiple-choice questions = 100 marks** · 120 suggested minutes · total time 2h 10m
- Reading time: turn on computer, log into Canvas · non-programmable calculator + 1 blank A4 allowed · one attempt — save & submit

## Chapter weightings
| Chapter | Weeks | Qs |
|---|---|---|
| Ch1 Introduction (OSI 7-layer / TCP-IP 5-layer models) | W1 | 3–5 |
| Ch3 Physical layer (point-to-point vs multipoint; simplex/half/full duplex; **attenuation**) | W2 | 3–5 |
| Ch4 Data link layer (frames; **parity, checksum, CRC** error detection) | W3 | 3–5 |
| Ch5 Network & Transport (IPv4 classes, subnets, masks; **UDP vs TCP**; DNS; ping/ICMP) | W4–5 | 10–15 |
| Ch2 Application layer (client-server, middleware, 2/3/n-tier, thick client, SMTP, Telnet, server farm) | W10 | 10–15 |
| Ch6 Network design | W7 | 5–10 |
| Ch7 LANs (**CSMA/CD vs CSMA/CA**, cables, APs, switch modes, WLAN standards) | W6 | 15–20 |
| Ch8 Backbone (VLANs) | W7 | 5–10 |
| Ch9 WAN | W10 | 5–10 |
| Ch10 Internet | W8 | 5–8 |
| Ch11 Network security | W11 | 5–8 |
| Ch12 Network management | W8 | 3–5 |

## Key facts called out in the deck
- **UDP**: connectionless, no setup/sequence/ACKs, fast but unreliable (video streaming) · **TCP**: connection-oriented, 3-way handshake, ACKs + sequence numbers (web/file transfer)
- **Ping** uses **ICMP** (basic interior protocol for connectivity testing)
- Error detection: **parity checking** (extra bit per byte) · **checksum** (sum ÷ 255 remainder) · **CRC** (binary division; CRC-16/CRC-32)
- CSMA/CD = wired Ethernet; **CSMA/CA = wireless (collision avoidance)**
- Application layer: middleware sits between client & server; **3-tier** = presentation / application / database logic; n-tier more scalable; **thick client** = logic on client; **server farm** = group of linked servers acting as one

## Revision links (course notes)
- [[COMP504 Networks/Notes/Ch01 - Introduction|Ch01]] · [[COMP504 Networks/Notes/Ch05 - Transport Layer Part 1|Ch05 Part 1]] · [[COMP504 Networks/Notes/Ch05 - Transport Layer Part 2|Ch05 Part 2]] · [[COMP504 Networks/Notes/Ch07 - Wired and Wireless LANs|Ch07]] · [[COMP504 Networks/Notes/Ch08 - Backbone Networks|Ch08]] · [[COMP504 Networks/Notes/Ch09 - Wide Area Networks|Ch09]] · [[COMP504 Networks/Notes/Ch11 - Network Security|Ch11]] · [[COMP504 Networks/Notes/Number Systems|Number Systems]] · [[COMP504 Networks/Notes/VLSM Subnetting - Block Method|VLSM]] · [[COMP504 Networks/Index|Course index]]
