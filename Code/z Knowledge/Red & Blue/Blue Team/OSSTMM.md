### Overview

The Open Source Security Testing Methodology Manual (OSSTMM) provides a structured approach for security testing. It includes methodologies for physical locations, human interactions, and all forms of communications.

### Key Components

- **Operational Security (OpSec):** Focuses on actual security rather than best practices, ensuring what you have does what it's supposed to do.
- **Attack Surface:** The total exposure an asset has to potential threats, measured as the lack of specific separations and functional controls.
- **Controls:** Measures to protect assets, categorized into Class A (Interactive) and Class B (Process) controls.

### Methodology

- **Quick Start:** Identify what you are testing, how you are testing, the types of controls discovered, and what is not tested.
- **Upgrading from Older Versions:** OSSTMM 3 introduces the RAV (Risk Assessment Values) which provide a factual attack surface metric.
- **Version Information:** OSSTMM 3.02 is the current version.

### Controls

- **Class A (Interactive Controls):**
    
    - **Authentication:** Verifying identities and permissions.
    - **Indemnification:** Legal and third-party assurances.
    - **Resilience:** Maintaining protection despite failures.
    - **Subjugation:** Ensuring interactions occur as per defined processes.
    - **Continuity:** Maintaining interactions despite failures.
- **Class B (Process Controls):**
    
    - **Non-repudiation:** Preventing denial of actions.
    - **Confidentiality:** Ensuring information is not accessible outside intended parties.
    - **Privacy:** Ensuring methods of interaction are not known outside intended parties.
    - **Integrity:** Ensuring assets and processes remain unchanged unless authorized.
    - **Alarm:** Notifying about interactions.

### Limitations

Five categories to describe flaws in security:

- **Vulnerability:** Allows unauthorized access or denial of authorized access.
- **Weakness:** Disrupts Class A controls.
- **Concern:** Disrupts Class B controls.
- **Exposure:** Unjustifiable visibility of targets or assets.
- **Anomaly:** Uncontrolled and unaccounted elements in operations.

### Security and Safety Definitions

- **Security:** Separation between an asset and threats, achieved by moving the asset, changing the threat, or destroying the threat.
- **Safety:** Controls in place to minimize the threat or its effects.

### Reporting and Certification

- **STAR (Security Test Audit Report):** Document the state of the security based on OSSTMM metrics.
- **Certification and Accreditation:** OSSTMM audits can be certified by ISECOM for a factual test, providing clear and measurable results.

### Trust and Metrics

- **Trust Analysis:** Evaluating relationships and interactions within a scope.
- **Operational Security Metrics (RAVs):** Quantifying the attack surface, providing a graphical representation of security state and changes over time.

### Application

- **Comprehensive Testing:** Encompasses Human, Physical, Wireless, Telecommunications, and Data Networks.
- **Legal and Compliance:** Suitable for various regulations and industry standards like PCI-DSS, ISO/IEC standards.

### Conclusion

OSSTMM 3 aims to provide a thorough, unbiased, and scientific approach to operational security testing, ensuring that security measures are practical, verifiable, and effective in real-world operations.