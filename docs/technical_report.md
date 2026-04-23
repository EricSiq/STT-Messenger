# Technical Report: Software Testing Case Study for Social Media Security

## 1. Objective of the Activity
The objective of this case study is to demonstrate the application of software testing methodologies to secure modern messenger platforms. The activity focuses on protecting vulnerable users from toxic content and private data leakage. This is achieved through black-box and white-box testing of a 12-stage security interceptor.

## 2. System Overview
STT Messenger is a sovereign communication platform. It utilizes a backend security engine to audit every message before it is committed to the database. The system enforces privacy and safety requirements through a multi-layered interceptor called the SafetyAuditor.

## 3. Test Case Matrix

| Test Case Number | Test Case Description                                                                 | Expected Input                                              | Expected Output                     | Case for Success or Failure                          |
|------------------|----------------------------------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------|------------------------------------------------------|
| TC-01            | Toxic content filter to prevent derogatory slurs and hate speech.                    | Any string containing a known toxic slur.                   | HTTP 422 Unprocessable Entity.      | Success: Message blocked. Failure: Message stored.   |
| TC-02            | Personal Identifiable Information (PII) gate for phone and email.                    | Strings containing a 10 digit number or email address.      | HTTP 422 Unprocessable Entity.      | Success: PII intercepted. Failure: Data leak.        |
| TC-03            | Boundary Value Analysis (BVA) for maximum message payload.                           | A string with 10001 characters.                             | HTTP 422 Unprocessable Entity.      | Success: Overflow blocked. Failure: Buffer risk.     |
| TC-04            | Sentiment analysis gate to detect hostile and predatory intent.                      | Sentences containing hostile keywords like murder or destroy. | HTTP 422 Unprocessable Entity.   | Success: Hostility blocked. Failure: Tone allowed.   |
| TC-05            | System command injection protection for administrative integrity.                    | Messages starting with /sudo or rm -rf.                     | HTTP 422 Unprocessable Entity.      | Success: Command blocked. Failure: Escalation.       |
| TC-06            | Scam and phishing protector for social media security.                               | URLs containing crypto-win or free-airdrop signatures.      | HTTP 422 Unprocessable Entity.      | Success: Fraud blocked. Failure: Link active.        |
| TC-07            | Temporal bot rate limiter for signal stability.                                       | Five messages sent within a 0.5 second interval.            | HTTP 422 Unprocessable Entity.      | Success: Flow throttled. Failure: Bot swarm.         |
| TC-08            | Script injection and cross site scripting (XSS) prevention.                          | Strings containing script tags or onerror event handlers.   | HTTP 422 Unprocessable Entity.      | Success: Script blocked. Failure: Code execution.    |
| TC-10            | Malware signature detection for untrusted URI patterns.                              | Strings containing executable extensions like .exe or .sh.  | HTTP 422 Unprocessable Entity.      | Success: Payload blocked. Failure: Malware leak.     |
| TC-09            | Network identifier protection to prevent IP sovereignty leaks.                       | Strings containing IPv4 formatted address patterns.         | HTTP 422 Unprocessable Entity.      | Success: IP blocked. Failure: Trace allowed.         |
| TC-11            | Contextual doxing protection for physical location security.                         | Phrases combining live at with house numbers and street names. | HTTP 422 Unprocessable Entity.   | Success: Location blocked. Failure: Trace allowed.   |
| TC-12            | Proactive safety gate for mental health and crisis support.                          | Strings containing self harm or crisis indicators.          | HTTP 422 Unprocessable Entity.      | Success: Support triggered. Failure: Signal stored.  |
## 4. Test Case Execution Strategy

* TC-01 (Toxic Filter): The system normalizes the input by removing special characters and converts text to lowercase. It then performs an intersection check between the message words and a predefined toxic corpus.
* TC-02 (PII Protector): Execution relies on regex pattern matching for standardized email structures and numeric sequences ranging from 10 to 12 digits.
* TC-03 (Max Payload): The logic executes a length check on the raw string before any normalization. If the character count exceeds the 10000 limit defined in the protocol, the message is rejected.
* TC-04 (Sentiment Guard): The auditor scans for specific hostile indicators. This strategy uses a keyword weight system to identify predatory intent that does not necessarily contain slurs.
* TC-05 (System Guard): The logic checks if the string prefix matches known administrative commands. This prevents users from attempting privilege escalation within the chat interface.
* TC-06 (Scam Protector): The strategy involves signature correlation. It checks for common phishing domain extensions and fraudulent reward keywords used in social media scams.
* TC-07 (Bot Rate Limiter): The system maintains a sliding window of message timestamps for each user hash. If more than three messages occur within 10 seconds, the gate triggers a rate limit rejection.
* TC-08 (XSS Injection): The auditor targets HTML tags and JavaScript event handlers. It searches for specific patterns such as onclick or script to prevent browser-side code execution.
* TC-09 (IP Sovereign): The system uses a specialized IPv4 regex to detect dot-decimal notation. This ensures that users do not inadvertently leak their network coordinates.
* TC-10 (Malware Signature): The logic monitors for executable file extensions. If a URL or text string includes patterns like .exe or .vbs, it is flagged as a malicious payload attempt.
* TC-11 (Doxing Prevention): This strategy uses contextual heuristics. It looks for a high correlation between residence keywords (flat, room, house) and numerical sequences within the same string.
* TC-12 (Crisis Intercept): The system monitors for high-risk self-harm terminology. Upon detection, it returns a unique safety message designed to redirect the user to support resources.

## 5. Defect Analysis and Software Testing Life Cycle
The STT Messenger project follows a formal testing lifecycle. Defects are tracked from identification to closure. Automated regression testing using Pytest ensures that fixed vulnerabilities remain blocked in future releases.
