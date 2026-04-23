# STT Messenger | CA3 Software Testing Case Study

STT Messenger is a high fidelity demonstration project for the CA3 Software Testing case study. It showcaseshow modern social media platforms can use rigorous testing methodologies to protect minors and vulnerable populations from toxic content and privacy leaks.

## 1. Key Features
* 12-Point Security Matrix: Comprehensive protection against slurs, PII, scams, malware, and XSS.
* Safety Auditor: A backend engine that normalizes and intercepts malicious signals.
* Visual Interception UI: Real time blocked feedback in the chat interface.

## 2. Repository Structure
* /backend: FastAPI security daemon with the SafetyAuditor engine.
* /frontend: Methodology Showcase dashboard.
* /tests: Automated Pytest suite with 100 percent security path coverage.
* /docs: CA3 submission artifacts including the Technical Report and Poster.

## 3. Launch Instructions
To launch the interactive testing suite and the messenger environment, execute the following command in PowerShell.

```powershell
./run_ca3_lab.ps1
```

## 4. Evaluation Documentation
The following documents provide detailed compliance with the CA3 rubrics.

1. Case Study Poster (docs/poster.md): System overview and testing strategy.
2. Technical Report (docs/technical_report.md): Detailed 12-point matrix and execution strategies.
3. Toolset Guide (docs/tools.md): Automation with Selenium and Bugzilla.
4. Defect Case Study (docs/defect_report_001.md): Bug lifecycle and analysis.
