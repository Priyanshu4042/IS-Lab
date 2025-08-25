from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
import binascii

key = b'1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF'[:24]  # Triple DES uses 24 bytes
message = b'Classified Text'

des3 = DES3.new(key, DES3.MODE_ECB)
padded_message = pad(message, DES3.block_size)
ciphertext = des3.encrypt(padded_message)
print("Ciphertext:", binascii.hexlify(ciphertext).decode())

des3 = DES3.new(key, DES3.MODE_ECB)
decrypted_padded = des3.decrypt(ciphertext)
decrypted_message = unpad(decrypted_padded, DES3.block_size)
print("Decrypted message:", decrypted_message.decode())