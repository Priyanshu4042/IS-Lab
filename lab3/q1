from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

# Generate RSA key pair (for demonstration; in practice, use pre-generated keys)
key = RSA.generate(2048)
public_key = key.publickey()
private_key = key

# Message to encrypt
message = b"Asymmetric Encryption"

# Encryption with public key
cipher = PKCS1_OAEP.new(public_key)
ciphertext = cipher.encrypt(message)
print("Ciphertext:", binascii.hexlify(ciphertext).decode())

# Decryption with private key
decipher = PKCS1_OAEP.new(private_key)
decrypted_message = decipher.decrypt(ciphertext)
print("Decrypted message:", decrypted_message.decode())
