# 📝 Component B: Technical Report - Software Testing Life Cycle (STLC)

## 🎯 1. Objective of the Activity
The objective of this case study is to demonstrate the application of high-fidelity software testing methodologies within a modern privacy-first social media ecosystem (**STT Messenger**). 

We specifically explore how rigorous **Black-Box EP/BVA** and **White-Box Path Coverage** can protect minors and vulnerable populations from:
- **Toxic Content**: Intercepting slurs and hate speech semantically.
- **Privacy Leakage**: Detecting PII (Phone/Email/IP/Address) before storage.
- **Hostile Sentiment**: Identifying predatory tones in real-time.

---

## 🏛️ 2. Comprehensive System Architecture
STT Messenger utilizes a **NeuroSymbolic Safety Layer** where every signal sent to the local SQLite database must pass through a 12-stage security pipeline called the `SafetyAuditor`.

### 2.1 Key Design Safeguards
1.  **Input Normalization**: Stripping punctuation and case-consistent auditing to prevent leetspeak bypasses.
2.  **Sovereign Storage**: Messages are never stored in plaintext; the `ENC:` prefix pattern simulates the Content Sovereignty required for private communication.

---

## 🔬 3. Methodology & Test Case Design

### 3.1 Black-Box Technique: Equivalence Partitioning (EP)
We partition the entire string input space into valid and invalid classes. For "Minor Protection," any signal belonging to the "Toxic" or "PII" class is redirected to a 422 Rejection.

### 3.2 Black-Box Technique: Boundary Value Analysis (BVA)
We rigorously test the 10,000-character payload limit. We verify the "Robustness" of the protocol by testing:
- **Min Boundary**: 1 character (Valid).
- **Max Boundary**: 10,000 characters (Valid).
- **Invalid Boundary**: 10,001 characters (Rejected).

### 3.3 White-Box Technique: Control Flow / Path Coverage
Every `if/else` condition in the `backend/main.py` auditor is exercised by our `tests/test_security` suite, ensuring zero dead code in the security pipeline.

---

## 📊 4. The 12-Point Security Matrix (Sample Data)

| Sr.No | Test Case Description | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| 1 | Toxic Slur Detection (EP) | 422 Rejection | 422 Rejection | ✅ PASS |
| 2 | PII Protection (Phone/Email) | 422 Rejection | 422 Rejection | ✅ PASS |
| 3 | Payload Boundary (10k+1) | 422 Rejection | 422 Rejection | ✅ PASS |
| 4 | Hostile Sentiment Guard | 422 Rejection | 422 Rejection | ✅ PASS |
| 5 | System Command Injection | 422 Rejection | 422 Rejection | ✅ PASS |
| 6 | Scam/Phishing Phing Detection| 422 Rejection | 422 Rejection | ✅ PASS |
| 7 | Bot Swarm Rate Limiting | 422 Rejection | 422 Rejection | ✅ PASS |
| 8 | XSS Injection Sanitization | 422 Rejection | 422 Rejection | ✅ PASS |
| 9 | IP Sovereignty Leak (PII) | 422 Rejection | 422 Rejection | ✅ PASS |
| 10 | Malware Signature Detection | 422 Rejection | 422 Rejection | ✅ PASS |
| 11 | Heuristic Doxing Prevention | 422 Rejection | 422 Rejection | ✅ PASS |
| 12 | Support/Crisis Intercept | 422 Rejection | 422 Rejection | ✅ PASS |

---

## 🛑 5. Defect Analysis & Tools Explanation

### 5.1 Defect Lifecycle
We handle all security bugs through a rigorous 6-phase cycle:
1. **New**: Found via automated Pytest or manual lab audit.
2. **Assigned**: Allocated to safety engineers.
3. **Open**: Root cause analysis in the `backend/main.py` layer.
4. **Fixed**: Code patch implemented.
5. **Pending Retest**: Regression suite scheduled.
6. **Closed**: Verified in the production-ready STT Messenger.

### 5.2 Automation Stack
- **Selenium**: Essential for verifying that "Blocked" messages correctly display as **struck-through** on the UI, ensuring user transparency.
- **Bugzilla**: Used to document and audit the history of security intercepts, providing a traceability log for safety auditors.
- **Pytest**: The core engine for our **Regression Testing**, triggering the 12-stage auditor on every build.

---

## 📈 6. Conclusion
By applying scientific software testing (EP, BVA, Path Coverage) at the **System Level**, we have created a messenger that doesn't just "talk" about safety—it mathematically enforces it.
