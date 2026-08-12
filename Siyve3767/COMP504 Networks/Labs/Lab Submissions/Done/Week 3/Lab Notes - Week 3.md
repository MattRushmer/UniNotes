---
tags:
  - comp504
  - networks
  - lab
  - switches
  - exam-topic
---

# Week 3 Lab — Configure Initial Switch Settings

> Assistance note for [[COMP504 Networks/Labs/Lab Submissions/Done/Week 3/2.5.5 Packet Tracer - Configure Initial Switch Settings.docx|2.5.5 Configure Initial Switch Settings.docx]] — **status: DONE, answers filled in** ✅

## What this lab covers
- Cisco IOS **configuration modes**: user EXEC (`Switch>`), privileged EXEC (`Switch#`), global config (`Switch(config)#`), config-line
- Securing **console** and **privileged** access with passwords + the `login` command
- **MOTD banner**, saving config to **NVRAM** (`copy running-config startup-config`)

## Key commands to remember (exam gold)
```
Switch> enable
Switch# configure terminal
Switch(config)# hostname S1
Switch(config)# line console 0
Switch(config-line)# password letmein
Switch(config-line)# login
Switch(config)# enable password c1$c0
Switch(config)# banner motd #Unauthorized access prohibited#
Switch# copy running-config startup-config
Switch# show running-config     # view live config (in RAM)
Switch# show startup-config     # view saved config (in NVRAM)
```

## Your answers (verified present)
- 24 FastEthernet + 2 Gigabit interfaces; vty lines 0-15
- `show startup-config` returns "not present" because nothing is saved to NVRAM yet
- The `login` command is required because `password` alone just stores the password — `login` makes the switch actually prompt for it

## Related vault notes
- [[COMP504 Networks/Notes/Ch07 - Wired and Wireless LANs|Ch07 - LANs]] — switch fundamentals
- [[COMP504 Networks/Notes/Ch01 - Introduction|Ch01 - Introduction]] — network device roles
