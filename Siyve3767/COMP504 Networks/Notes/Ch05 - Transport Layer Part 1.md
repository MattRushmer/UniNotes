---
tags:
  - comp504
  - networks
  - lecture
  - tcp-ip
  - exam-topic
---

# Ch05 - Network and Transport Layers (Part 1): TCP/IP

> Auto-extracted from [[COMP504 Networks/Lectures/Ch05 - Transport Layer Part 1.pptx|Ch05 - Transport Layer Part 1.pptx]]
> Source text: *Business Data Communications and Networking*, 14th ed, Chapter 5

## TCP/IP protocol suite
- Transport and network layers are closely tied; **TCP/IP** (Internet Protocol Suite) is the dominant protocol family
- Developed for **ARPANET** (US DoD) by Vinton Cerf and Bob Kahn in **1974**; used on the Internet and almost all backbones/WANs
- Two parts: **TCP** = transport layer protocol linking application to network · **IP** = routes messages to the final destination
- Transport layer links application software, provides **end-to-end delivery**, and **segments** messages

## TCP
- **Connection-oriented**; PDU = **TCP segment** with a 20-byte header (excluding options); typical header described as 192-bit
- Key header fields: **source port**, **destination port**, **sequence number** (for reassembly)

## UDP
- **Connectionless**, **best-effort** delivery — no acknowledgment; PDU = **datagram**
- Only four fields (8 bytes overhead): source port, destination port, length, CRC-16
- Used for small single packets, e.g. a **DNS request**

## IP (network layer)
- Network layer PDU = **packet**
- **IPv4**: 32-bit addresses, ~4.2 billion (some reserved) — being replaced by **IPv6**: 128-bit addresses (~3.4 × 10³⁸), 40-byte header
- Main IPv6 driver: address exhaustion (see [[COMP504 Networks/Notes/Number Systems|Number Systems]] for the binary/hex side of addressing)

## Transport layer functions
- **Linking to the application layer**: TCP/UDP use **port numbers** for simultaneous conversations; well-known ports — HTTP **80**, FTP **21**, Telnet **23**, SMTP **25**
- **Segmenting**: break large application messages into smaller segments, reassemble at the destination
- **Session management**: connection-oriented (session = conversation, established with **SYN/ACK**) vs connectionless messaging

## ARQ — Automatic Repeat reQuest
- On error, the receiver asks the sender to retransmit; two types:
  - **Stop-and-wait ARQ**: sender waits after each packet; receiver replies **ACK** or **NAK** (half-duplex flow)
  - **Continuous ARQ** (sliding window, full-duplex, provides flow control): **Selective-Repeat ARQ / LAP-M** (only errored packets resent) or **Go-Back-N** (error packet + all after it resent)
- Session termination uses a **four-way handshake**

## Quality of Service (QoS)
- Connection-oriented messaging with assigned priorities / classes of service
- **RSVP** and **RTSP**: request a connection with a guaranteed minimum data rate
- **RTP**: transports real-time packets; RTP packets are wrapped in UDP datagrams

## Exam-spotlight (from the in-deck quizzes)
- The transport layer links application layer to the network and handles end-to-end delivery — **routing is NOT a transport function** (that's the network layer)
- TCP/IP was developed for ARPANET in 1974 · typical TCP segment header = 192-bit · stop-and-wait ARQ = half duplex

## Related
- [[COMP504 Networks/Notes/Ch01 - Introduction|Ch01 - Introduction]] (layers) · [[COMP504 Networks/Notes/Ch05 - Transport Layer Part 2|Ch05 Part 2]] · [[COMP504 Networks/Notes/Number Systems|Number Systems]] · [[COMP504 Networks/Notes/Default Gateway|Default Gateway]] · [[COMP504 Networks/Index|Course index]]
