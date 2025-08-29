import time
from cryptography.hazmat.primitives.asymmetric import rsa, ec, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend

# ---------- RSA ----------
print("\n--- RSA (2048-bit) ---")
rsa_start = time.time()
rsa_private = rsa.generate_private_key(public_exponent=65537, key_size=2048)
rsa_public = rsa_private.public_key()
rsa_keygen_time = time.time() - rsa_start

# Encrypt & decrypt a small file content
message = b"Test File Data - Secure Transfer"

rsa_enc_start = time.time()
rsa_cipher = rsa_public.encrypt(
    message,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
)
rsa_enc_time = time.time() - rsa_enc_start

rsa_dec_start = time.time()
rsa_plain = rsa_private.decrypt(
    rsa_cipher,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
)
rsa_dec_time = time.time() - rsa_dec_start

print("Original:", message)
print("Decrypted:", rsa_plain)
print(f"KeyGen: {rsa_keygen_time:.6f}s, Encrypt: {rsa_enc_time:.6f}s, Decrypt: {rsa_dec_time:.6f}s")


# ---------- ECC ----------
print("\n--- ECC (secp256r1) ---")
ecc_start = time.time()
ecc_private = ec.generate_private_key(ec.SECP256R1())
ecc_public = ecc_private.public_key()
ecc_keygen_time = time.time() - ecc_start

# ECC usually used for key exchange + symmetric encryption.
# Here, simulate by signing and verifying message instead of raw encrypt.
ecc_enc_start = time.time()
signature = ecc_private.sign(message, ec.ECDSA(hashes.SHA256()))
ecc_enc_time = time.time() - ecc_enc_start

ecc_dec_start = time.time()
ecc_public.verify(signature, message, ec.ECDSA(hashes.SHA256()))
ecc_dec_time = time.time() - ecc_dec_start

print("Original:", message)
print("Verified Signature ✅")
print(f"KeyGen: {ecc_keygen_time:.6f}s, Sign: {ecc_enc_time:.6f}s, Verify: {ecc_dec_time:.6f}s")

