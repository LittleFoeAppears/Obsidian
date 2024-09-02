[Exercice Link](https://github.com/becodeorg/BXL-k4MK4r-2/blob/main/content/07-Red/Pentest/01-Informations_Gathering/Active/other.md)

#### 1. How many users can you find?

> ```bash
> rpcclient -U "" -N 10.12.1.36
> ```
> 
> Once connected, use the following command:
> ```
> enumdomusers
> ```
> 
>> Ex Output:
>> ```plaintext
>> user:[msfadmin] rid:[0x1f4]
>> user:[guest] rid:[0x1f5]
>> ...
>> 
>> ```
---
#### 2. What is the RID of msfadmin?

> ```
> queryuser msfadmin
> ```
>> Ex Output:
>> ```plaintext
>> User Name   :   msfadmin
>> Full Name   :   Msf Admin
>> Home Drive  :   \\10.12.1.36\msfadmin
>> Profile Path:   \\10.12.1.36\profiles\msfadmin
>> ...
>> Password last set time :  Thu, 11 Aug 2022 10:15:55 GMT
>> Password can change time :  Thu, 11 Aug 2022 10:15:55 GMT
>> Password must change time :  Fri, 11 Feb 2023 10:15:55 GMT
>> ```
---
#### 3. What is the path of msfadmin's profile?

> ```
> queryuser msfadmin
> ```
---
#### 4. When did msfadmin last change password?

> ```
> queryuser msfadmin
> ```
---
#### 5. When should msfadmin change its password?

> ```
> queryuser msfadmin
> ```
---

[[OSINT Active|Back to OSINT Active]]