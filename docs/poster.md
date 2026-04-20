# Component A: CA3 Poster - STT Messenger Safety Case Study

## 1. System Overview
STT Messenger is a sovereign communication platform designed to protect vulnerable users from toxic content and data leakage. The application features a real-time security auditor that intercepts malformed or malicious signals before database persistence.

## 2. Key Functionalities
* NeuroSymbolic Safety Auditor: A logic engine that evaluates message toxicity and sentiment.
* Privacy Guard: Automated PII and Doxing detection for physical and digital identifiers.
* Content Sovereignty: Encryption simulation of stored message contents.

## 3. Testing Strategy
The project follows a multi-level testing strategy to ensure safety requirements are met.

* Functional testing: Validating the 12 security gates.
* Regression testing: Automated verification of security patches.
* Integration testing: Verification of the backend API and frontend visual interception.

## 4. Test Case Design
The system utilize the following academic testing techniques.

* Black-box testing: Equivalence Partitioning and Boundary Value Analysis for content validation.
* White-box testing: Path coverage analysis of the SafetyAuditor logic branches.

## 5. Sample Test Cases

| Case Number | Description | Input | Expected Output | Status |
| :--- | :--- | :--- | :--- | :--- |
| TC-01 | Toxic Content | "bastard" | 422 Blocked | Passed |
| TC-02 | PII Protection | "9850593788" | 422 Blocked | Passed |
| TC-03 | Max Payload | Len: 10001 | 422 Blocked | Passed |
| TC-08 | XSS Injection | "<script>" | 422 Blocked | Passed |
| TC-11 | Doxing Guard | "Live at Flat 4" | 422 Blocked | Passed |
| TC-12 | Crisis Safety | "harm myself" | 422 Blocked | Passed |

## 6. Defect Analysis and Tools
The defect lifecycle involves identification, root cause analysis, fix implementation, and regression verification.

* Selenium: Cross-browser system testing for UI reliability.
* Bugzilla: Traceability and defect lifecycle management.
* Pytest: Core automation for security logic regression.
