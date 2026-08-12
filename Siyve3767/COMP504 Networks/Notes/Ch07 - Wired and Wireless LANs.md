---
tags:
  - comp504
  - networks
  - lecture
  - lan
  - ethernet
  - wireless
  - exam-topic
---

# Ch07 - Wired and Wireless LANs

> Auto-extracted from [[COMP504 Networks/Lectures/Ch07 - Wired and Wireless LANs.pptx|Ch07 - Wired and Wireless LANs.pptx]]
> Source text: *Business Data Communications and Networking*, 14th ed, Chapter 7

## LAN components
- **Client** · **server** · **network interface card (NIC)** · **network circuits** · **hubs / switches / access points** · **network operating system (NOS)**
- NIC connects the computer to the cable (wired) or is a radio transceiver (wireless); laptops have both wired + wireless NICs
- Circuits: **UTP** (most common), **STP** (only in interference-heavy areas), **fiber-optic**

## Hubs, switches, access points
- Act as junction boxes and **repeaters** (signals attenuate over distance); connection points = **ports**
- **Hub-based Ethernet** = logical **bus** topology; all frames flow to all computers → shared **collision domain**
- **Switch-based Ethernet** = logical + physical **star**; switch reads the address and retransmits only on the right circuit, using a **forwarding table** (learned; layer 2 switch)

## Media access control
- Wired: **CSMA/CD** (Carrier Sense Multiple Access with Collision Detection) — listen, transmit, detect collisions, send jamming signal
- Wireless (Wi-Fi): **CSMA/CA** (Collision Avoidance) — detecting collisions over radio is hard, so avoid them

## Wired Ethernet
- **IEEE 802.3**; a **layer 2 (data link)** protocol; needs layer 1 hardware
- Topology: logical vs physical

## Wireless Ethernet (Wi-Fi, IEEE 802.11)
- Physical star + logical bus (like hub Ethernet); 2.4 GHz and 5 GHz bands; AP range ~100–150 m; APs use different **channels** to avoid interference
- Association: **active scanning** (NIC sends probe frames) vs **passive scanning** (NIC listens for AP **beacon frames**)
- **DCF** (distributed coordination function, physical carrier sense): CSMA/CA with **stop-and-wait ARQ** (see [[COMP504 Networks/Notes/Ch05 - Transport Layer Part 1|Ch05 ARQ]])
- **PCF** (point coordination function, virtual carrier sense): solves the **hidden node problem**; **RTS/CTS** controlled access
- Versions: 802.11n (older) · 802.11ac (dual-band) · **802.11ax (Wi-Fi 6)**

## WLAN security (see also [[COMP504 Networks/Notes/Ch11 - Network Security|Ch11]])
- **WEP** — weak, easily cracked · **WPA** — longer key, changed per frame · **802.11i / WPA2** — AES, login server for master key · **MAC address filtering** — weak against determined attackers

## LAN design best practice
- Wired switched Ethernet for desktops + Wi-Fi **overlay** for mobile
- **Managed APs** wired into a **Wi-Fi controller** (load-balances clients)
- **Data center**: server farms/clusters behind a **load balancer**

## Improving LAN performance
- Find the **bottleneck** (server or circuit) first
- Server: faster NOS, second server, more memory/disks, **RAID**
- Circuit: bigger circuit, **segment the network** (more switches / more AP channels)
- Reduce demand: move files to clients, shift wired↔wireless, move demand off peak
- **Server virtualization** · **Storage area network (SAN)** / **NAS**

## Optional extra material
- Switch modes: **cut-through** (low latency), **store-and-forward** (error-checked), **fragment-free** (first 64 bytes)
- Domains/forests (Active Directory) · e-commerce edge · **SOHO** environments · powerline networking · site survey (50-ft radius per AP)

## Related
- [[COMP504 Networks/Notes/Ch01 - Introduction|Ch01]] (standards IEEE 802.3/802.11) · [[COMP504 Networks/Notes/Ch05 - Transport Layer Part 2|Ch05 Part 2]] (MAC addressing) · [[COMP504 Networks/Notes/Ch08 - Backbone Networks|Ch08]] · [[COMP504 Networks/Notes/Ch09 - Wide Area Networks|Ch09]] · [[COMP504 Networks/Notes/Ch11 - Network Security|Ch11]] · [[COMP504 Networks/Labs/Lab 01 - Ethernet Cable Configuration.pptx|Ethernet cable lab]] · [[COMP504 Networks/Index|Course index]]
