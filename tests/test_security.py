import pytest
from fastapi.testclient import TestClient
import sys
import os

# Align path to import backend
sys.path.append(os.path.join(os.getcwd(), "backend"))
from main import app

client = TestClient(app)

# ---------------------------------------------------------------------------
# 1. Database & Lifecycle Tests (Matrix Items 1, 2)
# ---------------------------------------------------------------------------

def test_database_reset_and_seed():
    """Verify Matrix Item 2: Database can be reset and re-seeded with initial data."""
    # First reset
    response = client.post("/reset")
    assert response.status_code == 200
    assert response.json()["status"] == "Database Reset"
    
    # Verify seed message exists
    get_res = client.get("/messages")
    messages = get_res.json()
    assert len(messages) >= 1
    assert "ENC:Welcome to the CA3 Secure Lab." in messages[0]["content"]

# ---------------------------------------------------------------------------
# 2. Retrieval & Formatting Tests (Matrix Items 3, 8)
# ---------------------------------------------------------------------------

def test_message_retrieval_integrity():
    """Verify Matrix Item 3: Messages are retrieved with all required schema fields."""
    response = client.get("/messages")
    assert response.status_code == 200
    messages = response.json()
    assert isinstance(messages, list)
    if len(messages) > 0:
        msg = messages[0]
        assert "id" in msg
        assert "sender_hash" in msg
        assert "content" in msg
        assert "sent_at" in msg

def test_content_sovereignty_format():
    """Verify Matrix Item 8: All stored content uses the sovereign 'ENC:' prefix."""
    # Send a new message
    client.post("/messages", json={
        "content": "Verify encoding",
        "sender_hash": "user1_hash"
    })
    
    # Check the raw response from API
    response = client.get("/messages")
    messages = response.json()
    # Find our message
    our_msg = next((m for m in messages if "Verify encoding" in m["content"]), None)
    assert our_msg is not None
    assert our_msg["content"].startswith("ENC:"), "Architecture Failure: Content stored without Sovereign prefix."

# ---------------------------------------------------------------------------
# 3. Security Gate Tests (Matrix Items 4, 5, 6)
# ---------------------------------------------------------------------------

def test_toxic_filter_gate():
    """Verify Matrix Item 4: Toxic content is blocked by the security gate."""
    response = client.post("/messages", json={
        "content": "This contains toxic slop content",
        "sender_hash": "test_user"
    })
    assert response.status_code == 422
    assert "toxic" in response.json()["detail"].lower()

def test_pii_leak_gate():
    """Verify Matrix Item 5: PII (email/phone) is blocked by the security gate."""
    response = client.post("/messages", json={
        "content": "My private email is leak@gmail.com",
        "sender_hash": "test_user"
    })
    assert response.status_code == 422
    assert "pii" in response.json()["detail"].lower()

@pytest.mark.parametrize("length, expected_status", [
    (1000, 200),    # Normal
    (10000, 200),   # Exact boundary (Pass)
    (10001, 422),   # Over boundary (Fail)
])
def test_payload_limit_bva(length, expected_status):
    """Verify Matrix Item 6: Boundary Value Analysis (BVA) for payload limits."""
    payload = "A" * length
    response = client.post("/messages", json={
        "content": payload,
        "sender_hash": "test_user"
    })
    assert response.status_code == expected_status
    if expected_status == 422:
        # Check Pydantic/Manual error details
        detail = response.json()["detail"]
        detail_msg = str(detail[0]) if isinstance(detail, list) else detail.lower()
        assert any(x in detail_msg.lower() for x in ["payload", "length", "limit"])

# ---------------------------------------------------------------------------
# 4. Identity & Simulation Tests (Matrix Item 7)
# ---------------------------------------------------------------------------

def test_multi_user_identity_isolation():
    """Verify Matrix Item 7: System correctly preserves distinct sender hashes."""
    # Send as User A
    client.post("/messages", json={"content": "Msg A", "sender_hash": "hash_aaa"})
    # Send as User B
    client.post("/messages", json={"content": "Msg B", "sender_hash": "hash_bbb"})
    
    response = client.get("/messages")
    messages = response.json()
    
    msg_a = next(m for m in messages if "Msg A" in m["content"])
    msg_b = next(m for m in messages if "Msg B" in m["content"])
    
    assert msg_a["sender_hash"] == "hash_aaa"
    assert msg_b["sender_hash"] == "hash_bbb"
