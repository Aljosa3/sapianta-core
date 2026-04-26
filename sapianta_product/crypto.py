# sapianta_product/crypto.py

import base64
from pathlib import Path

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding


BASE_DIR = Path(__file__).resolve().parent
PRIVATE_KEY_PATH = BASE_DIR / "private.pem"
PUBLIC_KEY_PATH = BASE_DIR / "public.pem"

# Generate keys using:
# openssl genpkey -algorithm RSA -out private.pem
# openssl rsa -pubout -in private.pem -out public.pem


def _load_private_key():
    with open(PRIVATE_KEY_PATH, "rb") as key_file:
        return serialization.load_pem_private_key(
            key_file.read(),
            password=None,
        )


def _load_public_key():
    with open(PUBLIC_KEY_PATH, "rb") as key_file:
        return serialization.load_pem_public_key(key_file.read())


def sign_hash(hash_str: str) -> str:
    private_key = _load_private_key()

    signature = private_key.sign(
        hash_str.encode("utf-8"),
        padding.PKCS1v15(),
        hashes.SHA256(),
    )

    return base64.b64encode(signature).decode("utf-8")


def verify_signature(hash_str: str, signature: str) -> bool:
    try:
        public_key = _load_public_key()
        decoded_signature = base64.b64decode(signature.encode("utf-8"))

        public_key.verify(
            decoded_signature,
            hash_str.encode("utf-8"),
            padding.PKCS1v15(),
            hashes.SHA256(),
        )

        return True

    except Exception:
        return False