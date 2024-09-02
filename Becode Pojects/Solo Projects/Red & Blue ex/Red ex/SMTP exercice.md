[Exercice Link](https://github.com/becodeorg/BXL-k4MK4r-2/blob/main/content/07-Red/Pentest/01-Informations_Gathering/Active/smtp.md)

#### 1. How many commands are allowed on port 25?

> ```bash
> nmap --script smtp-commands -p 25 10.12.1.36
> ```
> 
> **Ex Output**:
> ```plaintext
> PORT   STATE SERVICE
> 25/tcp open  smtp
> | smtp-commands: 
> |   10.12.1.36:
> |     EHLO
> |     HELO
> |     MAIL
> |     RCPT
> |     DATA
> |     RSET
> |     NOOP
> |     QUIT
> |     VRFY
> |_    EXPN
> 
> ```
> 
> - Response (Count the commands listed in the output) 
---

#### 2. How many users can you enumerate via port 25?

> For user enumeration on an SMTP server, you can use a tool like `smtp-user-enum`.
> 
> ```bash
> smtp-user-enum -M VRFY -U users.txt -t 10.12.1.36
> ```
> - Replace `users.txt` with a file containing potential usernames to enumerate. 
> 
> **Ex Output**:
> ```plaintext
> smtp-user-enum v1.0 ( http://pentestmonkey.net/tools/smtp-user-enum )
> 
> |----------------+-----------+------+-----------+-----------------+---------------|
> |               User                |    Result                 |
> |----------------+-----------+------+-----------+-----------------+---------------|
> | user1 | User exists           |
> | user2 | User exists           |
> | user3 | User does not exist   |
> | user4 | User exists           |
> | user5 | User does not exist   |
> |----------------+-----------+------+-----------+-----------------+---------------|
> 
> ```
> 
> - Response 3 users exist (Based on the example output).
---
#### 3. Send a mail from`admin@local` to `root@local` trough SMTP.

> To send an email via the SMTP server, you can manually connect using `telnet` or `nc` (netcat).
> ```bash
> telnet 10.12.1.36 25
> ```
> or
> ```bash
> nc 10.12.1.36 25
> ```
> 
> 
> **Ex SMTP Session**:
> ```plaintext
> 220 mail.example.com ESMTP Postfix
> HELO local
> 250 mail.example.com
> MAIL FROM: <admin@local>
> 250 2.1.0 Ok
> RCPT TO: <root@local>
> 250 2.1.5 Ok
> DATA
> 354 End data with <CR><LF>.<CR><LF>
> Subject: Test Email
> 
> This is a test email.
> .
> 250 2.0.0 Ok: queued as 12345
> QUIT
> 221 2.0.0 Bye
> 
> ```
> 
> - Response The email will be queued and delivered if all steps are completed successfully.
---
[[OSINT Active|Back to OSINT Active]]