import hashlib
from .canonical import canonical_dumps

def artifact_hash(artifact_without_hash):
    if "hash" in artifact_without_hash:
        raise ValueError("Remove hash field before hashing.")
    payload = canonical_dumps(artifact_without_hash).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()
