---

---

---
# 1. Microsoft Entra ID *(prev. Azure AD)*
#### <span style="color:#9a58fe">**Identity Types**</span> 
> - <span style="color:#787878">Internal Identities (2):</span>
>       - **Employees :** `users made and manage with org Entra ID`
>       - **User Types :** `users made in Entra ID have a UserType set to 'Member'`
>  ---
>  
> - <span style="color:#787878">External Identities (2):</span>
>       - **B2B Collabpration :** `External users (like partneers, vendors) accessing using they own IdPs. Usually have UserType 'Guest'`
>       - **B2C Access Management :** `External Consumers/customers accessing via social or local accounts`
>  
> ---

#### <span style="color:#9a58fe">**Hybrid Identity**</span> 
> - <span style="color:#787878">Definition:</span>
> Combines org AD and cloud services for seamless ID management.
>  ---
>  
> - <span style="color:#787878">Key Components (4):</span>
>       - **Entra Connect :** `sync on-premises AD to Entra ID`
>       - **PHS (Password Hash Sync) :** `sync hashes from org AD to Entra ID login`
>       - **PTA (Pass-trough Auth)  :** `use org AD without storing password hashes in cloud`
>       - **Federation :** `ADFS or other federation services to auth users with org AD`
>  
> ---

#### <span style="color:#9a58fe">**Authentication Methods**</span> 
> - <span style="color:#787878">Passwords:</span>
> Traditional username and password.
>  ---
>  
> - <span style="color:#787878">MFA (multy-fac auth):</span>
> Two or more verification methods. know *(password)*, have *(phone)*, are *(biometrics)*
>       - **Microsoft Authenticator App :** `one-time code or notification for auth`
>       - **Windows Hello for Business :** `passwordless sign-in using bio or PIN`
>       - **FIDO2 Security Keys :** `devices that use cryptography for auth without pass`
>  
> ---

#### <span style="color:#9a58fe">**Conditional Access**</span> 
> - <span style="color:#787878">Definition:</span>
> Controled access based on status conditions like user, location, device, app. Enforces security and restric access as needed.
>  ---
>  
> - <span style="color:#787878">Policy Components (3):</span>
>       - **Assignements :** `policy applies to: users, groups, directory roles`
>       - **Conditions :** `device state, location, sign-in risk, client app, etc`
>       - **Access Controls :** `decides access lvl, like requiring MFA, blocking access, allowing access with conditions`
>  
> ---

#### <span style="color:#9a58fe">**RBAC *(Role-Based Access Control)* **</span> 
> - <span style="color:#787878">Definition:</span>
> Access based on user roles. Fine-grained management with built-in or custom roles.
>  ---
>  
> - <span style="color:#787878">Components (3):</span>
>       - **Roles :** `permissions based on role like Reader, Contributor, Owner`
>       - **Roles Assignments :** `set users, groups, service principals, or managed identities`
>       - **Scope :** `how role applies to management groups, subscription, resource group, resource lvl`
>  
> ---

---
# 2. Identity Governance
#### <span style="color:#9a58fe">**Access Reviews**</span> 
> - <span style="color:#787878">Definition:</span>
> Review users ensure only the right users have access to resources.
>  ---
>  
> - <span style="color:#787878">Purpose:</span>
> Eliminate excessive rights due to changes in job roles, project status, etc.
>  ---
> - <span style="color:#787878">Automation:</span>
> Can be automated in Entra ID for ease compliance and security.
>  
> ---

#### <span style="color:#9a58fe">**PIM (Privileged Identity Management)**</span> 
> - <span style="color:#787878">Definition:</span>
> Manages, control and monitor access to critical resources. Use just-in-time access and ask justification for role activations.
>  ---
>  
> - <span style="color:#787878">Features (4):</span>
>       - **Just-in-Time Access :** `temporary access to resources`
>       - **Approval-Based Access :** `need approval to activate roles`
>       - **Time-Bound Access :** `set start and end dates for access`
>       - **Notification and Audit :** `notification when privileged roles are activated and save an audit trail of actions`
>  
> ---

#### <span style="color:#9a58fe">**Identity Protection**</span> 
> - <span style="color:#787878">Definition:</span>
> Risk-based policies and automated tools to protect id from threats.
>  ---
>  
> - <span style="color:#787878">Key Components (3):</span>
>       - **Risk Detection :** `id sus activities like atypical travel, sign-ins from anonymous IP, leaked credentials`
>       - **Risk Remediation :** `auto response to risks, like asking for MFA, or blocking access`
>       - **Integration with Conditional Access :** `enhance security by using risk signals into conditional access policies`
>  
> ---

---
# 3. Authentication Methods
#### <span style="color:#9a58fe">**Password Protection/Management**</span> 
> - <span style="color:#787878">Global Banned Password List:</span>
> Enforce Microsoft list of known weak passwords.
>  ---
>  
>  - <span style="color:#787878">Custom Banned Password List:</span>
> Allow org list of known weak passwords related.
>  ---
>  
> - <span style="color:#787878">Password Protection for On-Premises AD:</span>
> Extends password protection to org AD environment.
>  
> ---

