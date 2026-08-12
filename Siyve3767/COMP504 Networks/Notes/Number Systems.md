---
tags:
  - comp504
  - networks
  - lecture
  - number-systems
  - exam-topic
---

# Number Systems (Binary, Decimal, Hexadecimal)

> Auto-extracted from [[COMP504 Networks/Lectures/Number Systems.pptx|Number Systems.pptx]] — Cisco ITN Module 5

## Core concepts
- **Binary** (base 2): 1s and 0s called **bits**; how hosts, servers, and network equipment identify each other
- **Decimal** (base 10): digits 0–9
- **Hexadecimal** (base 16): digits 0–9 + A–F; used to represent **IPv6** addresses (128-bit) and **MAC** addresses
- **Positional notation** and **radix** — a digit's value depends on its position in the number

## IPv4 addressing (32-bit)
- IPv4 address = 32 bits in four **octets** (8 bits each), written as **dotted decimal**, e.g. 192.168.11.10
- Convert binary ↔ decimal using positional values 128 64 32 16 8 4 2 1
- Example: 11000000.10101000.00001011.00001010 = 192.168.11.10
- Practical examples: [[COMP504 Networks/Labs/Identifying IPv4 Addresses - Examples.pdf|Identifying IPv4 Addresses - Examples]] (lab) · [[COMP504 Networks/Reference/VLSM Subnetting - Block Method.pdf|VLSM Subnetting - Block Method]] (reference)

## Hexadecimal and IPv6
- IPv6 = 128 bits; every 4 bits = one hex digit → 32 hex values; each 4-hex-char group = a **hextet**
- Conversions: decimal → binary → hex, and hex → binary → decimal

## New terms
`dotted decimal notation` · `positional notation` · `radix` · `octet` · `hextet` · base 2 / 10 / 16

## Related
- [[COMP504 Networks/Notes/Ch01 - Introduction|Ch01 - Introduction]] (IP in the layered model) · [[COMP504 Networks/Notes/Default Gateway|Default Gateway]] (host routing uses the subnet mask) · [[COMP504 Networks/Index|Course index]]
