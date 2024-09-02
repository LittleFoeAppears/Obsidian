---

---
---
# 1. Security
#### <span style="color:#9a58fe">**DiD** *(Defense in Depth)*</span> 
> - <span style="color:#787878">Definition:</span>
> Multiple layers of defense to protect info and sys. 
> If one fails, others still provide some protection.
>  ---
>  
> - <span style="color:#787878">Layers (5):</span>
>       - **Physical Security :** `locks, security cam, access control systems`
>       - **Network Security :** `firewalls, IDS (intru detect sys), VPN`
>       - **Host Security :** `antivirus, HIPS (host-based intru prevention sys)`
>       - **Application Security :** `coding practice, app firewalls, security tests, etc`
>       - **Data Security :** `encryption, data masking, access controls sensitive data`
>  
> ---


#### <span style="color:#9a58fe">**Zero Trust Model**</span>
>  - <span style="color:#787878">Definition:</span>
> Never automatically trust anything inside or outside.
> Verification required for everyone attempting to access resources.
>   ---
> 
> - <span style="color:#787878">Principles (3):</span>
>       - **Assume Breach :** `operate like you have already been compromised`
>       - **Verify Explicitly :** `authenticate using every available data points`
>       - **Least Privilege Access :** `use JIT+JEA (just-in-time, just-enough-access), risk-based adaptive policies, and data protection for minimal access possible`
> --- 

---
# 2. Compliance
#### <span style="color:#9a58fe">**Governance**</span>
> - <span style="color:#787878">Definition:</span>
> Process of defining rules, roles, responsibilities, decision-making.
>  ---
> 
> - <span style="color:#787878">Key Aspects (2):</span>
>       - **Frameworks :** `implementing frameworks like COBIT, ISO 27001, ITIL`
>       - **Policies and Procedures :** `clear policies/procedures = compliance and manage risks`
> ---

#### <span style="color:#9a58fe">**Risk Management**</span>
> - <span style="color:#787878">Definition:</span>
> Process of identifying, assessing, and controlling threats from financial uncertainty, legal liabilities, strategic management errors, accidents, natural disasters, etc.
>   ---
> - <span style="color:#787878">Process (3):</span>
>       - **Identification :** `what could affect org`
>       - **Assessment :** `analyse identified risks`
>       - **Mitigation :** `measures to minimize or eliminate impact`
> ---

#### <span style="color:#9a58fe">**Compliance**</span>
> - <span style="color:#787878">Definition:</span>
> Operate within legal and regulatory framework following laws, regulations, guidelines, and relevant specifications.
>   ---
> - <span style="color:#787878">Key Areas (3):</span>
>       - **Data Residency :** `regulations to where data can be stored and processed`
>       - **Data Sovereignty :** `laws that determine how data is subject to country's law`
>       - **Data Privacy :** `ensure protection of personal data following regulations like GDPR and CCPA`
> ---

---
# 3. Identity Concepts
#### <span style="color:#9a58fe">**Identity as the Perimeter**</span>
> - <span style="color:#787878">Definition:</span>
> Since mobile and cloud network perimeter has dissolved. Identity is the new perimeter, so protecting user identities is crucial to secure access.
>   ---
> - <span style="color:#787878">Key Components (3):</span>
>       - **IdPs (Identity Providers) :** `services for id info and authentication like Microsoft Entra ID, Google Identity, Facebook Login`
>       - **Authentication :** `verifying id of user or sys. like passwords, biometrics, MFA (multi-factor auth), etc`
>       - **Authorization :** `what a authenticated user is allowed to do via roles and permissions`
> ---

#### <span style="color:#9a58fe">**Encryption**</span>
> - <span style="color:#787878">Symmetric Encryption:</span>
> Single key used for encryption and decryption. Fast and efficient for large data but need secure key management.
>      <span style="color:#787878">Ex :</span> `AES (Advanced Encryption Standard)`
>   ---
> - <span style="color:#787878">Asymmetric Encryption:</span>
> Pair of keys. Public key for encryption and Private key for decryption. More secure for key exchanges and digital signatures but resource intensive.
>       <span style="color:#787878">Ex :</span> `ECC (Elliptic Curve Cryptography)`
> ---

#### <span style="color:#9a58fe">**Hashing**</span>
> - <span style="color:#787878">Definition:</span>
> One-way cryptographic function to coverts data into a fixed-length string of characters. Used for data integrity and verification.
>        <span style="color:#787878">Ex :</span> `MD5, SHA-256`
>   ---
> - <span style="color:#787878">Characteristics (5):</span>
>       - **Deterministic :** `an input always produce the same output`
>       - **Fixed Length :** `output hash is always same lenght regardless of input`
>       - **Efficient :** `Quick to compute for any given input`
>       - **Preimage Resistant :** `should be impossible to reverse hash to get original input`
>       - **Collision Resistant :** `should be impossible to find two inputs that give same hash`
> ---