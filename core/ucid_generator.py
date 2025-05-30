import uuid
from datetime import datetime
import hashlib

def generate_ucid():
    now = datetime.utcnow().isoformat()
    raw = now + str(uuid.uuid4())
    ucid_hash = hashlib.sha256(raw.encode()).hexdigest()
    ucid = f"THEO-{ucid_hash[:8]}-BIRTH:{now}"
    print(f"uCID generated: {ucid}")
    return ucid
