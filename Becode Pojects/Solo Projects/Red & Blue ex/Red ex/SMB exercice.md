[Exercice Link](https://github.com/becodeorg/BXL-k4MK4r-2/blob/main/content/07-Red/Pentest/01-Informations_Gathering/Active/smb.md)

#### 1. What is the OS?

> ```bash
> nmap -O 10.12.1.36
> ```
---
#### 2. What is the version of Samba on the box?

> ```bash
> nmap -p 139,445 --script=smb-os-discovery 10.12.1.36
> ```
---
#### 3. How many group names are there? (use nbtstat)

> ```bash
> nbtstat -A 10.12.1.36
> ```
---
#### 4. What is the FQDN?

> ```bash
> nmap --script=dns-brute 10.12.1.36
> ```
---
#### 5. What is the Netbios computer name?

> ```bash
> nbtstat -A 10.12.1.36
> ```
---
#### 6. How many disks are shared?

> ```bash
> smbclient -L 10.12.1.36 -N
> ```
---
#### 7. Which one is available for reading and writing?

> ```bash
> smbclient //10.12.1.36/share -N (Replace "share" with actual shared disk)
> ```
---
#### 8. What flag did you find when you logged in?

> ```bash
> smbclient //10.12.1.36/share -N (Replace "share" with actual shared disk)
> ```
---
#### 9. What is the path that begins with c:\ in this file?

> ```bash
> smbclient //10.12.1.36/share -N (Replace "share" with actual shared disk)
> ```
---
#### 10. How many users can you find?

> ```bash
> enum4linux -U 10.12.1.36
> ```
---

[[OSINT Active|Back to OSINT Active]]
