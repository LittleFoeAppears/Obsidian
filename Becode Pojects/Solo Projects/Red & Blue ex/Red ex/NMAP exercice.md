[Exercice Link](https://github.com/becodeorg/BXL-k4MK4r-2/blob/main/content/07-Red/Pentest/01-Informations_Gathering/Active/nmap.md)

#### 1. How many TCP ports are open on the box?

> ```bash
> nmap -sT <target-ip>
> ```
> 
> - Response: The number of open TCP ports from the scan result.
---
#### 2. How many UDP ports are open on the box?

> ```
> nmap -sU <target-ip>
> ```
> 
> - Response: The number of open UDP ports from the scan result.
---
#### 3. What is the version of FTP?

> ```bash
> nmap -sV -p 21 <target-ip>
> ```
> 
> - Response: The version of FTP from the scan result.
---
#### 4. What is the version of SSH?
 
> ```bash
> nmap -sV -p 22 <target-ip>
> ```
> 
> - Response: The version of SSH from the scan result.
---
#### 5. What is the version of Apache?

> ```bash
> nmap -sV -p 80 <target-ip>
> ```
> 
> - Response: The version of Apache from the scan result.
---
#### 6. Is anonymous FTP access allowed on the box?

> ```bash
> nmap -p 21 --script=ftp-anon <target-ip>
> ```
> 
> - Response: Whether anonymous FTP access is allowed from the scan result.
---
#### 7. Do a SYN scan.

> ```bash
> nmap -sS <target-ip>
> ```
> 
> - Response: SYN scan result.
---
#### 8. Do a scan that bypasses a firewall.

> ```bash
> nmap -Pn <target-ip>
> ```
> 
> - Response: Scan result that bypasses the firewall.
---
#### 9. Run a scan with the default NSE scripts.

> ```bash
> nmap -sC <target-ip>
> ```
> 
> - Response: Scan result with the default NSE scripts.
---
#### 10. What service occupies port 8180?

> ```bash
> nmap -sV -p 8180 <target-ip>
> ```
> 
> - Response: The service occupying port 8180 from the scan result.
---
#### 11. What is the salt of the MySQL service?

> ```bash
> nmap --script=mysql-info <target-ip>
> ```
> 
> - Response: The salt of the MySQL service from the scan result.
---
#### 12. What is the domain name?

> ```bash
> nmap --script=dns-brute <target-ip>
> ```
> 
> - Response: The domain name from the scan result.
---
#### 13. What is the FQDN of the box?

> ```bash
> nmap --script=dns-brute <target-ip>
> ```
> 
> - Response: The FQDN of the box from the scan result.
---
#### 14. What is the OS version?

> ```bash
> nmap -O <target-ip>
> ```
> 
> - Response: The OS version from the scan result.
---
#### 15. What is the version of Samba?

> ```bash
> nmap -p 139,445 --script=smb-os-discovery <target-ip>
> ```
> 
> - Response: The version of Samba from the scan result.
---
#### 16. What is the name of the box?

> ```bash
> nmap -sP <target-ip>
> ```
> 
> - Response: The name of the box from the scan result.
---
#### 17. Do a scan on the subnet 10.xx.1.0/24. How many IP addresses respond?

> For Charleroi:
> 
> ```bash
> nmap -sP 10.11.0.1/24
> ```
> 
> For Bruxelles:
> 
> ```bash
> nmap -sP 10.12.0.1/24
> ```
> 
> For Ghent:
> 
> ```bash
> nmap -sP 10.13.0.1/24
> ```
> 
> - Response: The number of IP addresses that respond from the scan result.
---
#### 18. Do the same thing but with the top port option at 10.

> For Charleroi:
> 
> ```bash
> nmap --top-ports 10 10.11.0.1/24
> ```
> 
> For Bruxelles:
> 
> ```bash
> nmap --top-ports 10 10.12.0.1/24
> ```
> 
> For Ghent:
> 
> ```bash
> nmap --top-ports 10 10.13.0.1/24
> ```
> 
> - Response: The result of the scan using the top port option.
---

[[OSINT Active|Back to OSINT Active]]