---
tags:
  - comp504
  - networks
  - lecture
  - tcp-ip
  - addressing
  - routing
  - exam-topic
---

# Ch05 - Network and Transport Layers (Part 2): Addressing and Routing

> Auto-extracted from [[COMP504 Networks/Lectures/Ch05 - Transport Layer Part 2.pptx|Ch05 - Transport Layer Part 2.pptx]]
> Source text: *Business Data Communications and Networking*, 14th ed, Chapter 5

## Network layer basics
- Four basic operations: **addressing** end devices, **encapsulation**, **routing**, **de-encapsulation**
- IP encapsulates the transport-layer segment into an IP **packet**; the IP addressing doesn't change source→destination

## Three kinds of addresses
- **Application layer address** — server name (software-configured; virtually all servers have one)
- **Network layer address** — IP address (software-assigned; must be unique on the network)
- **Data link layer address** — **MAC address**, permanently encoded in the NIC hardware
- **ICANN** manages assignment of Internet addresses and domain-name rules

## IPv4 address space
- 32 bits → ~4.3 billion addresses; classes assigned by first byte: **Class A / B / C** · **127.x.x.x = loopback** · **224–239 = Class D (multicast)** · **240–254 = Class E (experimental)** · **255 = broadcast** · private ranges exist within each class
- IP address = **network portion** (same for all devices on the LAN/WAN) + **host portion** (unique per device); IPv6 calls these **prefix** and **interface ID**

## Subnets and subnet masks
- **Subnet** = logical subdivision of a network; first address = network address, last = broadcast (e.g. 128.192.56.0 / .255)
- **Subnet mask** decides whether a host is local or remote; written in dotted decimal or **prefix length / slash notation** (e.g. /24 = 255.255.255.0)
- The **logical AND** of host IP and subnet mask gives the network address → see [[COMP504 Networks/Notes/Number Systems|Number Systems]] (binary) and [[COMP504 Networks/Reference/VLSM Subnetting - Block Method.pdf|VLSM Subnetting]] (reference)

## MAC vs IP addressing in delivery
- Same network: frame uses the destination's actual **MAC address**
- Remote network: Layer 3 gives Layer 2 the **default gateway** IP; the MAC source/destination change hop to hop, while IP addressing stays the same → see [[COMP504 Networks/Notes/Default Gateway|Default Gateway]]

## Dynamic addressing
- **DHCP** (Dynamic Host Configuration Protocol) — a server supplies the network layer address each time a device connects

## Address resolution
- **DNS** — resolves application (server name) → IP: local **resolving name server** → **root server** → **top-level domain / authoritative name server**
- **ARP** — resolves IP → MAC by broadcasting "who has this IP?" on the subnet; owner replies with its MAC

## Routing
- **Routing** = determining the path through the network; done by routers using **routing tables**
- Types: **centralized** · **static** (own decisions per formal protocol) · **dynamic/adaptive**: **distance vector** (counts hops, e.g. RIP) vs **link state** (hops + circuit speed + busy-ness, e.g. IS-IS)
- **Routing protocols**: RIP (interior, distance vector, small nets) · IS-IS (interior, link state, large nets) · **OSPF** (interior hybrid) · **EIGRP** (interior hybrid, improved IGRP) · **BGP** (exterior, distance vector, between autonomous systems) · **ICMP** (error reporting)
- Message types: **unicast** · **broadcast** (all on LAN/subnet) · **multicast** (group, joined via **IGMP**)

## Anatomy of a router
- Three functions: determine a path · transmit packets · support many devices/protocols
- Configuration: **console (management) port**, network interface port, auxiliary port; most routers run **Cisco IOS**; **ACL** defines which packets are routed vs discarded

## TCP/IP host configuration (4 pieces)
1. IP address · 2. subnet mask · 3. DNS server IP · 4. gateway (router) IP (servers also need an application-layer name)

## Security implications
- Security wasn't a design focus of the original Internet/TCP/IP; the **TCP three-way handshake** is a widely exploited flaw → see [[COMP504 Networks/Notes/Ch11 - Network Security|Ch11]]
- Your IP address identifies you; websites can track OS, browser, time zone

## Related
- [[COMP504 Networks/Notes/Ch05 - Transport Layer Part 1|Ch05 Part 1]] · [[COMP504 Networks/Notes/Ch01 - Introduction|Ch01]] · [[COMP504 Networks/Notes/Number Systems|Number Systems]] · [[COMP504 Networks/Notes/Default Gateway|Default Gateway]] · [[COMP504 Networks/Notes/Ch09 - Wide Area Networks|Ch09 - WAN]] · [[COMP504 Networks/Index|Course index]]
