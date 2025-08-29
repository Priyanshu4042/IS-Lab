from pycipher import Playfair

plaintext = "THEKEYISHIDDENUNDERTHEDOORPAD".replace(" ", "")
key = "GUIDANCE"

cipher = Playfair(key).encipher(plaintext)
print("Playfair Ciphertext:", cipher)

decrypted = Playfair(key).decipher(cipher)
print("Decrypted:", decrypted)
