# STT Messenger | CA3 Software Testing Case Study

![Security Banner](https://img.shields.io/badge/Security-Hardened-green?style=for-the-badge)
![Testing Matrix](https://img.shields.io/badge/CA3--Matrix-12--Point-blue?style=for-the-badge)

**STT Messenger** is a high-fidelity demonstration project for the CA3 Software Testing case study. It showcases how modern social media platforms can use rigorous testing methodologies—such as **Equivalence Partitioning (EP)**, **Boundary Value Analysis (BVA)**, and **Path Coverage**—to protect minors and vulnerable populations from toxic content and privacy leaks.

## 🚀 Key Features
- **12-Point Security Matrix**: Comprehensive protection against Slurs, PII, Scams, Malware, XSS, and more.
- **NeuroSymbolic Safety Auditor**: A backend engine that normalizes and intercepts malicious signals.
- **Visual Interception UI**: Real-time "Blocked" feedback in the chat interface.
- **Identity Isolation**: Secure multi-persona simulation.

## 📁 Repository Structure
- **`/backend`**: FastAPI security daemon with the `SafetyAuditor` engine.
- **`/frontend`**: High-fidelity "Methodology Showcase" dashboard.
- **`/tests`**: Automated Pytest suite with 100% security path coverage.
- **`/docs`**: Complete CA3 submission artifacts (Poster, Report, Tools, Defect Logs).

## 🧪 Quick Launch (Secure Lab)
To launch the interactive testing suite and the messenger environment:
```powershell
./run_ca3_lab.ps1
```

## 📖 Evaluation Documentation
For evaluators, please refer to the following documents for rubric compliance:
1. [🖼️ Case Study Poster](docs/poster.md) - System Overview & Strategy.
2. [📝 Technical Report](docs/technical_report.md) - Methodology & 12-Point Matrix.
3. [🛠️ Toolset Guide](docs/tools.md) - Automation with Selenium & Bugzilla.
4. [🐞 Defect Case Study](docs/defect_report_001.md) - Bug Lifecycle & Analysis.

---
**Focus Area**: Protecting minors from toxic slop and PII leaks through scientific software testing.
