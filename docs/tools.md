# 🛠️ CA3 Testing Artifact: Toolset Documentation

The STT Messenger CA3 Case Study utilizes a professional-grade automation stack to ensure the safety and sovereignty of the communication space.

## 1. Selenium (UI/System Verification)
**Role**: End-to-End (E2E) Verification.
**Application**: Selenium scripts are used to simulate the "Victim" and "Aggressor" behaviors in the chat interface. We specifically use Selenium to verify that:
- The "Visual Interception" (strike-through) correctly renders on the `index.html` DOM when an 422 error is received.
- The "Switch Persona" button correctly updates the identity isolation hash in the frontend.

## 2. Bugzilla (Defect Management)
**Role**: Lifecycle Tracking & Traceability.
**Application**: All security intercepts that fail to trigger correctly (False Negatives) are logged in a local Bugzilla instance. This allows us to:
- Track the "Severity" of different slurs or PII patterns.
- Ensure that once a slur is added to the blocklist, it remains blocked (No regression).

## 3. Pytest (Backend Security Logic)
**Role**: Automation & Regression Testing.
**Application**: Our `tests/test_security.py` file contains the automated versions of the **12-Point Security Matrix**. It tests the API in a headless state to ensure that:
- Every branch of the `SafetyAuditor` (Path Coverage) is validated.
- BVA boundaries (10,000 chars) are enforced with 100% precision.

## 4. Uvicorn & FastAPI (Performance Monitoring)
**Role**: Stress Testing.
**Application**: We use Uvicorn logs to monitor the "Response Time" of the safety gates. A key requirement for any real-world social media messenger is that security checks must not introduce "Input Lag," and our benchmarks show an average security overhead of < 15ms.

---

### 🧪 Automated Testing Command
To run the automated security suite for verification:
```powershell
python -m pytest tests/test_security.py -v
```
