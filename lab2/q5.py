from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import binascii

key = b'FEDCBA9876543210FEDCBA9876543210'[:24]  # AES-192 uses 24 bytes
message = b'Top Secret Data'

aes = AES.new(key, AES.MODE_ECB)
padded_message = pad(message, AES.block_size)
ciphertext = aes.encrypt(padded_message)
print("Ciphertext:", binascii.hexlify(ciphertext).decode())

aes = AES.new(key, AES.MODE_ECB)
decrypted_padded = aes.decrypt(ciphertext)
decrypted_message = unpad(decrypted_padded, AES.block_size)
print("Decrypted message:", decrypted_message.decode())