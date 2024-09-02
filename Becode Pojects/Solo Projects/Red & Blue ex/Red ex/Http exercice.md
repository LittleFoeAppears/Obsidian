[Exercice Link](https://github.com/becodeorg/BXL-k4MK4r-2/blob/main/content/07-Red/Pentest/01-Informations_Gathering/Active/http.md)

#### 1. How many files could you find on port 80?

```bash
gobuster dir -u http://10.12.1.42 -w /usr/share/wordlists/dirb/common.txt
```
---
#### 2. What is the version of Apache?

```bash
nmap -p 80 --script=http-server-header 10.12.1.42
```
---
#### 3. What is the version of PHP?

```bash
nikto -h http://10.12.1.42
```
---
#### 4. What server extension is installed?

```bash
nikto -h http://10.12.1.42
```
---
#### 5. What is the name of the file in `testoutput`?

```bash
gobuster dir -u http://10.12.1.42/testoutput -w /usr/share/wordlists/dirb/common.txt
```
---
#### 6. Do a scan with Nikto on port 80.

```bash
nikto -h http://10.12.1.42
```
---
#### 7. An informative file in PHP seems to be available, what is its name?

```bash
gobuster dir -u http://10.12.1.42 -w /usr/share/wordlists/dirb/common.txt -x php
```
---
#### 8. What application has a name that starts with T and ends with Y?

- Install the Wappalyzer extension in your browser and visit `http://10.12.1.42`.
---
#### 9. What curl command can you use to see the server version?

```bash
curl -I http://10.12.1.42
```
---
#### 10. What tool for enumerating files does it do recursively? (By default)

- Response: `Dirbuster` (by default performs recursive directory enumeration).
---
#### 11. What other administration application is currently also on port 80?

- Install/use Wappalyzer extension in your browser and visit `http://10.12.1.42`.
---

[[OSINT Active|Back to OSINT Active]]