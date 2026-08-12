---
tags:
  - comp504
  - networks
  - lecture
  - security
  - risk
  - terminology
  - exam-topic
---

# Ch11 - Network Security

> Auto-extracted from [[COMP504 Networks/Lectures/Ch11 - Network Security.pptx|Ch11 - Network Security.pptx]]
> Source text: *Business Data Communications and Networking*, 14th ed, Chapter 11

## Security goals and threats
- Three primary goals: **Confidentiality** (no unauthorized disclosure) · **Integrity** (data not altered/destroyed) · **Availability** (continuous operation) — the same words appear as **quality attributes** in [[COMP507 IT Project Management/Notes/08 - Quality Management|COMP507 08 Quality]] (#terminology: same term, different framework)
- Two broad threat categories: **business continuity** (disruptions, destruction, disasters → availability + some integrity) and **unauthorized access / intrusion** (→ confidentiality + integrity)
- Why security matters: cybercrime is now a profession, hacktivism, mobile devices; average data breach ≈ $3.5M; SOX/HIPAA drive compliance

## Controls
- **Preventive** (stop) · **Detective** (reveal) · **Corrective** (remedy) — review periodically

## Risk assessment (step 1 of security)
- Frameworks: **OCTAVE** · **COBIT** · **NIST** guide
- Steps: develop **risk measurement criteria** (financial, productivity, reputation, safety, legal) → **inventory IT assets** (hardware, software, data, mission-critical apps) → **identify threats** + build **threat scenarios** (impact × likelihood = relative risk score) → document existing controls → identify improvements
- Risk strategies: **accept** · **mitigate** · **share** (insurance) · **defer** — the same framework as [[COMP507 IT Project Management/Notes/Week 05 - Risk Management|COMP507 project risk]] (avoid/mitigate/transfer/accept)

## Business continuity
- Two parts: prevention controls + **disaster recovery plan**
- Threats: viruses, theft, DoS, device failure, disaster
- **Malware**: viruses, macro viruses, **worms** (self-spreading), ransomware — stop with antivirus
- **DoS/DDoS**: flood the target; attacker builds a **botnet** (zombies/bots + DDoS handler); defenses = **traffic filtering**, **traffic limiting**, **traffic anomaly detector**
- **Device failure**: build **redundancy** (Internet, backbone, LANs, servers, fault-tolerant servers, **UPS**); **RAID 0–6** (RAID 1 = duplicate disks, RAID 6 = survives two disk failures)
- **Disaster recovery**: backup/recovery controls, **CDP** (continuous data protection), **disaster recovery drills**, two-level outsourcing

## Firewalls (perimeter security)
- **Packet-level firewall** — checks source/destination addresses against an **ACL** (see [[COMP504 Networks/Notes/Ch08 - Backbone Networks|Ch08]])
- **Application-level firewall** — per-application rules, **stateful inspection**
- **NAT firewall** — translates private ↔ public IPs (see [[COMP504 Networks/Notes/Ch05 - Transport Layer Part 2|Ch05 addressing]]); layered firewall architectures

## Intrusion prevention
- Four intruder types: casual (script kiddies) · thrill-seeking hackers/crackers · professional (espionage/fraud) · insiders (employees)
- **Security policy** + user profiles; remove accounts on departure
- **Security holes** and **zero-day attacks**; OS minimum security (C2); **Trojan horses/rootkits**, spyware, adware
- **IPS**: network-based or host-based; **misuse detection** (signatures) vs **anomaly detection** (baseline)
- Recovery: **computer forensics** · **honeypots** (fake servers to trap intruders)

## Encryption (intrusion prevention)
- **Symmetric** (single key; DES, 3DES, **AES**) vs **asymmetric / public key** (public key encrypts, private key decrypts)
- **Digital signatures** via invertible public-key algorithms; **PKI**: **certificate authority (CA)** issues **digital certificates**
- Software: **PGP** (email), **SSL** (web), **IPSec** (general; **transport mode** encrypts payload, **tunnel mode** encrypts whole packet — see [[COMP504 Networks/Notes/Ch09 - Wide Area Networks|Ch09 VPNs]])

## User authentication
- Something you **know** (password/passphrase) · **have** (phone, token → **two-factor**, one-time passwords) · **are** (biometrics)
- **Central authentication** (e.g. **Kerberos**); password managers
- **Social engineering**: **phishing** and similar attacks

## Best practice
- Disaster recovery plan + security policy · best investment = **user training** · expect more **two-factor authentication** and **encryption**

## Related
- [[COMP504 Networks/Notes/Ch07 - Wired and Wireless LANs|Ch07]] (WEP/WPA/WPA2) · [[COMP504 Networks/Notes/Ch05 - Transport Layer Part 2|Ch05 Part 2]] (TCP handshake flaw) · [[COMP504 Networks/Notes/Ch09 - Wide Area Networks|Ch09]] (VPNs) · [[COMP504 Networks/Notes/Ch08 - Backbone Networks|Ch08]] (ACLs/VLANs) · [[COMP504 Networks/Notes/Ch01 - Introduction|Ch01]] · [[COMP504 Networks/Index|Course index]]
