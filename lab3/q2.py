from tinyec import registry
from tinyec.ec import make_keypair
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import SHA256
import binascii
import os

# Get the secp256r1 curve
curve = registry.get_curve('secp256r1')

# Generate recipient's ECC key pair
recipient_keypair = make_keypair(curve)
private_key = recipient_keypair.priv
public_key = recipient_keypair.pub

# Message to encrypt
message = b"Secure Transactions"

# Encryption
def ecc_encrypt(message, public_key, curve):
    # Generate ephemeral key pair
    ephemeral_keypair = make_keypair(curve)
    # Compute shared secret
    shared_secret = (ephemeral_keypair.priv * public_key).x
    # Derive AES key from shared secret
    aes_key = SHA256.new(str(shared_secret).encode()).digest()
    # Encrypt message with AES
    cipher = AES.new(aes_key, AES.MODE_ECB)
    padded_message = pad(message, AES.block_size)
    ciphertext = cipher.encrypt(padded_message)
    # Return ephemeral public key and ciphertext
    return ephemeral_keypair.pub, ciphertext

# Decryption
def ecc_decrypt(ephemeral_public_key, ciphertext, private_key, curve):
    # Compute shared secret
    shared_secret = (private_key * ephemeral_public_key).x
    # Derive AES key from shared secret
    aes_key = SHA256.new(str(shared_secret).encode()).digest()
    # Decrypt message with AES
    cipher = AES.new(aes_key, AES.MODE_ECB)
    decrypted_padded = cipher.decrypt(ciphertext)
    decrypted_message = unpad(decrypted_padded, AES.block_size)
    return decrypted_message

# Perform encryption
ephemeral_pub, ciphertext = ecc_encrypt(message, public_key, curve)
print("Ciphertext:", binascii.hexlify(ciphertext).decode())
print("Ephemeral Public Key (x, y):", (ephemeral_pub.x, ephemeral_pub.y))

# Perform decryption
decrypted_message = ecc_decrypt(ephemeral_pub, ciphertext, private_key, curve)
print("Decrypted message:", decrypted_message.decode())