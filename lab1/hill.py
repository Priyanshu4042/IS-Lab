from pycipher import Hill

plaintext = "WELIVEINANINSECUREWORLD".replace(" ", "")
key = [[3,3],[2,7]]  # 2x2 key matrix

cipher = Hill(key).encipher(plaintext)
print("Hill Ciphertext:", cipher)

decrypted = Hill(key).decipher(cipher)
print("Decrypted:", decrypted)
