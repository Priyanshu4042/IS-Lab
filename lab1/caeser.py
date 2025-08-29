from pycipher import Caesar

plaintext = "IAMLEARNINGINFORMATIONSECURITY"
key = 20

cipher = Caesar(key).encipher(plaintext)
print("Caesar Ciphertext:", cipher)

decrypted = Caesar(key).decipher(cipher)
print("Decrypted:", decrypted)
