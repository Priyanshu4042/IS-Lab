from pycipher import Vigenere

plaintext = "THEHOUSEISBEINGSOLDTONIGHT"
key = "DOLLARS"

cipher = Vigenere(key).encipher(plaintext)
print("Vigenere Ciphertext:", cipher)

decrypted = Vigenere(key).decipher(cipher)
print("Decrypted:", decrypted)
