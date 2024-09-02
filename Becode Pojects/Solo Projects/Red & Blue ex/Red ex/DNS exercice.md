[Exercice Link](https://github.com/becodeorg/BXL-k4MK4r-2/blob/main/content/07-Red/Pentest/01-Informations_Gathering/Active/dns.md)


#### 1. Find the IP address of `adlp-corp.com`

^885a99

>```bash
>nslookup adlp-corp.com
>```
---
#### 2. Find the TXT record of `adlp-corp.com`

>```bash
>nslookup -query=TXT adlp-corp.com
>```
---
#### 3. Find the MX records of `becode.org`

>```bash
>nslookup -query=MX becode.org
>```
---
#### 4. Find the MX records of `adlp-corp.com`

>```bash
>nslookup -query=MX adlp-corp.com
>```
---
#### 5. Find the first NS name server of `adlp-corp.com`

>```bash
>nslookup -query=NS adlp-corp.com
>```
---
#### 6. Use a brute force tool to find subdomains of `adlp-corp.com`

>```bash
>pip install sublist3r
>```
>
>```bash
>sublist3r -d adlp-corp.com
>```
---
#### 7. Use theHarvester tool to find Linkedin users for `becode.org`

>```bash
>pip install theHarvester
>```
>
>```bash
>theHarvester -d becode.org -b linkedin
>```
---
#### 8. Use theHarvester tool to find IP addresses for `becode.org`

>```bash
>theHarvester -d becode.org -b all
>```
---
#### 9. Script to attempt a zone transfer from `adlp-corp.com`

>```python
>import dns.query
>import dns.zone
>
>domain = "adlp-corp.com"
>ns_server = "ns1.adlp-corp.com"  # Replace with actual NS server if known
>
>try:
>    zone = dns.zone.from_xfr(dns.query.xfr(ns_server, domain))
>    for name, node in zone.nodes.items():
>        print(zone[name].to_text(name))
>except Exception as e:
>    print(f"Zone transfer failed: {e}")
>```
---
#### 10. Script to attempt a brute force search for subdomains

>```python
>import subprocess
>
>domain = "adlp-corp.com"
>command = ["sublist3r", "-d", domain]
>
>try:
>    result = subprocess.run(command, capture_output=True, text=True)
>    print(result.stdout)
>except Exception as e:
>    print(f"Brute force search failed: {e}")
>```
---


[[OSINT Active|Back to OSINT Active]]