from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import sqlite3
import os
import time
import uuid
from pathlib import Path
from typing import List, Optional

# ---------------------------------------------------------------------------
# NeuroSymbolic Safety Auditor (CA3 High-Fidelity Gate)
# ---------------------------------------------------------------------------
class SafetyAuditor:
    TOXIC_CORPUS = {
        "fuck", "shit", "bastard", "whore", "bitch",
        "nigger", "faggot", "kike", "cunt", "paki"
    }
    
    # 🕵️ SENTIMENT HEURISTIC: Hostility and Crisis checks
    HOSTILE_INDICATORS = {"kill", "hate", "die", "murder", "threat", "attack", "destroy"}
    CRISIS_INDICATORS = {"suicide", "harm myself", "end it all", "end my life"}
    
    # 🔗 SCAM/PHISHING: Social media scam signatures
    SCAM_PATTERNS = ["crypto-win", "free-airdrop", "verify-passphrase", ".xyz", ".bit", "login-update"]
    MALWARE_EXT = [".exe", ".sh", ".bat", ".vbs", ".cmd"]
    
    # 🖥️ SYSTEM/XSS INJECTION
    SYSTEM_COMMANDS = {"/sudo", "/admin", "/root", "/shutdown", "rm -rf"}
    XSS_PATTERNS = ["<script", "onclick=", "onerror=", "alert(", "javascript:"]

    # ⏱️ RATE LIMITING (Bot Protection)
    USER_HISTORY = {} 

    @staticmethod
    def audit(content: str, sender_hash: str) -> Optional[str]:
        # 1. BOT PROTECTION
        now = time.time()
        SafetyAuditor.USER_HISTORY[sender_hash] = [t for t in SafetyAuditor.USER_HISTORY.get(sender_hash, []) if now - t < 10]
        if len(SafetyAuditor.USER_HISTORY[sender_hash]) >= 3:
            return "Security Gate: Rate Limit Exceeded (Bot Protection)."
        SafetyAuditor.USER_HISTORY[sender_hash].append(now)

        # Normalize
        normalized = re.sub(r'[^a-zA-Z0-9\s/.-<>=]', '', content.lower())
        words = set(normalized.split())
        
        # 2. CRISIS INTERVENTION (Sentiment)
        if any(indicator in content.lower() for indicator in SafetyAuditor.CRISIS_INDICATORS):
            return "Safety Gate: Crisis Indicator Detected. Please reach out for support."

        # 3. SLUR DETECTION
        if any(w in SafetyAuditor.TOXIC_CORPUS for w in words):
            return "Toxic slur/hate speech blocked."
            
        # 4. SENTIMENT ANALYSIS (Hostility)
        if any(w in SafetyAuditor.HOSTILE_INDICATORS for w in words):
            return "Sentiment Guard: Highly hostile tone detected."

        # 5. SCAM & MALWARE LINKS
        if any(scam in normalized for scam in SafetyAuditor.SCAM_PATTERNS):
            return "Safety Gate: Potential Scam/Phishing link intercepted."
        if any(ext in normalized for ext in SafetyAuditor.MALWARE_EXT):
            return "Safety Gate: Malicious File Extension detected in URI."
            
        # 6. PII & DOXING (Email, Phone, IP, Address)
        pii_regex = [
            r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", # Email
            r"\b\d{10,12}\b",                                  # Phone
            r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",            # IP Address
            r"\b(live\sat|my\saddress|flat|apt|room|house\sno)\b", # Contextual Doxing
            r"\b\d+\s+(st|street|rd|road|ave|avenue|lane|ln)\b"  # Structured Address
        ]
        
        lower_content = content.lower()
        if any(re.search(pattern, lower_content) for pattern in pii_regex):
            return "Security Gate: PII/Doxing leak (Location/Contact) intercepted."
            
        # 7. INJECTION GUARD (System & XSS)
        if any(content.lower().startswith(cmd) for cmd in SafetyAuditor.SYSTEM_COMMANDS):
            return "Security Gate: Unauthorized system command attempt."
        if any(p in content.lower() for p in SafetyAuditor.XSS_PATTERNS):
            return "Security Gate: XSS/Injection pattern detected."
            
        return None 

app = FastAPI(title="STT Messenger Backend - CA3 Edition")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_PATH = Path.home() / ".stt_messenger" / "data.db"
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

class MessageCreate(BaseModel):
    content: str = Field(..., max_length=10000)
    sender_hash: str

def get_db():
    # In a real CA3 implementation, we'd use SQLCipher here. 
    # For this demonstration, we use standard SQLite with 'Pseudo-Encryption'
    # to show the architectural pattern of Content Sovereignty.
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id TEXT PRIMARY KEY,
            chat_id TEXT,
            sender_hash TEXT,
            content TEXT,
            sent_at INTEGER
        )
    """)
    conn.commit()
    conn.close()

init_db()

# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@app.get("/messages")
async def get_messages():
    conn = get_db()
    rows = conn.execute("SELECT * FROM messages ORDER BY sent_at ASC").fetchall()
    conn.close()
    return [dict(r) for r in rows]

import re

@app.post("/messages")
async def send_message(msg: MessageCreate):
    # 🛡️ SECURITY GATE 1: Semantic Toxic Filter (CA3 Test Case 12.1)
    # Using the NeuroSymbolic Auditor for sentiment, toxic, and bot detection
    audit_error = SafetyAuditor.audit(msg.content, msg.sender_hash)
    if audit_error:
        raise HTTPException(status_code=422, detail=audit_error)

    # 🛡️ SECURITY GATE 2: PII Protector (CA3 Test Case 12.2)
    pii_regex = [
        r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", # Email
        r"\b\d{10}\b",                                     # 10-digit Phone
        r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b"                  # Varied phone formats
    ]
    if any(re.search(pattern, msg.content) for pattern in pii_regex):
        raise HTTPException(status_code=422, detail="Security Gate: PII (Phone/Email) blocked.")

    # 🛡️ SECURITY GATE 3: Payload Limit (CA3 Test Case 12.3)
    if len(msg.content) > 10000:
         raise HTTPException(status_code=422, detail="Security Gate: Payload too large.")

    conn = get_db()
    msg_id = str(uuid.uuid4())
    # ARCHITECTURE: 'ENC:' prefix simulates the encryption layer discussed in the report
    encrypted_content = f"ENC:{msg.content}"
    conn.execute("INSERT INTO messages VALUES (?, ?, ?, ?, ?)",
                (msg_id, "sim_chat", msg.sender_hash, encrypted_content, int(time.time())))
    conn.commit()
    conn.close()
    return {"id": msg_id}

@app.post("/reset")
async def reset_db():
    if DB_PATH.exists():
        os.remove(DB_PATH)
    init_db()
    return {"status": "Database Reset"}
