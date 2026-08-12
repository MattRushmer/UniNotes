---
tags:
  - comp504
  - networks
  - lecture
  - routing
  - exam-topic
---

# Default Gateway and Host Routing

> Auto-extracted from [[COMP504 Networks/Lectures/Default Gateway.pptx|Default Gateway.pptx]]

## Host forwarding decision
- Packets are always created at the source; every host builds its own routing table
- A host can send to: itself (127.0.0.1 IPv4 / ::1 IPv6) · local hosts (same LAN) · remote hosts (different LAN)
- How the source decides local vs remote:
  - IPv4 — uses its own IP + **subnet mask** plus the destination IP (addressing: [[COMP504 Networks/Notes/Number Systems|Number Systems]])
  - IPv6 — uses the network address/prefix advertised by the local router

## Default gateway (DGW)
- A **router** or Layer 3 switch can be a default gateway
- DGW features: an IP address in the LAN's range · can accept LAN data and forward it off the LAN · can route to other networks
- No default gateway (or a bad one) → traffic cannot leave the LAN
- IPv4: DGW learned statically or via **DHCP** · IPv6: via **router solicitation (RS)** or manual config
- The DGW is a static route that acts as the **last-resort route** in the routing table
- View a host's routing table on Windows: `route print` or `netstat -r` (Interface List, IPv4 Routing Table, IPv6 Routing Table)

## Router forwarding and routing tables
- Three types of routes:
  - **Directly connected** — auto-added when the interface is active and addressed
  - **Remote** — learned manually (**static route**) or dynamically (**routing protocol**)
  - **Default route** — forwards all unmatched traffic in a specific direction
- **Static routing**: configured manually; good for small, non-redundant networks; often used for default routes
- **Dynamic routing**: auto-discovers remote networks, keeps information current, chooses best paths, adapts to topology changes (protocols include **OSPF**, **EIGRP**, RIP)
- `show ip route` route sources: L = local interface · C = directly connected · S = static · O = OSPF · D = EIGRP

## New terms
`netstat -r` · `route print` · directly-connected · remote · default route · next-hop · metric · administrative distance · route source

## Related
- [[COMP504 Networks/Notes/Ch09 - Wide Area Networks|Ch09 - Wide Area Networks]] (routing over WANs) · [[COMP504 Networks/Notes/Ch08 - Backbone Networks|Ch08 - Backbone Networks]] · [[COMP504 Networks/Notes/Number Systems|Number Systems]] · [[COMP504 Networks/Index|Course index]]
