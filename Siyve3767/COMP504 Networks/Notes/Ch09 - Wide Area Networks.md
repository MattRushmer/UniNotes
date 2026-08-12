---
tags:
  - comp504
  - networks
  - lecture
  - wan
  - vpn
  - exam-topic
---

# Ch09 - Wide Area Networks

> Auto-extracted from [[COMP504 Networks/Lectures/Ch09 - Wide Area Networks.pptx|Ch09 - Wide Area Networks.pptx]]
> Source text: *Business Data Communications and Networking*, 14th ed, Chapter 9

## WAN basics
- WANs run long distances; most organizations **lease circuits** from **common carriers** (LEC = local, IXC = long-distance)
- Three service types: **dedicated-circuit** · **packet-switched** · **Internet-based VPN**

## Dedicated-circuit networks
- Leased for exclusive 24/7 use (private line services); point-to-point; flat monthly fee
- User equipment: multiplexers, **CSU/DSU**
- Architectures: **ring** · **star** (central computer = easy to manage but single point of failure) · **full mesh** (everyone connected, expensive) · **partial mesh** (most common)
- Services: **T-carrier** and **SONET**

## Packet-switched networks
- Multiple simultaneous connections over one physical circuit; pay for connection + packets
- **PAD** (packet assembly/disassembly device) at the user edge; **PVCs** (permanent virtual circuits) or **SVCs** between sites; connection via a carrier **POP**
- Three types:
  - **Frame relay** — oldest; unreliable (no error control); **CIR** (committed information rate) vs **MAR** (maximum allowable rate)
  - **MPLS** (multiprotocol label switching) — layer 2 service used with IP at layer 3
  - **Ethernet services** — carriers' own gigabit fiber networks; more flexible

## Virtual private networks (VPNs)
- Equivalent of a private packet-switched network over the public Internet; PVCs run as **tunnels** via **VPN gateways**
- Cheap and flexible, but only as reliable/secure as the Internet (mitigate with encryption)
- Types: **intranet VPN** (between an org's offices) · **extranet VPN** (between orgs) · **access VPN** (remote employees)
- Mechanism: VPN software encrypts and encapsulates packets with **IPSec ESP**; the VPN interface becomes the default interface
- Operates at layer 2 or layer 3 (the packet at that layer selects the tunnel)

## Best practice + SDWAN
- WAN design buys services, not products; increasingly Ethernet + Internet VPN + cloud
- **Software Defined WAN (SDWAN)**: software-managed routers; benefits = centralized management, cost reduction via traffic balancing, end-to-end visibility, security
- SDWAN planes: **Management (orchestration) plane** · **Control plane** · **Data plane**

## Security implications (see also [[COMP504 Networks/Notes/Ch11 - Network Security|Ch11]])
- A WAN is usually one of the most secure parts of the network (carrier traffic is hard to single out); VPN-over-Internet is the main risk → most orgs encrypt WAN traffic

## Related
- [[COMP504 Networks/Notes/Ch08 - Backbone Networks|Ch08 - Backbone]] · [[COMP504 Networks/Notes/Ch07 - Wired and Wireless LANs|Ch07 - LANs]] · [[COMP504 Networks/Notes/Ch05 - Transport Layer Part 2|Ch05 Part 2]] (routing protocols) · [[COMP504 Networks/Notes/Default Gateway|Default Gateway]] (routing) · [[COMP504 Networks/Index|Course index]]
