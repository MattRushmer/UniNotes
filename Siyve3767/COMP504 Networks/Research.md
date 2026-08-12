---
tags:
  - comp504
  - networks
  - research
  - moc
---

# COMP504 Networks — Research Hub

> Open questions, under-explored topics, and external leads found while reading the course notes. Everything here is **synthesis + external sources** — the course notes themselves were not edited.

## Table of contents
1. [[COMP504 Networks/Research#1-osi-vs-tcp-ip-which-layering-does-the-exam-expect|OSI vs TCP/IP layering — which does the exam expect?]]
2. [[COMP504 Networks/Research#2-ipv6-addressing|IPv6 addressing — beyond the basics]]
3. [[COMP504 Networks/Research#3-error-detection-parity-checksum-crc|Error detection: parity, checksum, CRC]]
4. [[COMP504 Networks/Research#4-subnetting-exam-strategy|Subnetting exam strategy (VLSM/CIDR)]]
5. [[COMP504 Networks/Research#5-udp-vs-tcp-when-to-use-which|UDP vs TCP — when to use which]]
6. [[COMP504 Networks/Research#6-wireless-standards-and-csmaca|Wireless standards and CSMA/CA]]
7. [[COMP504 Networks/Research#cross-course-connections|Cross-course connections]]

---

## 1. OSI vs TCP/IP — which layering does the exam expect?

### Summary
My notes record **two different layer counts**: Ch01 says the Internet/TCP-IP model has **5 layers** (Physical, Data Link, Network, Transport, Application), and the final-exam deck repeats "OSI 7-layer / TCP-IP 5-layer models". But most external references describe TCP/IP as **4 layers** (Application, Transport, Internet, Network Access) — the 5-layer version is a hybrid teaching model that splits Network Access into Data Link + Physical. This is worth settling, because the textbook (*Business Data Communications and Networking*, 14th ed.) uses the 5-layer Internet model, while certification materials (CCNA) use 4. **Open question: which answer does the exam expect?**

### Links to existing notes
- [[COMP504 Networks/Notes/Ch01 - Introduction|Ch01 - Introduction]] (layers, encapsulation, PDUs)
- [[COMP504 Networks/Notes/Ch05 - Transport Layer Part 1|Ch05 Part 1 - TCP/IP]] (transport layer)
- [[COMP504 Networks/Notes/Ch05 - Transport Layer Part 2|Ch05 Part 2 - addressing & routing]] (network layer)
- [[COMP504 Networks/Notes/FINAL EXAM Revision (2026)|FINAL EXAM Revision]] (explicit "5-layer" phrasing)

### External sources (not from my vault)
- **IETF RFC 1122** (Requirements for Internet Hosts) — defines the 4-layer Internet model. https://www.ietf.org/rfc/rfc1122.txt
- **Wikipedia: OSI model** — 7-layer reference + comparison table. https://en.wikipedia.org/wiki/OSI_model
- **Check Point: OSI vs TCP/IP** — side-by-side layer mapping. https://www.checkpoint.com/cyber-hub/network-security/what-is-the-osi-model-understanding-the-7-layers/osi-model-vs-tcp-ip-model/
- **Imperva: OSI model explained** — per-layer protocols. https://www.imperva.com/learn/application-security/osi-model/

### Connections
- Layer models are background for [[COMP517 Data Analysis/Notes/Week 01 - Introduction to Data Analysis|COMP517 (data over networks)]] and for any client-server discussion in [[COMP507 IT Project Management/Notes/Week 06 - Scope Management|COMP507 ITPM]].

---

## 2. IPv6 addressing

### Summary
My notes cover IPv6 **notation and structure** (128-bit, hex, hextets, prefix lengths) but stop there — no dedicated note on IPv6 **address types** (unicast/anycast/multicast), **SLAAC vs DHCPv6**, or how IPv6 changes subnetting. The Default Gateway note touches IPv6 router solicitation. Given the course's heavy IPv4 focus (subnetting, VLSM), IPv6 depth may or may not be examinable — worth confirming with the lecturer, and the content below fills the gap if it is.

### Links to existing notes
- [[COMP504 Networks/Notes/Number Systems|Number Systems]] (hex, IPv6 128-bit structure)
- [[COMP504 Networks/Notes/Default Gateway|Default Gateway]] (IPv6 RS, prefix-based routing)
- [[COMP504 Networks/Notes/VLSM Subnetting - Block Method|VLSM Subnetting]] (IPv4 block method; does it carry to IPv6?)

### External sources (not from my vault)
- **IETF RFC 4291** (IPv6 Addressing Architecture) — the authoritative address-type spec. https://www.rfc-editor.org/info/rfc4291
- **Cisco: IPv6 Addressing Guide** — GUA/LLA/loopback + SLAAC in practice. https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/ipv6_basic/configuration/xe-3s/ip6b-xe-3s-book/ip6-rfcs.html
- **LearnCisco: IPv6 address types** — unicast/anycast/EUI-64 explained for students. https://www.learncisco.net/courses/icnd-1/introducing-ipv6/ipv6-address-types.html

### Connections
- IPv6 hex addressing is the applied version of **hex** taught in [[MATH503 Mathematics/Notes/Week 04 - Permutations and Counting|MATH503 (counting/notation)]] — see also the binary theme in [[COMP517 Data Analysis/Notes/Week 01 - Introduction to Data Analysis|COMP517]].

---

## 3. Error detection: parity, checksum, CRC

### Summary
The exam deck lists **parity checking, checksum, and CRC** as key facts (Ch4 Data Link layer, 3-5 questions), but no note in my vault actually explains how each works — they only appear as one-liners in the revision deck. This is a classic "mentioned but not worked through" gap: parity (extra bit per byte), checksum (sum divided, remainder kept), CRC (binary polynomial division).

### Links to existing notes
- [[COMP504 Networks/Notes/FINAL EXAM Revision (2026)|FINAL EXAM Revision]] (definitions as called out in the deck)
- [[COMP504 Networks/Notes/Ch05 - Transport Layer Part 1|Ch05 Part 1]] (TCP checksums in context)

### External sources (not from my vault)
- **Wikipedia: Parity bit** — how the extra bit detects single-bit errors. https://en.wikipedia.org/wiki/Parity_bit
- **Wikipedia: Checksum** — summation-based detection and limits. https://en.wikipedia.org/wiki/Checksum
- **Wikipedia: Cyclic redundancy check** — CRC-16/CRC-32 polynomial division. https://en.wikipedia.org/wiki/Cyclic_redundancy_check

### Connections
- Error detection supports the **data quality / integrity** idea in [[COMP517 Data Analysis/Notes/Week 03 - Exploratory Data Analysis|COMP517 W03]] and the **Integrity security goal** in [[COMP504 Networks/Notes/Ch11 - Network Security|Ch11]] (#terminology).

---

## 4. Subnetting exam strategy (VLSM/CIDR)

### Summary
My vault has a solid **VLSM block method** reference (2^n blocks, k·2^n boundaries, network/broadcast) and binary-to-decimal conversion, but no worked practice beyond two examples, and no note on **CIDR notation or the older class-based (A/B/C) addressing** that the exam deck mentions ("IPv4 classes, subnets, masks", 10-15 Qs for Ch5). The exam is closed-book, 100 MCQs — so quick, reliable subnetting is a high-value skill to drill.

### Links to existing notes
- [[COMP504 Networks/Notes/VLSM Subnetting - Block Method|VLSM Subnetting - Block Method]]
- [[COMP504 Networks/Notes/Number Systems|Number Systems]] (binary ↔ decimal conversions)
- [[COMP504 Networks/Notes/Identifying IPv4 Addresses - Examples|Identifying IPv4 Addresses - Examples]]
- [[COMP504 Networks/Notes/FINAL EXAM Revision (2026)|FINAL EXAM Revision]] (IPv4 classes, masks weighting)

### External sources (not from my vault)
- **Cisco Networking Academy / CCNA subnetting practice** — the industry-standard drills. https://learningnetwork.cisco.com/s/article/subnetting-a-network
- **Subnetting practice generators** (e.g. subnettingpractice.com) — timed drills for exam speed. https://subnettingpractice.com/
- **Wikipedia: CIDR** — classless notation and why /27 etc. exists. https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing

### Connections
- The 2^n block math is the same **powers-of-two counting** as [[MATH503 Mathematics/Notes/Week 04 - Permutations and Counting|MATH503 W04]] (#combinatorics) — see [[COMP504 Networks/Research#2-ipv6-addressing|IPv6 section above]] too.

---

## 5. UDP vs TCP — when to use which

### Summary
The exam deck calls out **UDP vs TCP** as a key fact (Ch5, 10-15 Qs): UDP = connectionless, no setup/sequence/ACKs, fast but unreliable (video streaming); TCP = connection-oriented, 3-way handshake, ACKs + sequence numbers (web/file transfer). Ch05 Part 1 explains TCP's mechanics, but my notes have no consolidated TCP-vs-UDP comparison or "which protocol for which app" table — useful for quick MCQ recall.

### Links to existing notes
- [[COMP504 Networks/Notes/Ch05 - Transport Layer Part 1|Ch05 Part 1 - TCP/IP]] (TCP connection-oriented details)
- [[COMP504 Networks/Notes/FINAL EXAM Revision (2026)|FINAL EXAM Revision]] (UDP/TCP summary + example apps)

### External sources (not from my vault)
- **IETF RFC 793** (TCP) and **RFC 768** (UDP) — the primary specs. https://www.rfc-editor.org/rfc/rfc793 · https://www.rfc-editor.org/rfc/rfc768
- **Cloudflare Learning: What is UDP?** — plain-language TCP vs UDP with app examples. https://www.cloudflare.com/learning/ddos/glossary/user-datagram-protocol-udp/

### Connections
- "Connection vs connectionless" parallels the **client-server vs peer-to-peer** distinction in [[COMP504 Networks/Notes/Ch01 - Introduction|Ch01]].

---

## 6. Wireless standards and CSMA/CA

### Summary
Ch07 and the exam deck (15-20 Qs) cover **CSMA/CD (wired Ethernet) vs CSMA/CA (wireless collision avoidance)**, access points, and switch modes, but my notes don't list the **802.11 standards family** (a/b/g/n/ac/ax), frequency bands, or WLAN security (WPA2/3). These are classic exam trivia and useful for the WLAN section of Ch7.

### Links to existing notes
- [[COMP504 Networks/Notes/Ch07 - Wired and Wireless LANs|Ch07 - Wired and Wireless LANs]]
- [[COMP504 Networks/Notes/FINAL EXAM Revision (2026)|FINAL EXAM Revision]] (CSMA/CD vs CSMA/CA, WLAN standards)
- [[COMP504 Networks/Notes/Lab 01 - Ethernet Cable Configuration|Lab 01 - Ethernet Cabling]] (wired side)

### External sources (not from my vault)
- **Wikipedia: IEEE 802.11** — full standard family table (a/b/g/n/ac/ax, bands, speeds). https://en.wikipedia.org/wiki/IEEE_802.11
- **Cisco: What is Wi-Fi?** — 802.11 generations and WPA2/3 security basics. https://www.cisco.com/c/en/us/products/wireless/what-is-wifi.html

### Connections
- WLAN security (WPA2/3, encryption) ties to the **security goals** in [[COMP504 Networks/Notes/Ch11 - Network Security|Ch11 Network Security]] (#terminology) and the wireless threat side of [[COMP507 IT Project Management/Notes/Week 05 - Risk Management|COMP507 risk]].

---

## Cross-course connections

Topics here that also live in other courses' research hubs:
- **Statistics & distributions** → see [[COMP507 IT Project Management/Research#cross-course-connections|COMP507 Research]] and [[MATH503 Mathematics/Research#cross-course-connections|MATH503 Research]] (COMP504 touches sampling only lightly).
- **Binary / data representation** → shared with [[COMP517 Data Analysis/Research#cross-course-connections|COMP517 Research]] (binary in COMP517 W01) and [[MATH503 Mathematics/Research#cross-course-connections|MATH503 Research]] (2^n counting).
- **Risk & security** → shared with [[COMP507 IT Project Management/Research#cross-course-connections|COMP507 Research]] (COMP507 W05 risk ↔ Ch11 security, #risk, #terminology).

Back to [[COMP504 Networks/Research#table-of-contents|top]] · [[COMP504 Networks/Index|Course index]]
