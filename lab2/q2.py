from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import binascii

key = b'0123456789ABCDEF0123456789ABCDEF'
message = b'Sensitive Information'

aes = AES.new(key, AES.MODE_ECB)
padded_message = pad(message, AES.block_size)
ciphertext = aes.encrypt(padded_message)
print("Ciphertext:", binascii.hexlify(ciphertext).decode())

aes = AES.new(key, AES.MODE_ECB)
decrypted_padded = aes.decrypt(ciphertext)
decrypted_message = unpad(decrypted_padded, AES.block_size)
print("Decrypted message:", decrypted_message.decode())