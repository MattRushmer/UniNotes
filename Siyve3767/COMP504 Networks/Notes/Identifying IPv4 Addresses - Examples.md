---
tags:
  - comp504
  - networks
  - lab
  - addressing
  - subnetting
  - exam-topic
---

# Identifying IPv4 Addresses - Worked Examples

> Auto-extracted from [[COMP504 Networks/Labs/Identifying IPv4 Addresses - Examples.pdf|Identifying IPv4 Addresses - Examples.pdf]] (Duaa Al-Hamid)

## Method (per example)
1. Write the IP and subnet mask in binary
2. **Logical AND** them bit-by-bit → **network address**
3. **Broadcast address** = network address with all host bits set to 1
4. **First host** = network + 1 · **Last host** = broadcast − 1

## Worked examples
| IP/mask | Subnet mask | Network | Broadcast | Hosts |
|---|---|---|---|---|
| 10.1.8.200/26 | 255.255.255.192 | 10.1.8.192 | 10.1.8.255 | .193–.254 |
| 10.1.1.101/25 | 255.255.255.128 | 10.1.1.0 | 10.1.1.127 | .1–.126 |
| 209.165.200.227/27 | 255.255.255.224 | 209.165.200.224 | 209.165.200.255 | .225–.254 |
| 172.16.117.77/20 | 255.255.240.0 | 172.16.112.0 | 172.16.127.255 | .112.1–.127.254 |

- Tip: broadcast is NOT always .255 — only the host bits flip to 1 (e.g. /25 → .127)

## Related
- [[COMP504 Networks/Notes/Number Systems|Number Systems]] (binary conversions) · [[COMP504 Networks/Notes/Ch05 - Transport Layer Part 2|Ch05 Part 2]] (subnets & masks) · [[COMP504 Networks/Notes/VLSM Subnetting - Block Method|VLSM Subnetting]] · [[COMP504 Networks/Index|Course index]]
