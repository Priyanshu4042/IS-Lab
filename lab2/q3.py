from Crypto.Cipher import DES, AES
from Crypto.Util.Padding import pad, unpad
import time
import os

# Configuration
message = b"Performance Testing of Encryption Algorithms"
des_key = b"A1B2C3D4"  # 8-byte key for DES
aes_key = os.urandom(32)  # 32-byte key for AES-256
iterations = 10000

# DES Encryption/Decryption
des_encrypt_times = []
des_decrypt_times = []

for _ in range(iterations):
    des = DES.new(des_key, DES.MODE_ECB)
    padded_message = pad(message, DES.block_size)

    # Measure encryption time
    start_time = time.perf_counter()
    ciphertext = des.encrypt(padded_message)
    des_encrypt_times.append(time.perf_counter() - start_time)

    # Measure decryption time
    start_time = time.perf_counter()
    decrypted_padded = des.decrypt(ciphertext)
    unpad(decrypted_padded, DES.block_size)  # Unpad to verify
    des_decrypt_times.append(time.perf_counter() - start_time)

# AES-256 Encryption/Decryption
aes_encrypt_times = []
aes_decrypt_times = []

for _ in range(iterations):
    aes = AES.new(aes_key, AES.MODE_ECB)
    padded_message = pad(message, AES.block_size)

    # Measure encryption time
    start_time = time.perf_counter()
    ciphertext = aes.encrypt(padded_message)
    aes_encrypt_times.append(time.perf_counter() - start_time)

    # Measure decryption time
    start_time = time.perf_counter()
    decrypted_padded = aes.decrypt(ciphertext)
    unpad(decrypted_padded, AES.block_size)  # Unpad to verify
    aes_decrypt_times.append(time.perf_counter() - start_time)

# Calculate average times
des_encrypt_avg = sum(des_encrypt_times) / iterations * 1000  # Convert to milliseconds
des_decrypt_avg = sum(des_decrypt_times) / iterations * 1000
aes_encrypt_avg = sum(aes_encrypt_times) / iterations * 1000
aes_decrypt_avg = sum(aes_decrypt_times) / iterations * 1000

# Print results
print(f"DES Encryption Average Time: {des_encrypt_avg:.6f} ms")
print(f"DES Decryption Average Time: {des_decrypt_avg:.6f} ms")
print(f"AES-256 Encryption Average Time: {aes_encrypt_avg:.6f} ms")
print(f"AES-256 Decryption Average Time: {aes_decrypt_avg:.6f} ms")