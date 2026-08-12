---
tags:
  - comp504
  - networks
  - lecture
  - backbone
  - vlan
  - exam-topic
---

# Ch08 - Backbone Networks

> Auto-extracted from [[COMP504 Networks/Lectures/Ch08 - Backbone Networks.pptx|Ch08 - Backbone Networks.pptx]]
> Source text: *Business Data Communications and Networking*, 14th ed, Chapter 8

## Backbone basics
- Most backbones today use **high-speed Ethernet**; components: network cable (usually **fiber-optic**) + hardware that connects networks
- Device roles: **switches** (data link layer) · **routers** (network layer) · **VLAN switches** (layer 2 + routing combination)

## Switched backbones (distribution layer)
- Most common BN type; **star topology** with one backbone switch at the center
- Devices usually in one room (a **rack**): **MDF / CDF** (main/central distribution facility) connected by short **patch cables**; alternative = **chassis switch** (plug-in modules, flexible)

## Routed backbones (core layer)
- Forward packets by **network layer address**; also called subnetted/hierarchical backbones
- Used to connect buildings on a campus; keeps **broadcasts** inside one network segment

## VLANs (virtual LANs)
- Logical grouping of devices; each computer assigned a **VLAN ID**, matched to an IP subnet, assigned by **physical switch port**
- Benefits: smaller **broadcast domains** · better security (only same-VLAN users communicate) · lower cost (one switch, many groups) · better performance · simpler management
- Without layer 3 routing, devices in different VLANs cannot communicate
- Inter-switch frames use **IEEE 802.1Q tagging** (VLAN ID + priority inserted); a router strips the frame and reads the IP packet
- **Trunks**: point-to-point links between devices carrying multiple VLANs (Cisco default supports all VLANs, 802.1Q)
- Cisco config: `vlan <id>` + `name` (global config) · `switchport mode access` + `switchport access vlan <id>` (interface) · verify with `show vlan brief` · delete with `no vlan <id>`

## Best-practice design
- **Switched backbone or VLAN for the distribution layer + routed backbone for the core layer**; backbone technology = **gigabit Ethernet**

## Security implications (see also [[COMP504 Networks/Notes/Ch11 - Network Security|Ch11]])
- Router **ACLs** filter what traffic passes; **VLANs are the most secure backbone type** — ACLs and security can be applied at the switch level

## Related
- [[COMP504 Networks/Notes/Ch07 - Wired and Wireless LANs|Ch07 - LANs]] · [[COMP504 Networks/Notes/Ch09 - Wide Area Networks|Ch09 - WANs]] · [[COMP504 Networks/Notes/Ch05 - Transport Layer Part 2|Ch05 Part 2]] (routing/addressing) · [[COMP504 Networks/Notes/Ch01 - Introduction|Ch01]] · [[COMP504 Networks/Index|Course index]]
