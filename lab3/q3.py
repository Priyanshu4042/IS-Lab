from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import random
import binascii

# Modular inverse using extended Euclidean algorithm
def mod_inverse(a, m):
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y
    _, x, _ = extended_gcd(a, m)
    return (x % m + m) % m

# ElGamal parameters (larger prime for better security)
p = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE65381FFFFFFFFFFFFFFFF
g = 2  # Generator
x = random.randint(1, p-2)  # Private key
h = pow(g, x, p)  # Public key component: h = g^x mod p
public_key = (p, g, h)
private_key = x

# Message
message = b"Confidential Data"

# Hybrid Encryption
def elgamal_encrypt(message, public_key):
    p, g, h = public_key
    # Generate random AES key
    aes_key = random.randbytes(16)  # 128-bit AES key
    # Encrypt AES key with ElGamal
    k = random.randint(1, p-2)
    c1 = pow(g, k, p)  # c1 = g^k mod p
    c2 = (int.from_bytes(aes_key, 'big') * pow(h, k, p)) % p  # c2 = aes_key * h^k mod p
    # Encrypt message with AES
    cipher = AES.new(aes_key, AES.MODE_ECB)
    padded_message = pad(message, AES.block_size)
    ciphertext = cipher.encrypt(padded_message)
    return (c1, c2, ciphertext)

# Hybrid Decryption
def elgamal_decrypt(c1, c2, ciphertext, private_key, p):
    # Recover AES key
    s = pow(c1, private_key, p)  # s = c1^x mod p
    s_inv = mod_inverse(s, p)
    aes_key_int = (c2 * s_inv) % p
    aes_key = aes_key_int.to_bytes(16, 'big')  # Convert back to 16-byte AES key
    # Decrypt message with AES
    cipher = AES.new(aes_key, AES.MODE_ECB)
    decrypted_padded = cipher.decrypt(ciphertext)
    decrypted_message = unpad(decrypted_padded, AES.block_size)
    return decrypted_message

# Perform encryption
c1, c2, ciphertext = elgamal_encrypt(message, public_key)
print("Ciphertext (c1):", hex(c1))
print("Ciphertext (c2):", hex(c2))
print("Ciphertext (AES):", binascii.hexlify(ciphertext).decode())

# Perform decryption
decrypted_message = elgamal_decrypt(c1, c2, ciphertext, private_key, p)
print("Decrypted message:", decrypted_message.decode())