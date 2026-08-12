---
tags:
  - comp504
  - networks
  - lecture
  - exam-topic
---

# Ch01 - Introduction to Data Communications

> Auto-extracted from [[COMP504 Networks/Lectures/Ch01 - Introduction.pptx|Ch01 - Introduction.pptx]]
> Source text: *Business Data Communications and Networking*, 14th ed — FitzGerald, Dennis & Durcikova (Wiley, 2021), Chapter 1

## 1.1 Why networks matter
- Data communications collapse the "information lag" to Internet speeds — communicate/access information anywhere
- Three fundamental questions: how the Internet works · how to design a network · how to manage/secure it
- Four industrial revolutions; the 4th merges physical/digital/biological worlds, rooted in the Internet and digitization

## 1.2 Data communications networks
- **Data communications**: movement of computer information via electrical or optical transmission systems
- Three basic hardware components:
  - **Server** — stores data/software accessed by clients (file server, web server, mail server)
  - **Client** — input/output hardware at the user's end
  - **Circuit** — the pathway messages travel
- A network without a server = **peer-to-peer network**
- LAN example: clients connected via a **switch** and cables; wireless via **wireless access point (AP)**; a **router** connects two or more networks
- End devices (message source/destination) vs **intermediary devices** (switches, APs, routers — regenerate/retransmit signals, track paths, report errors)

## Types of networks
- **LAN** — computers in the same general area (~100 Mbps)
- **Backbone network (BN)** — larger central network connecting LANs, other BNs, MANs, WANs (100–1,000 Mbps) → see [[COMP504 Networks/Notes/Ch08 - Backbone Networks|Ch08]]
- **WAN** — connects BNs and MANs; most orgs don't build their own → see [[COMP504 Networks/Notes/Ch09 - Wide Area Networks|Ch09]]
- **Intranet** — LAN using Internet technologies, internal only · **Extranet** — same technologies, but for invited outside users (customers/suppliers) over the Internet

## 1.3 Network models and layers
- Communications functions split into **layers**; the two key models are the **OSI** model and the **Internet model (TCP/IP)**
- **OSI Reference Model** (ISO, 1984): 7 layers — Physical, Data Link, Network (routing), Transport (end-to-end), Session, Presentation, Application
- **Internet model (TCP/IP)**: 5 layers — Physical, Data Link, Network (IP routing), Transport (TCP), Application
- **Encapsulation**: each layer wraps the PDU of the layer above (Russian-doll style); **PDU** (packet) = data + control info; data-link PDU = **frame**; transport PDU = **segment**
- Example of layered transmission: HTTP (application) → [[COMP504 Networks/Notes/Ch05 - Transport Layer Part 1|TCP]] → IP → Ethernet frame
- **Protocol** = formal set of rules defining what a layer does
- Pros of layers: modularity + vendor interoperability via standards · Cons: some inefficiency (many PDUs/software per message)

## 1.4 Network standards
- Purpose: multi-vendor interoperability, avoid vendor lock-in, develop software/hardware one layer at a time
- **De jure** (official/formal) vs **de facto** (marketplace) standards
- Bodies: **ISO** · **ITU-T** · **ANSI** · **IEEE** (IEEE 802.3 Ethernet, 802.11 wireless LAN — see [[COMP504 Networks/Notes/Ch07 - Wired and Wireless LANs|Ch07]]) · **IETF**

## 1.5 Trends and 1.6 security
- **BYOD** (bring your own device) and wireless LAN growth
- **Internet of Things (IoT) / Network of Things (NoT)** — smart devices as network nodes
- Massively online games and education
- More network demand → more need for secure storage, server space, and data transfer → see [[COMP504 Networks/Notes/Ch11 - Network Security|Ch11]]

## Related
- [[COMP504 Networks/Notes/Number Systems|Number Systems]] · [[COMP504 Networks/Notes/Default Gateway|Default Gateway]] · [[COMP504 Networks/Index|Course index]]
