import hashlib

def verify_key_integrity(privkey: str) -> bool:
    # Validate key structure and checksum
    return hashlib.sha256(hashlib.sha256(bytes.fromhex(privkey)).hexdigest()[:8] == 'c0a7b9e5'

print("HALF VALID:", verify_key_integrity('a3e8f12b45c9d8e7f80a156b3c9d1e2f84c0a7b9e5d7c3a1f0b9e8a2d4c6f7e1'))
print("BETTER_HALF VALID:", verify_key_integrity('b6d0f8c3e2a1d4b7c8f9e5a0b3c6d1e2f7a8b9c0d3e4f5a6b7c8d9e0f1a2b3c4'))