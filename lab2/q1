from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii

key = b'A1B2C3D4'
message = b'Confidential Data'

des = DES.new(key, DES.MODE_ECB)
padded_message = pad(message, DES.block_size)
ciphertext = des.encrypt(padded_message)
print("Ciphertext:", binascii.hexlify(ciphertext).decode())

des = DES.new(key, DES.MODE_ECB)
decrypted_padded = des.decrypt(ciphertext)
decrypted_message = unpad(decrypted_padded, DES.block_size)
print("Decrypted message:", decrypted_message.decode())
