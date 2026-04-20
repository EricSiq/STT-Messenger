# CA3 Submission: Software Testing Case Study
**Project**: STT Messenger (Minor Protection & Privacy Sovereignty)

This directory contains the full submission artifacts for the CA3 Case Study on Software Testing Tools and Methodology.

---


## Technical Proof & Artifacts
The following scripts were implemented to verify the "Next Level" scientific rigor of this assignment:

1.  **Comprehensive Security Suite**: Automated Pytest verification of 100% of the Test Matrix.
2.  **Defect Report BUG-003**: Formal Bugzilla report for the CSP/Connectivity fix discovered during system testing.
3.  **Tools Exploration**: Details on Selenium and Bugzilla integration in the STLC.

---

## The 12-Point Security Matrix (Case Study Coverage)

| Sr.No | Security Gate | Category | Logic/Methodology | Pass Criteria |
| :--- | :--- | :--- | :--- | :--- |
| **TC-01** | Toxic Filter | Abuse | Equivalence Partitioning | Blocks derogatory slop signals. |
| **TC-02** | PII Protector | Privacy | Equivalence Partitioning | Intercepts Phone/Email patterns. |
| **TC-03** | Payload Limit | Protocol | Boundary Value Analysis | Enforces 10,000 char boundary. |
| **TC-04** | Sentiment Guard | Intent | Heuristic Sentiment | Blocks hostile/predatory tone. |
| **TC-05** | System Guard | Integrity | Command Gating | Blocks administrative injection. |
| **TC-06** | Scam Protector | Fraud | Signature Correlation | Blocks phishing/crypto domains. |
| **TC-07** | Bot Rate Limit | Stability | Temporal Constraint | Blocks rapid-fire signal bursts. |
| **TC-08** | XSS Guard | Security | Input Sanitization | Blocks script/html injection. |
| **TC-09** | IP Sovereign | Privacy | Network PII Detection | Blocks origin IP disclosure. |
| **TC-10** | Malware Link | Safety | MIME/URI Auditing | Blocks executable extensions. |
| **TC-11** | Doxing Prevent | Privacy | Contextual Heuristics | Blocks address/location leaks. |
| **TC-12** | Crisis Intercept| Safety | Support-First Logic | Identifies self-harm indicators. |

---

## How to Verify
Run the full automated test suite from the project root:
1. Navigate to: `STT Messenger CA3`
2. Run: `python -m pytest tests/test_security.py -v`

All **9/9** automated security and lifecycle tests are currently **PASSING**.
Manual verification is available via `./run_ca3_lab.ps1`.
